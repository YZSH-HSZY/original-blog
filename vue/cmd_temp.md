Microsoft Windows [版本 10.0.19042.1766]
(c) Microsoft Corporation。保留所有权利。

D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>adb version
Android Debug Bridge version 1.0.32

D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>adb devices
adb server is out of date.  killing...
* daemon started successfully *
List of devices attached
emulator-5554   device


D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>adb connect 127.0.0.1:8554
connected to 127.0.0.1:8554

D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>adb devices
List of devices attached
emulator-5554   device


D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>network /?
'network' 不是内部或外部命令，也不是可运行的程序
或批处理文件。

D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>netstat -ano | findstr 5037
  TCP    127.0.0.1:5037         0.0.0.0:0              LISTENING       500

D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>tasklist | findstr 500
spoolsv.exe                   4500 Services                   0     11,740 K
YoudaoDictHelper.exe          1792 Console                    1     17,500 K
msedge.exe                   13500 Console                    1     21,532 K
adb.exe                        500 Console                    1      2,032 K

D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>tasklist /?

TASKLIST [/S system [/U username [/P [password]]]]
         [/M [module] | /SVC | /V] [/FI filter] [/FO format] [/NH]

描述:
    该工具显示在本地或远程机器上当前运行的进程列表。


参数列表:
   /S     system           指定连接到的远程系统。

   /U     [domain\]user    指定应该在哪个用户上下文执行这个命令。

   /P     [password]       为提供的用户上下文指定密码。如果省略，则
                           提示输入。

   /M     [module]         列出当前使用所给 exe/dll 名称的所有任务。
                           如果没有指定模块名称，显示所有加载的模块。

   /SVC                    显示每个进程中主持的服务。

   /APPS 显示 Microsoft Store 应用及其关联的进程。

   /V                      显示详细任务信息。

   /FI    filter           显示一系列符合筛选器
                           指定条件的任务。

   /FO    format           指定输出格式。
                           有效值: "TABLE"、"LIST"、"CSV"。

   /NH                     指定列标题不应该
                           在输出中显示。
                           只对 "TABLE" 和 "CSV" 格式有效。

   /?                      显示此帮助消息。

筛选器:
    筛选器名称     有效运算符           有效值
    -----------     ---------------           --------------------------
    STATUS          eq, ne                    RUNNING | SUSPENDED
                                              NOT RESPONDING | UNKNOWN
    IMAGENAME       eq, ne                    映像名称
    PID             eq, ne, gt, lt, ge, le    PID 值
    SESSION         eq, ne, gt, lt, ge, le    会话编号
    SESSIONNAME     eq, ne                    会话名称
    CPUTIME         eq, ne, gt, lt, ge, le    CPU 时间，格式为
                                              hh:mm:ss。
                                              hh - 小时，
                                              mm - 分钟，ss - 秒
    MEMUSAGE        eq, ne, gt, lt, ge, le    内存使用(以 KB 为单位)
    USERNAME        eq, ne                    用户名，格式为
                                              [域\]用户
    SERVICES        eq, ne                    服务名称
    WINDOWTITLE     eq, ne                    窗口标题
    模块         eq, ne                    DLL 名称

注意: 当查询远程计算机时，不支持 "WINDOWTITLE" 和 "STATUS"
      筛选器。

Examples:
    TASKLIST
    TASKLIST /M
    TASKLIST /V /FO CSV
    TASKLIST /SVC /FO LIST
    TASKLIST /APPS /FI "STATUS eq RUNNING"
    TASKLIST /M wbem*
    TASKLIST /S system /FO LIST
    TASKLIST /S system /U 域\用户名 /FO CSV /NH
    TASKLIST /S system /U username /P password /FO TABLE /NH
    TASKLIST /FI "USERNAME ne NT AUTHORITY\SYSTEM" /FI "STATUS eq running"

D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>tasklist /V |findstr 500
svchost.exe                   4448 Services                   0     11,500 K Unknown         暂缺                                                    0:00:00 暂缺
spoolsv.exe                   4500 Services                   0     11,732 K Unknown         暂缺                                                    0:00:00 暂缺
qemu-system-i386.exe          7676 Console                    1     37,500 K Running         DESKTOP-K8NO2D3\USER                                    1:06:24 Android Emulator - Pixel_5_API_25:5554
YoudaoDictHelper.exe          1792 Console                    1     17,500 K Unknown         DESKTOP-K8NO2D3\USER                                    0:01:54 暂缺
msedge.exe                   13500 Console                    1     21,788 K Unknown         DESKTOP-K8NO2D3\USER                                    0:00:23 暂缺
adb.exe                        500 Console                    1      2,032 K Unknown         DESKTOP-K8NO2D3\USER                                    0:00:01 暂缺

