# setuptools

一个构建和发行python包的工具

[setuptools官方文档](https://setuptools.pypa.io/en/latest/userguide/quickstart.html)

## 安装

使用 pip 安装最新的setuptools `pip install --upgrade setuptools[core]`
相反，在创建新的 Python 包时，建议使用名为 build 的命令行工具。此工具将自动下载 setuptools 和项目可能具有的任何其他构建时依赖项。只需在包根目录下的 `pyproject.toml` 文件中指定它们。

## 使用

> 一个简易待发布的py项目如下:
```sh
mypackage
├── pyproject.toml  # and/or setup.cfg/setup.py (depending on the configuration method)
|   # README.rst or README.md (a nice description of your package)
|   # LICENCE (properly chosen license information, e.g. MIT, BSD-3, GPL-3, MPL-2, etc...)
└── mypackage
    ├── __init__.py
    └── ... (other Python files)
```

## 示例

### 包含c代码的项目指定编译器架构

指定的架构应该和python匹配, 使用`python -c "import sys; print(sys.version)"`查看架构

> 在window使用x64编译
```sh
set DISTUTILS_USE_SDK=1
set MSSdk=1
set PLATFORM=x64
python setup.py build
```