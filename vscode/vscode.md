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

### 快捷键 `keybindings.json` 配置
在用户的配置文件profiles中(`%APPDATA%Code/User/keybindings.json`)，设置自定义快捷键

如以下将运行label为`debug ui widget`的任务:
```json
{
    "key": "alt+a alt+s",
    "command": "workbench.action.tasks.runTask",
    "args": "debug ui widget"
}
```

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
        // vscode shell args中不能使用set等显示的命令,请在bat脚本中设置, cmd使用/k选项，保留执行脚本更改
        "icon": "terminal-cmd"
    },
}  // Windows 的终端配置文件自定义，即要打开的终端shell所在的路径

```
## remote-ssh扩展

**注意** 初次使用需要设置config文件位置(在非远程vscode窗口中,使用open ssh configuration file命令)，内容格式如下
```sh
Host <远程主机名称>
    HostName <远程主机IP>
    User <用户名>
    Port <ssh端口，默认22>
    IdentityFile <本机SSH私钥路径>
    ForwardAgent yes <VSCode 自己添加的，不用管>
    # 始终转发3000和27017端口
    LocalForward 127.0.0.1:3000 127.0.0.1:3000
    LocalForward 127.0.0.1:27017 127.0.0.1:27017
```
**注意** 如果你想要部分扩展在本地工作,你可以在settings.json中设置`remote.extensionKind`
> 覆盖扩展的类型。"ui" 扩展在本地计算机上安装和运行，而 "workspace" 扩展则在远程计算机上运行。通过使用此设置重写扩展的默认类型，可指定是否应在本地或远程安装和启用该扩展。

**注意** 启用`remote.SSH.allowLocalServerDownload`，扩展将回退到本地下载 VS Code Server，并在建立连接后远程传输。

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
这时还要设置 IP 充许，如果不设 IP 充许，将会被 Xming 拒绝而打不开：首先打开 Xming 安装文件夹找到 X*.hosts 文件 (* 号为上面 Display Number 数字)，如本例就是找到 X10.hosts 文件，打开并在 localhost 下面一行，添加 Linux 服务器的 IP 地址
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

## remote-ssh 和 Tunnels 的区别

1. `Remote-SSH` + `code-server`
- 传统方式, 基于标准 SSH 协议
- 需要在远程机器安装 VS Code Server
- 直接连接，无第三方中继
- 网络可达性和 SSH 配置

2. `VS Code Tunnels`
- 现代方式, 无需 SSH 配置或端口转发
- 使用微软的云服务进行中继
- GitHub 账户认证
- 自动 TLS/SSL 加密

|特性	        |VS Code Tunnels	    |Remote-SSH + code-server          |
|--------------|------------------------|----------------------------------|
|网络要求	     |只需出站 HTTPS	     |需要 SSH 端口可达                   |
|配置复杂度	     |简单	                 |复杂                               |
|安全性	        |TLS + GitHub 认证	     |SSH 密钥 + 网络隔离                |
|性能	        |经过中继，可能稍慢	      |直接连接，更快                      |
|跨网络	        |支持（如 NAT后）	      |需要 VPN/端口转发                  |
|安装要求	     |VS Code CLI	         |SSH Server + VS Code Server       |

## sftp使用
使用sftp在本地编写远程文件并自动同步

## vscode使用profile

### 使用profile配置不同语言的开发环境，可在不同设备同步

设置配置profile文件由设置、键盘快捷键、扩展、状态、任务和代码段组成。应用profile文件的vscode等同于用户级的相应设置。

**注意** 在导入profile时，对本地未安装的扩展会自动下载安装。
**注意** 有些设置只能在应用程序级别自定义。（如 update.mode 、语言包扩展、设置同步启用和工作区信任状态等）

## vscode + wsl配置轻量的linux开发环境

[参wsl安装笔记](../linux/wsl.md)

## vscode leetcode插件登录失效
1. 确保安装node
2. 选择leetcode-cn进入点
3. 新电脑先在网站登录leetcode，进行新设备登陆确认
4. 确保leetcode网站账户已退出，再登录vscode中leetcode插件

## 时间线

vscode的时间线位于资源管理器的一个标签, 用于查看一个文件的历史更改(包括git仓库中更改及本地文件变更)


## vscode插件

[vscode插件商城](https://marketplace.visualstudio.com/VSCode)

> 插件编写参考文档:
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


## bug

### vscode 通过 remote-ssh 连接 window 相关错误

> 描述: 连接失败, 使用 `git-sshd` 时 `powershell` 获取父进程为 `bash` 非 `sshd`, 导致错误
> 解决方案: 使用 `Window OpenSSL Server`, 安装如下
```powershell
# 检查具有 Administrator 组权限
(New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

# 检查 OpenSSL 客户端/服务端是否安装
Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

# Install the OpenSSH Client
Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

# Install the OpenSSH Server
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0

# Start the sshd service
Start-Service sshd

# OPTIONAL but recommended:
Set-Service -Name sshd -StartupType 'Automatic'

# Confirm the Firewall rule is configured. It should be created automatically by setup. Run the following to verify
if (!(Get-NetFirewallRule -Name "OpenSSH-Server-In-TCP" -ErrorAction SilentlyContinue)) {
    Write-Output "Firewall Rule 'OpenSSH-Server-In-TCP' does not exist, creating it..."
    New-NetFirewallRule -Name 'OpenSSH-Server-In-TCP' -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
} else {
    Write-Output "Firewall rule 'OpenSSH-Server-In-TCP' has been created and exists."
}
```

[适用于 Windows 的 OpenSSH 安装文档](https://learn.microsoft.com/zh-cn/windows-server/administration/openssh/openssh_install_firstuse?source=recommendations&tabs=powershell&pivots=windows-10)