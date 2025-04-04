# vcpkg

[微软vcpkg官方文档](https://learn.microsoft.com/zh-cn/vcpkg/)

## 安装

1. 下载vcpkg代码仓库 `git clone https://github.com/microsoft/vcpkg`
2. 运行启动脚本 `.\vcpkg\bootstrap-vcpkg.bat`(用于下载 vcpkg 可执行文件)

## 使用

在cmake中使用vcpkg安装的pkg `cmake -DCMAKE_TOOLCHAIN_FILE=D:/vcpkg/scripts/buildsystems/vcpkg.cmake ..`

msbuild 中使用 `D:\vcpkg\vcpkg.exe integrate install`