# vscode-cpp
此笔记介绍如何在vscode中配置c/c++开发环境, 包括build/debug/intelligent等

> 参考文档:
- [c-cpp-properties文件参考](https://code.visualstudio.com/docs/cpp/c-cpp-properties-schema-reference)

## intelligent

因为C/C++特有的宏机制, 在vscode中查看项目代码会有部分宏选项代码变暗, 无法搜索. 可以全局配置` C_Cpp.default.*` 也可在 `.vscode` 文件夹下配置`c_cpp_properties.json`文件夹


## c_cpp_properties.json示例

```json
{
  "env": {
    "myIncludePath": ["${workspaceFolder}/include", "${workspaceFolder}/src"],
    "myDefines": ["DEBUG", "MY_FEATURE=1"]
  },
  "configurations": [
    {
      "name": "Linux",
      "compilerPath": "/usr/bin/gcc",
      "compilerArgs": ["-m32"],
      "intelliSenseMode": "linux-gcc-x86",
      "includePath": ["${myIncludePath}", "/usr/include"],
      "defines": ["${myDefines}"],
      "cStandard": "gnu11",
      "cppStandard": "gnu++14",
      "configurationProvider": "ms-vscode.cmake-tools",
      "forcedInclude": ["${workspaceFolder}/common.h"],
      "compileCommands": "${workspaceFolder}/build/compile_commands.json",
      "dotConfig": "${workspaceFolder}/.config",
      "mergeConfigurations": true,
      "customConfigurationVariables": {
        "myVar": "myvalue"
      },
      "browse": {
        "path": ["${myIncludePath}", "/usr/include", "${workspaceFolder}"],
        "limitSymbolsToIncludedHeaders": true,
        "databaseFilename": "${workspaceFolder}/.vscode/browse.vc.db"
      }
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