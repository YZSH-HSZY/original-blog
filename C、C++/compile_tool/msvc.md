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

### 离线安装vs

> 参考文档
- [ms-离线安装vs](https://learn.microsoft.com/zh-cn/visualstudio/install/create-an-offline-installation-of-visual-studio?view=vs-2022)
```sh
vs_community_2019.exe --layout .\vs2019_layout 
--add Microsoft.VisualStudio.Component.VC.ATLMFC 
--add Microsoft.VisualStudio.Workload.VCTools --includeRecommended 
--add Microsoft.Component.HelpViewer    
--lang en-US zh-CN
```

> 在vs2019_layout目录下, 生成一个`vs_setup.exe`, 双击即可安装

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
    /Fe<file> 命名可执行文件
    /Fd[file] 命名 .PDB 文件
预处理器选项:
    /PD 打印所有宏定义
    /PH 在预处理时生成 #pragma file_hash
    /U<name> 移除预定义的宏
    /u 移除所有预定义的宏
    /D<name>{=|#}<text> 定义宏
    /I<dir> 添加到include搜索路径
语言选项:
    /std:<c++14|c++17|c++20|c++latest> C++ 标准版
    /std:<c11|c17|clatest> C 标准版本
其他杂项:
    /c 只编译，不链接
    /MP[n] 最多使用n个进程进行编译
    /source-charset:<iana-name>|.nnnn 源字符集
    /execution-charset:<iana-name>|.nnnn 执行字符集
    /utf-8 源和执行字符集均为 UTF-8
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

## EXAMPLE

### cli使用cl编译链接库的示例

`cl /Zi /utf-8 /I ..\install\include\cjson tt.c /link /LIBPATH:..\install\lib cjson.lib`

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