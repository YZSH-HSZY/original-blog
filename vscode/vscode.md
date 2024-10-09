## vscode调试支持
常见流行语言支持: `python`/`c/c++`/`cmake`,其他语言也可通过扩展支持

调试设置参配置文件`launch.json`

## vscode配置

vscode配置文件分为
1. 同步配置文件(profile) 用于多设备同步vscode配置,一般用不到。
2. 默认设置文件(default setting)(使用`ctrl+shift+p`打开命令面板，open default setting json)可以查看默认配置文件，默认只读。其中存放个setting文件各选项说明和示例。
3. 用户设置文件(user setting)(存放在`%USERPROFILE%\AppData\Roaming\Code\User\settings.json`)
4. 工作区设置文件(一般是`<工作区名称>.code-workspace`的文本文件)
5. 文件夹配置设置(存放在.vscode文件夹中，会自动创建。一般有代码编写配置和debug的配置信息)

### .vscode文件夹中常见文件说明

- settings.json：这个文件包含了项目的设置选项。可以在这里进行各种配置，如设置代码风格、启用或禁用扩展插件、定义编辑器的行为等。这些设置会覆盖全局设置，只对当前项目有效。
- launch.json：这个文件用于配置调试器。可以在这里设置调试选项，如指定调试目标（例如 Node.js、Python 等），设置启动参数、环境变量等。它定义了如何启动和调试Visual Studio Code项目。
- tasks.json：这个文件用于定义和配置任务（Tasks）。任务是在 VS Code 中执行的命令或脚本，可以自动化一些常见的工作流程，如编译代码、运行测试、构建项目等。可以在这里定义自定义任务，并通过快捷键或命令面板执行它们。
- extensions.json：这个文件用于记录项目所依赖的扩展插件。当共享项目时，其他人可以根据这个文件安装所需的插件，以便与大家的开发环境保持一致。

