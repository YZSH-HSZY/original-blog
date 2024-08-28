## vps

vps 是（VirtualPrivateServer 虚拟专用服务器）的简称，其是将一台服务器分割成为多个虚拟专享空间，其有自己的独立操作系统，独立 ip，但这都是虚拟化的.
在这里我们只稍微提一下概念区分，对于个人用户来说 vps 与云服务器的区别不大。以下示例也不过多区分。

### 系统镜像与应用镜像

系统镜像是一个单纯的系统，例 linux 系统，而应用镜像则已配置好应用软件，可以直接将项目部署运行而无需其他繁杂配置，如 nodejs 镜像等。

### window kms激活
`https://hub.nuaa.cf/zbezj/HEU_KMS_Activator/releases`

### 各软件的镜像下载网站
[清华大学开源软件下载镜像站](https://mirrors.tuna.tsinghua.edu.cn/)

### ubuntu20.04 与 ubuntu22.04 的异同

| 20.04             | 22.04             |
| ----------------- | ----------------- |
| GCC 10.3          | GCC 11.2          |
| Hplip 3.20.3      | Hplip 3.21.12     |
| LibreOffice 6.4.7 | LibreOffice 7.3.2 |
| （未引入）        | Pipewire 0.3.48   |
| Python3 3.8.2     | Python3 3.10.1    |
| Samba 4.13        | Samba 4.15        |
| Systemd 245.4     | Systemd 249.11    |

### 配置ubuntu中apt包管理的下载镜像
在操作前请做好备份
```
sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
apt-get clean
apt-get update
```
#### root用户初始化
配置好系统后，如果想切换到root用户，需要先初始化root用户
`sudo passwd root`

### vmware中ubuntu使用

(vmware 17激活码)[https://www.cnblogs.com/shiningrise/p/17049274.html]

#### wmware中ubuntu共享文件夹位置

#### vmware中ubuntu无法使用鼠标滚动

1. 查看`/etc/X11/xorg.conf`配置文件，若无，可能是xserver-xorg-input-all包缺失
- 使用`sudo apt install xserver-xorg-input-all`安装包
- 使用`sudo Xorg -configure`生成xorg.conf配置文件
- 修改xorg.conf内容
```
Section "InputDevice"
 
    Identifier "Configured Mouse"
    Driver "vmmouse"
    Option "Protocol" "ImPS/2"
    Option "CorePointer"
    Option "Device" "/dev/input/mice"
    Option "ZAxisMapping" "4 5"
    Option "Emulate3Buttons" "yes"
 
EndSection
```
**注意** 需要vmware tool工具和gpm包

2. 使用xshell之类的三分ssh工具连接



### xshell 工具介绍

Xshell 是一个强大的安全终端模拟软件，它支持 SSH1, SSH2, 以及 Microsoft Windows 平台的 TELNET 协议。
对开启 sshd 服务的主机可直接连接并使用 xftp 传输文件，而无需其他配置。可以使用学校和家庭版免费使用。

#### xshell backspace键乱码
在session界面，右键选择属性，配置键盘中backspace的键序列为ASCII 127

### xftp下载文件失败
1. xftp与xshell的端口是同一个，在防火墙放行该端口。
2. 查看下载文件是否具有读权限，使用`sudo chmod a+rw <download_file>`为所有用户添加读写权限

### ssh 更改端口

登录进入远程主机后，如果你的主机开放在公网上，那么做好安全措施是十分有必要的。
使用超级权限打开 ssh 配置文件，`vi /etc/ssh/sshd_config`
更改默认端口为你需要设置的端口。

### 查看登录日志

如果你的主机开放在公网，那么遭遇攻击是必然的。如何查看其他设备尝试登录的 IP 和次数，可以有争对性的防护以保护主机。

在/var/log 目录下，有这样 3 个文件 wtmp、btmp、secure。

> 其中 wtmp 记录登录成功的用户记录，btmp 记录登录失败的用户记录。不过这两个文件都是二进制的，同时需 root 权限才能打开。secure 记录所有登录，不过他是文档类型，非法登录用户可以较为方便的对其进行更改。

```
ubuntu@VM-12-17-ubuntu:/var/log$ last
ubuntu   pts/0        <login ip address>    Tue Jul 25 17:02   still logged in
ubuntu   pts/0        <login ip address>    Tue Jul 25 16:39 - 17:02  (00:22)
reboot   system boot  5.4.0-148-generi Tue Jul 25 16:38   still running
ubuntu   pts/0        <login ip address>  Mon Jul 24 17:36 - 19:05  (01:28)
reboot   system boot  5.4.0-148-generi Mon Jul 24 17:36 - 19:05  (01:28)
# last命令默认查看/var/log/wtmp文件内容，
第1列是登录用户，2是终端，3是登录IP，4是登录时间，5是状态（still logged in表处于登录状态）
其中reboot是系统用户，记录重启状态。(still running表系统正在运行)

# lastb默认查看/var/log/btmp文件内容，
ubuntu@VM-12-17-ubuntu:/var/log$ sudo lastb
admin    ssh:notty    189.195.123.54   Mon Jul 24 19:04 - 19:04  (00:00)
admin    ssh:notty    189.195.123.54   Mon Jul 24 19:04 - 19:04  (00:00)
wu       ssh:notty    161.35.79.199    Mon Jul 24 19:04 - 19:04  (00:00)
...
可以看到几乎我刚打开没几小时就开始遭受攻击了。
```

如果你想要看更加详细的记录，可以查看 auth.log 文件。

**统计登录失败的 IP 次数**

```
ubuntu@VM-12-17-ubuntu:/var/log$ sudo lastb | awk '{print $3}' | sort | uniq -c | sort -n
      1
      1 111.181.142.213
      2 161.35.79.199
      2 21
      2 Mon
      4 189.195.123.54
     50 211.193.31.52
```

**限制用户登录**

1. 编辑 sshd_config 文件，添加 AllowUsers 或 DenyUsers 项，值格式如<用户名>@<登录 ip>
2. 配置防火墙

### iptables


## tmux
tmux是一个 terminal multiplexer（终端复用器），它可以启动一系列终端会话。
tmux将会话session和窗口分开，在关闭命令窗口后，仍在运行的进程不会停止

你可以使用 `sudo apt-get install tmux` 安装

**作用**
1. 分屏。既可以同时使用多个命令行；
2. 会话与窗口解绑。当窗口意外关闭时，会话并不会终止，后面需要的时候，会话可以再次绑定窗口。尤其当使用SSH远程登录计算机时，可以不受断网的影响

### tmux术语
tmux 采用 client/server架构，主要有四个模块：

server：服务。tmux运行的基础服务，以下模块均依赖于此服务；
session：会话。一个服务可以包含多个会话；
window：窗口。一个会话可以包含多个窗口；
panel：窗格/面板。一个窗口可以包含多个窗格。
执行 tmux 命令时，即开启了一个服务，并创建了一个会话、窗口和窗格。

### 启动tmux
```
# 启动
$ tmux
# 退出
$ exit 或 Ctrl+D
```
在终端窗口上，运行tmux，其实就打开了一个终端与tmux服务的会话。只不过我们可以在tmux会话上层，再次输入’会话‘命令，使tmux上层运行的'会话'与终端窗口进行分离。这里面tmux其实可以称之为**伪窗口**（它其实是会话）。

### 会话相关命令

查看已有会话：tmux ls
新建会话：tmux new -s <session-name>

接入会话：tmux attach -t <session-name> 或 tmux a -t 0
重命名会话：tmux rename-session -t 0 <new-name>
切换会话：tmux switch -t <session-name> 或 tmux s -t 0
杀死会话：tmux kill-session -t <session-name> 或 tmux kill-session -t 0

### 会话操作

#### 分离会话
`$ tmux detach`
执行tmux ls可看到当前所有的tmux伪窗口。

#### 重接会话 
使用伪窗口编号`$ tmux attach -t 0`
使用伪窗口名称`$ tmux attach -t xiaoqi`

#### 杀死会话
彻底关闭某个会话，不想让其再执行
`$ tmux kill-session -t 0`使用会话编号

#### 使用会话名称
$ tmux kill-session -t <name>
切换会话
#### 使用会话编号
$ tmux switch -t 0

#### 使用会话名称
$ tmux switch -t <session-name>
重命名会话
$ tmux rename-session -t 0 <new-name>
#### 列出所有快捷键，及其对应的 Tmux 命令
$ tmux list-keys

#### 列出所有 Tmux 命令及其参数
$ tmux list-commands

#### 列出当前所有 Tmux 会话的信息
$ tmux info

#### 重新加载当前的 Tmux 配置
$ tmux source-file ~/.tmux.conf



### 快捷键相关命令

**注意** tmux 有大量快捷键，所有的快捷键都需要通过前缀键唤起，默认的前缀键是 Ctrl+b。

列出所有快捷键命令 `tmux list-keys`

1. 会话的快捷键
```
s：列出所有会话
d：离开当前会话
$：重命名当前会话
```

2. 窗口的快捷键
```
c：创建一个新窗口
n：切换到下一个窗口
w：从列表中选择窗口
<0~9>：切换到指定编号的窗口，编号显示在状态栏
,：窗口重命名
```

3. 窗格的快捷键
```
%：分成左右两个窗格
"：分成上下两个窗格
z：当前窗格全屏显示，再按一次恢复
q：显示窗格编号
t：在当前窗格显示时间
<arrow key>：光标切换到其他窗格
o：光标切换到下一个窗格
{：左移当前窗格
}：右移当前窗格
Ctrl+o：上移当前窗格
Alt+o：下移当前窗格
space：切换窗格布局
```

### tmux 配置鼠标支持

鼠标支持的内容：
> 用鼠标点击窗格来激活该窗格；
用鼠标拖动调节窗格的大小（拖动位置是窗格之间的分隔线）；
用鼠标点击来切换活动窗口（点击位置是状态栏的窗口名称）；
开启窗口/窗格里面的鼠标支持，用鼠标回滚显示窗口内容，按下shift的同时用鼠标选取文本，使用 ctrl+shift+c、ctrl+shift+v 的方式进行复制粘贴。

1. 配置文件 ~/.tmux.conf ，增加：`set-option -g mouse on`/`set -g mouse on`
2. 你也可以在tmux会话中，使用`ctrl+b`接`:`进入命令模式，输入`set -g mouse on`开启

## 报错
#### ip command not find
使用apt安装`iproute2`包

#### dns解析失效

- 临时配置dns(仅在/etc/resolv.conf不是软连接时生效)
配置`/etc/resolv.conf`文件,添加dns服务器
`echo "nameserver 8.8.8.8" >> /etc/resolv.conf`

**注意** 软连接`/etc/resolv.conf`一般有两种指向
`/run/systemd/resolve/stub-resolv.conf` 只有 ISP 给定的 DNS(系统默认的本地dns服务，地址127.0.0.53)，而自定义 DNS 仅在 `/run/systemd/resolve/resolv.conf` .
**这两个文件的区别**
> 使用 `resolv.conf` 替代`stub-resolv.conf` 将绕过许多 systemd 解析的配置，例如 DNS 应答缓存、每个接口的 DNS 配置、DNSSec 强制执行等。
> 使用 stub-resolv.conf 时，应用程序将向地址为 127.0.0.53 的 systemd 提供的 DNS 存根解析器发出 DNS 请求。此存根解析器会将 DNS 请求代理到 中 systemd-resolved 配置的上游 DNS 解析器，将它想要的任何逻辑应用于这些请求和应答，例如缓存它们。
> 使用 resolv.conf 时，应用程序将直接向 中配置的“真实”（又名上游）DNS 解析器发出 DNS 请求 systemd-resolved 。在这种情况下，仅充当“管理器” resolv.conf ， systemd-resolved 而不是DNS解析器本身。


**注意** 你需要先关闭systemd-resolved进程
`systemctl stop systemd-resolved`

- 配置永久dns`/etc/systemd/resolved.conf`
```
[Resolve]
DNS=114.114.114.114
DNS=8.8.8.8
#FallbackDNS=
#Domains=
#LLMNR=no
#MulticastDNS=no
#DNSSEC=no
#Cache=yes
#DNSStubListener=yes
```
##### 重启systemd-resolved服务
`systemctl restart systemd-resolved.service`

##### 查看dns状态
`systemd-resolve --status`