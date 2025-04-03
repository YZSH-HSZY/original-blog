# setuptools

一个构建和发行python包的工具

[setuptools官方文档](https://setuptools.pypa.io/en/latest/userguide/quickstart.html)

## 安装

使用 pip 安装最新的setuptools `pip install --upgrade setuptools[core]`
相反，在创建新的 Python 包时，建议使用名为 build 的命令行工具。此工具将自动下载 setuptools 和项目可能具有的任何其他构建时依赖项。您只需在包根目录下的 pyproject.toml 文件中指定它们，如以下部分所示。