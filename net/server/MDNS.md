## MDNS

mDNS(RFC 6762 Multicast DNS, 组播DNS), 使用UDP-5353端口，组播地址 224.0.0.251, 一般和 `DNS-SD(DNS服务侦测)` 结合使用.

> mDNS消息是发送到以下位置的多播UDP数据包：
- 以太网帧, 标准组播MAC地址: `01:00:5E:00:00:FB`(IPv4)/`33:33:00:00:00:FB`(IPv6)
- IPv4: `224.0.0.251`/IPv6: `ff02::fb`
- UDP Port: 5353

> 一个没有常规DNS服务器的小型网络, mDNS提供类似于DNS的服务和报文, 例如: 主机A需要局域网内的FTP服务, 那么它会向自身的mDNS服务查询, 接着A主机的mDNS服务就会在指定的地址上进行UDP广播, 以获取对应的服务地址和端口

**特点**
1. 组播 DNS(mDNS)能够在没有传统单播 DNS 服务器的情况下, 在本地链路上执行类似DNS操作的能力
2. 组播 DNS 指定部分 DNS 命名空间为本地免费使用, 无需支付年费, 也无需设置委托或配置传统 DNS 服务器来响应这些名称

**优点**
1. 几乎不需要管理或配置来设置
2. 在没有基础设施存在时也能工作
3. 在基础设施故障时也能正常工作

## DNS-SD

DNS-SD(DNS Service Discovery, 基于DNS协议的服务发现), 属于局域网服务发现协议的一种. 设备之间可以通过该协议自动发现服务; DNS-SD 兼容 mDNS 协议，同样使用 UDP 5353 端口, DNS-SD会周期性的在组播地址 224.0.0.251 广播自己感兴趣的服务名称

> DNS-SD 协议提供了一种主动查询服务的功能, 通过向目标主机发送查询名为` _services._dns-sd._udp.local`, 类型为 PTR 记录的 DNS 查询报文, 目标主机将返回自身开放的服务名称

## SSDP

SSDP(Simple Service Discovery Protocol, 简答服务发现协议), 属于局域网服务发现协议的一种. 是 UPnP(Universal Plug and Play) 的核心实现

## 参考文档

- [Avahi - mDNS/DNS-SD 的 Linux 服务发现](https://github.com/avahi/avahi.git)
- [RFC6762: 多播DNS](https://tools.ietf.org/html/rfc6762)
- [RFC6763: 基于DNS的服务发现](https://tools.ietf.org/html/rfc6763)

## MDNS相关释义

### Multicast DNS Names

属于组织或个人控制 DNS 命名空间, 可以申请分配一个全球唯一名称, 例如"test.example.com." 然而, 大多数家用电脑用户无法轻松访问他们有权限创建名称的全球 DNS 命名空间的任何部分。这使得大多数家用计算机在实际作上实际上是匿名的。

> MDNS 允许任何计算机用户选择为其计算机赋予链路本地 Multicast DNS 主机名, 如"single-dns-label.local.", 知道链路发生名称冲突并重新生成新的唯一名称

> `.local.` 是一个具有特殊语义的特殊域名，即任何以 `.local.` 结尾的完全限定名称都是链接本地域名, 且该域名仅在其起源链路上有意义。这类似于 `169.254/16` 前缀中的 IPv4 地址，或 `FE80::/10`前缀中的 IPv6 地址, 它们是本地链路且仅在其发源链路上有意义的

### message type

- `PTR Record`: Maps the service type (_printer._tcp.local) to a specific instance (MyPrinter._printer._tcp.local).
- `SRV Record`: Specifies the host (myprinter.local) and port (631).
- `A/AAAA Record`: Provides IPv4/IPv6 addresses.