## `<arpa/inet.h>`

### inet_ntop/inet_pton

> Usage: 包含 `#include <arpa/inet.h>`, 链接`-lc`
> inet_ntop: 将IPv4和IPv6地址从二进制格式转换为文本格式
> inet_pton: 将IPv4和IPv6地址从文本格式转换为二进制格式

### ntohl, ntohs, htonl, htons

这些函数用于处理网络字节序和主机字节序之间的转换，是网络编程中不可或缺的工具。


|函数	|作用	                          |转换方向                    |
|-------|---------------------------------|--------------------------|
|ntohl	|网络字节序转主机字节序 (32位)	    |network to host long       |
|ntohs	|网络字节序转主机字节序 (16位)	    |network to host short      |
|htonl	|主机字节序转网络字节序 (32位)	    |host to network long       |
|htons	|主机字节序转网络字节序 (16位)	    |host to network short      |

字节序问题：

大端序(Big-endian)：高位字节存储在低地址

小端序(Little-endian)：低位字节存储在低地址

网络协议使用大端序作为标准字节序

平台差异：

x86/ARM处理器通常是小端序

网络传输需要统一的大端序
