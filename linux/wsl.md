# wsl(window subsystem for linux)使用

## 安装

### wsl安装

**注意** 你需要确保开启了window功能--适用于linux的win子系统，根据以下操作打开
> Win + R，输入 `appwiz.cpl`，左上角找到“启动或关闭 Windows 功能”，启用wsl和虚拟机平台和虚拟机监控功能。
1. [从官网手动下载安装包](https://learn.microsoft.com/zh-cn/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package),将`.AppxBundle`以及解压后的`.appx` 文件更改为 zip 文件并解压，获取ubuntu.exe文件进行安装。
2. 从Microsoft Store安装，你可以设置-->存储-->更改新内容保存位置中将安装app的位置改到D盘WindowsApps目录下

### wsl查看可安装的linux发行版
`wsl --list --online` 或 `wsl -l -o` 查看在线商店可用的 Linux 发行版列表。

**注意** 出现==无法解析服务器的名称或地址错误==时，查看 `raw.githubsercontent.com` 能否ping通；可以在hosts手动更改该地址解析ip或者直接使用`114.114.114.114` `8.8.8.8`这两个dns服务器（在控制面版/网络适配器/ip4设置中）。

### wsl查看安装linux版本
查安装的发行版的 WSL 版本：`wsl -l -v`

### wsl设置默认版本和启动linux

- 使用命令 `wsl --set-default-version <1|2>` 启用wsl1或wsl2

- `wsl -s <DistributionName>` 或 `wsl --set-default <DistributionName>`，将 DistributionName 为要使用的 Linux 发行版的名称。 

- 要在 PowerShell 或 Windows 命令提示符下运行特定的 WSL 发行版而不更改默认发行版，请使用命令 `wsl -d <DistributionName>`

### 已启动的容器更改为wsl2
```sh
C:\Users\Administrator>wsl --set-version Ubuntu 2
正在进行转换，这可能需要几分钟时间...
有关与 WSL 2 的主要区别的信息，请访问 https://aka.ms/wsl2
转换完成。
```

## bug

### ubuntu首次启动报错
错误描述：`WslRegisterDistribution failed with error: 0x800701bc`
解决方案：
1. 下载安装[wsl更新msi程序](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)
2. 或者直接使用 `wsl --update`命令 从 Microsoft Store 下载并安装 WSL。

### wsl配置接口网络规则(解决无法访问公网)
1. 防火墙允许接口vEthernet (WSL)中流量通过 `New-NetFirewallRule -DisplayName "WSL" -Direction Inbound  -InterfaceAlias "vEthernet (WSL)"  -Action Allow`
   - 允许指定ip `New-NetFirewallRule -DisplayName "WSL" -Direction Inbound  -LocalAddress <ip> -Action Allow`
2. win+R，键入 wf.msc 打开高级安全控制台访问 Windows 防火墙。配置wsl规则

## example

### wsl设置root初始密码
在默认使用ubuntu登录wsl后，如果想以root用户登录，需初始设置root密码。
可以使用`sudo passwd root`设置

### wsl使用用户root

1. `ubuntu.exe config --default-user root`
**注意** 安装的Ubuntu位置需手动确定
2. `wsl --user <UserName>`以指定用户身份运行

### wsl使用usb设备
[官方教程](https://learn.microsoft.com/zh-cn/windows/wsl/connect-usb)
1. 安装 `usbipd-win` 项目(注意:同步安装服务)
2. 附加 USB 设备
    - 使用`usbipd list`查看设备
    - 使用 `usbipd bind --busid 3-1` 共享设备，从而允许其附加到 WSL(注意:需要管理员权限)
    - 使用 `usbipd attach --wsl --busid <busid>` 附加 USB 设备
    - 在wsl查看 `lsusb`
    - 使用 `usbipd detach --busid <busid>` 取消附加设备

> **注意** 使用`lsusb`查看usb设备信息,如:
`Bus 001 Device 002: ID 1a86:7523 QinHeng Electronics HL-340 USB-Serial adapter`

其中可以看到总线001的设备002是我们挂载的usb设备,可以通过`udevadm info -a -n <tty_symbol>`查看指定的设备idVendor、idProduct是否匹配获取TTY设备文件.
如果运行时未识别(手动挂载的usb设备),可以通过`$ sudo ln -s /dev/bus/usb/001/002 /dev/ttyUSB0`创建符号链接

### 内核重新编译

参[microsoft wsl-v6文档](https://learn.microsoft.com/en-us/community/content/wsl-user-msft-kernel-v6)
参[askubuntu问题回答](https://askubuntu.com/questions/1373910/ch340-serial-device-doesnt-appear-in-dev-wsl/)


**注意** 需要使用安装相应依赖`sudo apt install build-essential flex bison libssl-dev libelf-dev bc python3 pahole libncurses-dev`.
> 其中`pahole`如果没有,可以安装`dwarves`.
> 或者参考[pahole的包介绍](https://launchpad.net/ubuntu/jammy/+package/pahole)

- 下载wsl_kernel6内核 `git clone https://github.com/microsoft/WSL2-Linux-Kernel.git --depth=1 -b linux-msft-wsl-6.1.y`
- 建造内核 `make -j$(nproc) KCONFIG_CONFIG=Microsoft/config-wsl`
- 安装kernel modules and headers: `sudo make modules_install headers_install`
- 复制内核镜像到window文件系统下 `cp arch/x86/boot/bzImage /mnt/c/`
- 停止wsl实例 `wsl --shutdown`


> `uname -a` 更改前: `Linux DESKTOP-UAS0QBB 5.15.153.1-microsoft-standard-WSL2 #1 SMP Fri Mar 29 23:14:13 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux`
> 更改后: `Linux DESKTOP-UAS0QBB 6.1.21.2-microsoft-standard-WSL2+ #1 SMP Wed Sep 25 10:52:01 CST 2024 x86_64 x86_64 x86_64 GNU/Linux`

#### bug合集

##### 使用.wslconfig替换内核无法启动

[同类问题参](https://github.com/microsoft/WSL/issues/10212)

> 问题描述：
```
由于套接字没有连接并且(当使用一个 sendto 调用发送数据报套接字时)没有提供地址，发送或接收数据的请求没有被接受。
Error code: Wsl/Service/CreateInstance/CreateVm/WSAENOTCONN
```
> 通过日志收集wsl启动信息并分析

- 日志收集脚本可通过以下命令获取(在管理员权限下的powershell下执行)
```powershell
Invoke-WebRequest -UseBasicParsing "https://raw.githubusercontent.com/microsoft/WSL/master/diagnostics/collect-wsl-logs.ps1" -OutFile collect-wsl-logs.ps1

Set-ExecutionPolicy Bypass -Scope Process -Force

.\collect-wsl-logs.ps1
```
> 比对编译的配置文件`Microsoft/config-wsl`和官方示例文件`arch/x86/configs/config-wsl`中设置项的区别
> 添加设置项`CONFIG_HYPERV_VSOCKETS`/`CONFIG_VSOCKETS`

##### 通过tui菜单重新设置内核编译配置文件
命令`make menuconfig KCONFIG_CONFIG=Microsoft/config-wsl`
> 错误描述: `Your display is too small to run Menuconfig!`
> 解决方案: `ssh终端最大化`

**注意** 同上，请检查一下生成配置文件相应项是否缺少

## ko文件

ko文件是Linux内核模块的对象文件，它是从C源文件编译生成的二进制文件，用于在Linux系统上加载内核模块。(将内核的一些功能移动到内核模块ko中,可以根据需要加载内核功能，减小内核体积)

### ko文件的结构

ko文件的结构如下所示：

* Elf头部
*  Section头部表
*  Section数据
*  relocation表
*  String表
*  Symbol表

### ko文件的生成

ko文件可以通过make命令生成，例如:
`make -C /path/to/kernel/source M=$(pwd) modules`

## udev

udev是Linux内核中设备管理的主要组件，可以通过udev来管理Linux下的设备。提供了以下功能：

* Device Event Handling：udev可以在设备产生事件时立即响应，例如设备插入、拔出、renamed等。
* Device Property Management：udev可以对设备的属性进行管理，例如设备的名称、symlink、权限等。
* Device Node Management：udev可以对设备节点进行管理，例如设备节点的创建、删除、权限设置等。

> udev的主要组件包括：

*  udevd：udev的守护进程，负责侦听设备事件，并将事件转换为udev的事件。
*  udevadm：udev的命令行工具，提供了对设备的管理功能。
*  udev rules：udev的规则文件，提供了对设备的自定义规则。

### udev规则编写

udev rules文件通常存储在 `/etc/udev/rules.d/` 目录下，以数字开头，例如: `99-udisk.rules`

> 其格式如下：
`ACTION=="add", RUN+="/usr/bin/udiskie-mount -2 -o noatime %E{ID_FS_LABEL} %E{DEVNAME}"`

* ACTION：指定了事件的类型，例如add、remove等
* RUN：指定了要执行的命令
* OPTIONS：指定了要传递给命令的选项

例如上面的规则，表示在设备插入时，执行udiskie-mount命令，并传递设备的label和name作为参数。

**注意** udev rules文件的优先级是按照文件名的数字顺序来的，数字越小的规则文件优先级越高

#### udev规则编写示例

##### 将ch340的usb设备添加别名
通过 `lsusb` 查看厂家和产品id,如: 1a86:7523

创建 `/etc/udev/rules.d/99-ch340.rules` 文件，内容如下:
`SUBSYSTEM=="usb", ATTR{idVendor}=="1a86", ATTR{idProduct}=="7523", SYMLINK+="ttyCH340", GROUP="tty", MODE="0666"`

> 其中:
* SUBSYSTEM=="usb"：指定了事件的子系统是usb
* ATTR{idVendor}=="1a86"：指定了要匹配的usb设备的idVendor
* ATTR{idProduct}=="7523"：指定了要匹配的usb设备的idProduct
* SYMLINK+="ttyCH340"：将设备节点链接到 `/dev/ttyCH340` 位置
* GROUP="tty"：将设备节点的组设置为tty
* MODE="0666"：将设备节点的权限设置为0666
  
**注意** 这种别名只针对不需要通过额外的内核模块驱动的usb设备,wsl中ch340设备需要重新编译内核模块,因此请使用KERNEL指定,通过如下规则绑定:
```ini
SUBSYSTEM=="usb", ATTRS{idVendor}=="1a86", ATTRS{idProduct}=="7523", ENV{ID_VENDOR_ID}="$attr{idVendor}", ENV{ID_MODEL_ID}="$attr{idProduct}"
KERNEL=="ttyUSB*", SUBSYSTEM=="tty", ENV{ID_VENDOR_ID}=="1a86", ENV{ID_MODEL_ID}=="7523", SYMLINK+="tty_kc2w", GROUP="tty", MODE="0666"
```

> **注意** 对于自动识别的设备,存在多层封装,如:原始usnb bus->ch341 ko驱动转换的usb-serial->终端tty.可以通过以下命令查看udev识别设备的过程
`udevadm info -q property -n /dev/ttyUSB0`
`udevadm info -a -n <tty_symbol>`
> 之后通过 `ENV` 选项来传递环境变量从一个子系统到另一个子系统,在最终需要创建符号链接的地方进行规则匹配

### udevadm

udevadm 是一个用于管理和控制 udev 系统的命令行工具。它提供了一系列的命令来管理 udev 的行为

> 常用命令
* `udevadm info`: 显示设备的详细信息，包括设备的属性、父设备和子设备等。
* `udevadm trigger`: 触发 udev 事件，例如当设备插入或拔出时。
* `udevadm settle`: 等待 udev 事件处理完成，例如当设备插入或拔出时。
* `udevadm control`: 控制 udev 的行为，例如启用或禁用 udev 事件。
* `udevadm test`: 测试 udev 规则文件，检查规则文件是否正确。
* `udevadm monitor`: 监控 udev 事件，显示设备的插入、拔出和其他事件。
* `udevadm reload`: 重新加载 udev 规则文件，应用新的规则。
* `udevadm reload-rules`: 重新加载 udev 规则文件，应用新的规则。

> 应用场景
* 调试 udev 规则文件
* 监控设备事件
* 控制 udev 的行为
* 测试 udev 规则文件
  
#### 命令示例
- 显示设备的详细信息 `udevadm info -a -n /dev/ttyUSB0`
- 触发 udev 事件 `udevadm trigger -v -t add -s usb -a idVendor=1a86 -a idProduct=7523`
- 等待 udev 事件处理 `udevadm settle -t 10`

### bug

#### 设备重命名失效，报operation错误

1. 通过检查 `sudo udevadm test --action=add <dev_path>` 测试你编写的rule规则文件，dev_path可以通过 `udevadm info -a -n <tty_symbol>` 查看tty挂载的指定系统层级路径
2. 检查udev服务状态 `systemctl status udev`，如果报Host bus错误，确保systemd正常启动。
3. 或者通过 `/lib/udev/udevd --debug` 开启调试守护进程排查

## x11转发使用window显示
安装`x11-apps`用于测试

[vcxsrv下载](https://sourceforge.net/projects/vcxsrv/files/latest/download)

### bug

#### 启动应用出现错误`Illegal instruction`
> 解决方法: **关闭opengl支持**
1. 在远程服务上`export LIBGL_ALWAYS_INDIRECT=1`
2. 远程服务配置转发ip和显示`export DISPLAY=192.168.8.100:0`
3. XLaunch启动配置如下：
    - Multiple Windows
    - Start no client
    - 取消勾选 Native opengl
    - 勾选 Disable access control
4. Xlaunch是一个图像配置程序,通过启动vcxsrv程序开始x-server的; 上述对应命令行如下 `vcxsrv :10 -multiwindow -clipboard -nowgl -ac`

## wsl迁移
- 导出自定义的 WSL 映像，`wsl --export <Distro> <FileName>`，将映像打包到 tar 文件中
- 从共享或存储设备分发 WSL 映像，`wsl --import <Distro> <InstallLocation> <FileName>`，将指定的 tar 文件作为新的分发版导入