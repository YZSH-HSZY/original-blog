local onenet = Proto("OneNet", "OneNet Protocol")

-- OneNet Fixed Header fields
local fh_signature = ProtoField.string("onenet.signature", "Signature", base.ASCII)
local fh_version = ProtoField.uint16("onenet.version", "Version", base.HEX)
local fh_msg_seq_num = ProtoField.uint16("onenet.msg_seq_num", "Message Sequence Number", base.DEC)

-- OneNet Extension Header common fields
local eh_optional = ProtoField.bool("onenet.eh_optional", "Optional", 8, nil, 0x80)
local eh_final = ProtoField.bool("onenet.eh_final", "Final", 8, nil, 0x40)
local eh_type = ProtoField.uint16("onenet.eh_type", "Type", base.HEX, nil, 0x3FFF)
local eh_length = ProtoField.uint16("onenet.eh_length", "Header Length", base.DEC)

-- DTLS Encapsulation specific fields (Type 128)
local dtls_role = ProtoField.bool("onenet.dtls.dtls_role", "Role", 8, {"Server", "Client"}, 0x80)
local dtls_reserved = ProtoField.uint8("onenet.dtls.dtls_reserved", "Reserved", base.HEX, nil, 0x7F)
local dtls_spi = ProtoField.uint24("onenet.dtls.dtls_spi", "DTLS SPI", base.HEX)

-- ESP Encapsulation specific fields (Type 136)
local esp_sa_spi = ProtoField.uint32("onenet.esp.esp_sa_spi", "SA SPI", base.HEX)
local esp_sqn = ProtoField.uint32("onenet.esp.esp_sqn", "SQN", base.HEX)
local esp_auth_tag = ProtoField.bytes("onenet.esp.esp_auth_tag", "Authentication Tag")
local esp_iv = ProtoField.bytes("onenet.esp.iv", "ESP IV")
local esp_add = ProtoField.bytes("onenet.esp.add", "ESP ADD")
local esp_ciphertext = ProtoField.bytes("onenet.esp.ciphertext", "ESP Ciphertext")

onenet.fields = {
    fh_signature, fh_version, fh_msg_seq_num,
    eh_optional, eh_final, eh_type, eh_length,
    dtls_role, dtls_reserved, dtls_spi,
    esp_sa_spi, esp_sqn, esp_auth_tag, esp_iv, esp_add, esp_ciphertext
}

local dtls_dissector = Dissector.get("dtls")

function ipv6_to_bytes(ipv6_str)
    -- 输入验证
    ipv6_str = tostring(ipv6_str or "::")
    if not ipv6_str:match("^[%x:]*$") then
        error("无效的IPv6地址: "..ipv6_str)
    end

    -- 分割所有块（包括空块）
    local blocks = {}
    local start_pos = 1
    local double_colon_pos
    
    while true do
        local colon_pos = ipv6_str:find(":", start_pos)
        local block
        
        if colon_pos then
            block = ipv6_str:sub(start_pos, colon_pos-1)
            start_pos = colon_pos + 1
        else
            block = ipv6_str:sub(start_pos)
        end
        
        -- 记录空块位置（处理::）
        if block == "" then
            if double_colon_pos then
                error("IPv6地址中只能有一个::压缩")
            end
            double_colon_pos = #blocks + 1
        else
            -- table.insert(blocks, block)
            table.insert(blocks, string.format("%04x",tonumber(block,16)))
        end
        
        if not colon_pos then break end
    end

    -- 补全压缩部分
    if double_colon_pos then
        local needed_zeros = 8 - #blocks
        for i = 1, needed_zeros do
            -- table.insert(blocks, double_colon_pos, "0")
            table.insert(blocks, double_colon_pos, "0000")
        end
    elseif #blocks ~= 8 then
        error("非压缩IPv6地址必须有8个区块")
    end

    -- 转换为字节
    local ba = ByteArray.new(table.concat(blocks))
    return ba
end

-- 自定义ESP解析器
local function esp_dissector(buffer, pinfo, tree)
    -- pinfo.cols.protocol = "OneNet-ESP"
    local esp_tree = tree:add("ESP")
    local_offset = 0

    -- 获取IPv6层信息
    local ipv6_info = {
        src = nil,
        dst = nil,
        sport = nil,
        dport = nil,
    }
    
    -- 通过pinfo获取
    if pinfo.net_src and pinfo.net_dst and pinfo.src_port 
            and pinfo.dst_port then
        ipv6_info.src = pinfo.net_src
        ipv6_info.dst = pinfo.net_dst
        ipv6_info.sport = pinfo.src_port
        ipv6_info.dport = pinfo.dst_port
    end
    
    -- 解析ESP头 (26字节: Len + SA SPI + SQN + Tag)
    if buffer:len() >= 26 then
        esp_tree:add(eh_length, buffer(local_offset, 2))
        local_offset = local_offset + 2
        esp_tree:add(esp_sa_spi, buffer(local_offset, 4))
        local_offset = local_offset + 4
        esp_tree:add(esp_sqn, buffer(local_offset, 4))
        local_offset = local_offset + 4
        esp_tree:add(esp_auth_tag, buffer(local_offset, 16))
        payload_local_offset = local_offset + 16
        
        -- other package data
        esp_tree:add(esp_iv, buffer(2, 8))

        local add_data = ByteArray.new()
        add_data:append(ipv6_to_bytes(tostring(ipv6_info.src)))
        add_data:append(ipv6_to_bytes(tostring(ipv6_info.dst)))
        add_data:append(ByteArray.new(string.format("%04x", ipv6_info.sport)))
        add_data:append(ByteArray.new(string.format("%04x", ipv6_info.dport)))
        add_data:append(ByteArray.new(pinfo.private["onenet_fixed_header"])) 
        esp_tree:add(esp_add, add_data:tvb()(0))
        
        -- 如果有负载数据
        if buffer:len() > 26 then
            esp_tree:add(esp_ciphertext, buffer(26, buffer:len()-26))
        end
    else
        esp_tree:add(buffer, "Incomplete ESP Header")
    end
