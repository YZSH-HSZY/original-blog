# tcpdump

tcpdump用于转储网络流量, 其作用描述如下:

- tcpdump打印出网络接口上匹配布尔表达式的数据包内容的描述, 支持 `-w <file>` 保存 `packet data` 到文件, 或者使用 `-r <file>` 选项从文件中读取`packet data`以分析
- 所有的使用方法中只有匹配表达式的packet会被tcpdump处理
- 如果不带`-c`标志运行, 将继续捕获数据包，直到被`SIGINT`(通常是`Ctrl+C`)/`SIGTERM`(通常是`kill`命令)信号中断; 使用`-c`标志
 

> 参见 `pcap-filter` 了解包过滤语法

## options

```sh
tcpdump [ -AbdDefhHIJKlLnNOpqStuUvxX# ] [ -B buffer_size ]
        [ -c count ] [ --count ] [ -C file_size ]
        [ -E spi@ipaddr algo:secret,...  ]
        [ -F file ] [ -G rotate_seconds ] [ -i interface ]
        [ --immediate-mode ] [ -j tstamp_type ] [ -m module ]
        [ -M secret ] [ --number ] [ --print ] [ -Q in|out|inout ]
        [ -r file ] [ -s snaplen ] [ -T type ] [ --version ]
        [ -V file ] [ -w file ] [ -W filecount ] [ -y datalinktype ]
        [ -z postrotate-command ] [ -Z user ]
        [ --time-stamp-precision=tstamp_precision ]
        [ --micro ] [ --nano ]
        [ expression ]
Options:
    - `-i <interface>` 监听链路层数据, 未指定-i和-d时默认监听最小eth(不包括回环地址), 如eth0
    - `-n` 禁用 IP/端口解析(显示数字而非域名)
    - `-e` 显示链路层头（MAC 地址）
    - `-A` 用ASCII显示每个包(除去链路级标头)
    - `-X` 打印每个包的头及除去链路级标头的HEX+ASCII数据
    - `-v` 增加 TTL、校验和等头部信息
    - `-vv` 增加 TCP 窗口大小
    - `-vvv` 最高详细度(显示部分应用层数据)
    - `-t` 去掉时间戳
```

## pcap-filter
包过滤器语法, 由pcap_compile(3PCAP)用于将字符串编译成过滤器程序。然后可以将生成的过滤器程序应用于一些数据包流，以确定哪些数据包将被提供给pcap_loop(3PCAP)、pcap_dispatch(3PCAP)、pcap_next(3PCAP)或pcap_next_ex(3PCAP)

> syntax: `{qualifiers} {primitives}`
> `qualifiers = {type|dir|proto}`
>   - `type = host|net|port|portrange <value>`(未指定type 限定符, 默认为host)
>   - `dir = src|dst|src or dst|src and dst|ra|ta|addr1|addr2|addr3|addr4`(ra, ta, addr1, addr2, addr3, addr4 qualifiers只对IEEE 802.11无线局域网层有效)
>   - `proto = ether|fddi|tr|wlan|ip|ip6|arp|rarp|decnet|sctp|tcp|udp`

### 区分net/host限定词

tcpdump 中, net 和 host 是两种不同的过滤条件
- `host`: `host <IP或域名>` 匹配 单个主机
- `net`: `net <网络地址> [mask <子网掩码> | CIDR]` 匹配整个网络或子网

### example
- `'udp && dst host ff02::fb'`
- `'udp && host ff02::fb && src host fe80::eed6:8aff:feea:c8a5'`

## example
- `tcpdump -i eth0 port 80 -w http_traffic.pcap`
- `tcpdump -i ens38 ip proto mdns`
- `tcpdump -n -i eno1 'udp && dst host ff02::fb && src host fe80::eed6:8aff:feea:c8a5' -X -v -v` 16进制+ASCII显示fe80::eed6:8aff:feea:c8a5-->ff02::fb的udp数据包