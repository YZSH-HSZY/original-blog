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

## MSVC构建工具

MSVC提供两种大型项目的配置和生成工具

- NMAKE 和生成文件(makefile-like)
- MSBuild 和项目文件(xml description file)

> nmake 和 msbuild都是两种命令行自动编译系统, vs 2005已经采用了msbuild系统
