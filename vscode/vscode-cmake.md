# vscode-cmake
microsoft推出的一个适用于vscode的cmake-tool插件

> 参考文档:
> - [cmake tools官方仓库](https://github.com/microsoft/vscode-cmake-tools)
> - [CMake Tools常见设置](https://github.com/microsoft/vscode-cmake-tools/blob/main/docs/cmake-settings.md)


## setting

|设置项|描述|作用空间|
|-----|---|------|
|`cmake.environment`          |     |user/workspace/folder|
|`cmake.configureEnvironment` |     在配置时传递给 CMake|user/workspace/folder|

### cmake预设

> 参考文档:
- [Microsoft-cmake预设](https://learn.microsoft.com/zh-cn/cpp/build/cmake-presets-vs?view=msvc-170#sourcing-the-environment-when-building-with-command-line-generators-on-windows)

CMake 支持两种文件, 允许用户指定常见的配置、构建和测试选项, `CMakePresets.json`/`CMakeUserPresets.json` 