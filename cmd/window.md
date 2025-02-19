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