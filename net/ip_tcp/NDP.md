IPv6 邻居发现协议（NDP, Neighbor Discovery Protocol） 是 IPv6 中替代 IPv4 ARP 的机制，用于：

解析目标 IPv6 地址对应的 MAC 地址。

维护邻居的可达性状态。

ip -6 neigh show 会显示：

已知的 IPv6 邻居地址（同一链路层网络中的设备）。

对应的 MAC 地址。

邻居状态（如 REACHABLE、STALE、DELAY、INCOMPLETE 等）。

. 邻居状态（Neighbor States）
IPv6 邻居缓存表的状态反映了目标设备的可达性，常见状态包括：

状态	说明
REACHABLE	邻居确认可达（最近收到过响应，通信正常）。
STALE	邻居可能不可达，但未主动验证（超过一定时间未通信）。
DELAY	系统正在等待验证邻居的可达性（延迟探测）。
INCOMPLETE	正在解析 MAC 地址（NDP 请求已发送，但未收到响应）。
FAILED	解析失败（无法获取 MAC 地址，通常目标不存在或网络问题）。
PERMANENT	静态记录（手动配置，不会过期）。

清除所有邻居缓存 `sudo ip -6 neigh flush all`