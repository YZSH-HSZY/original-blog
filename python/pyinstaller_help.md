# pyinstaller
pyinstaller是一个python的打包库
[官方文档](https://pyinstaller.org/en/stable/spec-files.html "spec规范文件说明")

## 选项

`-F或--onefile` 打包为一个可执行文件
`-w` 不提供控制台窗口（即打包为一个gui界面）

## spec文件

PyInstaller 首先做的事情是构建一个 spec（规格）文件 `myscript.spec` .该文件默认存储在 `--specpath` 目录中，通常是当前目录。

**注意** 一般情况下，你不需要修改spec文件，仅当你在以下情景下，可能需要：

1. 当你想要将数据文件与应用打包在一起时。
2. 当你想要包含 PyInstaller 不知道的其他来源的运行时库（ .dll 或 .so 文件）时。
3. 当你想要为可执行文件添加 Python 运行时选项时。
4. 当你想要创建一个包含合并通用模块的多程序捆绑包时。

### 创建spec文件

- 通过`pyi-makespec [options] <name.py> [other scripts …]`生成
- 通过`pyinstaller <py_file>`打包时生成

### 通过spec文件打包
`pyinstaller [options] <name.spec>`

### spec文件示例
```python
a = Analysis(['minimal.py'],
         pathex=['/Developer/PItests/minimal'],
         binaries=None,
         datas=None,
         hiddenimports=[],
         hookspath=None,
         runtime_hooks=None,
         excludes=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,... )
coll = COLLECT(...)
```

### spec结构说明

spec文件中包含4个类classes, `Analysis`, `PYZ`, `EXE`, `COLLECT`

> 其中 `Analysis` 接受一组脚本名称作为输入。它分析所有导入和其他依赖关系。生成的对象包含以下属性
- scripts : 命令行中指定的 Python 脚本
- pure : 脚本所需的纯 Python 模块
- pathex : 寻找导入的路径列表（类似于 `PYTHONPATH` ），包括通过 `--paths` 选项提供的路径。
- binaries : 需要的非 Python 模块，包括通过 `--add-binary` 选项给出的名称
- datas : 非二元文件包含在应用中，包括通过 `--add-data` 选项给出的名称
> `PYZ` 的实例是一个 `.pyz` 归档，其中包含所有来自 a.pure 的 Python 模块
> `EXE` 的实例由分析的脚本和 PYZ 存档构建而成，用于创建可执行文件
> `COLLECT` 的实例从所有其他部分创建输出文件夹

**注意** 在单文件模式下，没有调用 `COLLECT` ， `EXE` 实例接收所有脚本、模块和二进制文件


## 问题集合

### pyinstaller打包exe文件运行报错

**问题描述** `ImportError: DLL load failed while importing win32gui: 找不到指定的模块`

**解决方法:**
在交互式命令行中，导入模块，通过__file__属性找到文件路径，在pyinstaller的spec规范文件中指定位置重新使用`pyinstaller [options] <name.spec>`打包或者直接打包时使用命令行选项指定
