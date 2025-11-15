
## MDNS
mDNS(RFC 6762 Multicast DNS, 组播DNS), 使用5353端口，组播地址 224.0.0.251, 一般和 `DNS-SD(DNS服务侦测)` 结合使用.

> mDNS消息是发送到以下位置的多播UDP数据包：
- 以太网帧, 标准组播MAC地址: `01:00:5E:00:00:FB`(IPv4)/`33:33:00:00:00:FB`(IPv6)
- IPv4: `224.0.0.251`/IPv6: `ff02 :: fb`
- UDP Port: 5353

> 一个没有常规DNS服务器的小型网络, mDNS提供类似于DNS的服务和报文, 例如: 主机A需要局域网内的FTP服务, 那么它会向自身的mDNS服务查询, 接着A主机的mDNS服务就会在指定的地址上进行UDP广播, 以获取对应的服务地址和端口

## DNS-SD
DNS-SD(DNS Service Discovery, 基于DNS协议的服务发现), 属于局域网服务发现协议的一种. 设备之间可以通过该协议自动发现服务; DNS-SD 兼容 mDNS 协议，同样使用 UDP 5353 端口, DNS-SD会周期性的在组播地址 224.0.0.251 广播自己感兴趣的服务名称

> DNS-SD 协议提供了一种主动查询服务的功能, 通过向目标主机发送查询名为` _services._dns-sd._udp.local`, 类型为 PTR 记录的 DNS 查询报文, 目标主机将返回自身开放的服务名称

## SSDP
SSDP(Simple Service Discovery Protocol, 简答服务发现协议), 属于局域网服务发现协议的一种. 是 UPnP(Universal Plug and Play) 的核心实现

## 参考文档

- [Avahi - mDNS/DNS-SD 的 Linux 服务发现](https://github.com/avahi/avahi.git)
- [RFC6762: 多播DNS](https://tools.ietf.org/html/rfc6762)
- [RFC6763: 基于DNS的服务发现](https://tools.ietf.org/html/rfc6763)

## message type

- `PTR Record`: Maps the service type (_printer._tcp.local) to a specific instance (MyPrinter._printer._tcp.local).
- `SRV Record`: Specifies the host (myprinter.local) and port (631).
- `A/AAAA Record`: Provides IPv4/IPv6 addresses.