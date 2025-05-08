# Wireshark’s Lua API 

此部分介绍wireshark提供的供lua使用的API接口

> 参考文档:
- [pinfo模块介绍](https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Pinfo.html#lua_class_Pinfo)

## build-module

### pinfo

存储包信息

> 支持的信息有:
- `pinfo.src_port`: Packet的源端口
- `pinfo.dst_port`: Packet的目的端口
- `pinfo.net_src`: Packet网络层的源地址(Type=Address)
- `pinfo.net_dst`: Packet网络层的目的地址(Type=Address)

## example

### 在上一级解析中添加私有数据给下一层协议解析使用

- 在上一级解析中使用`pinfo.private`的PrivateTable存储信息
> `pinfo.private["onenet_fixed_header"] = tostring(buffer(0, 8):bytes())`
**注意** pinfo.private的值只能存储字符串

### ipv6地址转buffer

```lua
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
```