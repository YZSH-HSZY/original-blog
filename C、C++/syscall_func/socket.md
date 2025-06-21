# socket
socket相关的系统调用笔记

> Socket本质上是应用层与TCP/IP协议族通信的中间软件抽象层, 是一组接口/门面模式，把复杂的TCP/IP协议族隐藏在Socket接口后面

## 使用

添加头文件 `include <sys/socket.h>`

### socket创建

`int socket(int domain, int type, int protocol);`

创建用于通信的socket端点, 返回指向该端点的文件描述符; 成功则返回当前未打开的最小文件描述符编号
```sh
Arguments:
- domain: 指定通信域, 选择通信使用的协议簇, 可选值如:
    * AF_UNIX: 本机通信(man 7 unix)
    * AF_LOCAL: AF_UNIX的同义词
    * AF_INET: IPv4协议(man 7 ip)
    * AF_AX25: 业余无线电AX.25协议(man 4 ax25)
    * AF_IPX: IPX-Novell协议
    * AF_APPLETALK: 路由协议组(man 7 ddp)
    * AF_X25: ITU-T X.25/ISO/IEC 8208协议(man 7 x25)
    * AF_INET6: IPv6协议(man 7 ipv6)
    * AF_DECnet: DECet协议
    * AF_KEY: 密钥管理协议, 最初用于IPsec
    * AF_NETLINK: 内核用户接口设备(man 7 netlink)
    * AF_PACKET: 低级packet接口(man 7 packet)
    * AF_RDS: RDS可靠数据报协议(man 7 rds)
    更多地址簇相关细节参address_families(7)
- type: 指定socket类型
    * SOCK_STREAM: 提供可靠的、基于连接的字节流
    * SOCK_DGRAM: 支持数据报(无连接、最大长度固定的不可靠消息)
    * SOCK_SEQPACKET: 为固定最大长度的数据报提供一个有序、可靠、基于双向连接的数据传输路径,每次输入系统调用都要求使用者读取整个数据包
    * SOCK_RAW: 提供原始网络协议访问
    * SOCK_RDM: 提供不保证排序的可靠数据报层
    * SOCK_PACKET: 过时, 不应该在新程序中使用(参packet(7))
    注意,某些套接字类型可能未被协议簇实现
- protocol: 指定套接字使用的特定协议
    通常,在给定的协议族中,只有一个协议存在以支持特定的套接字类型;在这种情况下,可以将protocol指定为0
    然而,可能存在许多协议,在这种情况下,必须以这种方式指定一个特定的协议.要使用的协议号特定于要在其中进行通信的domain(参protocols(5))
    关于如何将协议名称字符串映射到协议编号(参见getprotoent(3))
    类unix平台上支持的proto定义在/usr/include/linux/in.h或/usr/include/netinet/in.h中, 部分示例如下:
    * IPPROTO_IP: TCP虚拟协议
    * IPPROTO_ICMP: 因特网控制消息协议
    * IPPROTO_IGMP: 互联网组管理协议
    * IPPROTO_IPIP: IPIP隧道(旧的KA9Q隧道使用94)
    * IPPROTO_TCP: 传输控制协议
    * IPPROTO_EGP: 外部网关协议
    * IPPROTO_PUP: PUP协议
    * IPPROTO_UDP: 用户数据包协议
```

#### 几种特定的socket示例

- `socket(AF_INET6, SOCK_RAW, IPPROTO_RAW)` 手动填充ip首部, 传统由内核自动填充

### socket选项

#### SO_REUSEADDR/SO_REUSEPORT的连接复用

- `SO_REUSEADDR` 用于通知内核, 设置socket可重用端口(连接为 `TIME_WAIT` 状态占用的), 在服务程序停止后立即重启时十分有用
> 如 `netstat -ano|grep 8080` 显示的存在8080的TIME_WAIT连接
`tcp        0      0 127.0.0.1:8080          127.0.0.1:38358         TIME_WAIT   等待 (53.98/0/0)`
> 此时如果重启进程(未设置`SO_REUSEADDR`)会报 `Address already in use`, 设置此选项可使用该端口
- `SO_REUSEPORT` 允许不同进程socket完全重复绑定(在相同ip和port并且均设置此选项), 内核会自动分配连接给不同的进程

**注意** 
- `SO_REUSEADDR`和`SO_REUSEPORT`需要内核选项`net.ipv4.tcp_tw_reuse`/`net.ipv4.tcp_timestamps`开启
- 使用 `sysctl net.ipv4.tcp_tw_reuse`查看对应内核参数值, 0关闭, 1允许TIME_WAIT复用, 2仅允许环回地址复用
- `TIME_WAIT` 是主动关闭连接方断开连接的最后一个状态, 因此在复现`SO_REUSEADDR`行为时需要服务端主动关闭连接

> 参考文档:
- [小林coding](https://zhuanlan.zhihu.com/p/450296852)

#### IPPROTO_IPV6

设置是否仅允许IPV6通信, 1表示套接字只能处理 IPv6 流量, 0表示套接字可以同时处理 IPv6 和 IPv4 流量(通过 IPv4 映射地址，如 `::FFFF:192.168.1.1`)

#### CtTestApplication

组播数据回送(即发送方是否接受自身发送出的数据)

**注意** 其行为在window/unix平台上表现不一致
> 比较流行说法是window应用到接受者,unix应用到发送者下
> 即Window: 本地的两个程序, ON-->OFF(not receive); OFF-->ON(receive)
> Unix: ON-->OFF(receive); OFF-->ON(not receive)

#### IPV6_ADD_MEMBERSHIP

在指定接口上加入多播组

> example:
`setsockopt(_multicast_sock, IPPROTO_IPV6, IPV6_ADD_MEMBERSHIP, (char*)&group, sizeof(group))`

#### IPV6_DROP_MEMBERSHIP
在指定接口上退出多播组

#### setsockopt
```c
int setsockopt(int sockfd, int level, int optname,
    const void optval[.optlen],
    socklen_t optlen);
``` 

操作由文件描述符sockfd引用的套接字的选项, 选项可能存在于多个协议级别; 它们被套接字层的上层使用

### 一些设置socket选项的示例

- `setsockopt(_unicast_sock.load(), IPPROTO_IPV6, IPV6_V6ONLY, reinterpret_cast<char *>(&yes),sizeof(yes));`: 设置socket仅允许IPV6通信
- `setsockopt(sock, SOL_SOCKET, SO_REUSEPORT, reinterpret_cast<void *>(&yes), sizeof(yes))`: 设置支持复用端口进行连接

### socket发送

#### sendto

```c
ssize_t sendto(int sockfd, const void buf[.len], size_t len, int flags,
    const struct sockaddr *dest_addr, socklen_t addrlen);
```

> flags由多个参数按位异或组成
> - `MSG_CONFIRM`: