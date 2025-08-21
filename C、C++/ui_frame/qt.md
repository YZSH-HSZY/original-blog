# qt

## install

> ubuntu:
> - `qtbase5-dev`

> Window source compile:
> depends:
```
Windows:
   --------
     Open a command prompt.
     Ensure that the following tools can be found in the path:
     * Supported compiler (Visual Studio 2012 or later,
        MinGW-builds gcc 4.9 or later)
     * Perl version 5.12 or later   [http://www.activestate.com/activeperl/]
     * Python version 2.7 or later  [http://www.activestate.com/activepython/]
     * Ruby version 1.9.3 or later  [http://rubyinstaller.org/]
```
> - `..\qt-everywhere-src-5.15.10\configure.bat -verbose -opensource -debug-and-release -shared -confirm-license -platform win32-msvc -make libs -opengl desktop -prefix D:\qt-5.15.10-windows-x86-msvc`

> qt-online-installer for window
- `qt-online-installer-windows-x64-online.exe --mirror https://mirrors.ustc.edu.cn/qtproject`

**资源**
- [阿里云qt在线安装镜像站](https://mirrors.aliyun.com/qt/archive/online_installers/4.10/)

## tool

### uic(Qt User Interface Compiler)

用于将ui文件生成.h文件

### rcc(Qt Resource Compiler)

构建过程中将资源嵌入到Qt应用程序中

### moc(Qt Meta Object Compiler)

将存在`宏Q_OBJECT`的 `.h` 文件转为 `.cpp` 文件

### qt creator

跨平台的qt项目编辑器

> 常用快捷键:
> - `F2`: 跳转到函数定义
> - `Shift+F2`: 在函数声明和定义间转换
> - `F4`: 在源文件和头文件间跳转
> - `Ctrl + K`: 文件名快速跳转
> - `Ctrl + L`: 跳转到行
> - `Ctrl + [`: 跳转到代码块起始
> - `Ctrl + ]`: 跳转到代码块末尾

## package and deploy

> 相关工具: 
1. `windeployqt`: Qt 部署工具, 用于收集qt程序的依赖项
- `windeployqt --release --no-compiler-runtime --dir ./deploy MyApp.exe`

2.  `Inno Setup`: 用于 Windows 应用的开源安装程序制作工具
- 安装 `Inno Setup`
- 创建一个`.iss`文件, 类似于Pascal的脚本语言, 如:
```yaml
[Setup]
AppName=QGC Ground Station
AppVersion=1.0
DefaultDirName={pf}\QGC Ground Station
OutputDir=userdocs:Inno Setup Examples Output
[Files]
Source: "*"; DestDir: "{app}"
[Icons]
Name: "{group}\QGC Ground Station"; Filename: "{app}\your_program.exe"
```
- `iscc.exe your_script.iss`: 生成安装程序


## plugins

### 显示platforms

qt提供插件支持的数据显示, 如 `linuxfb/offscreen/minimal/vnc` 等

- `linuxfb`: 用于 Linux 的帧缓冲设备, 直接将Qt 应用程序直接渲染到帧缓冲区, 对于嵌入式系统或没有窗口系统的环境很有用
- `minimal`: 非常基础的 Qt 平台接口实现, 通常用于测试
- `offscreen`: 离屏插件允许渲染到离屏缓冲区, 适用于不立即在屏幕上显示渲染结果的程序, 例如图像处理或渲染到纹理
- `vnc`: 通过 VNC 协议实现远程访问 Qt 应用程序, 允许用户远程与应用程序交互

## run

### example

#### 开发板的fb显示的qt程序使用x11转发

- 本地机器开启x-server
- 开发板机器设置显示屏 `export DISPLAY=192.168.8.50:10`
- 开发板机器设置qt程序显示后端 `export QT_QPA_PLATFORM=xcb`


#### `QTimer::singleShot(0, Callfunc)`

将操作放到下次事件循环中

