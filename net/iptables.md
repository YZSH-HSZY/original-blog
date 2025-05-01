# iptables
iptables 为一用户空间命令行程序，用于配置 Linux 数据包过滤和网络地址转换 （NAT）规则集。它面向系统和网络管理员

## EXAMPLE

```sh
# 允许外部访问本地9022端口
iptables -A INPUT -p tcp --dport 9022 -j ACCEPT

# 设置NAT转发规则
iptables -t nat -A PREROUTING -p tcp --dport 9022 -j DNAT --to-destination 192.100.1.11:22
iptables -t nat -A POSTROUTING -p tcp -d 192.100.1.11 --dport 22 -j SNAT --to-source 192.168.8.14

# 允许转发到目标地址
iptables -A FORWARD -p tcp -d 192.100.1.11 --dport 22 -j ACCEPT

# 检查 NAT 规则是否生效
iptables -t nat -L -n -v
```