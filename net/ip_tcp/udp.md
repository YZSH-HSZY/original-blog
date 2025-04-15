# udp
UDP(User Datagram Protocol, 用户数据报协议)是一种简单的、无连接的传输层协议，用于在网络中传输数据。

[UDP-RFC文档](https://datatracker.ietf.org/doc/html/rfc768)

## data format

- 伪首部: `source address(4B)` + `destination address(4B)` + `zero(1B)` + `protocol(1B)` + `UDP length(2B)`
- 首部: `Source Port(2 bytes)` + `Destination Port(2 bytes)` + `Length(2 bytes)` + `Checksum(2 bytes)`
- payload数据

> Checksum计算由 `IP报头`, `UDP 报头`, `数据`组成的伪报文的补码和(2B, 不足尾部零填充)

**注意** 因为校验和Checksum计算的需要, UDP引入伪首部的概念
**注意** 伪首部为虚拟概念, 在实际数据传输中无对应