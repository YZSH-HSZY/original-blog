# nanomsg

nanomsg 是一个套接字库，提供了几种常见的通信模式。旨在使网络层快速、可扩展且易于使用。它是用 C 语言实现的，适用于各种OS，无需进一步的依赖。

> nanomsg提供以下扩展性协议:
- PAIR: 简单的一对一通信
- BUS: 简单的多对多或一对多通信
- REQREP: 允许构建无状态服务集群来处理用户请求
- PUBSUB: 将消息分发给大量感兴趣的订阅者
- PIPELINE: 聚合来自多个来源的消息，并在多个目的地之间对它们进行负载均衡
- SURVEY: 允许一次性查询多个应用程序的状态

> 支持的传输机制如下:
- INPROC: 在一个进程内的传输(线程、模块等之间)
- IPC: 在单台机器不同进程间的传输
- TCP: 通过 TCP 进行网络传输
- WS: 基于 TCP 的 websockets


[nanomsg官网](https://nanomsg.org/)

## BUS机制

> 参考文档
- [官方bus介绍](https://nanomsg.org/gettingstarted/bus.html)

> BUS 模式的核心规则
1. `bind()`: 表示该节点可以接收发送到该地址的消息, 相当于声明自己的接收地址
2. `connect()`: 表示该节点可以向目标地址发送消息, 相当于声明自己要发送给谁

**注意** Nanomsg 的 BUS 模式会自动建立反向通道(只有node存在bind地址并且存在其他节点connect到该地址), 如下所示:
```
bus1 = test_socket (AF_SP, NN_BUS);
test_bind (bus1, SOCKET_ADDRESS_A);
bus2 = test_socket (AF_SP, NN_BUS);
test_connect (bus2, SOCKET_ADDRESS_A);
test_send (bus1, "AH");
rc = nn_recv (bus2, buf, 3, 0);
errno_assert (rc >= 0);
buf[rc] = '\0';
printf("\nrevc-->:len:%d;msg:%s\n", rc, buf); // revc-->:len:2;msg:AH
```

###  BUS注意事项

1. 如果使用tcp作为bus的socket绑定, 在调用send和revc时, 需要等待一段时间, 用于tcp慢启动
2. nanomsg的通信时独有协议的实现, 在进行网络socket测试时, 传统nc工具不能很好兼容
3. bus的多对多机制通过星状拓扑实现(及每个nn_socket都有自身地址并连接到其他地址)

### BUS测试

- `./nanocat --bus --bind tcp://127.0.0.1:12345 --connect tcp://127.0.0.1:12345 --ascii` 总线模式绑定并连接到tcp::12345, 显示接受的消息的ASCII部分(所有非ascii字符替换为点)
- `./nanocat -i 3 --data lp  --bus --connect tcp://127.0.0.1:12345 --ascii` 总线模式连接到tcp::12345, 并每3s发送数据lp

## C-API

### 通用结构

#### nn_socket

#### nn_setsockopt

设置socket选项
> 原型: `int nn_setsockopt (int s, int level, int option, const void *optval, size_t optvallen)`
- `s`: 指定socket
- `level`: 指定协议等级, `NN_SOL_SOCKET`(通用套接字), 特定socket选项(如`NN_SUB`)


#### nn_bind

**注意** 一个地址只能被`bind`一次, 一个`nn_socket`可以`bind`多个地址


#### nn_pollfd

```c
struct nn_pollfd {
    int fd;
    short events;
    short revents;
};
```
用于`nn_poll`的专属结构, 检查指定socket可读性和/或可写性

> 参数`events` 指定要检查哪些事件, 支持值有:
- `NN_POLLIN`: 检查fd套接字可以无阻塞接受至少一条数据
- `NN_POLLOUT`: 检查fd套接字可以无阻塞发送至少一条数据
> 参数`revents` 在nn_poll函数返回后, 包含fd的`NN_POLLIN`和`NN_POLLOUT`的按位组合

### nn_poll

轮询一组SP套接字的可读性和/或可写性

```c
#include <nanomsg/nn.h>
int nn_poll (struct nn_pollfd *fds, int nfds, int timeout);
```

- `fds` 参数是一个包含 `nn_pollfd` 结构的数组，其中 `nfds` 指定数组的大小
- `timeout` 指定无时间时, 函数阻塞的时间(以毫秒为单位)