#### launch.json配置示例

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Debug",  // 调试配置名
            "type": "cppdbg",
            "request": "launch",
            "program": "${workspaceFolder}/build/your_executable",
            "args": [],
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": false,
            "MIDebuggerServerAddress": "localhost:1234",
            "preLaunchTask": "build"
        }
    ]
}
```

### 配置示例

#### snippets 代码片段设置
[官方配置文档](https://code.visualstudio.com/docs/editor/userdefinedsnippets)
```
"python annotation template": {
    "prefix": "pyT",
    "body": [
        "#!/usr/bin/python",
        "# cython: language_level=3",
        "# -*- coding:utf-8 -*-",
        "# @filename : ${TM_FILENAME}",
        "# @package : $1",
        "# @Time : $CURRENT_YEAR/$CURRENT_MONTH/$CURRENT_DATE $CURRENT_HOUR:$CURRENT_MINUTE",
        "# @Author : qgq",
        "# @desc : $2"
    ],
    "description": "print python annotation template"
}
```

#### 配置运行python文件路径
在工作区配置选项中的setting里配置`"python.terminal.executeInFileDir": true`
说明：在终端中执行文件时，是否在文件的目录中使用 execute，而不是当前打开的文件夹（一般指工作区目录）

#### Microsoft python语言服务设置运行路径
在用户配置或工作区配置中添加`"python.terminal.executeInFileDir": true`，表示在打开文件的当前路径下
也可以直接在插件设置界面中更改

#### python语言服务重启
命令面板中使用`clear cache and reload window`重启窗口来重新启动Microsoft python语言服务

## vscode内置变量
1. `launch.json and tasks.json`文件中，使用`${variableName} `引用vscode内置变量
[vscode内置变量](https://code.visualstudio.com/docs/editor/variables-reference)

2. `settings.json`文件中内置变量引用,如以下示例在settings中可用

**注意** 以下示例只在具体对应项生效，或者在`cwd\env\shell\shellArgs` 中

> 基于打开的工作区或活动编辑器等当前上下文控制窗口标题。根据上下文替换变量:
- `"window.title": "${dirty}${activeEditorShort}${separator}${rootName}${separator}${appName}"`
```
"${activeEditorShort}": 文件名 (例如 myFile.txt)。
"${activeEditorMedium}": 相对于工作区文件夹的文件路径 (例如, myFolder/myFileFolder/myFile.txt)。
"${activeEditorLong}": 文件的完整路径 (例如 /Users/Development/myFolder/myFileFolder/myFile.txt)。
"${activeFolderShort}": 文件所在的文件夹名称 (例如, myFileFolder)。
"${activeFolderMedium}": 相对于工作区文件夹的、包含文件的文件夹的路径, (例如 myFolder/myFileFolder)。
"${activeFolderLong}": 文件所在文件夹的完整路径 (例如 /Users/Development/myFolder/myFileFolder)。
"${folderName}": 文件所在工作区文件夹的名称 (例如 myFolder)。
"${folderpath}": 文件所在工作区文件夹的路径 (例如 /Users/Development/myFolder)。
${rootName}: 具有可选远程名称和工作区指示器的工作区的名称(如果适用)(例如 myFolder、myRemoteFolder [SSH] 或 myWorkspace [工作区])。
${rootNameShort}: 已缩短的工作区名称，不包含后缀(例如 myFolder、myRemoteFolder 或 myWorkspace)。
"${rootPath}": 打开的工作区或文件夹的文件路径 (例如 /Users/Development/myWorkspace)。
"${profileName}": 在其中打开工作区的配置文件的名称(例如数据科学(配置文件))。如果使用默认配置文件，则忽略此选项。
"${appName}": 例如 VS Code。
${remoteName}: 例如 SSH
${dirty}: 表明活动编辑器具有未保存更改的时间的指示器。
${focusedView}: 当前聚焦的视图名称。
"${separator}": 一种条件分隔符 ("-"), 仅在被包含值或静态文本的变量包围时显示。
```

> `"terminal.integrated.tabs.title":`控制终端标题。变量根据上下文被替换:
- ' ${cwd} ':终端的当前工作目录
- ' ${cwdFolder} ':终端的当前工作目录，在多根工作空间中显示，或者在单个根工作空间中示与初始工作目录不同的值。
- ' ${workspaceFolder} ':启动终端的工作空间
- ' ${local} ':表示远程工作区中的本地终端
- ' ${process} ':终端进程名
- ' ${separator} ':一个条件分隔符(' - ')，仅在被带值或静态文本的变量包围时显示。
- ' ${sequence} ':进程提供给终端的名称
- ' ${task} ':表示该终端与一个任务相关联
  
> `"terminal.integrated.tabs.description"`控制显示在标题右侧的终端描述。变量根据上下文被替换:
- ' ${cwd} ':终端的当前工作目录
- ' ${cwdFolder} ':终端的当前工作目录，在多根工作空间中显示，或者在单个根工作空间中示与初始工作目录不同的值。在Windows上，只有在启用shell集成时才会显示。
- ' ${workspaceFolder} ':启动终端的工作空间
- ' ${local} ':表示远程工作区中的本地终端
- ' ${process} ':终端进程名
- ' ${separator} ':一个条件分隔符(' - ')，仅在被带值或静态文本的变量包围时显示。
- ' ${sequence} ':进程提供给终端的名称
- ' ${task} ':表示该终端与一个任务相关联

### 设置vscode终端环境变量
```
"terminal.integrated.env.windows": {
    "path": "C:\\opt\\ros\\melodic\\x64;${env:path}"
},  // 具有环境变量的对象，这些变量将添加到将由 Windows 上的终端使用的 VS Code 进程。即打开终端时，对环境变量进行更改。
"terminal.integrated.defaultProfile.windows": "Command Prompt",  // Windows 上的默认终端配置文件,即默认的打开终端。
"terminal.integrated.profiles.windows": {
    "Command Prompt": {
        "path": [
            "${env:windir}\\Sysnative\\cmd.exe",
            "${env:windir}\\System32\\cmd.exe",
        ],
        // 指向 shell 可执行文件的路径
        "args": [
            "&&C:\\opt\\ros\\melodic\\x64\\setup.bat"
        ],
        // vscode shell args中不能使用set等显示的命令,请在bat脚本中设置
        "icon": "terminal-cmd"
    },
}  // Windows 的终端配置文件自定义，即要打开的终端shell所在的路径

```
## remote-ssh扩展
**注意** 初次使用需要设置config文件位置(在非远程vscode窗口中,使用open ssh configuration file命令)，内容格式如下
```
Host <远程主机名称>
    HostName <远程主机IP>
    User <用户名>
    Port <ssh端口，默认22>
    IdentityFile <本机SSH私钥路径>
    ForwardAgent yes <VSCode 自己添加的，不用管>