D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>listof /?
'listof' 不是内部或外部命令，也不是可运行的程序
或批处理文件。

D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>wmic /?

WMIC 已弃用。

[全局开关] <命令>

可以使用以下全局开关:
/NAMESPACE           别名在其上操作的命名空间的路径。
/ROLE                包含别名定义的角色的路径。
/NODE                别名在其上操作的服务器。
/IMPLEVEL            客户端模拟级别。
/AUTHLEVEL           客户端身份验证级别。
/LOCALE              客户端应使用的语言 ID。
/PRIVILEGES          启用或禁用所有权限。
/TRACE               将调试信息输出到 stderr。
/RECORD              记录所有输入命令和输出内容。
/INTERACTIVE         设置或重置交互模式。
/FAILFAST            设置或重置 FailFast 模式。
/USER                会话期间要使用的用户。
/PASSWORD            登录会话时要使用的密码。
/OUTPUT              指定输出重定向模式。
/APPEND              指定输出重定向模式。
/AGGREGATE           设置或重置聚合模式。
/AUTHORITY           指定连接的 <授权类型>。
/?[:<BRIEF|FULL>]    用法信息。

有关特定全局开关的详细信息，请键入: switch-name /?


当前角色中可以使用以下别名:
ALIAS                    - 对本地系统上可用别名的访问
BASEBOARD                - 基板(也称为主板或系统板)管理。
BIOS                     - 基本输入/输出服务(BIOS)管理。
BOOTCONFIG               - 启动配置管理。
CDROM                    - CD-ROM 管理。
COMPUTERSYSTEM           - 计算机系统管理。
CPU                      - CPU 管理。
CSPRODUCT                - SMBIOS 中的计算机系统产品信息。
DATAFILE                 - 数据文件管理。
DCOMAPP                  - DCOM 应用程序管理。
DESKTOP                  - 用户的桌面管理。
DESKTOPMONITOR           - 桌面监视器管理。
DEVICEMEMORYADDRESS      - 设备内存地址管理。
DISKDRIVE                - 物理磁盘驱动器管理。
DISKQUOTA                - 用于 NTFS 卷的磁盘空间使用量。
DMACHANNEL               - 直接内存访问(DMA)通道管理。
ENVIRONMENT              - 系统环境设置管理。
FSDIR                    - 文件系统目录项管理。
GROUP                    - 组帐户管理。
IDECONTROLLER            - IDE 控制器管理。
IRQ                      - 中断请求线路(IRQ)管理。
JOB                      - 提供对使用计划服务安排的作业的访问。
LOADORDER                - 定义执行依赖关系的系统服务的管理。
LOGICALDISK              - 本地存储设备管理。
LOGON                    - 登录会话。
MEMCACHE                 - 缓存内存管理。
MEMORYCHIP               - 内存芯片信息。
MEMPHYSICAL              - 计算机系统的物理内存管理。
NETCLIENT                - 网络客户端管理。
NETLOGIN                 - 网络登录信息(属于特定用户)管理。
NETPROTOCOL              - 协议(及其网络特征)管理。
NETUSE                   - 活动网络连接管理。
NIC                      - 网络接口控制器(NIC)管理。
NICCONFIG                - 网络适配器管理。
NTDOMAIN                 - NT 域管理。
NTEVENT                  - NT 事件日志中的项目。
NTEVENTLOG               - NT 事件日志文件管理。
ONBOARDDEVICE            - 主板(系统板)中内置的通用适配器设备的管理。
OS                       - 已安装操作系统的管理。
PAGEFILE                 - 虚拟内存文件交换管理。
PAGEFILESET              - 页面文件设置管理。
PARTITION                - 物理磁盘的已分区区域的管理。
PORT                     - I/O 端口管理。
PORTCONNECTOR            - 物理连接端口管理。
PRINTER                  - 打印机设备管理。
PRINTERCONFIG            - 打印机设备配置管理。
PRINTJOB                 - 打印作业管理。
PROCESS                  - 进程管理。
PRODUCT                  - 安装程序包任务管理。
QFE                      - 快速修复工程。
QUOTASETTING             - 卷上的磁盘配额设置信息。
RDACCOUNT                - 远程桌面连接权限管理。
RDNIC                    - 对特定网络适配器的远程桌面连接管理。
RDPERMISSIONS            - 特定远程桌面连接的权限。
RDTOGGLE                 - 远程打开或关闭远程桌面侦听程序。
RECOVEROS                - 操作系统出现故障时将从内存收集的信息。
REGISTRY                 - 计算机系统注册表管理。
SCSICONTROLLER           - SCSI 控制器管理。
SERVER                   - 服务器信息管理。
SERVICE                  - 服务应用程序管理。
SHADOWCOPY               - 卷影副本管理。
SHADOWSTORAGE            - 卷影副本存储区域管理。
SHARE                    - 共享资源管理。
SOFTWAREELEMENT          - 系统上安装的软件产品元素的管理。
SOFTWAREFEATURE          - SoftwareElement 的软件产品子集的管理。
SOUNDDEV                 - 声音设备管理。
STARTUP                  - 当用户登录到计算机系统时自动运行的命令的管理。
SYSACCOUNT               - 系统帐户管理。
SYSDRIVER                - 基本服务的系统驱动程序管理。
SYSTEMENCLOSURE          - 物理系统外壳管理。
SYSTEMSLOT               - 物理连接点(包括端口、插槽和外设以及专用连接点)的管理。
TAPEDRIVE                - 磁带驱动器管理。
TEMPERATURE              - 温度传感器(电子温度计)数据管理。
TIMEZONE                 - 时区数据管理。
UPS                      - 不间断电源(UPS)管理。
USERACCOUNT              - 用户帐户管理。
VOLTAGE                  - 电压传感器(电子电压表)数据管理。
VOLUME                   - 本地存储卷管理。
VOLUMEQUOTASETTING       - 将磁盘配额设置与特定磁盘卷相关联。
VOLUMEUSERQUOTA          - 每用户存储卷配额管理。
WMISET                   - WMI 服务操作参数管理。

