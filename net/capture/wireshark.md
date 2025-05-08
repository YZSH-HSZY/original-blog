# wireshark
一款跨平台的抓包工具

> 参考文档:
- [wireshark 开发者指南](https://www.wireshark.org/docs/wsdg_html_chunked/)

## 过滤规则

### 几种常见的过滤规则
- `ip.src == <ip_address>` 只保留原ip地址为指定值的包
udp

`tcp.payload contains "GET"`
`tcp.payload contains 47.45.54` 16进制
`http.content_type contains "application/json"` 过滤 HTML 内容

!icmp and ip.src == 223.168.1.149 and ip.dst == 223.168.1.105 and (udp.payload contains e4.4d.a0.ab or udp.payload contains e1.f2.00.a3)

!icmp and ip.src == 223.168.1.149 and ip.dst == 223.168.1.105 and (udp.payload contains e4.4d.a0.ab or udp.payload contains e4.4d.90.84.aa.09.fd or udp.payload contains e1.f2.00.a3)

!icmp and ip.src == 223.168.1.149 and ip.dst == 223.168.1.105 and (udp.payload[3] == 0d )

188     udp.payload[3]==0d
188     udp.payload[3]==0d and udp.payload[0]==15

<!-- 311     0d 15 -->

326     udp.payload[3]==0d or udp.payload[3]==15 

311     udp.payload[8] == 50 and udp.payload[9] == d6 and udp.payload[10] == bf 

138     udp.payload[3]==15
68      udp.payload[3]==15 and udp.payload[0]==15
70      udp.payload[3]==15 and udp.payload[0]==08

<!-- length -->
311     udp.payload[12] == 08
311     udp.payload[24] == 05
311     udp.payload[12] == 08 and udp.payload[24] == 05
8910

<!--  -->
621     !icmp and ip.src == 223.168.1.149 and ip.dst == 223.168.1.105 and (udp.payload[12] == 00 and udp.payload[24] != 05)
    
    KP27A
    NMEA2000<->0183 Gateway(KC-2W)
    NMEA 2000 PC Interface (NGT-1)

## 协议解析器

### 自定义协议解析器

1. 使用lua脚本
> 确保wireshark支持lua, 在 `Help --> About Wireshark` 查看是否存在内容 `with Lua 5.2.4,`
> 参考文档[使用lua编写dissector](https://www.wireshark.org/docs/wsdg_html_chunked/wslua_dissector_example.html)
> 参[wireshark-lua API reference](./wireshark-lua.md)

2. 使用c语言编写二进制插件, 需编译安装wireshark获取头文件

## 插件

> 参考文档
- [wireshark官方插件示例](https://gitlab.com/wireshark/wireshark/-/tree/master/plugins)

## example

### 在使用前向保密连接时解密TLS数据

> 现代 TLS 默认使用 ECDHE(Elliptic Curve Diffie-Hellman Ephemeral) 或 DHE(Diffie-Hellman Ephemeral) 密钥交换，即使您提供了 RSA 私钥，也无法解密，因为前向保密(PFS)机制会为每个会话生成临时的密钥

1. 服务端直接记录 TLS 会话密钥
```
// example to record tls key in server
SSL_CTX_set_keylog_callback(ssl_ctx, [](const SSL *ssl, const char *line) {
    FILE *keylog = fopen("/path/to/sslkeylogfile.txt", "a");
    if (keylog) {
        fprintf(keylog, "%s\n", line);
        fclose(keylog);
    }
});
```
2. 服务端强制使用非PFS加密套件
```
// disable PFS to allow rsa direct decryption
svr.set_tls_options(SSL_OP_NO_ECDHE | SSL_OP_NO_DHE);
```
3. 中间人代理
```
# use mitmproxy record secret key
mitmproxy --set sslkeylogfile=/path/to/keys.log
```

### Packet重放

可通过nc实现, 如`echo "314e455400010001408000080000000016fefd000000000000000100560100004a000100000000004afefd680ee1d7c5e18205416e704a860cd8cb743ffa8a61a4089d87ce188fb2c24cff002012894487efa8da8306df7090c379326612e47edcfeccc7d73341c3cce28f83b9000200a90100" | xxd -r -p | nc -6u fe80::42:c0ff:fe64:102%br0 20112`