end

function onenet.dissector(buffer, pinfo, tree)
    pinfo.cols.protocol = onenet.name
    local offset = 0
    local buf_len = buffer:len()
    
    -- Create protocol tree
    local onenet_tree = tree:add(onenet, buffer(), "OneNet Protocol")
    
    -- Parse Fixed Header (8 bytes)
    if buf_len < 8 then
        pinfo.desegment_len = 8 - buf_len
        return
    end
    
    pinfo.private["onenet_fixed_header"] = tostring(buffer(0, 8):bytes())

    local fixed_header_tree = onenet_tree:add("OneNet Fixed Header")
    fixed_header_tree:add(fh_signature, buffer(offset, 4))  -- Signature (4B)
    offset = offset + 4
    
    -- Explicit big-endian reading for version and sequence number
    fixed_header_tree:add(fh_version, buffer(offset, 2))    -- Version (2B)
    offset = offset + 2
    fixed_header_tree:add(fh_msg_seq_num, buffer(offset, 2))-- Seq Num (2B)
    offset = offset + 2
    
    -- Parse Extension Headers (if any)
    local ext_header_count = 0
    local payload_offset = offset
    local last_type = nil
    
    while offset + 4 <= buf_len do
        ext_header_count = ext_header_count + 1
        local ext_header_tree = onenet_tree:add("OneNet Extension Header #" .. ext_header_count)
        
        -- Parse common extension header fields (4 bytes)
        local header_bytes = buffer(offset, 4)
        local optional_bit = header_bytes:bitfield(0, 1)
        local final_bit = header_bytes:bitfield(1, 1)
        local type_value = header_bytes:bitfield(2, 14)
        local length_value = header_bytes(2, 2):uint()
        
        ext_header_tree:add(eh_optional, buffer(offset, 1))
        ext_header_tree:add(eh_final, buffer(offset, 1))
        ext_header_tree:add(eh_type, buffer(offset, 2))
        ext_header_tree:add(eh_length, buffer(offset + 2, 2))
        
        offset = offset + 4
        last_type = type_value
        
        -- Check if this is the final extension header
        if final_bit == 1 then
            payload_offset = offset
            -- Handle type-specific fields
            if type_value == 128 then  -- DTLS Encapsulation
                if offset + 4 <= buf_len then
                    local dtls_specific_tree = ext_header_tree:add("DTLS Encapsulation Specific Fields")
                    dtls_specific_tree:add(dtls_role, buffer(offset, 1))
                    dtls_specific_tree:add(dtls_reserved, buffer(offset, 1))
                    -- Read 24-bit SPI in big-endian
                    dtls_specific_tree:add(dtls_spi, buffer(offset + 1, 3))
                    payload_offset = offset + 4
                end
            elseif type_value == 136 then  -- ESP
                if offset + 24 <= buf_len then
                    local esp_specific_tree = ext_header_tree:add("ESP Specific Fields")
                    esp_specific_tree:add(esp_sa_spi, buffer(offset, 4))
                    offset = offset + 4
                    esp_specific_tree:add(esp_sqn, buffer(offset, 4))
                    offset = offset + 4
                    esp_specific_tree:add(esp_auth_tag, buffer(offset, 16))
                    payload_offset = offset + 16

                    -- Skip the built-in ESP dissector to avoid duplicate fields
                    -- last_type = nil
                end
            end
            break
        end
    end
    
    -- Parse payload based on the last extension header type
    if payload_offset < buf_len then
        local payload_len = buf_len - payload_offset
        if payload_len > 0 then
            local payload_buffer = buffer(payload_offset, payload_len)
            
            -- Dispatch to appropriate dissector
            if last_type == 128 and dtls_dissector then
                dtls_dissector:call(payload_buffer:tvb(), pinfo, tree)
                pinfo.cols.protocol = "OneNet-DTLS-Encapsulation"
                -- dtls_dissector(payload_buffer:tvb(), pinfo, tree)
            elseif last_type == 136 and esp_dissector then
                pinfo.cols.protocol = "OneNet-ESP"
                -- esp_dissector:call(payload_buffer:tvb(), pinfo, tree)
                -- 调用自定义ESP解析器
                esp_dissector(
                    buffer(payload_offset - 26, buf_len - payload_offset + 26):tvb(), 
                    pinfo, 
                    tree
                )
            else
                pinfo.cols.protocol = "OneNet-Unknown"
                onenet_tree:add(payload_buffer, "Payload Data")
            end
        end
    end
end

-- Register the dissector to UDP port 10111
-- local udp_port = DissectorTable.get("udp.port")
-- udp_port:add(10111, onenet)
-- udp_port:add(20112, onenet)

-- 注册到UDP启发式解析表
function onenet_heuristic(buffer, pinfo, tree)
    -- Check if the packet has the expected OneNet signature
    if buffer:len() < 4 or buffer(0, 4):string() ~= "1NET" then
        return false
    end

    -- Call the main dissector function if the signature is found
    onenet.dissector(buffer, pinfo, tree)
    return true
end

-- Register the heuristic dissector for OneNet
onenet:register_heuristic("udp", onenet_heuristic)