# vscode-cpp
此笔记介绍如何在vscode中配置c/c++开发环境, 包括build/debug/intelligent等

> 参考文档:
- [c-cpp-properties文件参考](https://code.visualstudio.com/docs/cpp/c-cpp-properties-schema-reference)

## intelligent

因为C/C++特有的宏机制, 在vscode中查看项目代码会有部分宏选项代码变暗, 无法搜索. 可以全局配置` C_Cpp.default.*` 也可在 `.vscode` 文件夹下配置`c_cpp_properties.json`文件夹

## debug
安装ms-vscode.cpptools

**注意** 在ubuntu16.04中, 需要vscode 1.98.2以下;及cpptools 1.24.1以下

[cpptools vsix下载](https://github.com/microsoft/vscode-cpptools/releases)

### example

#### 调试另一平台编译程序

在 `launch.json` 中添加 `sourceFileMap`配置, 用于传递给调试引擎的源文件映射, 示例如:
```json
{
  "name": "BATTLE-QtCommunicate_launch_gdb",
  "type": "cppdbg",
  "request": "launch",
  "program": "/home/smartwork/work/OneNet/reference/OneNetCommunicate/OneNetCommunicate/Qt/QtCommunicate/QtCommunicate",
  "args": [],
  "sourceFileMap": {
      "/OneNet": "/home/smartwork/work/OneNet"
  }
}
```

#### 使用gdb原生命令

vscode的调试控制台中可以通过 `-exec` 前缀执行gdb调试命令, 如
- `-exec catch syscall write` 捕获系统调用write, 发生时暂停

## c_cpp_properties.json示例

```json
{
  "env": {
    "myIncludePath": ["${workspaceFolder}/include", "${workspaceFolder}/src"],
    "myDefines": ["DEBUG", "MY_FEATURE=1"]
  },
  "configurations": [
    {
      "name": "Linux",    //配置标识符. 选择 Mac/Linux/Win32 时将在对应平台上自动配置, 但标识符可以为任何内容, 在vscode状态栏中可选择激活的配置
      "compilerPath": "/usr/bin/gcc",  //生成项目的编译器的完整路径, 将查询编译器以确定用于 IntelliSense 的系统包含路径和默认定义; 为空字符串时将跳过查询, 省略 compilerPath 属性不会跳过查询
      "compilerArgs": ["-m32"],  // 用于修改使用的 include 或 define 的编译器参数, 空格分隔参数应在数组中作为单独的参数输入
      "intelliSenseMode": "linux-gcc-x86", //要使用的 IntelliSense 模式映射到 MSVC/gcc/Clang 等特定于体系结构的变体, 未设置将为该平台选择默认值;如(Windows:windows-msvc-x64;Linux: linux-gcc-x64;macOS: macos-clang-x64)
      "includePath": ["${myIncludePath}", "/usr/include"], //指定 ** 以指示递归搜索,如果compilerPath 设置中指定了编译器, 则无需在此列表中列出系统包含路径
      "defines": ["${myDefines}"], //分析文件时供 IntelliSense 引擎使用的预处理器定义列表
      "cStandard": "gnu11", //用于 IntelliSense 的 C 语言标准版本
      "cppStandard": "gnu++14", // 用于 IntelliSense 的 C++ 语言标准版本
      "configurationProvider": "ms-vscode.cmake-tools", //可以为源文件提供 IntelliSense 配置信息的 VS Code 扩展的 ID, 如果指定将优先于 c_cpp_properties.json 中的其他设置
      //configurationProvider 候选扩展必须实现 vscode-cpptools-api
      "forcedInclude": ["${workspaceFolder}/common.h"], //在处理任何源文件之前应包含的文件列表
      "compileCommands": "${workspaceFolder}/build/compile_commands.json", //工作区的 compile_commands.json 文件的完整路径, 如果存在将使用该文件配置 IntelliSense
      "dotConfig": "${workspaceFolder}/.config", //由 Kconfig 系统创建的 .config 文件的路径
      "mergeConfigurations": true, // 设置为 true 可将include,defines,forced includes与配置提供程序的路径合并
      "customConfigurationVariables": {
        "myVar": "myvalue"
      }, //可通过命令 ${cpptools:activeConfigCustomVariable} 查询的自定义变量, 一版用于 launch.json 或 tasks.json 中的输入变量
      "browse": {
        "path": ["${myIncludePath}", "/usr/include", "${workspaceFolder}"],
        "limitSymbolsToIncludedHeaders": true,
        "databaseFilename": "${workspaceFolder}/.vscode/browse.vc.db"
      }  //供 转到定义/声明 功能使用
    },
    {
      "name": "Mac",
      "compilerPath": "/usr/bin/clang",
      "intelliSenseMode": "macos-clang-x64",
      "includePath": ["${myIncludePath}"],
      "defines": ["${myDefines}"],
      "cStandard": "c11",
      "cppStandard": "c++17",
      "macFrameworkPath": ["/System/Library/Frameworks", "/Library/Frameworks"],
      "browse": {
        "path": ["${myIncludePath}", "${workspaceFolder}"]
      }
    },
    {
      "name": "Win32",
      "compilerPath": "C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.28.29333/bin/Hostx64/x64/cl.exe",
      "intelliSenseMode": "windows-msvc-x64",
      "includePath": ["${myIncludePath}"],
      "defines": ["${myDefines}", "_WINDOWS"],
      "cStandard": "c17",
      "cppStandard": "c++20",
      "windowsSdkVersion": "10.0.19041.0",
      "browse": {
        "path": ["${myIncludePath}", "${workspaceFolder}"]
      }
    }
  ],
  "version": 4,
  "enableConfigurationSquiggles": true
}

```