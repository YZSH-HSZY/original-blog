# qt

> 参考文档:
- [qt6官方文档](https://doc.qt.io/qt-6/zh/qtcore-index.html)
- [qt5.15源码编译教程](https://doc.qt.io/archives/qt-5.15/windows-requirements.html#building-from-source)

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

> 链接openssl和qt
- 下载openssl源码, 根据文档安装依赖perl/nasm
- 编译openssl`perl Configure {VC-WIN32,VC-WIN64A} --prefix=C:\opt\openssl`
- 查看版本及架构 `openssl version -a`
- 选择编译qt-everywhere, 注意此架构因和openssl/msvc保持一致
```sh
set OPENSSL_DIR=C:\opt\openssl
.\configure -opensource -platform win32-msvc -developer-build -mp -release -v \
-confirm-license -nomake examples -nomake tests -nomake tools -no-iconv -no-dbus -no-plugin-manifests -no-opengl \
OPENSSL_PREFIX=%OPENSSL_DIR% -openssl-linked -I  %OPENSSL_DIR%\include -L %OPENSSL_DIR%\lib OPENSSL_LIBS="libssl.lib libcrypto.lib Ws2_32.lib Gdi32.lib Advapi32.lib Crypt32.lib User32.lib" -skip qt3d -skip qtactiveqt \
-skip qtandroidextras -skip qtconnectivity -skip qtdatavis3d -skip qtdeclarative \
-skip qtdoc -skip qtgamepad -skip qtgraphicaleffects -skip qtimageformats -skip qtlottie \
-skip qtmacextras -skip qtmultimedia -skip qtnetworkauth -skip qtpurchasing \
-skip qtquick3d -skip qtquickcontrols -skip qtquickcontrols2 -skip qtquicktimeline \
-skip qtremoteobjects -skip qtscript -skip qtscxml -skip qtsensors -skip qtserialbus \
-skip qtserialport -skip qtspeech -skip qttools -skip qtvirtualkeyboard -skip qtwayland \
-skip qtwebchannel -skip qtwebengine -skip qtwebglplugin -skip qtwebsockets \
-skip qtwebview -skip qtwinextras -skip qtx11extras -skip qtxmlpatterns \
-no-feature-appstore-compliant -no-feature-bearermanagement -no-feature-commandlineparser \ -no-feature-ftp -no-feature-future -no-feature-geoservices_esri -no-feature-gestures \
-no-feature-gssapi -no-feature-jalalicalendar -no-feature-sqlmodel -no-feature-sspi \
-no-feature-udpsocket
```

**编译注意事项**
- 如果不带`-openssl-linked`选项, 那么qtnetwork库缺少ssl相关符号
- `-debug-and-release` 同时生成调试和发布两种库

**资源**
- [阿里云qt在线安装镜像站](https://mirrors.aliyun.com/qt/archive/online_installers/4.10/)

### 编译选项

- `-opensource` 构建Qt的开源版本
- `-platform <target>` Select host mkspec [detected]
- `-xplatform <target>` Select target mkspec when cross-compiling [PLATFORM]
- `-mp` 使用多个处理器进行编译(仅限MSVC)
- `-developer-build` 编译和链接Qt来开发Qt本身
- `-debug-and-release` 构建两个版本的Qt(包含调试和不包含, 仅适用Apple/Windows)
- `-make <part>` 将`<part>`添加到要构建的部件列表中, 指定此选项将首先清除默认列表
- `-opengl <api>` 启用OpenGL支持。支持api: `s2(Windows默认)`/`desktop(Unix默认)`/`dynamic(仅限Windows)`
- `-openssl-linked` 使用OpenSSL并链接到libssl
- `-D <string>` Pass additional preprocessor define
- `-I <string>` Pass additional include path
- `-L <string>` Pass additional library path
- `-F <string>` Pass additional framework path (Apple only)
- `-prefix <dir>` 安装目录

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

#### QMap使用自定义key实现多键排序

```cpp
struct TableModelMapKey {
    int src;
    int dst;
    int pgn_no;
    bool operator<(const TableModelMapKey& o) const {
        if (src != o.src) return src < o.src;
        else if (dst != o.dst) return dst < o.dst;
        else if (pgn_no != o.pgn_no) return pgn_no < o.pgn_no;
        return false;
    }
};
QMap<TableModelMapKey, int> pl;
```
**注意** qmap自定义可以仅重载`<`运算符, 通过`a<b`,`b<a`判断`==`关系

#### 自定义model

- [TreeModel](./qt_example/qt_treemodel.md)

#### `QTimer::singleShot(0, Callfunc)`

将操作放到下次事件循环中

