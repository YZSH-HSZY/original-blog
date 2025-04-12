# route

route操作网络路由表, window系统提供的命令行工具, 用于查看、添加、删除或修改本地 IP 路由表

**注意** Windows 路由表遵循 "最长前缀匹配"(Longest Prefix Match), 即掩码更长的路由优先匹配

## USAGE

```bat
ROUTE [-f] [-p] [-4|-6] command [destination]
                  [MASK netmask]  [gateway] [METRIC metric]  [IF interface]
:: Options:
    -f 清除所有网关项的路由表
    -p 与 ADD 命令结合使用时, 将路由设置为在系统引导期间保持不变(即重启也生效)
    -4 强制使用 IPv4
    -6 强制使用 IPv6
:: Command
    PRINT 打印路由
    ADD 添加路由
    DELETE 删除路由
    CHANGE 修改现有路由
```

## example
- 显示路由表 `route print`
- 显示指定接口的路由表 `route print if <iface-index>`
- 将指定网络走特定路由 `route add 223.168.1.0 mask 255.255.255.0 192.168.177.94 if 29 -p`
> `-p` 表示永久路由(重启后仍然有效)
> `if 29` 指定接口索引(从您的接口列表看, 29对应的是以太网2)