# NDP

IPv6 邻居发现协议(NDP, Neighbor Discovery Protocol) 是 IPv6 中替代 IPv4 ARP 的机制，用于解析目标 IPv6 地址对应的 MAC 地址。维护邻居的可达性状态

节点(主机和路由器)使用邻居发现来确定已知驻留在连接链路上的邻居的链路层地址，并快速清除无效的缓存值

[NDP-RFC文档](https://datatracker.ietf.org/doc/html/rfc4861)

## 术语

- IP: 互联网协议版本 6
- node(节点): 实现 IP 的设备
- ICMP(Internet Control Message Protocol, Internet 控制消息协议): Internet 协议版本 6
- router(路由器): 转发未明确寻址到自身的 IP 数据包的节点
- host(主机): 非路由器的任意节点
- upper layer(上层): IP 之上的协议层, 如TCP/UDP/OSPF
- link(链路): 节点可以在链路层通过其进行通信的通信设施或介质
- interface(接口): 节点与链接的连接
- neighbors(邻居): 连接到同一链路的节点
- address(地址): 接口或一组接口的 IP 层标识符
- anycast address(任播地址): 一组接口的标识符（通常属于不同的节点）。发送到任播地址的数据包将被传递到该地址所标识的接口之一

## 相关命令

- `ip -6 neigh show` 显示如下
    * `已知的 IPv6 邻居地址(同一链路层网络中的设备)`
    * `对应的 MAC 地址`
    * `邻居状态(Neighbor States)`, 如 REACHABLE、STALE、DELAY、INCOMPLETE 等
- 清除所有邻居缓存 `sudo ip -6 neigh flush all`

### 邻居状态(Neighbor States)

IPv6 邻居缓存表的状态反映了目标设备的可达性，常见状态包括

|状态           	|说明                                                |
|-------------------|---------------------------------------------------|
|REACHABLE          |邻居确认可达（最近收到过响应，通信正常）               |
|STALE          	|邻居可能不可达，但未主动验证（超过一定时间未通信）      |
|DELAY          	|系统正在等待验证邻居的可达性（延迟探测）               |
|INCOMPLETE         |正在解析 MAC 地址（NDP 请求已发送，但未收到响应）      |
|FAILED         	|解析失败（无法获取 MAC 地址，通常目标不存在或网络问题） |
|PERMANENT          |静态记录（手动配置，不会过期）                         |

### 特殊地址 address

- all-nodes multicast address: 到达所有节点的链路本地范围地址(FF02::1)
- all-routers multicast address: 到达所有路由器的链路本地作用域地址(FF02::2)
- solicited-node multicast address: 根据请求目标的地址计算的链路本地范围多播地址
- link-local address: 具有可用于到达邻居的仅链路范围的单播地址
- unspecified address: 指示缺少地址的保留地址值(0::0), 不被用作目的地地址

## message format

### Neighbor Solicitation Message Format(邻居请求消息格式)

节点发送邻居请求以请求目标节点的链路层地址，同时也向目标提供它们自己的链路层地址。当节点需要解析地址时，邻居请求是多播的，而当节点试图验证邻居的可达性时，邻居请求是单播的。

- IP Fields:
    * Source Address
    * Destination Address
    * Hop Limit
- ICMP Fields:
    * Type: 135(0x87), 1B
    * Code: 0, 1B
    * Checksum: ICMP checksum, 2B
    * Reserved: 必须被发送方初始化为零, 4B
    * Target Address: 请求目标的 IP 地址, 它不能是多播地址
    * Possible options: 可能的选择
        * Source link-layer address: 源链路层地址发送方的链路层地址, 源链路层地址发送方的链路层地址

### Neighbor Advertisement Message Format(邻居通告消息格式)
节点响应于邻居请求而发送邻居通告，并且发送未经请求的邻居通告以便(不可靠地)快速传播新信息

- IP Fields:
    * Source Address
    * Destination Address
    * Hop Limit
- ICMP Fields:
    * Type: 136(0x88), 1B
    * Code: 0, 1B
    * Checksum: ICMP checksum, 2B
    * R: Router flag, 1b; 当设置时,R 位表示发送方是路由器
    * S: Solicited flag, 1b; 当设置时,指示数据包是响应于来自目的地地址的邻居请求而发送的
    * O: Override flag, 1b; 当设置时,指示通告应覆盖现有缓存条目并更新缓存的链路层地址
    * Reserved: 必须被发送方初始化为零, 29b
    * Target Address: 请求目标的 IP 地址, 它不能是多播地址
    * Possible options: 可能的选择
        * Target link-layer address: 目标链路层地址目标的链路层地址, 通告的发送者