有关特定别名的详细信息，请键入: alias /?

CLASS     - 按 Esc 键可获取完整 WMI 架构。
PATH      - 按 Esc 键可获取完整 WMI 对象路径。
CONTEXT   - 显示所有全局开关的状态。
QUIT/EXIT - 退出程序。

有关 CLASS/PATH/CONTEXT 的详细信息，请键入: (CLASS | PATH | CONTEXT) /?


D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>process /?
'process' 不是内部或外部命令，也不是可运行的程序
或批处理文件。

D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>ps /?
'ps' 不是内部或外部命令，也不是可运行的程序
或批处理文件。

D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>$PSVersionTable
'$PSVersionTable' 不是内部或外部命令，也不是可运行的程序
或批处理文件。

D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>$PSVersionTable$
'$PSVersionTable$' 不是内部或外部命令，也不是可运行的程序
或批处理文件。

D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>%PSVersionTable%
'%PSVersionTable%' 不是内部或外部命令，也不是可运行的程序
或批处理文件。

D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>wmic process get 'adb.exe'
节点 - DESKTOP-K8NO2D3
错误:
描述 = 无效查询



D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>wmic process where name="adb.exe" get exexcutablepath
节点 - DESKTOP-K8NO2D3
错误:
描述 = 无效查询



D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>wmic process where name="adb.exe" get executablepath
ExecutablePath
D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs\adb.exe


D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>gcim
'gcim' 不是内部或外部命令，也不是可运行的程序
或批处理文件。

D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>wmic process where name="emulator.exe" get executablepath,pid
节点 - DESKTOP-K8NO2D3
错误:
描述 = 无效查询



D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>wmic process where name="emulator.exe"
Caption       CommandLine                        CreationClassName  CreationDate               CSCreationClassName   CSName           Description   ExecutablePath                       ExecutionState  Handle  HandleCount  InstallDate  KernelModeTime  MaximumWorkingSetSize  MinimumWorkingSetSize  Name          OSCreationClassName    OSName                                                               OtherOperationCount  OtherTransferCount  PageFaults  PageFileUsage  ParentProcessId  PeakPageFileUsage  PeakVirtualSize  PeakWorkingSetSize  Priority  PrivatePageCount  ProcessId  QuotaNonPagedPoolUsage  QuotaPagedPoolUsage  QuotaPeakNonPagedPoolUsage  QuotaPeakPagedPoolUsage  ReadOperationCount  ReadTransferCount  SessionId  Status  TerminationDate  ThreadCount  UserModeTime  VirtualSize  WindowsVersion  WorkingSetSize  WriteOperationCount  WriteTransferCount
emulator.exe  emulator.exe  -avd Pixel_5_API_25  Win32_Process      20230628114953.613457+480  Win32_ComputerSystem  DESKTOP-K8NO2D3  emulator.exe  E:\AndroidSDK\emulator\emulator.exe                  13464   149                       468750          1380                   200                    emulator.exe  Win32_OperatingSystem  Microsoft Windows 10 专业版|C:\WINDOWS|\Device\Harddisk0\Partition3  361                  6168                3088        10580          14184            10944              4440817664       8696                8         10833920          13464      9                       207                  10                          208                      21                  7987               1                                   1            156250        4437618688   10.0.19042      12288           9                    354


