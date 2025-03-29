# ipv6

## bug

### 向不存在的 IPv6 地址发送 UDP 数据包时，tcpdump 可能无法捕获该数据包

1. 数据包未真正离开主机
IPv6 邻居发现（NDP）失败
ping6 不存在的地址会显示 Destination unreachable

2. 协议栈丢弃数据包
本地协议栈拦截: 系统检测到目标不可达（如无路由或邻居不可达），可能在 内核层 直接丢弃数据包，不会传递给网卡驱动，因此 tcpdump 无法捕获
3. 过滤规则干扰
如果 tcpdump 使用了过滤条件（如 host fe80::1234），可能因地址拼写错误或范围限制（如 scope link 地址未指定接口）导致过滤失效

检查 NDP 状态 `ip -6 neigh show`
查看内核丢包统计（IPv6） netstat -s -6 | grep -i "unreachable\|dropped"

临时关闭 ICMPv6 错误响应 `sysctl -w net.ipv6.icmp.echo_ignore_all=1`

链路本地地址（Scope Link）的特殊性
IPv6 链路本地地址（如 fe80::1%eth0）仅在同一链路层（同一网段）有效，但向自身发送时仍会被内核优化为环回路径。

