### wsa安装

**注意** 你需要确保开启了`window功能--适用于linux的win子系统`，根据以下操作:
- 打开Win + R，输入 `appwiz.cpl`，
- 左上角找到“启动或关闭 Windows 功能”，启用hyper-v和虚拟机平台和虚拟机监控功能。

**安装方式**
1. 你可以在微软商店安装，直接搜索`Windows Subsystem for Android™ with Amazon Appstore`即可，会自动安装亚马逊应用商店（亚马逊应用商店和wsa捆绑在一起，卸载它也会同步卸载wsa）
2. 借助github上项目MagiskOnWSALocal构建WSA安装包,项目地址：https://github.com/LSPosed/MagiskOnWSALocal ，需要用到Ubuntu虚拟机。（总大小：大概3G）
> - Build arch（硬件架构）：默认选 x64，绝大多数电脑都是x64的架构，极少数使用Arm架构的电脑（比如使用高通骁龙芯片的）选arm64
> - WSA release type（WSA版本）：默认选择稳定版 retail，如果想使用预览版/Beta频道/Dev频道则选择其他选项
> - Magisk version（Magisk的版本）：默认选择 stable，其余和上一条同理(magisk是用户态root方案，与kernelsu内核态root方案对应，选其一即可)
> - Install Gapps（是否安装谷歌框架）：需要选 是，不需要选 否
> - Which GApps：选择OpenGApps
> - Remove Amazon Appstore（是否需要亚马逊应用商店）：不需要选 否
> - Root solution（是否root）：需要root权限选 magisk
> - Compress output（是否压缩output）：如果选 是，安装文件将会打包为一个.7z压缩包，如果选 否，安装文件就是一个文件夹
> 最后：打开文件夹/解压后的文件夹，找到Install.ps1，右键选择 使用Power Shell运行（如果失败则可能需要使用管理员模式的Power Shell运行），然后耐心等待安装

**ps1文件运行错误错误**：错误消息：禁止在此系统上运行脚本
> 通过管理员权限（win+x,选择终端管理员）运行power shell，然后输入命令
`set-ExecutionPolicy RemoteSigned` 输入yes。安装结束恢复默认策略使用`set-ExecutionPolicy Default`命令


### wsa 开发者模式
打开应用`适用于window的android子系统`,在高级设置里打开开发者选项;默认的adbd端口为`58526`

#### wsa的安卓设置应用
在任意浏览器中输入 `wsa://com.android.settings`

### android目录介绍

/system/app/    这里存放一些系统的app
/system/bin/    这里存放的主要是Linux的一些自带的组件
/system/build.prop     这里记录了系统的属性信息
/system/fonts/     这里存放系统的字体文件。手机root后，可以下载TTF文件去替换系统的字体文件，就可以修改字体了
/system/framework/    这里存放的是系统的核心文件、框架层
/system/lib/    这里存放的几乎是所有的共享库(.so)文件
/system/media/    这里用来保存系统铃声、系统提示音
 /system/usr/   这里用来保存用户的配置文件。例如：键盘布局、共享、时区文件等

### adb shell read-only file system

按照以下步骤解决:
1. 确认具有写权限
2. 使用`mount | grep <path>`查看目录挂载方式是否为ro(read only);或者在`/proc/self/mounts`文件中查看目录挂载方式
3. 通过`mount -o remount -o rw /system/bin`更改为读写挂载