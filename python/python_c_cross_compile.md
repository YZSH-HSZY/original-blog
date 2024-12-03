## python项目编译构建

distutils模块
There are three possible config files: distutils.cfg in the
Distutils installation directory (ie. where the top-level
Distutils __inst__.py file lives), a file in the user's home
directory named .pydistutils.cfg on Unix and pydistutils.cfg
on Windows/Mac; and setup.cfg in the current directory.

无distutils.cfg需新建
[build]
compiler=mingw32

[build_ext]
compiler=mingw32

## cython
在python的基础上融合了C、C++ 的静态类型，包含一个编译器，负责将 Cython 源代码翻译成高效的 C 或者 C++ 源代码；Cython 源文件被编译之后的最终形式可以是 Python 的扩展模块（.pyd），也可以是一个独立的可执行文件。

[cython官方文档](https://cython.readthedocs.io/en/latest/)

### 编译器配置
- `windows`
安装MingW-w64编译器：conda install libpython m2w64-toolchain -c msys2
在Python安装路径下找到\Lib\distutils文件夹，创建distutils.cfg写入如下内容：
`[build] compiler=mingw32`
- `macOS`
安装XCode即可
- `linux`
gcc一般都是配置好的，如果没有就执行这条命令： sudo apt-get install build-essential

### 基本使用示例

