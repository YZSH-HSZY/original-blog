# hyper-v

window的部分版本自带Hyper-V虚拟机, 可以使用其来进行不同环境开发


> 资源参考:
- [三方window镜像iso下载(支持指定版本号)](https://uupdump.net/)
- [hyper-v版本支持的系统区别](https://learn.microsoft.com/zh-cn/windows-server/virtualization/hyper-v/plan/should-i-create-a-generation-1-or-2-virtual-machine-in-hyper-v)

## example

### 新建虚拟机

1. hyper-v管理器 --> 新建, 之后根据提示操作
> Win11只支持第 2 代虚拟机, 32位的win10仅在第一代支持
> 内存必须>20G, win10系统占17G

### 动态磁盘扩展和c盘扩展

- hyper-v管理器 --> 编辑磁盘 --> 扩展
- 此电脑 --> 管理 --> 磁盘管理 --> 选中c盘 --> 扩展卷

### hyper-v挂载物理机磁盘

在 `连接 --> 显示选项 --> 本地资源 --> 驱动器 --> 勾选对应磁盘`

### 物理机挂载虚拟机磁盘镜像文件


## 问题

### window系统初始启动时无法进入系统

选中>链接>启动(在启动的同时一直不停的上下按动f2键, 进入安装界面)

### window11虚拟机无法启动

虚拟处理器必须大于2

### 默认Default Switch网络适配器只能单边访问(V-Machine->Host)

Hyper-V 默认交换机（Default Switch）的 NAT 过滤和防火墙策略。默认允许虚拟机主动访问外部网络，但默认阻止外部网络（包括宿主机）主动访问虚拟机。

> 解决方案: 在虚拟机的网络防火墙中打开 `ICMP回显` 的入站规则