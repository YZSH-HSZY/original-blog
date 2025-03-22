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
```

## example
- `tcpdump -i eth0 port 80 -w http_traffic.pcap`
- `tcpdump -i ens38 ip proto mdns`