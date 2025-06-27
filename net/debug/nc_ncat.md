# nc/ncat

nc(netcat) 和 ncat 是网络工具中的"瑞士军刀", 可用于TCP/UDP连接、端口扫描、数据传输等

- nc(netcat): 任意TCP和UDP连接和监听
- ncat: 连接和重定向socket(netcat的改进版, 由Nmap项目开发)

## exmaple

- 向指定地址和端口发送udp数据包 `sudo echo xsaxKL | nc -6u fe80::eed6:8aff:feea:c8a5%eno1 33738`
> 注意: 如果指定ipv6地址是自身,会被内核优化至环回地址(此时抓包需要指定`-I lo`才可捕获对应数据包)
> 注意: 如果指定ipv6是本地链路地址,需要指定网卡(即`%eno1`)
> 广播地址如`ff02::16f`不会被优化至环回