D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>tasklist /V |findstr 13464
emulator.exe                 13464 Console                    1         12 K Unknown         DESKTOP-K8NO2D3\USER                                    0:00:00 暂缺

D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>adb connect 127.0.0.1:13464
unable to connect to :5555

D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>adb decvices
Android Debug Bridge version 1.0.32

 -a                            - directs adb to listen on all interfaces for a connection
 -d                            - directs command to the only connected USB device
                                 returns an error if more than one USB device is present.
 -e                            - directs command to the only running emulator.
                                 returns an error if more than one emulator is running.
 -s <specific device>          - directs command to the device or emulator with the given
                                 serial number or qualifier. Overrides ANDROID_SERIAL
                                 environment variable.
 -p <product name or path>     - simple product name like 'sooner', or
                                 a relative/absolute path to a product
                                 out directory like 'out/target/product/sooner'.
                                 If -p is not specified, the ANDROID_PRODUCT_OUT
                                 environment variable is used, which must
                                 be an absolute path.
 -H                            - Name of adb server host (default: localhost)
 -P                            - Port of adb server (default: 5037)
 devices [-l]                  - list all connected devices
                                 ('-l' will also list device qualifiers)
 connect <host>[:<port>]       - connect to a device via TCP/IP
                                 Port 5555 is used by default if no port number is specified.
 disconnect [<host>[:<port>]]  - disconnect from a TCP/IP device.
                                 Port 5555 is used by default if no port number is specified.
                                 Using this command with no additional arguments
                                 will disconnect from all connected TCP/IP devices.

