
## window官方提供的工具

- [Autoruns-window监视器](https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns)
- [Process Monitor-window进程监听器](https://learn.microsoft.com/en-us/sysinternals/downloads/procmon)
- [process-explorer 官方进程dll查看器](https://learn.microsoft.com/en-us/sysinternals/downloads/process-explorer)
- [三方window镜像下载(支持指定版本号)](https://uupdump.net/)

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