```
**注意** 如果你想要部分扩展在本地工作,你可以在settings.json中设置`remote.extensionKind`
> 覆盖扩展的类型。"ui" 扩展在本地计算机上安装和运行，而 "workspace" 扩展则在远程计算机上运行。通过使用此设置重写扩展的默认类型，可指定是否应在本地或远程安装和启用该扩展。

### 配置本地hosts以适应不同的局部IP变化
window下hosts文件在`c:\windows\system32\drivers\etc`下

## vscode + x11 配置远程开发弹窗
1. 你需要下载xmind,安装好后你得到一个(xmind和xlaunch),启动xlaunch
[xmind官网下载](https://sourceforge.net/projects/xming)

2. 在C:\Program Files (x86)\Xming\X0.hosts(xmind的安装目录)下,更改X0.hosts文件,
localhost下添加远程服务器ip
```
localhost
192.168.80.129
```
3. 更改remote-ssh的配置文件,添加x11转发信任
```
Host stoneyshi
    HostName *.*.*.*
    ForwardX11 yes
    ForwardX11Trusted yes
    ForwardAgent yes
    User *****
    Port 16000  #ssh连接端口
```
4. 远程服务器安装remote x11插件,本地vscode安装remote x11(ssh)
5. 配置DISPLAY变量

**注意1** 需设置DISPLAY变量;不能设置为(0.0,会在debug中显示连接超时);可设置为`DISPLAY=localhost:10.0`
这时还要设置 IP 充许，如果不设 IP 充许，将会被 Xming 拒绝而打不开：首先打开 Xming 安装文件夹找到 X*.hosts 文件 (* 号为上面 Display Number 数字），如本例就是找到 X10.hosts 文件，打开并在 localhost 下面一行，添加 Linux 服务器的 IP 地址
![最终效果如图](image.png)

**注意2** 如果你遇到x11启动失败的错误,可以打开remote x11设置文件,开启log level 为debug;查看vscode output面板中remote x11和remote x11(ssh)的输出调试信息

**注意3** 如果你配置的ssh-key是加密的(需要密码解密),你需要使用agent或Pageant(在window上)
> 参:[vscode remote x11 page](https://marketplace.visualstudio.com/items?itemName=spadin.remote-x11&ssr=false#overview)
> [vscode agent文档](https://code.visualstudio.com/docs/remote/troubleshooting#_ssh-tips)
```
# Make sure you're running as an **Administrator powelsheel**
Set-Service ssh-agent -StartupType Automatic
Start-Service ssh-agent
Get-Service ssh-agent
```
在vscode设置文件中启用
"remoteX11.SSH.authenticationMethod": "agent"
使用`ssh-add -l`查看添加的ssh代理
使用命令`ssh-add  "C:\Users\YZSH_\.ssh\id_rsa"`添加需要代理的密钥文件



> [Pageant 下载page](https://winscp.net/download/pageant.exe);Pageant属于winscp的一部分,你可以安装winscp也可以只安装Pageant
**注意** Pageant不支持open-ssh-2.0 私钥

**注意4** 第一次运行xeyes显示成功后，后面显示失败，或一直显示失败，但是不报错
> 可能原因：Xming软件或服务器的IP被防火墙拦住了，将Xming软件、远程服务器的IP放入防火墙的白名单即可，除了防火墙之外，可能有其他安全软件会把Xming放在黑名单，查看下，解除禁止即可;然后重启窗口

### 在docker中配置vscode + x11
- 创建容器时,需要使用`--volume="$HOME/.Xauthority:/root/.Xauthority:rw"`挂载卷
> 在容器中执行`xauth list`
如果出现`xauth:  file /root/.Xauthority does not exist`,说明你需要重新挂载该卷
```
docker run -it -v $PWD/noetic_ros_data:/data --device=/dev/dri --group-add video --volume=/tmp/.X11-unix:/tmp/.X11-unix  --env="DISPLAY=$DISPLAY" --env="QT_X11_NO_MITSHM=1" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" -p=9022:22 --name=xming_ros_ssh_test noetic:2.0.1 /bin/bash
```
**注意** 安装`apt install x11-apps`使用xeyes测试x11转发是否成功

## sftp使用
使用sftp在本地编写远程文件并自动同步

## vscode使用profile

### 使用profile配置不同语言的开发环境，可在不同设备同步

设置配置profile文件由设置、键盘快捷键、扩展、状态、任务和代码段组成。应用profile文件的vscode等同于用户级的相应设置。

**注意** 在导入profile时，对本地未安装的扩展会自动下载安装。
**注意** 有些设置只能在应用程序级别自定义。（如 update.mode 、语言包扩展、设置同步启用和工作区信任状态等）

## vscode + wsl配置轻量的linux开发环境

### wsl安装
**注意** 你需要确保开启了window功能--适用于linux的win子系统，根据以下操作打开
> Win + R，输入 `appwiz.cpl`，左上角找到“启动或关闭 Windows 功能”，启用wsl和虚拟机平台和虚拟机监控功能。
1. [从官网手动下载安装包](https://learn.microsoft.com/zh-cn/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package),将`.AppxBundle`以及解压后的`.appx` 文件更改为 zip 文件并解压，获取ubuntu.exe文件进行安装。
2. 从Microsoft Store安装，你可以设置-->存储-->更改新内容保存位置中将安装app的位置改到D盘WindowsApps目录下

### wsl查看可安装的linux发行版
`wsl --list --online` 或 `wsl -l -o` 查看在线商店可用的 Linux 发行版列表。

**注意** 出现==无法解析服务器的名称或地址错误==时，查看 `raw.githubsercontent.com` 能否ping通；可以在hosts手动更改该地址解析ip或者直接使用`114.114.114.114` `8.8.8.8`这两个dns服务器（在控制面版/网络适配器/ip4设置中）。

### wsl查看安装linux版本
查安装的发行版的 WSL 版本：wsl -l -v

### wsl设置默认版本和启动linux

- 使用命令 `wsl --set-default-version <1|2>` 启用wsl1或wsl2

- `wsl -s <DistributionName>` 或 `wsl --set-default <DistributionName>`，将 DistributionName 为要使用的 Linux 发行版的名称。 

- 要在 PowerShell 或 Windows 命令提示符下运行特定的 WSL 发行版而不更改默认发行版，请使用命令 `wsl -d <DistributionName>`

### ubuntu首次启动报错
错误描述：`WslRegisterDistribution failed with error: 0x800701bc`
解决方案：
1. 下载安装[wsl更新msi程序](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)
2. 或者直接使用 `wsl --update`命令 从 Microsoft Store 下载并安装 WSL。

### wsl配置接口网络规则(解决无法访问公网)
1. 防火墙允许接口vEthernet (WSL)中流量通过 `New-NetFirewallRule -DisplayName "WSL" -Direction Inbound  -InterfaceAlias "vEthernet (WSL)"  -Action Allow`
   - 允许指定ip `New-NetFirewallRule -DisplayName "WSL" -Direction Inbound  -LocalAddress <ip> -Action Allow`
2. win+R，键入 wf.msc 打开高级安全控制台访问 Windows 防火墙。配置wsl规则

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

## vscode leetcode插件登录失效
1. 确保安装node
2. 选择leetcode-cn进入点
3. 新电脑先在网站登录leetcode，进行新设备登陆确认
4. 确保leetcode网站账户已退出，再登录vscode中leetcode插件

## vscode插件编写

[官方插件示例](https://github.com/microsoft/vscode-extension-samples)
[官方插件编写文档](https://code.visualstudio.com/api/get-started/your-first-extension#:~:text=Then,%20inside%20the%20editor,%20press%20F5.%20This%20will%20compile%20and%20run%20the%20extension%20in%20a%20new%20Extension%20Development%20Host%20window.)

**注意** 你需要全局安装vscode扩展开发构建工具
`npm install -g yo generator-code`

### 第一个示例hello world
1. 确保已有Node.js 和 Git环境
2. 确认**全局安装**yo和generator-code
3. 使用`yo code`初始化构建vscode扩展项目
4. 根据提示提供初始信息
5. 为了确保不会污染工作区，你需要在新窗口开发扩展

**注意** 如果你的node是在conda环境里，你需要将路径添加到env变量中
```
# settings.json
"terminal.integrated.env.windows": {
    "path": "${env:path}C:\\Users\\YZSH_\\anaconda3;"
},

如果在task中设置,终端在每次任务执行后关闭，环境变量被重置。
```

### LSP(Language Server Protocol) 语言服务协议

由微软提供，定义了在编辑器或IDE与语言服务器之间使用的协议，该语言服务器提供了例如自动补全，转到定义，查找所有引用等的功能；语言服务器索引格式的目标是支持在开发工具中进行丰富的代码导航或者一个无需本地源码副本的WebUI。

**lsp通过JSON-RPC语言协议与服务器进行通信**

#### GRPC与JSON-RPC
都属于RPC(Remote Procedure Call 远程过程调用)内部定义术语
1. RPC会隐藏底层的通讯细节。
2. RPC在使用形式上像调用本地函数一样去调用远程的函数。

> gRPC: Google开发的高性能、通用的开源RPC框架，主要面向移动应用开发并基于HTTP2协议标准而设计，基于ProtoBuf(Protocol Buffers)序列化协议开发，且支持众多开发语言。
> JSON-RPC: JSON-RPC是一个无状态且轻量级的远程过程调用(RPC)协议,即通过json格式实现通信。
