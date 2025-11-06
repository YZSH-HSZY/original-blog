
## window官方提供的工具

- [Autoruns-window监视器](https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns)
- [Process Monitor-window进程监听器](https://learn.microsoft.com/en-us/sysinternals/downloads/procmon)
- [process-explorer 官方进程dll查看器](https://learn.microsoft.com/en-us/sysinternals/downloads/process-explorer)
- [三方window镜像下载(支持指定版本号)](https://uupdump.net/)

## example

### window开启自启动设置
要查看Windows的开机自启动项
1. 打开“运行”窗口，或者直接按“win+R”，然后输入“msconfig”。
2. 进入系统配置的窗口，选择其中的“启动”。
3. 点击“打开任务管理器”，就可以看到电脑的所有启动项。
4. 在任务管理器窗口中切换到“启动”选项卡，就可以查看到当前电脑开机时所有的启动项了。
5. 在注册表中查找启动路径，当导航到`HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`时，在右侧表格中可以看到开机自启动项名称以及路径信息。

### window11内存占用过高

> 解决方案:
- 使用RAMMap进行内存清理,在Empty中点击所有,[RAMMap下载地址](https://download.sysinternals.com/files/RAMMap.zip)
p

### window保留存储的空间过高

- `C:\ProgramData\Microsoft\Search\Data\Applications\Windows\Windows.edb` 文件太大
> cmd下 运行`control /name Microsoft.IndexingOptions`
> 点击 高级-->重建 来重建索引

### window10右键菜单太慢

### window系统文件损坏,尝试修复命令

`sfc /scannow`
`DISM /Online /Cleanup-Image /RestoreHealth`
`DISM /Online /Cleanup-Image /RestoreHealth /Source:E:\sources\install.wim:1 /LimitAccess`
`regsvr32 /u pcasvc.dll`
`regsvr32 /i pcasvc.dll`

### 重装系统

#### 批量更改文件权限

> 在重装系统后, administrator用户为安装时设置的账户, 和之前的Administrators 组权限不匹配, 可通过如下更改:
`icacls "D:\yzsh\ssh" /grant administrator:F /t`

### window原生hash计算工具certutil

`certutil -hashfile C:\path\to\your\file.txt {MD5,SHA1,SHA256,SHA512}`  

## Windows Sysinternals Tool

`Windows Sysinternals` 是一套由微软发布的强大免费工具集，包含74个实用工具，旨在帮助用户管理、维护和故障排除Windows系统。它涵盖了多个关键方面，包括进程管理、内存控制、网络监控和磁盘管理等。用户可以通过Microsoft Store 安装和更新这些工具。Sysinternals工具最初由Winternals公司开发，旨在解决工程师在工作中遇到的各种问题

> 参考文档
> - [sysinternals工具集首页](https://learn.microsoft.com/zh-cn/sysinternals/downloads/)

### Process Monitor

监控 Windows 的高级工具, 显示文件系统、注册表和进程/线程活动的实时情况, 包括监控和过滤功能

### Process explorer

进程浏览器, 可用于:
- 查看选定进程已打开的句柄
- 查看进程已加载的动态链接库(DLL)和内存映射文件

### TCPView

显示系统上所有 TCP 和 UDP 终结点的详细列表, 提供gui/cli版本, 相较于NETSTAT信息更丰富