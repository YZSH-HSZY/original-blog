# wsl(window subsystem for linux)使用

## 内核重新编译

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

### bug合集

#### 使用.wslconfig替换内核无法启动

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

#### 通过tui菜单重新设置内核编译配置文件
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