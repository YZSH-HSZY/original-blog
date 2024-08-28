# wireshark
一款跨平台的抓包工具

## 过滤规则

### 几种常见的过滤规则
- `ip.src == <ip_address>` 只保留原ip地址为指定值的包
udp

`tcp.payload contains "GET"`
`tcp.payload contains 47.45.54` 16进制

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