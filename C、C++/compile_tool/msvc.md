# MSVC

MSVC(Microsoft Visual C++)是微软为 Windows 平台开发的编译器，专门用于编译 C 和 C++ 代码。它是 Visual Studio 的默认编译器，广泛用于 Windows 应用程序的开发

> MSVC 编译器工具链主要由两个核心组件构成: `cl.exe` 和 `link.exe`
- `cl.exe`: 用于控制 Microsoft C/C++ 编译器和链接器的命令行工具
- `link.exe`: 将通用对象文件格式 (COFF) 对象文件和库链接起来，以创建可执行 (.exe) 文件或动态链接库 (DLL)

> 参考文档
- [MSVC官方文档](https://learn.microsoft.com/zh-cn/cpp/build/building-on-the-command-line)

## MSVC安装

- [在 Visual Studio 中安装 C++ 支持](https://learn.microsoft.com/zh-cn/cpp/build/vscpp-step-0-installation?view=msvc-170)
- [Visual Studio 生成工具-只安装命令行工具集](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2022)
- [vs2022](https://aka.ms/vs/17/release/vs_buildtools.exe)
- [vs2019](https://aka.ms/vs/16/release/vs_community.exe)
- [vs2017](https://aka.ms/vs/15/release/vs_community.exe)

## MSVC版本

- `ToolsVersion` 构建系统, 如 MSBuild 引擎版本
- `Visual Studio` IDE 版本号
- `WindowsTargetPlatformVersion` Windows SDK版本, 如`10.0.22621.0`
- `PlatformToolset` VC++ 编译器/链接器版本, 如`v143`

> 简易的对应关系如下:
- `VS2012`: ToolsVersion(`4.0`)/Visual Studio IDE(`11.0`)/PlatformToolset(`v110`)
- `VS2013`: ToolsVersion(`12.0`)/Visual Studio IDE(`12.0`)/PlatformToolset(`v120`)
- `VS2015`: ToolsVersion(`14.0`)/Visual Studio IDE(`14.0`)/PlatformToolset(`v140`)
- `VS2017`: ToolsVersion(`15.0`)/Visual Studio IDE(`15.0`)/PlatformToolset(`v141`)
- `VS2019`: ToolsVersion(`16.0`)/Visual Studio IDE(`16.0`)/PlatformToolset(`v142`)
- `VS2022`: ToolsVersion(`17.0`)/Visual Studio IDE(`17.0`)/PlatformToolset(`v143`)

### 离线安装vs

> 参考文档
- [ms-离线安装vs](https://learn.microsoft.com/zh-cn/visualstudio/install/create-an-offline-installation-of-visual-studio?view=vs-2022)
- [ms-vs2019组件目录](https://learn.microsoft.com/zh-cn/visualstudio/install/workload-component-id-vs-community?view=vs-2019)
- [Visual Studio 的局域网络安装](https://learn.microsoft.com/zh-cn/visualstudio/install/create-a-network-installation-of-visual-studio?view=vs-2022#configure-the-contents-of-a-layout)

#### 一个轻量的仅包含帮助界面及最少C++桌面依赖的vs2019环境如下

```sh
vs_community_2019.exe --layout .\vs2019_layout 
--add Microsoft.Component.HelpViewer    
--add Microsoft.VisualStudio.Workload.NativeDesktop --includeRecommended
--lang en-US zh-CN
```
> 在vs2019_layout目录(仅2.29GB)下, 生成一个`vs_setup.exe`, 双击即可安装, `--includeRecommended`安装所有推荐部分(必须)

## 术语

- 源字符集(Source Character Set): 编译器解析源代码文件时使用的字符编码
- 执行字符集(Execution Character Set): 编译器将字符串和字符字面量（如"Hello"或'A'）转换为最终可执行文件时使用的编码, 影响程序运行时这些字面量的内存表示形式
- 生成文件: MSVC提供的类似Makefile的描述文件, 供nmake编译
- 项目文件: MSVC使用的msbuild处理的项目描述文件(xml格式)
- MSVCRT.LIB: Microsoft Visual C Runtime Library(动态链接版)
- LIBCMT.LIB: LIBC Multithreaded (Static)(静态多线程 C 运行时库)

## MSVC构建工具

MSVC提供两种大型项目的配置和生成工具

- NMAKE 和生成文件(makefile-like)
- MSBuild 和项目文件(xml description file)

> nmake 和 msbuild都是两种命令行自动编译系统, vs 2005已经采用了msbuild系统

## 编译系列工具

### cl

#### OPTIONS

```bash
优化选项:
    /O1 最大优化(优选空间)
    /O2 最大优化(优选速度)
    /Od 禁用优化(默认)
    /Ob<n> 内联扩展(默认 n=0) 
生成选项:
    /GR[-] 启用 C++ RTTI(Run-Time Type Identification, 运行时类型定义)
    /Qpar[-] 启用并行代码生成
    /utf-8
    /Zi 启用调试信息
输出选项:
    /Fo<file> 命名对象文件
    /Fi[file] 命名预处理的文件
    /Fe<file> 命名可执行文件
    /Fd[file] 命名 .PDB 文件
预处理器选项:
    /P 预处理到文件 
    /PD 打印所有宏定义
    /PH 在预处理时生成 #pragma file_hash
    /U<name> 移除预定义的宏
    /u 移除所有预定义的宏
    /D<name>{=|#}<text> 定义宏
    /I<dir> 添加到include搜索路径
语言选项:
    /std:<c++14|c++17|c++20|c++latest> C++ 标准版
    /std:<c11|c17|clatest> C 标准版本
    /permissive[-] 启用或禁用严格一致性模式, /permissive表宽松模式

    /Zc:arg1[,arg2]      C++ 语言合规性，支持参数:
        forScope[-]           对范围规则强制使用标准 C++
        wchar_t[-]            wchar_t 是本机类型，不是 typedef
        auto[-]               对 auto 强制使用新的标准 C++ 含义
        trigraphs[-]          启用三元祖(默认关闭)
        rvalueCast[-]         强制实施标准 C++ 显式类型转换规则
        strictStrings[-]      禁用从字符串文本到 [char|wchar_t]*的转换(默认关闭)
        implicitNoexcept[-]   在必需的函数上启用隐式 noexcept
        threadSafeInit[-]     启用线程安全的本地静态初始化
        inline[-]             如果是 COMDAT，则删除未引用的函数或数据或仅使用内部链接(默认关闭)
        sizedDealloc[-]       启用 C++14 全局大小解除分配函数(默认开启)
        throwingNew[-]        假设运算符 new 在故障时引发(默认关闭)
        referenceBinding[-]   临时引用不会绑定到非常数lvalue 引用(默认关闭)
        twoPhase-             禁用两阶段名称查找
        ternary[-]            对条件运算符强制使用 C++11 规则(默认关闭)
        noexceptTypes[-]      强制执行 C++17 noexcept 规则(在 C++17 或更高版本中默认开启)
        alignedNew[-]         对动态分配的对象启用 C++17 对齐方式(默认开启)
        hiddenFriend[-]       强制实施标准 C++ 隐藏好友规则(/permissive- 所隐含)
        externC[-]            强制实施外部 "C" 函数的标准 C++ 规则(/permissive- 所隐含)
        lambda[-]             使用更新的 lambda 处理器提供更好的 lambda 支持(默认为关闭)
        tlsGuards[-]          生成 TLS 变量初始化的运行时检查(默认情况下启用)
        zeroSizeArrayNew[-]   针对大小为零的对象数组的调用对象 new/delete (默认启用)
其他杂项:
    /c 只编译，不链接
    /MP[n] 最多使用n个进程进行编译
    /source-charset:<iana-name>|.nnnn 源字符集
    /execution-charset:<iana-name>|.nnnn 执行字符集
    /utf-8 源和执行字符集均为 UTF-8
    /TP 所有文件均使用cpp编译
    /Tp<source file> 将文件编译为 .cpp
    /TC 所有文件均使用c编译
    /Tc<source file> 将文件编译为 .c
链接选项:
    /LD 创建 .DLL
    /LDd 创建 .DLL 调试库
    /link [链接器选项和库]
    /MD 与 MSVCRT.LIB 链接(动态链接运行时库)
    /MDd 与 MSVCRTD.LIB 调试库链接
    /MT 与 LIBCMT.LIB 链接(静态链接运行时库)
    /MTd 与 LIBCMTD.LIB 调试库链接
    /LIBPATH<:search_path> 添加库文件的搜索路径
诊断选项:
    /Wall 启用所有警告
    /w 禁用所有警告
    /W<n> 设置警告等级(默认 n=1)

```

## nmake

微软推出的类make的Makefile系列构建工具, 使用如下:
```sh
用法:     NMAKE @commandfile
        NMAKE [选项] [/f makefile] [/x stderrfile] [macrodefs] [targets]
/A 生成所有已计算的目标
/B 如果时间戳相等则生成
/C 取消输出消息
/D 显示生成消息
/E 覆盖 env-var 宏
/G 显示 !include 文件名
/HELP 显示简短的用法消息
/I 忽略命令中的退出代码
/K 遇到错误时继续生成不相关的目标
/N 显示命令但不执行
/NOLOGO 取消显示版权信息
/P 显示 NMAKE 信息
/Q 检查时间戳但不生成
/R 忽略预定义的规则/宏
/S 取消显示已执行的命令
/T 更改时间戳但不生成
/U 转储内联文件
/Y 禁用批处理模式
/? 显示简短用法消息
```

### nmake多线程编译

```sh
set CL=/MP4
nmake
```

## EXAMPLE

### cli使用cl编译链接库的示例

`cl /Zi /utf-8 /I ..\install\include\cjson tt.c /link /LIBPATH:..\install\lib cjson.lib`

### 工程升级

`devenv /Upgrade <sln_file>`

> 使用指定版本的devenv升级sln项目
`"C:\Program Files\Microsoft Visual Studio\2022\Professional\Common7\IDE\devenv.exe" /Upgrade "project.sln"`

### 命令行生成lib

静态库是目标文件(.obj)的集合, msvc中lib的生成分为两步:
- coff文件生成: `cl /c example.cpp`
- coff打包为lib `lib /OUT:example.lib example.obj libdep1.lib`

## BUG

### /MT和/MD混用造成的内存管理冲突

不同模块(DLL/EXE)使用不同版本的运行时库(如静态链接 /MT 和动态链接 /MD 混用)时，它们各自维护独立的内存堆(Heap)，导致在一个模块中分配的内存无法在另一个模块中正确释放

### /MT不同模块管理同一内存的冲突

> 静态链接（/MT）的内存管理机制
> - 每个模块拥有独立的堆管理器
> - 堆隔离性: 不同模块的堆管理器 不共享堆状态

常见解决方案:
- 优化模块结构, 遵循谁分配;谁释放
- 使用/MD动态库共享内存
- 使用全局堆(Windows API), 绕过 CRT 堆
```c
// 分配
void* p = HeapAlloc(GetProcessHeap(), 0, 100);
// 释放（可在任何模块中调用）
HeapFree(GetProcessHeap(), 0, p);
```
- 自定义内存管理器, 在模块间传递内存分配器接口, 确保所有操作使用同一套逻辑：