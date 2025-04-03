# uv
uv是一个新兴的python项目和包管理工具,使用rust编写.

[uv官方文档](https://docs.astral.sh/uv/)

## 安装
以下方式任选其一:
1. `pip install uv`
2. window: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
3. linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`

## 使用
- `uv init` 初始化项目
- `uv sync` 从同步配置文件中同步依赖
- `uv add {pip_pkg}` 项目添加依赖, 在`pyproject.toml`中
- `uv install python 3.9` 安装指定python版本解释器
- `uv venv --python 3.9` 创建 `.venv` 目录, 包管理虚拟环境