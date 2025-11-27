## cmd命令

### mklink

mklink 的作用是创建符号链接，也可创建硬链接。可作用与文件/目录。
在控制台 cmd 中显示帮助信息如下：

```
MKLINK [[/D] | [/H] | [/J]] Link Target

        /D      创建目录符号链接。默认为文件
                符号链接。
        /H      创建硬链接而非符号链接。
        /J      创建目录联接。
        Link    指定新的符号链接名称。
        Target  指定新链接引用的路径
                (相对或绝对)。
```

==注意==：在 cmd 中如果使用相对路径指定引用，需要使用'\'符作为路径分割符。

### mstsc

mstsc 是 windows 专业版内置的远程桌面工具，你可以在 cmd 中使用该命令打开远程桌面连接工具。
windows 远程连接中，被连接主机需要的默认开放端口为 tcp:3389

### echo

在 cmd 中，使用 echo 输出自带换行。可以查看 echo 命令的帮助如下：

```
C:\Users\USER>echo /?
显示消息，或者启用或关闭命令回显。

  ECHO [ON | OFF]
  ECHO [message]

若要显示当前回显设置，请键入不带参数的 ECHO。
```

> 可以看到 cmd 中 echo 命令不像 Linux 下有着众多的扩展选项。因此如果想要在 cmd 中输出换行符，只能借助其他方式实现。
> 这是几种实现方式 1.借助临时文件和命令连接符& `echo "as">>1.txt & echo "new line as">>1.txt & type 1.txt` 2.借助 cmd 下的取消转义符^将特殊字符：换行符或管道符等普通化，示例如下：

```
C:\Users\USER>echo as^
More?		<----此处输入换行
More? xtr
as
xtr
```

### dir

显示目录中的文件和子目录列表

```sh
DIR [drive:][path][filename] [/A[[:]attributes]] [/B] [/C] [/D] [/L] [/N]
  [/O[[:]sortorder]] [/P] [/Q] [/R] [/S] [/T[[:]timefield]] [/W] [/X] [/4]
```

> 选项
- `/A`          显示具有指定属性的文件
  `D`  目录               `R`  只读文件
  `H`  隐藏文件            `A`  准备存档的文件
  `S`  系统文件            `I`  无内容索引文件
  `L`  重新分析点          `O`  脱机文件
  `-`  表示"否"的前缀
  如: `dir /A-D .` 显示当前目录下所有文件(不包括目录)
- `/B`          使用空格式(没有标题信息或摘要)

### for

`FOR %variable IN (set) DO command [command-parameters]`

  %variable  指定一个单一字母可替换的参数。
  (set)      指定一个或一组文件。可以使用通配符。
  command    指定对每个文件执行的命令。
  command-parameters
             为特定命令指定参数或命令行开关。

在批处理程序中使用 FOR 命令时，指定变量请使用 %%variable
而不要用 %variable。变量名称是区分大小写的，所以 %i 不同于 %I.

如果启用命令扩展，则会支持下列 FOR 命令的其他格式:

- `FOR /D %variable IN (set) DO command [command-parameters]`

    如果集中包含通配符，则指定与目录名匹配，而不与文件名匹配。

- `FOR /R [[drive:]path] %variable IN (set) DO command [command-parameters]`

    检查以 [drive:]path 为根的目录树，指向每个目录中的 FOR 语句。
    如果在 /R 后没有指定目录规范，则使用当前目录。如果集仅为一个单点(.)字符，
    则枚举该目录树。

- `FOR /L %variable IN (start,step,end) DO command [command-parameters]`

    该集表示以增量形式从开始到结束的一个数字序列。因此，(1,1,5)将产生序列
    1 2 3 4 5，(5,-1,1)将产生序列(5 4 3 2 1)

### find 或 findstr

cmd 中 find 和 findstr 命令类似与 shell 的 grep 命令，作用是在文件中寻找字符串。其中 find 不支持正则，而 findstr 支持
1.find 命令帮助信息如下

```
E:\git\blog>find /?
在文件中搜索字符串。

FIND [/V] [/C] [/N] [/I] [/OFF[LINE]] "string" [[drive:][path]filename[ ...]]

  /V         显示所有未包含指定字符串的行。
  /C         仅显示包含字符串的行数。
  /N         显示行号。
  /I         搜索字符串时忽略大小写。
  /OFF[LINE] 不要跳过具有脱机属性集的文件。
  "string" 指定要搜索的文本字符串。
  [drive:][path]filename
             指定要搜索的文件。

如果没有指定路径，FIND 将搜索在提示符处键入
的文本或者由另一命令产生的文本。
```

2.findstr 有两种查找方式，文本查找和正则表达式查找

`ipconfig|findstr /R /i /c:"^[^ipv]*192\.168"`此命令查找 ip 配置信息中地址 192 前不出现 i、p、v 字符的行。

