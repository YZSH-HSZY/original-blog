
## distutils模块
distutils是Python的一个标准库模块，用于构建和分发Python包. 它是Python最早的打包工具，现在已被setuptools和pip等更现代的工具所取代，了解distutils有助于理解Python打包的基础。

> 配置文件中有三种可能的配置文件
> 1. 在Distutils安装目录中(即Distutils __inst__.py 文件所在目录)的 `distutils.cfg` 
> 2. 在用户家目录中的 `.pydistutils.cfg`(Unix下)/`pydistutils.cfg`(Windows/Mac下)
> 3. 在当前目录下 `setup.cfg`

**注意** 老项目编译安装时无distutils.cfg需新建, 示例如下
```ini
[build]
compiler=mingw32

[build_ext]
compiler=mingw32
```

**注意** distutils已经停止开发，新项目应该使用setuptools

### distuils与其他工具比较

- setuptools: 扩展了distutils的功能，是现在的事实标准
- pip: Python的包安装工具
- wheel: 新的分发格式

### distuils的简易使用

1. 创建简单的setup.py
```py
from distutils.core import setup

setup(
    name="mypackage",
    version="1.0",
    description="A simple example package",
    author="Your Name",
    author_email="your@email.com",
    py_modules=["mymodule"],
)
```
2. 打包构建
- python setup.py build: 构建包
- python setup.py install: 安装包
- python setup.py sdist: 创建源码分发
- python setup.py bdist: 创建二进制分发
