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

#### 使用/etc/init.d查看服务
```
ubuntu@yzsh:~$ /etc/init.d/ssh status
 * sshd is not running
```
## /proc目录查看进程信息
`<pid>/fd`有几个标准设备，1=stdout;2=stderr
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
## linux command介绍

### find命令

#### find查找文件
`find <find_path> -name <file_name>`

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

### for命令
1. `for i in "Start learning from yiibai.com"; do echo $i; done`
2. `for num in {1..10..1}; do echo $num; done`
3. `arr=( "Welcome","to","yiibai.com" );for i in "${arr[@]}" ;do echo $i ;done`
4. `for ((i=1; i<=10; i++)) ;do echo "$i" ;done`

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
```
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
```
Usage: du [OPTION]... [FILE]...
展示指定文件系统的占用或者默认显示全部文件系统占用
option:
 -h 以符合人类阅读的方式显示大小
 -i 显示inode使用信息而不是块占用
```

### 软件包管理
ubuntu使用apt作为默认的包管理器,是一个命令行包管理工具,提供命令用于 搜索/管理/查询 包信息;提供与一些专有的APT工具(如apt-get、apt-cache)具有相同作用的命令，默认情况下启用交互式选项。

#### apt命令

##### apt镜像源

`sudo sed -i -r 's#http://(archive|security).ubuntu.com#https://mirrors.aliyun.com#g' /etc/apt/sources.list`

##### apt search搜索可用包
`apt search <pkg_sname>`

##### apt show显示安装包元信息(包括大小、版本、依赖关系)
`apt show <pkg_name>`

##### apt upgrade升级软件包
`apt upgrade <pkg_name>`

##### apt install安装软件包
- `apt install <pkg_name>`
- 如果我们想安装一个软件包，但如果软件包已经存在，则不要升级它，可以使用 –no-upgrade 选项: `sudo apt install <pkg_name> --no-upgrade`

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


### sed命令
`sed [OPTION]... {script-only-if-no-other-script} [input-file]...`,如：`sed '[match_lines]s<segment_sign default /><match_string><segment_sign default /><rex_string><segment_sign default />' `

example:
`sed '2,$s/原字符串/替换字符串/g' # 替换2到最后一行`
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

#### linux在文件中查找替换
sed -i s/172.17.2.0:8000/172.17.0.2:8000/g `grep "172.17.2.0" -rl ./`

### dd文件操作

```
Usage: dd [OPERAND]...
  or:  dd OPTION
dd命令用于复制文件，根据操作数进行转换和格式化。如剪切二进制文件头部元信息等。

操作数:
     if   指定输入文件 input file
     of   指定输出文件 output file
     bs   每次读或写的字节数(覆盖ibs/obs) BYTES
     ibs  每次读的字节数 input BYTES
     obs  每次写的字节数 output BYTES
     skip 指定输入时跳过的ibs数 
     seek 指定输出时跳过的obs数 
```
example:
`dd if=<file_name> of=<output_file> bs=<bytes at a time> skip=<skip n ibs>`
     将if指定文件，跳过skip*bs个字节输出到of文件中。

### kill与pkill
```
kill 用于杀死一个进程
pkill 用与关闭一个终端
```
1. kill 介绍
Kill是一个shell内置功能，有两个原因:它允许使用作业id替代进程id，并且允许在您可以创建的进程达到限制时杀死进程。
> 使用方式 `kill [-s sigspec | -n signum | -sigspec] pid | jobspec ... `
> 通过 `-l | -L` 选项列出所有可发送符号名

### ssh使用密钥登录

openssh是ssh协议的开源实现，包括ssh客户端和sshd服务端。在客户端可以连接远程主机，服务端开放端口供其他主机登录本机（默认端口22，可在/etc/ssh中更改）