具体参阅[microsoft 手册-findstr 命令](https://learn.microsoft.com/zh-cn/windows-server/administration/windows-commands/findstr "microsoft学习网站")

### set

1. 字符串截取
set 目标字符串=%源字符串:~起始值,截取长度%
截取长度为负数时，表示截取指定段，负数即从右开始计数

```
set a=asdfh
set a=%a:~2,-1%
echo %a%
df
```

2. 字符串拼接，类似 strcat，将一个字符串连接到另一个字符型指针或字符数组的末尾。
set 目标字符串=%目标字符串%%源字符串%

3. 数值计算, 使用 `/A` 选项评估字符串为数字表达式, 如
`set /a 1*1024`

### msg

msg 将消息发送给用户。

```
MSG {username | sessionname | sessionid | @filename | *}
    [/SERVER:servername] [/TIME:seconds] [/V] [/W] [message]

  username            标识指定的用户名。
  sessionname         会话名。
  sessionid           会话 ID。
  @filename           识别这样一个文件，该文件含有将所发消息发送到的用户
                      名、会话名和会话标识号的列表。
  *                   给指定服务器上的所有会话发送信息。
  /SERVER:servername  要联系的服务器(默认值是当前值)。
  /TIME:seconds       等待接收器确认消息的时间延迟。
  /V                  显示有关执行的操作的信息。
  /W                  等待用户的响应，跟 /V 一起有用。
  message             要发送的消息。如果没有指定，发出提示，或者从 stdin
                      读取。
示例：
msg %USERNAME% /time:1 "%ipValue%已复制"
向user发送消息，1秒后关闭弹窗
```

### ftp

连接 ftp 服务，可以交互使用 Ftp（cmd 中输入 ftp 即可）。

```
FTP [-v] [-d] [-i] [-n] [-g] [-s:filename] [-a] [-A] [-x:sendbuffer] [-r:recvbuffer] [-b:asyncbuffers] [-w:windowsize] [host]

  -v              禁止显示远程服务器响应。
  -n              禁止在初始连接时自动登录。
  -i              关闭多文件传输过程中的
                  交互式提示。
  -d              启用调试。
  -g              禁用文件名通配(请参阅 GLOB 命令)。
  -s:filename     指定包含 FTP 命令的文本文件；命令
                  在 FTP 启动后自动运行。
  -a              在绑字数据连接时使用所有本地接口。
  -A              匿名登录。
  -x:send sockbuf 覆盖默认的 SO_SNDBUF 大小 8192。
  -r:recv sockbuf 覆盖默认的 SO_RCVBUF 大小 8192。
  -b:async count  覆盖默认的异步计数 3
  -w:windowsize   覆盖默认的传输缓冲区大小 65535。
  host            指定主机名称或要连接到的远程主机
                  的 IP 地址。

注意:
  - mget 和 mput 命令将 y/n/q 视为 yes/no/quit。
  - 使用 Ctrl-C 中止命令。
```

交互式使用 ftp 面板中，使用 open 命令连接服务时，如果指定端口请用空格分隔 ip 和 port

### runas

以指定用户身份运行程序

```
runas /noprofile /user:mymachine\administrator cmd
   /noprofile        指定不应该加载用户的配置文件。
                     这会加速应用程序加载，但
                     可能会造成一些应用程序运行不正常。默认为/profile

```

解决禁止输入空密码，参[cmd_bat_example](./cmd_bat_example.md)

### wmic

格式如下

```
D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>wmic process where name="adb.exe" get executablepath
ExecutablePath
D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs\adb.exe
```

```
D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>wmic /?
WMIC 已弃用。
[全局开关] <命令>
```

wmic 的替代品就是 powershell 的 Get-WmiObject。

```
PS C:\Users\Student> help Get-CimInstance
名称
    Get-CimInstance
PS C:\Users\Student> help Get-CimInstance
别名
    gcim
```

### regedit

打开注册表编辑器
也可以使用 reg 命令在 cmd 中操作注册表，以下为禁用 window 更新医生服务的 cmd 命令：
`reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WaaSMedicSvc" /v "Start" /t REG_DWORD /d "4" /f`
位置 HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services 中，可设置服务启动类型
Start 值为 4 表禁用，为 3 表手动

### sc

SC 是用来与服务控制管理器和服务进行通信的命令行程序。
可以操作禁用的服务并更改其状态，

```
sc config <服务名serverName> start={boot|system|auto|demand|disabled|delayed-auto}
disabled为禁用，demand为手动
```

### net

net 可以对未禁用的服务更改其状态，如启动、停止、暂停、恢复等

### schtasks

SCHTASKS /parameter [arguments]
使管理员能够在本地或远程系统上创建、删除、查询、更改、运行和结束定时任务。

### tasklist

`tasklist [/S system [/U username [/P [password]]]] [/M [module] | /SVC | /V] [/FI filter] [/FO format] [/NH]`

工具显示在本地或远程机器上当前运行的进程列表

```
/S     system           指定连接到的远程系统。
/U     [domain\]user    指定应该在哪个用户上下文执行这个命令。
/P     [password]       为提供的用户上下文指定密码。如果省略，则提示输入。
/M     [module]         列出当前使用所给 exe/dll 名称的所有任务。如果没有指定模块名称，显示所有加载的模块。
/SVC                    显示每个进程中主持的服务。
/APPS 显示 Microsoft Store 应用及其关联的进程。
/V                      显示详细任务信息。
/FI    filter           显示一系列符合筛选器指定条件的任务。
/FO    format           指定输出格式。有效值: "TABLE"、"LIST"、"CSV"。
/NH                     指定列标题不应该在输出中显示。只对 "TABLE" 和 "CSV" 格式有效。
```

### chdir

类似 `Unix` 命令 `pwd`, 显示当前目录的名称或将其更改

## 基本示例

### 后台运行阻塞命令
```sh
# 如后台开启usbipd服务
start /B cmd /c "usbipd server"

# 命令解析
start  通启动一个单独的窗口以运行指定的程序或命令
  /B     表示 不打开新窗口启动
  cmd /c {cmd}   表示 执行字符串指定的命令然后终止
```