device commands:
  adb push [-p] <local> <remote>
                               - copy file/dir to device
                                 ('-p' to display the transfer progress)
  adb pull [-p] [-a] <remote> [<local>]
                               - copy file/dir from device
                                 ('-p' to display the transfer progress)
                                 ('-a' means copy timestamp and mode)
  adb sync [ <directory> ]     - copy host->device only if changed
                                 (-l means list but don't copy)
                                 (see 'adb help all')
  adb shell                    - run remote shell interactively
  adb shell <command>          - run remote shell command
  adb emu <command>            - run emulator console command
  adb logcat [ <filter-spec> ] - View device log
  adb forward --list           - list all forward socket connections.
                                 the format is a list of lines with the following format:
                                    <serial> " " <local> " " <remote> "\n"
  adb forward <local> <remote> - forward socket connections
                                 forward specs are one of:
                                   tcp:<port>
                                   localabstract:<unix domain socket name>
                                   localreserved:<unix domain socket name>
                                   localfilesystem:<unix domain socket name>
                                   dev:<character device name>
                                   jdwp:<process pid> (remote only)
  adb forward --no-rebind <local> <remote>
                               - same as 'adb forward <local> <remote>' but fails
                                 if <local> is already forwarded
  adb forward --remove <local> - remove a specific forward socket connection
  adb forward --remove-all     - remove all forward socket connections
  adb reverse --list           - list all reverse socket connections from device
  adb reverse <remote> <local> - reverse socket connections
                                 reverse specs are one of:
                                   tcp:<port>
                                   localabstract:<unix domain socket name>
                                   localreserved:<unix domain socket name>
                                   localfilesystem:<unix domain socket name>
  adb reverse --norebind <remote> <local>
                               - same as 'adb reverse <remote> <local>' but fails
                                 if <remote> is already reversed.
  adb reverse --remove <remote>
                               - remove a specific reversed socket connection
  adb reverse --remove-all     - remove all reversed socket connections from device
  adb jdwp                     - list PIDs of processes hosting a JDWP transport
  adb install [-lrtsd] <file>
  adb install-multiple [-lrtsdp] <file...>
                               - push this package file to the device and install it
                                 (-l: forward lock application)
                                 (-r: replace existing application)
                                 (-t: allow test packages)
                                 (-s: install application on sdcard)
                                 (-d: allow version code downgrade)
                                 (-p: partial application install)
  adb uninstall [-k] <package> - remove this app package from the device
                                 ('-k' means keep the data and cache directories)
  adb bugreport                - return all information from the device
                                 that should be included in a bug report.

  adb backup [-f <file>] [-apk|-noapk] [-obb|-noobb] [-shared|-noshared] [-all] [-system|-nosystem] [<packages...>]
                               - write an archive of the device's data to <file>.
                                 If no -f option is supplied then the data is written
                                 to "backup.ab" in the current directory.
                                 (-apk|-noapk enable/disable backup of the .apks themselves
                                    in the archive; the default is noapk.)
                                 (-obb|-noobb enable/disable backup of any installed apk expansion
                                    (aka .obb) files associated with each application; the default
                                    is noobb.)
                                 (-shared|-noshared enable/disable backup of the device's
                                    shared storage / SD card contents; the default is noshared.)
                                 (-all means to back up all installed applications)
                                 (-system|-nosystem toggles whether -all automatically includes
                                    system applications; the default is to include system apps)
                                 (<packages...> is the list of applications to be backed up.  If
                                    the -all or -shared flags are passed, then the package
                                    list is optional.  Applications explicitly given on the
                                    command line will be included even if -nosystem would
                                    ordinarily cause them to be omitted.)

  adb restore <file>           - restore device contents from the <file> backup archive

  adb help                     - show this help message
  adb version                  - show version num

scripting:
  adb wait-for-device          - block until device is online
  adb start-server             - ensure that there is a server running
  adb kill-server              - kill the server if it is running
  adb get-state                - prints: offline | bootloader | device
  adb get-serialno             - prints: <serial-number>
  adb get-devpath              - prints: <device-path>
  adb status-window            - continuously print device status for a specified device
  adb remount                  - remounts the /system and /vendor (if present) partitions on the device read-write
  adb reboot [bootloader|recovery] - reboots the device, optionally into the bootloader or recovery program
  adb reboot-bootloader        - reboots the device into the bootloader
  adb root                     - restarts the adbd daemon with root permissions
  adb usb                      - restarts the adbd daemon listening on USB
  adb tcpip <port>             - restarts the adbd daemon listening on TCP on the specified port
networking:
  adb ppp <tty> [parameters]   - Run PPP over USB.
 Note: you should not automatically start a PPP connection.
 <tty> refers to the tty for PPP stream. Eg. dev:/dev/omap_csmi_tty1
 [parameters] - Eg. defaultroute debug dump local notty usepeerdns

adb sync notes: adb sync [ <directory> ]
  <localdir> can be interpreted in several ways:

  - If <directory> is not specified, /system, /vendor (if present), and /data partitions will be updated.

  - If it is "system", "vendor" or "data", only the corresponding partition
    is updated.

environmental variables:
  ADB_TRACE                    - Print debug information. A comma separated list of the following values
                                 1 or all, adb, sockets, packets, rwx, usb, sync, sysdeps, transport, jdwp
  ANDROID_SERIAL               - The serial number to connect to. -s takes priority over this if given.
  ANDROID_LOG_TAGS             - When used with the logcat option, only these debug tags are printed.

D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>adb devices
List of devices attached
emulator-5554   device


D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>adb devices -l
List of devices attached
emulator-5554          device product:sdk_google_phone_x86 model:Android_SDK_built_for_x86 device:generic_x86


D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>adb connect 127.0.0.1:13464
unable to connect to 127.0.0.1:13464:13464

D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>adb connect 127.0.0.1
connected to 127.0.0.1:5555

D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>adb devices -l
List of devices attached
emulator-5554          device product:sdk_google_phone_x86 model:Android_SDK_built_for_x86 device:generic_x86
127.0.0.1:5555         offline


D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>adb devices
List of devices attached
emulator-5554   device
127.0.0.1:5555  offline


D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>adb connect 127.0.0.1:13464
unable to connect to :5555

D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>adb disconnect 127.0.0.1


D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>adb devices
List of devices attached
emulator-5554   device


D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>adb connect 127.0.0.1:13464
unable to connect to 127.0.0.1:13464:13464

D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>tasklist /V |findstr 5555

D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>adb connect 127.0.0.1:2
unable to connect to 127.0.0.1:2:2

D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>adb devices
List of devices attached


D:\HBuilder\HBuilderX\plugins\launcher\tools\adbs>