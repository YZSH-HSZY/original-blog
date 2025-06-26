# io文档

这个文档记录linux下一些io操作的笔记和实践

> 参考文档
* [野火 linux开发文档](https://doc.embedfire.com/linux/imx6/base/zh/latest/system_programing/socket_io.html)


## io分类

在操作系统中，程序运行的空间分为内核空间和用户空间，用户空间所有对io操作的代码（如文件的读写、socket的收发等）都会通过系统调用进入内核空间完成实际的操作。因此了解不同种类的io，可以在高并发/高性能等应用场景中，选择不同的方案，以获取最佳平衡.

### 同步io

在某个应用程序运行时，如果需要读写某个文件，此时就发生了 I/O 操作，在I/O操作的过程中，系统会将当前线程挂起，而其他**需要CPU执行的代码就无法被当前线程执行**，这就是同步I/O操作，因为一个IO操作就阻塞了当前线程，导致其他代码无法执行。

### 异步io

当程序需要对I/O进行操作时，异步io只发出I/O操作的指令，并不等待I/O操作的结果，然后就去执行其他代码了。一段时间后，当I/O返回结果时，再通知CPU进行处理。这样用户空间中的程序**不需要等待内核空间中的 I/O 完成实际操作**，就可执行其他任务，提高CPU的利用率。

### 阻塞io

当用户进程调用了 read()/recvfrom() 等系统调用函数，它会进入内核空间中，当这个网络I/O没有数据的时候，内核就要等待数据的到来，而在用户进程这边，整个进程会被阻塞，直到内核空间返回数据。当内核空间的数据准备好了，它就会将数据从内核空间中拷贝到用户空间，此时用户进程才解除阻塞的的状态，重新运行起来。

> 阻塞I/O的特点就是在IO执行的**两个阶段（用户空间与内核空间）都被阻塞了**

### 非阻塞io

当用户进程调用 read()/recvfrom() 等系统调用函数时，如果内核空间中的数据还没有准备好，那么它并不会阻塞用户进程，而是立刻返回一个error。

对于应用进程来说，它发起一个 read() 操作后，并不需要等待，而是马上就得到了一个结果。用户进程判断结果是一个 error 时，它就知道内核中的数据还没有准备好，那么它可以再次调用 read()/recvfrom() 等函数。

> 非阻塞I/O的特点是用户进程需要不断的 **主动询问** 内核空间的数据准备好了没有。

### 多路复用io

多路复用I/O就是我们说的 `select`/`poll`/`epoll` 等操作，复用的好处就在于 单个进程 就可以同时处理 多个 网络连接的I/O，能实现这种功能的原理就是 `select`/`poll`/`epoll` 等函数会不断的 轮询 它们所负责的所有 socket ，当某个 socket 有数据到达了，就通知用户进程。

#### io多路复用的适用场景

> I/O复用适用于以下情况：

1. 当客户处理多个描述符时
2. 服务器在高并发处理网络连接的时候
3. 服务器既要处理监听套接口，又要处理已连接套接口，一般也要用到I/O复用
4. 如果一个服务器即要处理TCP，又要处理UDP，一般要使用I/O复用
5. 如果一个服务器要处理多个服务或多个协议，一般要使用I/O复用

#### select

select 属于 `synchronous I/O multiplexing`, select允许程序监视多个文件描述符，直到一个或多个文件描述符"准备好"进行某类I/O操作(例如: 可能的输入)。如果一个文件描述符可以执行相应的I/0操作，那么它就被认为准备好了(例如: read or sufficiently small write), 此时select不会阻塞

**WARNNING** select 只能监视FD_SETSIZE小于1024的文件描述符数---对于许多现代应用程序来说，这是一个不合理的低限制;但是这个限制不会改变。所有现代应用程序都应该使用poll或epoll，它们不会受到此限制。

> select的缺点
   1. 每次调用 select, 都需要把 fd 集合从用户态拷贝到内核态，这个开销在 fd 很多时会很大。
   2. 同时每次调用 select 都需要在内核遍历传递进来的所有 fd ，这个开销在 fd 很多时也很大。
   3. 每次在 select() 函数返回后，都要通过遍历文件描述符来获取已经就绪的 socket 。
   4. select 支持的文件描述符数量太小了，默认是 1024 。

#### poll
poll/ppoll 等待文件描述符上的某个事件, 其执行和select类似, poll等待一组文件描述符中的一个准备好执行I/O

> poll的缺点
   1. 包含大量文件描述符的数组被整体复制于用户态和内核的地址空间之间，而不论这些文件描述符是否就绪
   2. 同select一样, 它的开销随着文件描述符数量的增加而线性增大

#### epoll
epoll I/0事件通知功能, 相对于`select`/`poll`, 更加灵活。epoll API执行与poll类似的任务：监视多个文件描述符，以查看它们中的任何一个是否可能实现I/0。

> epoll API既可以用作边缘触发接口，也可以用作水平触发接口，并且可以很好地扩展到大量监视的文件描述符。
> epoll API的核心概念是epoll实例，这是一个内核内的数据结构，从用户空间的角度来看，它可以被视为两个列表的容器
> - 兴趣列表(有时也称为epoll set): 进程已注册要监视的一组文件描述符。
> - 就绪列表: 为I/O"准备好"的文件描述符集合。就绪列表是兴趣列表中文件描述符的子集（或者更准确地说，是对文件描述符的一组引用）。作为对这些文件描述符的I/0活动的结果，就绪列表由内核动态填充。

#### io多路复用的优缺点

> 与多进程和多线程技术相比， I/O多路复用技术的最大优势是系统开销小，系统不必创建进程/线程，也不必维护这些进程/线程，从而大大减小了系统的开销。但select，poll，epoll本质上都是同步I/O，因为他们都需要 在读写事件就绪后自己负责进行读写 ，也就是说这个读写过程是 阻塞的，而异步I/O则无需自己负责进行读写，异步I/O的实现会负责把数据从内核拷贝到用户空间。

## IO阻塞总结

IO操作大致分为两个阶段:
1. 等待数据准备完成
2. 数据从内核空间拷贝至用户空间

**不同IO分类的阻塞阶段**

> - 阻塞IO: 在两个阶段上面都是阻塞的
> - 非阻塞IO: 在第1阶段，程序不断的轮询直到数据准备好，第2阶段还是阻塞的
> - IO复用: 在第1阶段，当一个或者多个IO准备就绪时，通知程序，第2阶段还是阻塞的，在第1阶段还是轮询实现的，只是所有的IO都集中在一个地方，这个地方进行轮询
> - 异步IO: 第1,2阶段都不阻塞，常用的异步IO模型:如 windows之上的iocp,linux AIO等

**因此`阻塞IO`/`非阻塞IO`/`多路复用IO`均属于同步IO**

## 使用示例

### epoll

```c
int epoll_fd = epoll_create1(0);
if (epoll_fd == -1) {
   perror("epoll_create1");
   exit(1);
}

for (auto &service : unicast_services) {
   struct epoll_event event_;
   event_.events = EPOLLIN | EPOLLOUT;
   event_.data.fd = service->GetSocket();
   if (epoll_ctl(epoll_fd, EPOLL_CTL_ADD, event_.data.fd, &event_) == -1) {
      perror("epoll_ctl ADD");
   }
}
struct epoll_event events[MAX_ONENET_APP_SERVICE_NUM + 1 - 2];
char buffer[2048];
struct sockaddr_in6 peer_addr;
socklen_t peer_len = sizeof(peer_addr);

while (true) {
   int nfds = epoll_wait(epoll_fd, events, sizeof(events) / sizeof(events[0]), -1);
   if (nfds == -1) {
      perror("epoll_wait");
      exit(1);
   }
   for (int i = 0; i < nfds; i++) {
      int fd = events[i].data.fd;
      if (events[i].events & EPOLLIN) {
         recvfrom(fd, buffer, sizeof(buffer), 0, (struct sockaddr *)&peer_addr, &peer_len);
      } else if (events[i].events & EPOLLOUT) ...
   }
}
```