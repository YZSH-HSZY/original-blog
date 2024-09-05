# pyinstaller
pyinstaller是一个python的打包库
[官方文档](https://pyinstaller.org/en/stable/spec-files.html "spec规范文件说明")

## 选项

`-F或--onefile` 打包为一个可执行文件
`-w` 不提供控制台窗口（即打包为一个gui界面）
`-p` 提供在import时的查找路径

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

## pyinstaller的路径问题

打包应用在启动时，pyinstaller的启动加载器会设置 `sys.frozen` 属性，并在 `sys._MEIPASS` 中存储打包文件夹的绝对路径。
- 对于单文件夹(普通打包)打包，这是打包内的 `_internal` 文件夹的路径。
- 对于单文件(即通过`-F`或`--onefile`)打包，这是启动加载器创建的临时文件夹的路径。

> 当您的程序未打包时，Python 变量 `__file__` 指的是包含该变量的模块的当前路径。从打包脚本导入模块时，PyInstaller 启动程序会将模块的 `__file__` 属性设置为相对于打包文件夹的正确路径。

### 可执行文件的路径

当正常的 Python 脚本运行时， `sys.executable` 是执行的程序路径(即 Python解释器)。在打包的exe文件中， `sys.executable` 是exe文件的路径(不是 Python解释器路径)，而是单文件应用中的启动加载器或单文件夹应用中的可执行文件。

> 你可以通过这种方法来定位用户实际启动的exe可执行文件

> 一种示例如下：
```python
frozen = 'not'
if getattr(sys, 'frozen', False):
    # we are running in a bundle
    frozen = 'ever so'
    bundle_dir = sys._MEIPASS
else:
    # we are running in a normal Python environment
    bundle_dir = os.path.dirname(os.path.abspath(__file__))
print( 'we are',frozen,'frozen')
print( 'bundle dir is', bundle_dir )
print( 'sys.argv[0] is', sys.argv[0] )
print( 'sys.executable is', sys.executable )
print( 'os.getcwd is', os.getcwd() )
# output:
# we are ever so frozen
# bundle dir is C:\Users\admin\AppData\Local\Temp\_MEI116202
# sys.argv[0] is dist\main.exe
# sys.executable is D:\yzsh\all_project\ProductProcess\dist\main.exe
# os.getcwd is D:\yzsh\all_project\ProductProcess
```
## 问题集合

### pyinstaller打包exe文件运行报错

**问题描述** `ImportError: DLL load failed while importing win32gui: 找不到指定的模块`

**解决方法:**
在交互式命令行中，导入模块，通过__file__属性找到文件路径，在pyinstaller的spec规范文件中指定位置重新使用`pyinstaller [options] <name.spec>`打包或者直接打包时使用命令行选项指定

### pyinstaller打包的exe文件创建目录不生效

当程序被打包成 `.exe` 文件后，PyInstaller 会将所有资源文件解压到一个临时目录中，`sys._MEIPASS` 提供了这个临时目录的路径。并且PyInstaller 启动程序会将模块的 `__file__` 属性设置为相对于打包文件夹的正确路径。因此你通过`__file__` 创建的文件和目录均在自动生成的临时目录下。

### pyinstaller报`OSError: could not get source code`

取消 `-w` 选项，在控制台执行，报`File "<frozen importlib._bootstrap>", line 991, in _find_and_load`
1. 根据报错信息，排查执行错误，这里发现是在`import inflect`时报错，可以使用`--collect-all inflect`
2. 参issue[get source code错误](https://github.com/pyinstaller/pyinstaller/issues/4764)