1. 在客户端使用`ssh-keygen -t <use_key_way>`生成密钥对，一般选用rsa加密方式。可以在($HOME/.ssh目录中）查看。生成id_rsa和id_rsa.pub两个密钥文件。

2. 将客户端的公钥发送到服务端,在客户端执行`ssh-copy-id <ssh_server_user@remote_address> -p <sshd_port>`。

3. 在服务端登录用户主目录的.ssh目录中，查看authorized_keys文件是否正确添加公钥。

### sftp或scp传输文件到服务器
sftp(ssh file transfer protocol, ssh文件传输协议)
与scp相比，sftp支持断点续传和图形化操作,但相较于scp传输较慢。

**使用**
- sftp使用与ssh类似,均需要选与服务器建立连接,使用`sftp <username>@<server_ip_address>`连接服务器
- 使用`put -r <local_dir> <remote_dir>`上传文件夹
- 使用`get -r <remote_dir> <local_dir>`下载文件夹
- 使用`help`或`?`查看帮助信息

### curl设置代理
`curl -x 127.0.0.1:7890 https://a.com/test.exe --output test.exe`

## 文件类型
|文件类型	 |说明                                                   |
|-----------|-------------------------------------------------------|
|b	        |块设备，是一些提供系统存取数据的接口设备，例如硬盘。|
|c	        |字符设备，是一些串行端口的接口设备，例如键盘、鼠标、打印机、tty终端。|
|d	        |目录，类似于Windows的文件夹。|
|l	        |软链接文件，类似于Windows的快捷方式。|
|s	        |套接字文件（socket），用于进程之间的通信。|
|-	        |文件，分纯文本文件（ASCII）和二进制文件（binary）。|

## linux shell使用
### 环境变量
`echo $var_name` 查看环境变量值
`export` 查看全部环境变量

`export PATH=PATH:/bin` 向环境变量中添加值
注意：使用此方法更改的环境变量仅当前终端、当前用户有效，窗口关闭即失效

`.bashrc`或`.bash_profile` 配置文件，在末尾添加一行`export PATH=PATH:/bin`
对当前用户有效，永久生效

配置`/etc/bashrc或/etc/profile或/etc/environment` 文件
对所有用户有效

## linux用户和组命令

### 用户和组管理
1. 查看有系统哪些组`compgen -g`
2. 查看当前用户的组`groups [user_name]`
3. 为当前用户添加附加组`uermod -aG {group_name} [user_name]`

## linux文本操作
### awk 命令

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

#### 指定输入输出分隔符
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

#### awk选项
在`{}`中可以使用`$n`获取列分割后数组对应值,`$0`获取本行内容
`-v var=value`
定义一个用户定义变量，在`{}`中直接用变量名获取，也可以在awk命令末尾通过`<variable_name>=<vaule>`定义

#### awk内建变量和运算符
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

#### awk调用shell命令

1. 使用system()函数,如 `dpkg -L libreadline-dev | awk '{system("if [ -f "$1" ];then echo "$1";fi")}'`
**注意** system括号里面的参数没有加上双引号的话，awk认为它是一个变量，它会从awk的变量里面把它们先置换为常量，然后再回传给shell

2. 借助管道符;如下所示
```
echo 1 | awk '{print $1|"xargs echo "}'
1
```
> 无论使用system还是管道调用shell命令，都是新开一个shell，在相应的cmdline参数送回给shell，所以要注意当前shell变量与新开shell变量问题

### grep命令
grep用于在文件中查找字符串，支持正则表达式(DFA引擎/NFA引擎)
**注意** DFA引擎以文本为推导进行匹配，NFA引擎以表达式为推导进行匹配
```
Usage: grep [OPTION]... PATTERN [FILE]...
Search for PATTERN in each FILE

Pattern selection and interpretation:
  -E, --extended-regexp     PATTERN 作为扩展正则，支持?/+/()/{}/|等
  -F, --fixed-strings       PATTERN 作为字符串，不进行正则解析
  -G, --basic-regexp        PATTERN 作为基本正则(default)，仅支持较少符号
  -P, --perl-regexp         PATTERN 作为 Perl格式 正则，提供更多功能，包括非捕获组、命名捕获组等
```

## linux socket和tcp/udp系列命令

### lsof

lsof(list open file, 列出打开文件),在linux下一切皆文件，如普通文件，目录，特殊的块文件，管道，socket套接字，设备等。因此我们可以使用

#### lsof查看端口被那些程序占用
使用 -i 选项指定
`-i i  select by IPv[46] address: [46][proto][@host|addr][:svc_list|port_list]`
**注意** 需管理员权限

### ss
ss(Socket Statistics, socket统计)，可以用来获取socket统计信息，它显示和netstat类似的内容。与netstat相比ss的优势在于它能够显示更多更详细的有关TCP和连接状态的信息，比netstat更快速更高效。

### nmap
nmap 一款网络端口扫描工具

### netcat
netcat 是一个使用 TCP 或 UDP 协议的网络工具，可以在两台计算机之间建立连接，进行数据传输。它支持多种网络操作，包括但不限于：

- 端口监听：在指定端口上监听传入的连接。
- 端口扫描：扫描目标主机上的开放端口。
- 数据传输：在两台计算机之间传输文件或数据。
- 反向 shell：在目标主机上执行命令并获取 shell 访问。
- 代理：通过中间服务器转发流量。



## linux登录、文件传输

#### ssh使用密钥登录

openssh是ssh协议的开源实现，包括ssh客户端和sshd服务端。在客户端可以连接远程主机，服务端开放端口供其他主机登录本机（默认端口22，可在/etc/ssh中更改）

1. 在客户端使用`ssh-keygen -t <use_key_way>`生成密钥对，一般选用rsa加密方式。可以在($HOME/.ssh目录中）查看。生成id_rsa和id_rsa.pub两个密钥文件。

2. 将客户端的公钥发送到服务端,在客户端执行`ssh-copy-id <ssh_server_user@remote_address> -p <sshd_port>`。

3. 在服务端登录用户主目录的.ssh目录中，查看authorized_keys文件是否正确添加公钥。

#### sftp或scp传输文件到服务器
sftp(ssh file transfer protocol, ssh文件传输协议)
与scp相比，sftp支持断点续传和图形化操作,但相较于scp传输较慢。

**使用**
- sftp使用与ssh类似,均需要选与服务器建立连接,使用`sftp <username>@<server_ip_address>`连接服务器
- 使用`put -r <local_dir> <remote_dir>`上传文件夹
- 使用`get -r <remote_dir> <local_dir>`下载文件夹
- 使用`help`或`?`查看帮助信息






## linux二进制文件查看

### hexdump
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
### xxd
默认以1字节为单位按16进制解释

### od

## linux命令
### seq命令
生成数组,指定first到last和间隔steps
```
Usage: seq [OPTION]... LAST
  or:  seq [OPTION]... FIRST LAST
  or:  seq [OPTION]... FIRST INCREMENT LAST
Print numbers from FIRST to LAST, in steps of INCREMENT.
```


### find命令

#### find选项
- `-type [b/d/c/p/l/f]`   设备|目录|字符设备|管道|符号链接|普通文件
- `-size N[bcwkMG]` 查大小为n的文件（）
-name   filename             #查找名为filename的文件
-perm                        #按执行权限来查找
-user    username             #按文件属主来查找
-group groupname            #按组来查找
-mtime   -n +n                #按文件更改时间来查找文件，-n指n天以内，+n指n天以前
-atime    -n +n               #按文件访问时间来查GIN: 0px">

-ctime    -n +n              #按文件创建时间来查找文件，-n指n天以内，+n指n天以前

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



## linux network配置管理器
linux有NetworkManager和systemd-networkd两个网络配置管理器,你只需要其中一个正常工作即可.使用下述命令将另一个禁用;推荐使用NetworkManager
`systemctl enable NetworkManager`
`systemctl disable systemd-networkd`

- networkd 通常用于网络环境相当静态的服务器安装。
- NetworkManager 通常用于桌面安装，并且用于所有以前版本的 Ubuntu。 NetworkManager 在网络需求变化很大的环境中更容易使用.

### nmcli与nmtui
nmcli 是 NetworkManager 的命令，用于管理网络设置和连接。nmtui是tui版本的管理工具.
显示网络设备信息`nmcli device show docker0`
显示连接信息`nmcli connection show`

> 示例: 添加一个网络连接,类型桥接bridge,别名docker0,连接的接口名docker0,分配ip4地址,启用自动连接
`sudo nmcli connection add type bridge ifname docker0 con-name docker0  ip4 172.17.0.1/16 autoconnect true`

### netplan
适用与(systemd-networkd或者networkmanager)的网络配置文件管理.使用netplan你可以统一配置systemd-networkd和networkmanager,而不需要分别到他们的配置目录下配置接口信息.
Netplan读取/etc/netplan下的描述网络用的各个yaml文件，生成backend config后端配置项。将这些后端配置项通过yaml文件里指定的renderers渲染器(systemd-networkd或者networkmanager)将配置下发到Linux内核中。

netplan generate
以/etc/netplan 配置为输入为renderer指定的底层网络管理工具生成配置文件。
netplan apply
应用配置，使配置生效。
netplan try
试用配置，然后等待用户的确认；如果网络中断或没有给出确认，就自动回滚。

**注意** 注意在/etc/netplan目录下，有多个yaml文件存在，netplan是根据字母表排序，挨个生效的，后面的yaml指定的配置会覆盖前面的yaml指定的配置。

## linux的一些使用示例
### linux的wifi连接
如果使用`iwlist wlan0 scan`扫描wifi时,效果较差可以使用`sudo wpa_cli -i wlan0 scan_result`


`sudo wpa_cli -i wlan0 list_network`

## 查看video设备信息
`v4l2-ctl -d /dev/video -all`
需要安装v4l-utils

## 查看ubuntu的Codename
`lsb_release -a`
输出如下:
```
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 20.04.3 LTS
Release:        20.04
Codename:       focal
```

### ping命令
`sudo apt-get install ping` //centos 使用
`sudo apt-get install inetutils-ping`  //ubuntu

### 命令后台运行
1. 使用 `&` 符
> dockerd 1>/dev/null 2>&1 &
2. 使用 nohup 命令
`nohup {command}`

**注意** nohup和&的区别，nohup不会挂起，在用户正常退出后，命令仍在后台运行。而&在shell终端关闭后，会结束掉启动的后台命令
## 串口操作

### stty配置串口

stty 打印或更改终端特性

#### 选项
```
-F, --file=DEVICE  使用指定的设备打开而不是默认的stdin
```
### cat读取串口数据

### echo发送串口数据

### 使用socat创建虚拟串口对

1. 安装socat
2. 创建一对虚拟串口`socat PTY,link=/dev/ttyV0,mode=777 PTY,link=/dev/ttyV1,mode=777`
 - `PTY` 表示创建一个伪终端（虚拟串口）。
 - `link=/dev/ttyV0` 和 `link=/dev/ttyV1` 分别指定了虚拟串口的设备文件名称。
 - `mode=777` 设置了设备文件的权限，以便所有用户都可以访问。
3. 查看虚拟串口`ls -l /dev/ttyV*`
4. 使用cat/echo测试虚拟串口对是否建立连接