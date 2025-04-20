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
    SOCK_DGRAM: 支持数据报(无连接、最大长度固定的不可靠消息)
    SOCK_SEQPACKET: 为固定最大长度的数据报提供一个有序、可靠、基于双向连接的数据传输路径；
每次输入系统调用都要求使用者读取整个数据包。

```

### socket选项

#### setsockopt
```c
int setsockopt(int sockfd, int level, int optname,
    const void optval[.optlen],
    socklen_t optlen);
``` 