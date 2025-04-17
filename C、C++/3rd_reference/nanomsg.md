# nanomsg

nanomsg 是一个套接字库，提供了几种常见的通信模式。旨在使网络层快速、可扩展且易于使用。它是用 C 语言实现的，适用于各种OS，无需进一步的依赖。

> nanomsg提供以下扩展性协议:
- PAIR: 简单的一对一通信
- BUS: 简单的多对多通信
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