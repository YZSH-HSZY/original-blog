# linux
[linux标准](https://refspecs.linuxfoundation.org/lsb.shtml)

## linux与unix、posix的关系

unix最开始是操作系统的名字，之后逐渐演变为一种通用的标准。与linux有着相似的外部接口和结构，但区分与linux，unix是专有的，而linux是基于GNU GPL v2 开源的一个系统内核，你可以基于该内核开发自己的发行版。

linux也被称为`类unix系统(unix-like)`，在GPL v2许可下，你可以对源码进行更改、发行等。

posix(Portable Operating System Interface, 可移植操作系统接口) 是一个遵循 `IEEE STD 1003.1` 的标准。包含一系列接口定义(命令行、错误状态、多任务等，区分于具体实现)，linux发行版一般在不同程度上支持posix，由于posix认证昂贵，实际官方认证的linux发行较少。

## service服务管理
服务启动方式`service nginx start` 或 `systemctl start nginx`;

**service与systemctl的区别**
1. linux默认在 `/etc/init.d` 目录下通过脚本文件管理服务，并以服务的名称命名。service命令本质就是通过去 `/etc/init.d` 目录下执行脚本实现。
2. systemctl 是一个新的系统服务管理工具，它是 systemd 系统和服务管理器的一部分。systemd 是一个用于 linux 启动进程的系统和服务管理器。相比之下，systemctl 拥有更加全面的功能，可以用于控制服务的状态，查看服务的状态，重启和重新加载服务，并在服务失败时自动重启服务。对于支持systemd的软件，在安装时会在目录`/usr/lib/systemd/system`下创建server文件

**注意** 可以使用`ps -p 1 -o comm=`显示当前init系统类型: systemd或sysv或init

#### 使用 systemcli 查看服务信息

以 vsftpd 服务为例：
ftp 状态查看：systemctl status vsftpd
启动 ftp 服务：systemctl start vsftpd
重启 ftp 服务：systemctl restart vsftpd
停止 ftp 服务：systemctl stop vsftpd
设置开机自启：systemctl enable vsftpd

- 查看安装服务及其启动状态 `sudo systemctl list-unit-files`

#### 使用/etc/init.d查看服务
```
ubuntu@yzsh:~$ /etc/init.d/ssh status
 * sshd is not running
```

#### 查看引导程序
1. `ps -ef`查找pid为1的程序
2. `stat /sbin/init`
3. `readlink /sbin/init` 

> 输出如下:
```bash
(base) ubuntu@DESKTOP-UAS0QBB:~/work/esp/hello_world$ ps -ef
UID          PID    PPID  C STIME TTY          TIME CMD
root           1       0  1 14:27 ?        00:00:00 /sbin/init
root           2       1  0 14:27 ?        00:00:00 /init
...
(base) ubuntu@DESKTOP-UAS0QBB:~$ stat /sbin/init
  File: /sbin/init -> /lib/systemd/systemd
  Size: 20              Blocks: 0          IO Block: 4096   symbolic link
Device: 820h/2080d      Inode: 372701      Links: 1
Access: (0777/lrwxrwxrwx)  Uid: (    0/    root)   Gid: (    0/    root)
...
(base) ubuntu@DESKTOP-UAS0QBB:~$ readlink /sbin/init
/lib/systemd/systemd
```

#### wsl2使用systemd
参[wsl2使用systemd文档](https://learn.microsoft.com/zh-cn/windows/wsl/systemd)

在wsl2中使用systemd管理服务,在`/etc/wsl.conf`配置中,添加如下:
```ini
[boot]
systemd=true
```

使用`systemctl list-unit-files --type=service`查看systemd是否运行

#### 问题systemd已运行,但使用systemctl查询仍报错
```sh
(base) ubuntu@DESKTOP-UAS0QBB:~$ systemctl status sshd
System has not been booted with systemd as init system (PID 1). Can't operate.
Failed to connect to bus: Host is down
```
> 解决方法: 
1. 检查`wsl.conf`中`systemd`有无开启，重启wsl2
2. 如果不行可重新安装systemctl,移除冲突三方包 `sudo apt install -y --allow-remove-essential systemctl`



## linux使用示例

### cd 命令常用示例

cd ..                   返回上一级目录

cd 或 cd ~           返回 home 目录

cd -                    返回刚才的目录

cd - 目录名       返回指定目录

### 查看linux信息

#### 查看系统信息 uname

`uname -m` 直接显示 Linux 系统架构
`lsb_release -a` 显示系统版本信息和别名

#### 查看系统版本
```
ubuntu@ubuntu:~$ cat /proc/version
Linux version 5.4.0-169-generic (buildd@lcy02-amd64-102) (gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.2)) #187-Ubuntu SMP Thu Nov 23 14:52:28 UTC 2023

ubuntu@ubuntu:~$ cat /etc/os-release 
NAME="Ubuntu"
VERSION="18.04.5 LTS (Bionic Beaver)"
ID=ubuntu
```

#### linux获取shell编码
```
ubuntu@ubuntu:~$ locale
LANG=en_US.UTF-8
LANGUAGE=
LC_CTYPE="en_US.UTF-8"
LC_NUMERIC="en_US.UTF-8"
LC_TIME="en_US.UTF-8"
LC_COLLATE="en_US.UTF-8"
LC_MONETARY="en_US.UTF-8"
LC_MESSAGES="en_US.UTF-8"
LC_PAPER="en_US.UTF-8"
LC_NAME="en_US.UTF-8"
LC_ADDRESS="en_US.UTF-8"
LC_TELEPHONE="en_US.UTF-8"
LC_MEASUREMENT="en_US.UTF-8"
LC_IDENTIFICATION="en_US.UTF-8"
LC_ALL=
```

### 查看linux资源消耗

#### 查看文件的磁盘使用情况
查看指定文件/目录存储消耗 `du -sh [path...]`
选项 `-x` 对每一个参数，列出总大小；`-h` 以符合人类可读方式显示

#### 查看磁盘使用情况
查看指定文件/目录所在磁盘分区的存储消耗 `df -h [path...]`
`-h` 以符合人类可读方式显示

#### 查看进程资源使用情况
```
wheeltec@wheeltec:~$ ps -la
F S   UID   PID  PPID  C PRI  NI ADDR SZ WCHAN  TTY          TIME CMD
0 S  1000 14717 11547  1  80   0 - 109674 poll_s pts/1   00:00:22 terminator
0 S  1000 15177 14749  1  80   0 - 100944 poll_s pts/0   00:00:08 roscore
0 S  1000 15688 15207  2  80   0 - 101149 poll_s pts/3   00:00:07 roslaunch
0 R  1000 16339 16131  0  80   0 -  2384 -      pts/4    00:00:00 ps
```
选项 `-l` 列出详细信息；`-a` 列出所有进程

#### 查看当前内存使用情况
```
wheeltec@wheeltec:~$ free -h
total        used        free      shared  buff/cache   available
Mem:           3.9G        955M        1.6G         29M        1.4G        2.8G
Swap:          1.9G          0B        1.9G
```

#### 查看最大内存使用程序
- `top -o %MEM` 以内存排序
- `ps aux --sort -%cpu` 选项 `--sort` 接收多个参数`[+|-]key,...`, +为递增

#### 查看系统硬件信息
```
wheeltec@wheeltec:~$ lshw
WARNING: you should run this program as super-user.
wheeltec                    
    description: Computer
    product: NVIDIA Jetson Nano Developer Kit
    serial: 142162210373808081fd
    width: 64 bits
    capabilities: smp cp15_barrier setend swp
  *-core
       description: Motherboard
       physical id: 0
     *-cpu:0
          description: CPU
          product: cpu
          physical id: 0
          bus info: cpu@0
          size: 1428MHz
          capacity: 1428MHz
          capabilities: fp asimd evtstrm aes pmull sha1 sha2 crc32 cpufreq
     *-memory
          description: System memory
          physical id: 7
          size: 3964MiB
     *-pci
          description: PCI bridge
          product: NVIDIA Corporation
          vendor: NVIDIA Corporation
          physical id: 2
          bus info: pci@0000:00:02.0
          version: a1
          width: 32 bits
          clock: 33MHz
          capabilities: pci normal_decode bus_master cap_list
          configuration: driver=pcieport
          resources: irq:83 ioport:1000(size=4096) ioport:20000000(size=1048576)
        *-network
             description: Ethernet interface
             product: RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller
             vendor: Realtek Semiconductor Co., Ltd.
             physical id: 0
             bus info: pci@0000:01:00.0
             logical name: eth0
             version: 19
             serial: 48:b0:2d:6b:cc:f4
             size: 100Mbit/s
             capacity: 1Gbit/s
             width: 64 bits
             clock: 33MHz
             capabilities: bus_master cap_list ethernet physical tp 10bt 10bt-fd 100bt 100bt-fd 1000bt-fd autonegotiation
             configuration: autonegotiation=on broadcast=yes driver=r8168 driverversion=8.045.08-NAPI duplex=half latency=0 link=no multicast=yes port=twisted pair speed=100Mbit/s
             resources: irq:404 ioport:1000(size=256) memory:20004000-20004fff memory:20000000-20003fff
  *-network:1
       description: Wireless interface
       physical id: 2
       bus info: usb@1:2.4.1
       logical name: wlan0
       serial: 90:de:80:48:40:66
       capabilities: ethernet physical wireless
       configuration: broadcast=yes driver=rtl88x2bu ip=192.168.165.220 multicast=yes wireless=IEEE 802.11bgn
WARNING: output may be incomplete or inaccurate, you should run this program as super-user.
```

#### 使用dmidecode查看DMI(Desktop Management Interface)信息
DMI是一种开放标准, 允许不同厂商的硬件和软件之间进行通信和交互

- 查看内存信息 `dmidecode -t memory`
- 查看内存数量 `dmidecode | grep -C 16 'Speed:'  | grep -A 16 "Memory Device" | grep 'Memory Device' | wc -l`
- 获取内存条频率 `dmidecode | grep -C 16 'Speed:'  | grep -A 16 "Memory Device" | grep 'Speed:'`

#### lspci查看外部设备
PCI(Peripheral Component Interconnect, 外围设备互连),一种计算机总线标准，用于连接计算机主板和外部设备，如显卡、网卡、声卡等。

### 查看标准输出文件占用

1. 通过信号 `SIGSTOP` 停止进程(终端打印停止) 和 `SIGCONT` 恢复进程(终端打印恢复) 来确定当前占用stdout的pid
2. `strace -fe write $(lsof -t "/proc/$$/fd/1" | sed 's/^/-p/')` 查看打开fd为1的stdout进程pid,并使用sed封装为-p选项,之后通过strace跟踪系统调用write

**注意** 对于strace追踪的系统调用输出, 如 `[pid  1450] read(30, "\300\0\200x\300\200\0x\300x\0\200x\300\200\0\370\200\0x\300x<\376\200x<\376\200\0x\300"..., 255) = 129` 可以使用 `ls -ahl /proc/1450/fd/30` 查看其指向的设备

### /proc目录查看进程信息
`<pid>/fd`有几个标准设备，1=stdout;2=stderr

### 查看ubuntu的Codename
`lsb_release -a`
输出如下:
```
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 20.04.3 LTS
Release:        20.04
Codename:       focal
```

### 命令后台运行
1. 使用 `&` 符
> dockerd 1>/dev/null 2>&1 &
2. 使用 nohup 命令
`nohup {command}`

**注意** nohup和&的区别，nohup不会挂起，在用户正常退出后，命令仍在后台运行。而&在shell终端关闭后，会结束掉启动的后台命令

### linux释放缓存
- 清除 PageCache `sudo sysctl vm.drop_caches=1`
- 清除 dentry 和 inode: `sudo sysctl vm.drop_caches=2`
- 清除 PageCache 以及 dentry 和 inode: `sudo sysctl vm.drop_caches=3`
> 等同 `echo <1|2|3> > /proc/sys/vm/drop_caches`

## linux command介绍

### linux快捷命令
> 常见快捷键:
```sh
Ctrl + L 清屏
Ctrl + A 移动光标到开头
Ctrl + E 移动光标到结尾

Ctrl + K 剪切光标到结尾
Ctrl + U 剪切光标到行首
Ctrl + Y 粘贴剪切字符
```

### linux历史命令 `!`

参[csdn博客](https://blog.csdn.net/weixin_44966641/article/details/121705593)

> 常见用法:
> `!!` 执行上一条命令
> `!<n>` 执行history中指定行号的命令
> `!<-n>` 执行倒数第几条命令，`!-1` 等同 `!!`
> `!<cmd>` 执行最近的cmd执行动作
> `!$` 获取上一条命令的最后一个参数
> `!^` 获取上一条命令的第一个参数（包括选项）

### seq命令
生成数组,指定first到last和间隔steps
```
Usage: seq [OPTION]... LAST
  or:  seq [OPTION]... FIRST LAST
  or:  seq [OPTION]... FIRST INCREMENT LAST
Print numbers from FIRST to LAST, in steps of INCREMENT.
```


### find命令

> example:
> - `find <find_path> -name <file_name>` 在路径下查找文件
> - `find . -type f -name "*.txt" ! -name "f*"` 查找所有不以f开头的txt文件
> - `find . -type f -regex ".*/[^f][^/]*\.txt"` 查找所有不以f开头的txt文件
> - `find . -type f -regex ".*\.\(md\|png\)$"` 找到所有*.md/*.png文件
> - `find . -type f \( -name "*.md" -o -name "*.png" \)` 找到所有*.md/*.png文件
> - `find . -type f -name "*.txt" -not -path "./build/*"` 查找所有txt文件, 排除`build`目录

#### find选项

- `-type [b/d/c/p/l/f]`   #设备|目录|字符设备|管道|符号链接|普通文件
- `-size N[bcwkMG]`       #查大小为n的文件（）
- `-name   filename`      #查找名为filename的文件
- `-perm`                 #按执行权限来查找
- `-user    username`     #按文件属主来查找
- `-group groupname`      #按组来查找
- `-mtime   -n +n`        #按文件更改时间来查找文件，-n指n天以内，+n指n天以前
- `-atime    -n +n`       #按文件访问时间来查GIN: 0px">
- `-ctime    -n +n`       #按文件创建时间来查找文件，-n指n天以内，+n指n天以前
- `-exec <command> {;,+}` #4.2.12版本添加, 使用 `\;`/`\+` 避免结束符被shell转义, 使用 `{}` 替换为每个找到的文件名, `;`是对每个文件均调用一次, `+`是批量文件调用一次(`{}`必须在末尾用于替换批量文件)

#### find根据时间变化查找文件
```sh
find {-[a|c|m][time|min]} [+-=]<number>
+ 表示 number天/分钟 之前
- 表示 number天/分钟到当前时间
= [number-1, number]
```
- atime是指access time，即文件被读取或者执行的时间，修改文件是不会改变access time的。
- ctime即change time文件状态改变时间，指文件的i结点被修改的时间，如通过chmod修改文件属性，ctime就会被修改。
- mtime即modify time，指文件内容被修改的时间。 

**注意** 可以使用stat查看文件的atime、ctime、mtime

### dhclient命令
dhclient命令的作用是：使用动态主机配置协议动态的配置网络接口的网络参数，也支持BOOTP协议。
- (ubuntu 20.04)问题:
> 有时,使用`ip address查看网络接口的IP时，出现下述输出;表示接口未启用
`2: ens33: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000`
- 解决方案:
`sudo dhclient ens33` 重新动态配置网络接口
`sudo systemctl restart network-manager.service`
- 结果:
`2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000`

### tar命令
tar用于linux下的文件压缩解压
```sh
Usage: tar [OPTION...] [FILE]...
GNU 'tar' saves many files together into a single tape or disk archive, and can
restore individual files from the archive.

Examples:
  tar -cf archive.tar foo bar  # Create archive.tar from files foo and bar.
  tar -tvf archive.tar         # List all files in archive.tar verbosely.
  tar -xf archive.tar          # Extract all files from archive.tar.
  
选项:
-c: 建立压缩档案
-x: 解压
-t: 查看内容
-r: 向压缩归档文件追加内容文件
-u: 更新压缩归档文件中的内容文件
-C, --directory=DIR: 提取文件至目录 DIR
```

### for命令
1. `for i in "Start learning from yiibai.com"; do echo $i; done`
2. `for num in {1..10..1}; do echo $num; done`
3. `arr=( "Welcome","to","yiibai.com" );for i in "${arr[@]}" ;do echo $i ;done`
4. `for ((i=1; i<=10; i++)) ;do echo "$i" ;done`

### ip命令
需要使用apt安装`iproute2`包

### ping命令
`sudo apt-get install ping` //centos 使用
`sudo apt-get install inetutils-ping`  //ubuntu


### tar命令
tar用于linux下的文件压缩解压
```
Usage: tar [OPTION...] [FILE]...
GNU 'tar' saves many files together into a single tape or disk archive, and can
restore individual files from the archive.

Examples:
  tar -cf archive.tar foo bar  # Create archive.tar from files foo and bar.
  tar -tvf archive.tar         # List all files in archive.tar verbosely.
  tar -xf archive.tar          # Extract all files from archive.tar.
  
选项:
-c: 建立压缩档案
-x: 解压
-t: 查看内容
-r: 向压缩归档文件追加内容文件
-u: 更新压缩归档文件中的内容文件
```

### zip命令
zip 默认操作是添加或替换列表中的zipfile条目，可以特殊名称 `-` 从标准输入中压缩。

> 示例
- `zip -r {output_zip_name} {dirs_or_files}` 将指定目录或文件添加到压缩文件
- `zip [-sf, --show-files] {zip_file}` 显示将要操作的文件

### dmidecode
查看DMI(Desktop Management Interface)信息, 需要使用 `apt install dmidecode` 安装包

```sh
选项:
 -t, --type TYPE        仅显示给定的硬件类型,支持如下格式
    bios/基本输入输出系统
    system/系统
    baseboard/主板
    chassis/机箱风扇
    processor/中央处理器,即CPU
    memory/内存
    Cache/缓存
    connector/连接器
    slot
```

### top 命令

前五行输出

```
top - 15:15:07 up 2 days, 22:36,  2 users,  load average: 0.00, 0.02, 0.00
Tasks: 112 total,   1 running, 111 sleeping,   0 stopped,   0 zombie
%Cpu(s):  1.0 us,  0.7 sy,  0.0 ni, 98.3 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :   1982.6 total,    184.8 free,    255.1 used,   1542.7 buff/cache
MiB Swap:      0.0 total,      0.0 free,      0.0 used.   1541.7 avail Mem

# 输出参数介绍、
top - 当前时间 up 系统远行时间, 当前登陆用户数 users,  load average: 系统负载，即任务队列的平均长度。 三个数值分别为 1 分钟、5 分钟、15 分钟前到现在的平均值
Tasks: 进程总数 total,   正在运行的进程数 running, 睡眠的进程数 sleeping,   停止的进程数 stopped,   僵尸进程数 zombie
%Cpu(s):  用户空间占用CPU百分比 us,  内核空间占用CPU sy,  用户进程空间内改变过优先级的进程占用CPU ni, 空闲CPU id,  等待输入输出的CPU时间 wa,  硬中断（Hardware IRQ）占用CPU的 hi,  软中断（Software Interrupts）占用CPU si,  用于有虚拟cpu的情况，用来指示被虚拟机偷掉的cpu时间 st
MiB(单位) Mem :   物理内存总量 total,    空闲内存总量 free,    使用的物理内存总量 used,   用作内核缓存的内存量 buff/cache
MiB Swap:     交换区总量 total,   空闲交换区总量 free,  使用的交换区总量 used.   缓冲的交换区总量 avail Mem
```
### du

du命令可以查看磁盘使用情况;
```sh
Usage: du [OPTION]... [FILE]...
  or:  du [OPTION]... --files0-from=F
总结文件集合的磁盘使用情况, 递归地应用于目录.
option:
 -h 以符合人类阅读的方式显示大小
 -s 仅显示每个参数的总数
 -c 在末尾显示所有文件参数的大小总数
```

### df
df命令可以查看文件系统的磁盘占用
```sh
Usage: df [OPTION]... [FILE]...
展示指定文件系统的占用或者默认显示全部文件系统占用
option:
 -h 以符合人类阅读的方式显示大小
 -i 显示inode使用信息而不是块占用
 -T 打印文件系统类型,如ext4
```

### strings
用于在对象文件或二进制文件中查找可打印的字符串。它可以提取文件中的文本字符串，通常是至少4个字符长的可打印字符序列，并且以换行符或空字符结束。

选项:
* -a 或 --all：扫描整个文件，而不仅仅是目标文件的初始化和装载段。
* -f 或 --print-file-name：在显示字符串前先显示文件名。
* -n 或 --bytes=[number]：设置最小字符串长度，默认是4个字符。
* -t 或 --radix={o,d,x}：输出字符的位置，基于八进制、十进制或十六进制。
* -e 或 --encoding={s,S,b,l,B,L}：选择字符大小和排列顺序，例如 s表示7-bit，S表示8-bit，b和l表示16-bit，B和L表示32-bit。

> 示例:
- 查看libstdcxx中支持的GLIBCXX版本 `strings /home/smartwork/miniconda3/lib/libstdc++.so.6 | grep "GLIBCXX_"`

### 软件包管理
ubuntu使用apt作为默认的包管理器,是一个命令行包管理工具,提供命令用于 搜索/管理/查询 包信息;提供与一些专有的APT工具(如apt-get、apt-cache)具有相同作用的命令，默认情况下启用交互式选项。

**注意** 如果你需要交叉编译安装开发库,但使用apt install 指定平台的库,如`libx11-dev:i386` 报错:不能定位软件包`Unable to locate package libx11-dev:i386`。可以使用 `dpkg --add-architecture i386 && apt update` 更新软件包的架构搜索列表

**注意** 如果需要离线安装ubuntu软件包,可到ubuntu仓库源中下载deb包, 以xvfb包为例 [ubuntu仓库源包下载](http://archive.ubuntu.com/ubuntu/pool/universe/x/xorg-server/)

#### apt命令

> example:
- `apt search <pkg_sname>` 搜索可用包
- `apt show <pkg_name>` 显示安装包元信息(包括大小、版本、依赖关系)
- `apt upgrade <pkg_name>` 升级软件包
- `apt install <pkg_name>` 安装软件包
- `apt install <pkg_name> --no-upgrade` 安装一个软件包，但如果软件包已经存在，则不要升级它
- `apt list --all-versions <pkg_name>` 查看指定软件包的所有版本

##### apt镜像源

`sudo sed -i -r 's#http://(archive|security).ubuntu.com#https://mirrors.aliyun.com#g' /etc/apt/sources.list`

##### apt changelog查看未安装包更新元数据
`apt changelog <pkg_name>`检查包的更新日志以及该软件包是否已经安装在您的系统。
**注意** 默认从网络下载.changelog文件

##### apt source获取安装包源码
`apt  source <pkg_name>`;apt source 每次下载出来的都是该版本最新的源码包，下载不到历史包

##### apt-file

**注意** 你需要安装apt-file工具`sudo apt install apt-file`，并在查找时更新apt-file的数据库，使用命令`sudo apt-file update`

- 查找文件所对应的安装包
> 从数据库中查找文件所在安装包 `apt-file find <file_name>`，只要更新了数据库，即时未安装对应的包也可以找到，在获取c/c++未知头文件时极为有用。
- 列出安装包中所有文件 `apt-file list <pkg_name>`


#### apt查看安装包的安装时间
查在日志文件中 `/var/log/apt/history.log` 查看安装包的时间

#### whereis查看安装包位置
```
Usage:
 whereis [options] [-BMS <dir>... -f] <name>
找到命令的二进制文件、源文件和手册页文件。可使用该命令查看已安装软件位置
```

#### which查看命令位置
```
Usage: /usr/bin/which [-a] args
     example:
      wheeltec@wheeltec:~$ which python
      /usr/bin/python
```

#### dpkg查看安装包版本
```
# 简要列出包信息（包括版本信息）
dpkg -l <package_name>
```

#### dpkg查看安装包所拥有的文件
```
# 列出包"拥有"的文件。
dpkg -L <package_name>
```

#### dpkg查看某一文件所属的包
```
# 获取文件所在包
dpkg -S <file_full_path>
```

#### dpkg查看deb包的内容

`dpkg -c sqlite3-doc_3.45.1-1ubuntu2.5_all.deb`

### sed命令

sed 流编辑器过滤和转换文本

`sed [OPTION]... {script-only-if-no-other-script} [input-file]...`,如：`sed '[match_lines]s<segment_sign default /><match_string><segment_sign default /><rex_string><segment_sign default />' `

example:
`sed '2,$s/原字符串/替换字符串/g' # 替换第2行到最后一行`
`sed 's/^/添加的头部&/g' 　　　　 # 在所有行首添加`
`sed 's/$/&添加的尾部/g' 　　　　 # 在所有行末添加`
`sed 's/^/添加的头部&/g;s/$/&添加的尾部/g' # 同时执行两个替换规则`

**注意** 
1. 单引号' 是没有办法用反斜线\转义的,这时候可以使用双引号做行替换脚本
2. 更改在s后定义的分隔符,有时候替换目录字符串的时候有较多/，这个时候换成其它的分割符是比较方便(无需不断使用\转义)
3. 在末尾加g替换每一个匹配的关键字,否则只替换每行的第一个
4. 行首匹配符^,行尾匹配符$
5. 多个替换可以在同一条命令中执行,用分号;分隔
6. &获取匹配项指针

> option:
- `-i` 选项指定在文件中替换字符串，取代默认方式(sed默认是将替换后内容输出到stdout)
- `-E, -r, --regexp-extended` 使用扩展正则

#### linux在文件中查找替换
sed -i s/172.17.2.0:8000/172.17.0.2:8000/g `grep "172.17.2.0" -rl ./`

#### 替换二进制文件中指定值

`sed 's/\x42\x49\x54\x4d\x41\x50\x04\x00\x00\x00\x4e\x55\x4c\x4c/\x42\x49\x54\x4d\x41\x50\x04\x00\x00\x00\x44\x31\x36\x4c/g' a.hex > b.hex`

### dd文件操作

```
Usage: dd [OPERAND]...
  or:  dd OPTION
dd命令用于复制文件，根据操作数进行转换和格式化。如剪切二进制文件头部元信息等。

操作数:
     if       指定输入文件 input file
     of       指定输出文件 output file
     bs       每次读或写的字节数(覆盖ibs/obs) BYTES
     ibs      每次读的字节数 input BYTES
     obs      每次写的字节数 output BYTES
     skip     指定输入时跳过的ibs数 
     seek     指定输出时跳过的obs数 
     count    拷贝指定n个输入块
```
> example:
- `dd if=<file_name> of=<output_file> bs=<bytes at a time> skip=<skip n ibs>`
     将if指定文件，跳过skip*bs个字节输出到of文件中
- `dd if=2022.tuf of=2022_tmp/l.dat bs=1 skip=592 count=300611877` 将2022.tuf文件的592偏移处拷贝300611877 bytes到2022_tmp/l.dat中
- `dd if=/dev/urandom of=l.dat bs=1M count=1` 生成一个指定大小的随机文件

### kill与pkill
```
kill 用于杀死一个进程
pkill 用与关闭一个终端
```
1. kill 介绍
Kill是一个shell内置功能，有两个原因:它允许使用作业id替代进程id，并且允许在您可以创建的进程达到限制时杀死进程。
> 使用方式 `kill [-s sigspec | -n signum | -sigspec] pid | jobspec ... `
> 通过 `-l | -L` 选项列出所有可发送符号名

### ssh

linux上ssh一般为openssh(ssh协议的开源实现)，包括ssh客户端和sshd服务端。在客户端可以连接远程主机，服务端开放端口供其他主机登录本机（默认端口22，可在/etc/ssh中更改）

> 使用方式如下:
1. 在客户端使用`ssh-keygen -t <use_key_way>`生成密钥对，一般选用rsa加密方式(生成id_rsa/id_rsa.pub),可以在($HOME/.ssh目录中)查看。
2. 将客户端的公钥发送到服务端,在客户端执行`ssh-copy-id <ssh_server_user@remote_address> -p <sshd_port>`
3. 在服务端登录用户主目录的.ssh目录中，查看authorized_keys文件是否正确添加公钥
4. 配置ssh-config文件，避免每次连接时手动指定密钥文件

#### ssh-config
配置ssh-config一个连接示例如下:
```sh
Host test
  HostName 192.168.8.14
  User smartwork
  IdentityFile "D:\yzsh\ssh\smartwork"
```
> 选项:
- Host: 
  * 下接限制声明(直到下一个Host关键字), 仅适用于匹配关键字后给出的模式之一的主机。
  * 提供了多个模式, 用空格分隔
  * `*`可为所有主机提供全局默认值
  * host是命令行上给出的ssh参数, 如`test`
  * 可用`!`作为前缀来否定模式条目.如果一个否定的项匹配, 则忽略Host项
- HostName:
  * 要登录的真实主机名
  * 如果主机名包含字符序列`%h`, 那么将被替换为命令行中指定的主机名
  * 默认是命令行中给出的名称
  * 允许IP

### sftp或scp
sftp(ssh file transfer protocol, ssh文件传输协议)
与scp相比，sftp支持断点续传和图形化操作,但相较于scp传输较慢。

> sftp使用
- sftp使用与ssh类似,均需要选与服务器建立连接,使用`sftp <username>@<server_ip_address>`连接服务器
- 使用`put -r <local_dir> <remote_dir>`上传文件夹
- 使用`get -r <remote_dir> <local_dir>`下载文件夹
- 使用`help`或`?`查看帮助信息

> scp使用
- scp 只支持一行指令(在源和目的地址间同步)，不支持交互tui界面
- `scp [-r] [-P port] [-i identity_file] source_path target_path` 将源路径下文件拉取到目标路径, -r拉取目录


### curl(命令行统一资源定位符, CommandLine Uniform Resource Locator)
```sh
选项:
-x, --proxy [protocol://]host[:port]              Use this proxy
-X, --request <method>                            Specify request method to use,like POST | GET
-d, --data <data>                                 HTTP POST data
-4, --ipv4                                        Resolve names to IPv4 addresses
-6, --ipv6                                        Resolve names to IPv6 addresses
-G, --get                                         Put the post data in the URL and use GET
```

**注意** -d选项传递json数据的双引号,需转义

#### curl设置代理
`curl -x 127.0.0.1:7890 https://a.com/test.exe --output test.exe`

#### curl使用指定网卡操作
`curl --interface ens38 http://[fe80::f9d6:6cd5:c2e6:8059%ens38]/`

### wget
wget 多线程 metalink/文件/网站 下载工具

#### wget设置代理
`wget -e "http_proxy=http://127.0.0.1:8087" http://example.com/file`

### tcpdump

tcpdump命令行网络流量分析器, 使用`apt install tcpdump`安装
> 参[tcpdump工具使用笔记](../net/capture/tcpdump.md)

### ulimit

获取或设置用户限制, 一般用于生成coredump文件

- `ulimit -c` 获取当前限制策略, 0表未启动coredump收集
- `ulimit -c unlimited` 临时启用coredump大小无限制



## 文件系统

### 相关配置文件

- `/etc/fstab`(File System Table)是 Linux 系统中一个重要的配置文件，用于定义系统启动时自动挂载的文件系统。它包含了文件系统的挂载点、设备、文件系统类型以及挂载选项等信息。通过 /etc/fstab，系统可以自动挂载所需的文件系统，而无需手动干预。

### linux文件类型
|文件类型	 |说明                                                   |
|-----------|-------------------------------------------------------|
|b	        |块设备，是一些提供系统存取数据的接口设备，例如硬盘。|
|c	        |字符设备，是一些串行端口的接口设备，例如键盘、鼠标、打印机、tty终端。|
|d	        |目录，类似于Windows的文件夹。|
|l	        |软链接文件，类似于Windows的快捷方式。|
|s	        |套接字文件（socket），用于进程之间的通信。|
|-	        |文件，分纯文本文件（ASCII）和二进制文件（binary）。|

### 文件系统类型

- ext4: Linux 常用文件系统
- vfat: FAT32 文件系统
- ntfs: Windows NTFS 文件系统
- swap: 交换分区
- tmpfs: 内存文件系统

### mount
mount 挂载一个文件系统

> Unix系统中所有可访问的文件都被安排在一个大树中，即文件层次结构，根位于/。这些文件可以分布在几个设备上。mount命令用于将在某些设备上找到的文件系统附加到大文件树中。相反，umount命令将再次分离它。文件系统用于控制数据如何存储在设备上或通过网络或其他服务以虚拟方式提供。

> 示例:
> - 标准挂载命令 `mount -t type device dir`, 将类型为type的文件系统(位于device)挂载到目录dir中
> - `mount /tmp/disk.img /mnt -t vfat -o loop=/dev/loop3` 绑定回环设备`/dev/loop3`和`disk.img`对应, 然后挂载到`/mnt`目录下, 仅使用 `-o loop` 将会找到空闲的回环设备使用
> - `dd if=/dev/zero of=/path/to/virtualfs.img bs=1M count=1024 && mkfs.ext4 /path/to/virtualfs.img && sudo mount -o loop /path/to/virtualfs.img /mnt/virtualfs` 创建一个虚拟磁盘文件,然后挂载
> - `sudo mount /dev/nvme0n1p6 /media/ubuntu/nvmep6/` 挂载一块实际硬盘的分区

#### mount挂载img磁盘镜像

以树莓派 2022-09-06-raspios-bullseye-arm64-lite.img 为例:
- `fdisk -l <img_file>` 查看磁盘镜像文件扇区
- `mount -o loop,offset=<start_point*block_size> <img_file> <mount_point>` 挂载一个磁盘分区设备(其中起始点和快大小可由fdisk -l获取)
- `umount <mount_point>` 取消挂载

### blkid
blkid: 定位/打印块设备属性, 可查看文件系统UUID和LABEL

```sh
(base) smartwork@192.168.8.1:~/work/mblog$ blkid
/dev/nvme0n1p2: UUID="5cb1ced6-89ab-4519-ba54-89ec20cda850" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="9c568112-ca35-4dab-8957-6c33734a2c00"
```

### mkfs
mkfs 创建一个Linux 文件系统。

> 示例:
> - 制作ext4文件系统镜像 `mkfs.ext4 ubuntu_base.img`

### Loop Device
Loop Device 是 Linux 系统中的一种虚拟设备，允许将普通文件（如磁盘镜像文件）作为块设备挂载到文件系统中。通过 Loop Device，文件可以像物理磁盘一样被访问和操作，常用于挂载 ISO 镜像、磁盘镜像文件或创建虚拟文件系统。

> `loop device`常见作用
1. 挂载镜像文件：将 ISO 镜像、磁盘镜像文件（如 .img）挂载为文件系统，方便访问其中的内容。
2. 创建虚拟文件系统：使用文件作为存储介质，创建虚拟文件系统（如加密文件系统）。
3. 测试和开发：在开发和测试环境中，使用 Loop Device 模拟磁盘设备，避免对物理磁盘的操作。
4. 容器和虚拟化：在容器或虚拟化环境中，使用 Loop Device 挂载镜像文件作为虚拟磁盘。

#### losetup

losetup控制和显示回环设备

> 示例:
> - `losetup -a` 列出所有使用的回环设备
> - `sudo losetup -Pf disk.img`: `-P`自动扫描文件分区并分配loop设备`-f`
> - `sudo losetup /dev/loop0 /path/to/image.iso` 将文件与 Loop Device 关联
> - `sudo losetup -d /dev/loop0` 解除文件与 Loop Device 的关联
> - `sudo mount /dev/loop0 /mnt/loop` 挂载已关联的 Loop Device
> - `sudo umount /mnt/loop && sudo losetup -d /dev/loop0` 卸载并解除关联


## linux用户管理

### linux用户和组命令

#### 用户和组管理
1. 查看有系统哪些组`compgen -g`
2. 查看当前用户的组`groups [user_name]`
3. 为当前用户添加附加组`uermod -aG {group_name} [user_name]`

#### useradd
用于创建用户，支持选项有:
```sh
Options:
      --badname                 do not check for bad names
  -b, --base-dir BASE_DIR       指定新用户家目录创建的基本目录(默认为: /home)
  -d, --home-dir HOME_DIR       手动指定新用户家目录(默认为: base_dir/user_name)
  -e, --expiredate EXPIRE_DATE  新用户的截至有效日期
  -m, --create-home             强制创建用户家目录
  -M, --no-create-home          强制不创建用户家目录
  -N, --no-user-group           不创建同名组
  -o, --non-unique              允许创建具有重复（非唯一）UID的用户（即同一用户的副本）
  -p, --password PASSWORD       指定密码
  -r, --system                  创建系统用户(默认无家目录)
  -R, --root CHROOT_DIR         指定登录的chroot(变化root目录)
  -P, --prefix PREFIX_DIR       prefix directory where are located the /etc/* files
  -s, --shell SHELL             新账户的登录shell
  -u, --uid UID                 新账户的uid
  -U, --user-group              创建同名组
```

**注意** chroot是将特定用户与其他用户分离的一种手段，它会现在指定用户的访问范围。
参[SSH 用户会话限制](https://linux.cn/article-8313-1.html)

##### /etc/skel 在用户添加时，家目录创建上的作用
使用 `useradd` 创建用户，会将 `/etc/skel`文件夹中的文件和目录复制到用户家目录中。 可用此管理用户配置文件


### linux权限管理

常见的权限管理命令有 `chmod`/`chown` , 前者用于更改文件权限,后者用于更改所有者

linux基本文件权限有 r(4,读)/w(2.写)/x(1,执行)

> linxu除了普通权限外也有附加权限(包括 Set位权限`suid/sgid` 和 Sticky位权限 `sticky`)
  - suid(set User ID,set UID)的意思是进程执行一个文件时通常保持进程拥有者的UID。然而，如果设置了可执行文件的suid位，进程就获得了该文件拥有者的UID。
  - sgid(set Group ID,set GID)意思也是一样，只是把上面的进程拥有者改成了文件拥有组（group）。
  - sticky 一般用于为目录设置特殊的附加权限,当目录被设置了粘滞位权限后,即便用户对该目录有写的权限,也不能删除该目录中其他用户的文件数据
> 以数字表示的全附加位 `SGTrwxrwxrwx` 此时(S-->4;G-->2;T-->1), 如 `chmod 4755 {file}` 为`S--rwx-r-xr-x`/`rwsr-xr-x`

示例:
```sh
-rwsr-xr-x 表示设置了suid，且拥有者有可执行权限
-rwSr--r-- 表示suid被设置，但拥有者没有可执行权限
-rwxr-sr-x 表示sgid被设置，且组用户有可执行权限
-rw-r-Sr-- 表示sgid被设置，但组用户没有可执行权限
-rwxr-xr-t 表示设置了粘滞位且其他用户组有可执行权限
-rwxr--r-T 表示设置了粘滞位但其他用户组没有可执行权限
```

#### sudo无密码执行文件

- 使用 `sudo visudo` 添加规则, 如`smartwork ALL=(ALL) NOPASSWD:ALL`
- 将上述步骤保存的 `/etc/sudoers.tmp` 移动到 `/etc/sudoers`

> sudo相关配置文件
* `/etc/sudo.conf`            Sudo front-end configuration
* `/etc/sudoers`              List of who can run what
* `/etc/sudoers.tmp`          Default temporary file used by visudo

## linux文件操作

### 文本相关
#### awk 命令

`Usage: awk [POSIX or GNU style options] [--] 'program' file ...`

awk文件操作命令，将一长串字符串分割为每条记录进行处理，默认为行分割，每行数据以列分隔符分割处理。列分隔符为空白符，可手动指定。

> program可以包含以下几个部分:
`BEGIN{ 这里面放的是执行前的语句 };{这里面放的是处理每一行时要执行的语句};END {这里面放的是处理完所有的行后要执行的语句 }`
其中BEGIN和END部分可选，行执行语句由pattern和action两部分组成，形如'pattern + {action}';可以忽略其中之一，省略pattern将对所有匹配行执行action，省略action将缺省输出
例：`awk '!a[$0]++' file...`将输出非重复行

**注意** 
1. awk默认为软连接文件，指向gawk
```
(base) ubuntu@yzsh:~$ ll `which awk`
lrwxrwxrwx 1 root root 21 May 31  2023 /usr/bin/awk -> /etc/alternatives/awk*
(base) ubuntu@yzsh:~$ ll /etc/alternatives/awk
lrwxrwxrwx 1 root root 13 May 31  2023 /etc/alternatives/awk -> /usr/bin/gawk*
```
2. awk的程序脚本必须使用单引号包裹

##### 指定输入输出分隔符
```
指定列输入分割
     awk -F ":" '{print $2}' a.txt 
     awk -F: '{print $2}' a.txt 
     awk 'BEGIN{FS = ":"};{print $2}' a.txt
     awk '{print $2}' FS=":" a.txt
指定行输入分割
     awk 'BEGIN{RS="_"} {print $0}' a.txt  
     awk '{print $0}' RS="_" a.txt  
指定列输出分割     
     awk 'BEGIN{OFS = "_"} {print $1, $2, $3}' a.txt 
     awk '{print $1, $2, $3}' OFS="_" a.txt
指定行输出分割     
     awk '{print $0}' ORS="_" a.txt
```

##### awk选项
在`{}`中可以使用`$n`获取列分割后数组对应值,`$0`获取本行内容
`-v var=value`
定义一个用户定义变量，在`{}`中直接用变量名获取，也可以在awk命令末尾通过`<variable_name>=<vaule>`定义

##### awk内建变量和运算符
|变量          |描述|
|--------------|----|
|$n	          |当前记录的第n个字段，字段间由FS分隔|
|$0	          |完整的输入记录|
|ARGC	     |命令行参数的数目|
|ARGIND	     |命令行中当前文件的位置(从0开始算)|
|ARGV	     |包含命令行参数的数组|
|CONVFMT	     |数字转换格式(默认值为%.6g)ENVIRON环境变量关联数组|
|ERRNO	     |最后一个系统错误的描述|
|FIELDWIDTHS	|字段宽度列表(用空格键分隔)|
|FILENAME	     |当前文件名|
|FNR	          |各文件分别计数的行号|
|FS	          |字段分隔符(默认是任何空格)|
|IGNORECASE	|如果为真，则进行忽略大小写的匹配|
|NF	          |一条记录的字段的数目|
|NR	          |已经读出的记录数，就是行号，从1开始|
|OFMT	     |数字的输出格式(默认值是%.6g)|
|OFS	          |输出字段分隔符，默认值与输入字段分隔符一致。|
|ORS	          |输出记录分隔符(默认值是一个换行符)|
|RLENGTH	     |由match函数所匹配的字符串的长度|
|RS	          |记录分隔符(默认是一个换行符)|
|RSTART	     |由match函数所匹配的字符串的第一个位置|
|SUBSEP	     |数组下标分隔符(默认值是/034)|

|运算符	                    |描述|
|-----------------------------|---|
|= += -= *= /= %= ^= **=	     |赋值|
|?:	||  &&  < <= > >= != ==  |C语句|
|~ 和 !~	                    |匹配正则表达式和不匹配正则表达式|
|空格	                    |连接|
|+ - ! * / %	               |加，减，逻辑非，乘，除与求余|
|^ ***	                    |求幂|
|++ --	                    |增加或减少，作为前缀或后缀|
|$	                         |字段引用|
|in	                         |数组成员|
<!--  输出第二列包含 "th"，并打印第二列与第四列 -->
`awk '$2 ~ /th/ {print $2,$4}' log.txt`
~ 表示模式开始。// 中是模式。

##### awk调用shell命令

1. 使用system()函数,如 `dpkg -L libreadline-dev | awk '{system("if [ -f "$1" ];then echo "$1";fi")}'`
**注意** system括号里面的参数没有加上双引号的话，awk认为它是一个变量，它会从awk的变量里面把它们先置换为常量，然后再回传给shell

2. 借助管道符;如下所示
```
echo 1 | awk '{print $1|"xargs echo "}'
1
```
> 无论使用system还是管道调用shell命令，都是新开一个shell，在相应的cmdline参数送回给shell，所以要注意当前shell变量与新开shell变量问题

#### grep命令

grep用于在文件中查找字符串，支持正则表达式(DFA引擎/NFA引擎)

**注意** DFA引擎以文本为推导进行匹配，NFA引擎以表达式为推导进行匹配

```sh
Usage: grep [OPTION]... PATTERN [FILE]...
Search for PATTERN in each FILE

Pattern selection and interpretation:
  -E, --extended-regexp     PATTERN 作为扩展正则，支持?/+/()/{}/|等
  -F, --fixed-strings       PATTERN 作为字符串，不进行正则解析
  -G, --basic-regexp        PATTERN 作为基本正则(default)，仅支持较少符号
  -P, --perl-regexp         PATTERN 作为 Perl格式 正则，提供更多功能，包括非捕获组、命名捕获组等
```

> 示例:
> `echo -e "ex\nfg" | grep -E "ex|fg"` 查找多个或匹配
> `echo -e "ex\nfg\nlp" | grep -E -v "fg|x"` 查找多个不匹配
> `grep -arPl "\x00\x60" det_dat/` 查找二进制文件是否包含指定内容

### 二进制文件相关

#### hexdump
```
usage: <hexdump|hd> [-bcCdovx] [-e fmt] [-f fmt_file] [-n length]
               [-s skip] [file ...]

以十六进制、十进制、八进制、二进制或 ascii 显示文件内容。(默认按两字节解释,显示受机器大小端影响)

option：
 -b, --one-byte-octal      单字节八进制显示
 -c, --one-byte-char       单字节字符显示
 -C, --canonical           规范化 hex+ASCII 显示
 -d, --two-bytes-decimal   双字节十进制显示
 -o, --two-bytes-octal     双字节八进制显示
 -x, --two-bytes-hex       双字节十六进制显示
 -L, --color[=<模式>]      解释颜色格式化限定符
                             默认启用颜色
 -e, --format <格式>       用于显示数据的格式化字符串
 -f, --format-file <文件>  包含格式字符串的文件
 -n, --length <长度>       只解释规定字节长度的输入
 -s, --skip <偏移>         跳过开头的指定字节偏移
 -v, --no-squeezing        输出相同的行

 -h, --help                display this help
 -V, --version             display version
```
#### xxd

做一个十六进制转储或相反, 默认以1字节为单位按16进制解释

```sh
Options:
  -r 反向操作, 结合 -p 转换十六进制存储为二进制, 结合 -b 转换bit存储为二进制
  -p 输出连续十六进制存储字符串
  -b 切换到位(二进制数字)转储, 将字节写入为8位数字"1"和"0"
```

> example
- 将hex字符串转为二进制输出 `echo 100293190312f201ff01ec231e000bff0000346498003403ffffb01003 | xxd -r -p`

#### od
```sh
-A, --address-radix=[doxn]    指定文件偏移量的输出格式(即左侧地址基数)，代表十进制、八进制、十六进制和无基数
      --endian={big|little}   按照指定的字节序交换输入字节
-j, --skip-bytes=字节数     处理前先跳过 <字节数> 个输入字节
-N, --read-bytes=字节数     最多读取 <字节数> 个输入的字节
-S 字节数, --strings[=字节数]  仅显示至少包含 <字节数>（默认为 3）个
                                  可打印字符的、以 NUL 结尾的字符串
-t, --format=类型           选择一个或多个输出格式
-v, --output-duplicates     不使用 "*" 字符代替被省略的行
-w[字节数], --width[=字节数]  每一行输出 <字节数> 个字节；
                                如未指定 <字节数>，则默认为 32
    --traditional           接受以上述第三种格式提供的参数
    --help        显示此帮助信息并退出
    --version     显示版本信息并退出


传统的格式说明符可以混合使用，不同的格式可以累加：
  -a   即 -t a， 输出字符的名称，忽略最高位
  -b   即 -t o1，输出八进制字节
  -c   即 -t c， 输出可打印字符或者使用反斜杠转义
  -d   即 -t u2，输出无符号十进制数，两个字节为一个输出单位
  -f   即 -t fF，输出浮点数
  -i   即 -t dl，输出十进制整型 (int)
  -l   即 -t dL，输出十进制长整型 (long)
  -o   即 -t o2，输出八进制数，两个字节为一个输出单位
  -s   即 -t d2，输出十进制数，两个字节为一个输出单位
  -x   即 -t x2，输出十六进制数，两个字节为一个输出单位
```

> 示例: 
- `od -t x1c -w16 -Ax temp.txt` 以一行16个字节，地址基数16进制输出单位为单字节的16进制数和ascii字符码

### 文件比对

#### cmp二进制文件比对
cmp 逐个字节比较两个文件

#### diff
diff: 行行比较文件命令

> 选项:
```sh
OPTION:
  -r 递归地比较所有子目录
  -n 输出一个RCS格式diff
  -u,-U NUM,--unified[=NUM] 输出统一上下文的NUM行（默认3行）
  -p 显示更改在哪个C函数中
```

> 示例:
> 1. 递归比较两文件夹并将差异导出为一个patch `diff -r -u -p qemu-6.0.0 quard_star_tutorial/qemu-6.0.0/ > temp.patch`, 之后可用于 `patch` 命令恢复

#### patch

patch 将diff文件应用于原始文件

> 选项:
```sh
OPTIONS:
  -pnum  or  --strip=num
    从补丁文件中找到的每个文件名，并去掉包含num个前导斜杠的最小前缀。由一个或多个相邻斜杠组成的序列被算作一个斜杠。这控制了如何处理在补丁文件中找到的文件名，以防止将文件保存在与发送补丁的人不同的目录中。例如，假设补丁文件中的文件名为
    /u/howard/src/blurfl/blurfl.c
       setting -p0 gives the entire file name unmodified, -p1 gives
          u/howard/src/blurfl/blurfl.c
       without the leading slash, -p4 gives
          blurfl/blurfl.c
       not specifying -p at all just gives you `blurfl.c`
  -u, --unified
    将补丁文件解释为统一格式的补丁文件(unified diff),通常以 --- 和 +++ 开头
```

> 示例
> ``


## linux 网络管理

### linux socket和tcp/udp系列命令

#### lsof

lsof(list open file, 列出打开文件),在linux下一切皆文件，如普通文件，目录，特殊的块文件，管道，socket套接字，设备等。因此我们可以使用

##### lsof查看端口被那些程序占用
使用 -i 选项指定
`-i i  select by IPv[46] address: [46][proto][@host|addr][:svc_list|port_list]`
**注意** 需管理员权限

##### lsof查看当前使用连接的进程
`lsof -P -i -n`
-i 查看使用ip4/6连接
-P 选择无端口名(即固定端口不选择,ssh/http/mysql)
-n 选择无主机名(即排除localhost等)

#### ss
ss(Socket Statistics, socket统计)，可以用来获取socket统计信息，它显示和netstat类似的内容。与netstat相比ss的优势在于它能够显示更多更详细的有关TCP和连接状态的信息，比netstat更快速更高效。

#### nmap
nmap 一款网络端口扫描工具

#### netcat
netcat 是一个使用 TCP 或 UDP 协议的网络工具，可以在两台计算机之间建立连接，进行数据传输。它支持多种网络操作，包括但不限于：

- 端口监听：在指定端口上监听传入的连接。
- 端口扫描：扫描目标主机上的开放端口。
- 数据传输：在两台计算机之间传输文件或数据。
- 反向 shell：在目标主机上执行命令并获取 shell 访问。
- 代理：通过中间服务器转发流量。



### linux登录、文件传输

##### ssh使用密钥登录

openssh是ssh协议的开源实现，包括ssh客户端和sshd服务端。在客户端可以连接远程主机，服务端开放端口供其他主机登录本机（默认端口22，可在/etc/ssh中更改）

1. 在客户端使用`ssh-keygen -t <use_key_way>`生成密钥对，一般选用rsa加密方式。可以在($HOME/.ssh目录中）查看。生成id_rsa和id_rsa.pub两个密钥文件。

2. 将客户端的公钥发送到服务端,在客户端执行`ssh-copy-id <ssh_server_user@remote_address> -p <sshd_port>`。

3. 在服务端登录用户主目录的.ssh目录中，查看authorized_keys文件是否正确添加公钥。

##### sftp或scp传输文件到服务器
sftp(ssh file transfer protocol, ssh文件传输协议)与scp相比，sftp支持断点续传和图形化操作,但相较于scp传输较慢。
scp(Secure Copy Protocol, 安全复制协议), scp在文件传输速度上优于sftp,在网络延迟较高的情况下,scp使用了更高效的传输算法，不需要等待数据包的确认。

**sftp使用**
- sftp使用与ssh类似,均需要选与服务器建立连接,使用`sftp <username>@<server_ip_address>`连接服务器
- 使用`put -r <local_dir> <remote_dir>`上传文件夹
- 使用`get -r <remote_dir> <local_dir>`下载文件夹
- 使用`help`或`?`查看帮助信息

**scp使用**
- `scp [-r] [-P port] [-i identity_file] source_path target_path` 将源路径下文件拉取到目标路径, -r拉取目录
> 示例: `scp -P 22 -F /etc/ssh/ssh_config ./auto-t113-linux.zip work@192.168.8.1:/home/work/cross/file_system`

### linux network配置管理器
linux有NetworkManager和systemd-networkd两个网络配置管理器,你只需要其中一个正常工作即可.使用下述命令将另一个禁用;推荐使用NetworkManager
`systemctl enable NetworkManager`
`systemctl disable systemd-networkd`

- networkd 通常用于网络环境相当静态的服务器安装。
- NetworkManager 通常用于桌面安装，并且用于所有以前版本的 Ubuntu。 NetworkManager 在网络需求变化很大的环境中更容易使用.

#### 禁用dhcp失败时分配的局部ipv4地址169.254

> 临时删除局部ipv4 `sudo ip addr del 169.254.223.15/16 dev eth0`
> 检查dhcp是否失败, 手动触发dhcp
```sh
sudo dhclient -r eth0  # 释放当前租约
sudo dhclient -v eth0  # 重新请求 IP
journalctl -u dhcpcd -n 50  # 查看 DHCP 客户端日志
```

1. 修改 NetworkManager 配置, 编辑 `/etc/NetworkManager/conf.d/no-link-local.conf`, 添加如下内容:
```ini
[connection]
ipv4.link-local=0
```
2. 使用 sysctl(内核参数)
```bash
echo "net.ipv4.conf.eth0.accept_link_local = 0" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
```

#### nmcli与nmtui
nmcli 是 NetworkManager 的命令，用于管理网络设置和连接。nmtui是tui版本的管理工具.
显示网络设备信息`nmcli device show docker0`
显示连接信息`nmcli connection show`

> 示例: 添加一个网络连接,类型桥接bridge,别名docker0,连接的接口名docker0,分配ip4地址,启用自动连接
`sudo nmcli connection add type bridge ifname docker0 con-name docker0  ip4 172.17.0.1/16 autoconnect true`

#### netplan
适用与(systemd-networkd或者networkmanager)的网络配置文件管理.使用netplan你可以统一配置systemd-networkd和networkmanager,而不需要分别到他们的配置目录下配置接口信息.
Netplan读取/etc/netplan下的描述网络用的各个yaml文件，生成backend config后端配置项。将这些后端配置项通过yaml文件里指定的renderers渲染器(systemd-networkd或者networkmanager)将配置下发到Linux内核中。

netplan generate
以/etc/netplan 配置为输入为renderer指定的底层网络管理工具生成配置文件。
netplan apply
应用配置，使配置生效。
netplan try
试用配置，然后等待用户的确认；如果网络中断或没有给出确认，就自动回滚。

**注意** 注意在/etc/netplan目录下，有多个yaml文件存在，netplan是根据字母表排序，挨个生效的，后面的yaml指定的配置会覆盖前面的yaml指定的配置。


## linux配置和特殊文件

### 配置文件

### 特殊文件

#### /proc/net/tcp

`/proc/net/tcp` 是Linux内核提供的一个虚拟文件，用于显示当前系统的TCP连接状态信息。内容如下:
```sh
sl  local_address  rem_address    st  tx_queue           rx_queue     tr        tm->when  retrnsmt  uid       timeout  inode                             
0:  0100007F:0277  00000000:0000  0A  00000000:00000000  00:00000000  00000000  0         0         17350917  1        0000000000000000  100  0  0   10  0
```
> 字段说明:
> - sl: 序号
> - local_address: 本地IP地址和端口（16进制）
> - rem_address: 远程IP地址和端口（16进制）
> - st: 连接状态（数字代码）
> - tx_queue: 发送队列长度
> - rx_queue: 接收队列长度
> - tr: 定时器信息
> - tm->when: 超时时间
> - retrnsmt: 重传次数
> - uid: 用户ID
> - timeout: 超时时间
> - inode: inode号

> 连接状态id对应:
```sh
00: TCP_ESTABLISHED
01: TCP_SYN_SENT
02: TCP_SYN_RECV
03: TCP_FIN_WAIT1
04: TCP_FIN_WAIT2
05: TCP_TIME_WAIT
06: TCP_CLOSE
07: TCP_CLOSE_WAIT
08: TCP_LAST_ACK
09: TCP_LISTEN
0A: TCP_CLOSING
```

#### /proc/self/exe

符号连接, 指向当前执行文件的绝对路径

## linux的一些使用示例
### linux的wifi连接
如果使用`iwlist wlan0 scan`扫描wifi时,效果较差可以使用`sudo wpa_cli -i wlan0 scan_result`


`sudo wpa_cli -i wlan0 list_network`

## linux 设备管理

linux 系统中，设备被分为几种主要类型，每种类型有不同的特性和用途，如:

1. 块设备(Block Device)
  - 用于存储设备，如硬盘、SSD、USB 驱动器等
  - 以固定大小的块(如 512 字节、4KB)为单位进行读写
  - 相关命令: `lsblk`/`mount`/`mkfs`
2. 字符设备(Character Device)
  - 以字符流为单位进行读写，支持按字节访问
  - 通常不支持随机访问，适合顺序读写
  - 相关命令: `ls`/`cat`/`echo`
3. 网络设备(Network Device)
  - 通过网络协议(如 TCP/IP)进行数据传输
  - 支持高速数据传输，适合网络通信
  - 相关命令: `ip link`/`ifconfig`/`ip addr`
4. 特殊设备(Special Device)
  - 直接对应物理设备，而是提供特殊功能
  - 用于系统管理和调试
  - 相关示例: `cat /dev/null`/`dd if=/dev/zero of=file.bin bs=1M count=10`
5. 伪设备(Pseudo Device)
  - 由内核虚拟化，不直接对应物理硬件
  - 用于实现特殊功能，如内存文件系统、进程间通信等
  - 相关示例: `/dev/loop0`/`tmpfs`/`/dev/fd`

**注意**
> 在 Linux 中，设备文件通过主设备号(Major Number)和次设备号(Minor Number)标识：
> - 主设备号: 标识设备类型(如硬盘、键盘)
> - 次设备号: 标识同一类型设备中的具体实例(如第一块硬盘、第二块硬盘)

### video设备

> 参考文档
- [xorg配置文件加载顺序](https://www.x.org/releases/current/doc/man/man5/xorg.conf.5.xhtml)

**注意** 更新配置文件后使用 `systemctl restart display-manager.service` 重启显示管理

#### 常见配置文件的区别

|文件路径	                              |用途	            |优先级	  |是否推荐手动修改|
|--------------------------------------|-----------------|--------|---------------|
|/usr/share/X11/xorg.conf.d/xorg.conf	  |系统默认配置	    |最低	    |否（可能被覆盖）|
|/etc/X11/xorg.conf.d/10-headless.conf	|无显示器环境配置	|中	      |是|
|/etc/X11/xorg.conf.d/10-dummy.conf	    |虚拟显示器配置	  |中	      |是|
|/etc/X11/xorg.conf	                    |传统全局配置	    |最高	    |尽量避免|

#### 查看可用显示接口

`xrandr --listmonitors`

#### 查看当前屏幕信息

- xorg日志文件 `/var/log/Xorg.0.log`(默认主显示)/`/var/log/Xorg.1.log`(默认虚拟屏)
- `DISPLAY=:1 xrandr` 显示指定设备的分辨率

#### 无显示器模式（如服务器）切换回物理显示器

- 强制启用 nomodeset
- 更改 `/etc/default/grub` 中设置为 `GRUB_CMDLINE_LINUX_DEFAULT="quiet splash nomodeset"`
- `sudo update-grub && sudo reboot`

#### 设置默认登录界面

[ubuntu问答社区](https://askubuntu.com/questions/1260142/ubuntu-set-default-login-desktop)

#### 查看video设备信息
`v4l2-ctl -d /dev/video -all`
需要安装v4l-utils

#### 显示服务
linux中一切皆文件，包括界面的显示，linux上显示为c/s架构，显示服务器通过显示服务器协议与其客户端进行通信。用于在显示器上绘制内容并发送输入事件。

Linux中提供了三种显示服务器协议，包括X11/Wayland/Mir
- X Window System(通常仅称为X或X11)应用程序和显示器不必在同一台计算机上

#### xserver虚拟驱动

- 安装虚拟驱动 `apt install xerver-xorg-video-dummy`
- 创建虚拟配置文件 `/usr/share/X11/xorg.conf.d/xorg.conf`
文件配置内容如下:
```sh
Section "Monitor"
  Identifier "Monitor0"
  HorizSync 28.0-80.0
  VertRefresh 48.0-75.0
  # https://arachnoid.com/modelines/
  # 1024x768 @ 60.00 Hz (GTF) hsync: 47.70 kHz; pclk: 64.11 MHz
  Modeline "1360x768_60.00" 64.11 1024 1080 1184 1344 768 769 772 795 -HSync +Vsync
EndSection
Section "Device"
  Identifier "Card0"
  Driver "dummy"
  VideoRam 256000
EndSection
Section "Screen"
  DefaultDepth 24
  Identifier "Screen0"
  Device "Card0"
  Monitor "Monitor0"
  SubSection "Display"
    Depth 24
    Modes "1360x768_60.00"
  EndSubSection
EndSection
```

### 串口操作

#### 查看系统支持的串口驱动
```sh
(base) ubuntu@DESKTOP-UAS0QBB:~/install_drive$ ls /sys/bus/usb/drivers/
cdc_acm  cdc_ether  cdc_ncm  hub  r8153_ecm  usb  usbfs  usbhid
```

**注意** 查看串口驱动发现ch340驱动无(在wsl中均无,这些即使通过usbipd将usb设备附加到wsl上,仍然不能使用ch340转的串口),因此需要重新编译wsl内核.参[wsl内核重新编译](https://askubuntu.com/questions/1373910/ch340-serial-device-doesnt-appear-in-dev-wsl/)

#### 查看是否已存在对应的串口驱动内核
在此目录下 `/usr/lib/modules/6.8.0-49-generic/kernel/drivers/usb/serial/` 查看
存在可通过 `modprobe cp210x` 挂载

#### stty配置串口

stty 打印或更改终端特性
```sh
stty -F /dev/ttyCH343USB0 speed 115200 cs8 -parenb -cstopb raw -echo -echoe -echok -echoctl -echoke
# speed 串口波特率
# cs8 数据位8位
# parenb 无校验
# cstopb 停止位1位
```

##### 选项
```
-F, --file=DEVICE  使用指定的设备打开而不是默认的stdin
```

##### stty更改串口波特率
```sh
stty -F /dev/ttyUSB0 115200  # 更改终端为波特率
cat /dev/ttyUSB0  # 显示终端数据
```

#### cat读取串口数据

`cat /dev/ttyACM1`

**注意** 输出的前提是串口没有被其他软件加软件锁(及不存在 `/run/lock/LCK..ttyACM1` 文件, 旧系统使用 `/var/lock` )

#### echo发送串口数据

#### socat

socat通用数据流中继工具, 支持网络协议/串口/套接字/文件等, 核心功能是 在两个数据流之间建立双向通道, 如:
- 网络协议(TCP, UDP, SSL, IPv4/IPv6, UNIX Socket)
- 串口/终端设备(/dev/ttyS*, PTY 虚拟终端)
- 文件或管道(读取/写入文件，进程间通信)
- 系统设备(如标准输入/输出、原始块设备)

> Example:
> - 虚拟串口PTY转发 `socat PTY,link=/dev/ttyVIRT0,rawer TCP:192.168.1.100:1234`
> - 记录串口数据到文件 `socat /dev/ttyUSB0,b115200,raw OPEN:/tmp/serial.log,creat,append`
> - 进程间通信(管道) `socat EXEC:"python3 script.py",pipes PIPE:/tmp/mypipe`

##### 使用socat将串口数据打印到标准输出

`socat /dev/ttyUSB0 –`

##### 使用socat创建虚拟串口对

1. 安装socat
2. 创建一对虚拟串口`socat PTY,link=/dev/ttyV0,mode=777 PTY,link=/dev/ttyV1,mode=777`
 - `PTY` 表示创建一个伪终端（虚拟串口）。
 - `link=/dev/ttyV0` 和 `link=/dev/ttyV1` 分别指定了虚拟串口的设备文件名称。
 - `mode=777` 设置了设备文件的权限，以便所有用户都可以访问。
3. 查看虚拟串口`ls -l /dev/ttyV*`
4. 使用cat/echo测试虚拟串口对是否建立连接

##### 使用usbip共享USB设备
共享usb设备分为两个部分(client和server)

[usbip官方网站](https://usbip.sourceforge.net/)
[uspip-win适用于window的usb/ip客户端](https://github.com/vadimgrn/usbip-win2/)

**注意** 区分usbip和usbipd-win项目，如下：
- usbip是一个早期项目(采用c/s架构，客户端可以连接的服务器访问共享的usb设备，现在已经内置到linux的kernel中)
- usbipd-win是一个window上的服务程序，适用于wsl和hyper-v上共享本地usb设备，也可用于共享window上usb设备到局域网中，需要配置3240端口的出入站规则和开启server服务

使用如下:
1. 查看有无usbip命令，无安装如下包
```sh
(base) s@sm:~$ dpkg -S `which usbip`
linux-tools-common: /usr/bin/usbip
```
2. 挂载usb/tcp转换的内核驱动
```sh
sudo modprobe usbip-core
sudo modprobe vhci-hcd
sudo modprobe usbip_host
```
3. 在服务端(即需要共享的usb设备物理主机)将usb设备bind `usbipd bind -b <bus_id>`
4. 在客户端查看有无共享设备 `usbip list -r 192.168.8.100 -v`
5. 附加远程usb设备 `usbip attach --remote=127.0.0.1 --busid=1-1`
6. 在客户端查看挂载的远程usb设备是否成功 `usbip port`


## linux内核

### dkms(Dynamic Kernel Module System, 动态内核模块系统)

DKMS是一个框架，旨在允许升级单个内核模块不改变整个内核。并且支持在系统内核升级时自动重新编译和安装第三方驱动和模块。


### modprobe
modprobe在Linux内核中添加和删除模块
> 默认在 `/lib/modules/$(uname -r)` 下查找所有模块

**注意** 对于 .zst格式的ko压缩包,需要使用 `zstd -d <zst_file>` 解压缩, 才能挂载

### dmesg
dmesg打印或控制内核环缓冲区

**注意** 默认行为是显示来自内核环缓冲区的所有消息

### wsl内核重新编译

1. 下载 `https://github.com/microsoft/WSL2-Linux-Kernel/tree/v5.6-rc2` 内核代码
2. 通过 `make menuconfig KCONFIG_CONFIG=Microsoft/config-wsl` 配置自定义内核配置
**注意** 如果报错 `Your display is too small to run Menuconfig!`,需要将终端最大化(tui形式)
3. 勾选`Device Drivers -> USB Support -> USB Serial Converter support`
> 包括(CH341/CH210X等)
4. 使用`make KCONFIG_CONFIG=Microsoft/config-wsl -j8` 编译代码
5. 将编译好的内核复制到 Windows 用户目录：`cp arch/x86/boot/bzImage /mnt/c/Users/<your-user-name-here>/wsl_kernel`
6. 在 Windows 用户目录中创建一个名为 `.wslconfig` 的文件,键入以下内容:
```ini
[wsl2]
kernel = C:\\Users\\<your-user-name-here>\\wsl_kernel
```

```
编译输出:
BUILD   arch/x86/boot/bzImage
Setup is 14012 bytes (padded to 14336 bytes).
System is 8849 kB
CRC 1f316c7f
Kernel: arch/x86/boot/bzImage is ready  (#1)
```

## bug or problem

### 启动时出现 KERNEL PANIC! Please reboot your computer. VFS: unable to mount root fs on unkonwn-block(0,0)

一般是由于linux自动更新不完全造成的启动失败, 解决方法如下:

- 开机时按 `F11` 进入 `recover menu`(或者 `ESC`进入UEFI界面 --> 选择`Ubuntu System bootload` 进入恢复界面)
- `Advanced options for ubuntu` --> 选择旧系统(recovery mode) --> 开启 `fsck` (文件系统的读写模式) --> `system-summary`(查看系统信息是否正常) --> `root` (进入单用户模式)
- 输入密码登录shell
- `dpkg -l | grep linux-image` 查看当前系统内核版本
- `update-initramfs -u -k 6.14.0-29-generic` 更新出问题的内核
- `update-grub` 更新grub