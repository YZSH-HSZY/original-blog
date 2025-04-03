## pip命令
[pip官方文档](https://pip.pypa.io/en/stable/cli/pip/)

### pip镜像源
常用镜像源地址：

阿里云：https://mirrors.aliyun.com/pypi/simple/
清华大学：https://pypi.tuna.tsinghua.edu.cn/simple/
中国科学技术大学：https://pypi.mirrors.ustc.edu.cn/simple/
豆瓣：https://pypi.douban.com/simple/

**你可以通过-i <镜像网站> 来指定临时镜像源**

**全局镜像源配置**
```
# 查看pip配置列表
ubuntu@VM-12-17-ubuntu:/usr/lib/python3.8/lib-dynload$ pip config list
global.index-url='http://mirrors.tencentyun.com/pypi/simple'
global.trusted-host='mirrors.tencentyun.com'
# 配置pip全局镜像源
pip config set global.index-url <镜像源地址>
```

### pip环境迁移
1. 导出pip包 `pip freeze > requirements.txt`
2. 下载`pip download -d packages -r requirements.txt`，使用`--only-binary=:all:`选项获取wheel包，对于一个指定包会同步处理其依赖包
3. 使用`pip install --no-index --find-links ./packages  -r requirements.txt`进行离线安装

### pip查看一个指定包的依赖
1. 安装`pipdeptree`包
2. `pipdeptree -r -p <pkg>` 查看依赖于指定包的其他包
3. `pipdeptree -p <pkg>` 查看指定包依赖的其他包


### wheel文件下载地址

清华镜像源：https://pypi.tuna.tsinghua.edu.cn/simple/windows-curses/
如果直接访问 https://pypi.tuna.tsinghua.edu.cn/simple 可能禁止访问，可以将相应下载的wheel包添加在路径中
你也可以在pypi这个包资源管理网站(https://pypi.org)中，搜索指定包然后下载wheel文件

## pyc/pyo/pyd/py文件
1. .py表示一个python的源代码文件，可以使用记事本之类的编辑器编辑。

> Python附带了一个解释器，你可以选择交互式的运行python代码，也可以选择把python写成脚本文件来运行。两种情况下，解析器都是先解析你的代码，然后编译为字节码（bytecode），然后通过python虚拟机来运行代码。

.pyc、.pyo和.pyd类型的文件，**都是python的解释器在把python代码转化为字节码的过程中产生的**。在把源代码转化为操作系统可以执行的机器指令的过程中，中间一定会生成字节码。

但是，python的虚拟机和其他虚拟机（比如Java虚拟机，Erlang虚拟机）是不同的。**python的虚拟机直接连接操作系统和硬件**来执行原生的机器指令。

2. .pyc文件类型，当你导入一个模块时，解释器会自动生成.pyc文件，这样会节省下次导入的时间。

3. 当有模块被导入的时候，解释器也会产生.pyo文件，只不过需要告诉解释器开启优化设置。这样可以产生更小的字节码文件。命令如下：`python -O <py文件>`

> 产生.pyo文件就不再产生.pyc文件了（python3.5以前是.pyo，python3.5以后就是产生.opt-1.pyc文件）。

4. 和前两个相比，.pyd文件类型是平台相关的，**只和Windows平台有关系**。在Windows平台下，.pyd文件是一个包含python代码的库，可以被其他的python程序调用，为了让这个库可以被其他python程序调用，被打包成动态链接库（dynamic link library）。

> 动态链接库是Windows平台下的代码库，在运行时被调用。它有利于代码重用、代码模块化，并且可以更快的启动程序。因此，DLL在Windows操作系统中发挥了重要作用。

.pyc和.pyo都包含字节码文件，但是.pyo更紧凑。

.pyd是动态链接库，只会在Windows操作系统中见到。

所有这些类型的文件都是被其他的python程序调用。

## python 虚拟环境

python虚拟环境是用来解决项目依赖环境冲突的，常见的环境管理工具有conda、virtualenv/venv等
[anaconda参考](anaconda_help.md)

```sh
venv是py官方自带的环境管理工具，不过其只能在已有py的机器上创建一个环境目录(为当前py的拷贝)

$ pip install virtualenv
virtualenv 可以管理多个py版本的环境，不过每次创建环境均会生成一个目录

$ pip install {virtualenvwrapper, virtualenvwrapper-win}
# virtualenvwrapper是virtualenv的扩展工具（在统一的目录 ~/.virtualenvs 中管理所有虚拟环境），可以方便的创建、删除、复制、切换不同的虚拟环境。
activate <env_name>/bin/activate  # 激活环境
deactivate  # 取消激活环境

创建虚拟环境：mkvirtualenv [虚拟环境名称]
virtualenv venv --python=python3.7 指定python版本
列出虚拟环境：lsvirtualenv
切换虚拟环境：workon [虚拟环境名称]
查看当前环境安装了哪些包：lssitepackages
进入当前环境的目录：cdvirtualenv [子目录名]
进入当前环境的site-packages目录：cdsitepackages [子目录名]
控制当前环境是否使用global site-packages：toggleglobalsitepackages
复制虚拟环境：cpvirtualenv [source] [dest]
退出虚拟环境：deactivate
删除虚拟环境：rmvirtualenv [虚拟环境名称]
```

### uv
uv是一个新兴的python项目和包管理工具,使用rust编写.

[uv官方文档](https://docs.astral.sh/uv/)
[uv-blog](./env_manage/uv.md)

## python调试（pdb模块）

[官方pdb文档](https://docs.python.org/zh-cn/3/library/pdb.html#module-pdb)

python调试有两种方式
1. 侵入式调试（即在python运行到该位置时自动暂停并进入调试模式，中断进入调试器的典型用法是插入
python内置pdb模块，你可以使用`import pdb; pdb.set_trace()`来设置断点
> 3.7 新版功能: 内置函数 breakpoint()，当以默认参数调用它时，可以用来代替 import pdb; pdb.set_trace()。

然后你可以单步执行这条语句之后的代码，并使用 continue 命令来关闭调试器继续运行。

2. 非侵入式调试，在命令行下调用pdb调试其他脚本`python -m pdb <myscript.py>`

**pdb函数**

1. pdb.run(statement, globals=None, locals=None)
在调试器控制范围内执行 statement （以字符串或代码对象的形式提供）。调试器提示符会在执行代码前出现，你可以设置断点并键入 continue，也可以使用 step 或 next 逐步执行语句（上述所有命令在后文有说明）。可选参数 globals 和 locals 指定代码执行环境，默认时使用 __main__ 模块的字典。（请参阅内置函数 exec() 或 eval() 的说明。）

2. pdb.runeval(expression, globals=None, locals=None)
Evaluate the expression (given as a string or a code object) under debugger control. When runeval() returns, it returns the value of the expression. Otherwise this function is similar to run().

3. pdb.runcall(function, *args, **kwds)
使用给定的参数调用 function （以函数或方法对象的形式提供，不能是字符串）。runcall() 返回的是所调用函数的返回值。调试器提示符将在进入函数后立即出现。

4. pdb.set_trace(*, header=None)
在调用本函数的堆栈帧处进入调试器。用于硬编码一个断点到程序中的固定点处，即使该代码不在调试状态（如断言失败时）。如果传入 header，它将在调试开始前被打印到控制台。

在 3.7 版更改: 仅关键字参数 header。

5. pdb.post_mortem(traceback=None)
进入 traceback 对象的事后调试。如果没有给定 traceback，默认使用当前正在处理的异常之一（默认时，必须存在正在处理的异常）。

6. pdb.pm()
在 sys.last_traceback 中查找 traceback，并进入其事后调试。

**pdb命令**
1. 帮助信息
- h(elp) [command]
> 不带参数时，显示可用的命令列表。参数为 command 时，打印有关该命令的帮助。help pdb 显示完整文档（即 pdb 模块的文档字符串）。由于 command 参数必须是标识符，因此要获取 ! 的帮助必须输入 help exec。

2. 执行命令
- s(tep)
> 运行当前行，进入被调用函数内部

- n(ext)
> 运行当前行，不进入被调用函数内部

- unt(il) [lineno]
如果不带参数，则继续运行，直到行号比当前行大时停止。
对于参数lineno，继续执行，直到到达大于或等于lineno的行。在这两种情况下，当当前帧返回时也停止。
With lineno, continue execution until a line with a number greater or equal to lineno is reached. In both cases, also stop when the current frame returns.

在 3.2 版更改: 允许明确给定行号。

- r(eturn)
继续运行，直到当前函数返回。

- c(ont(inue))
继续运行，仅在遇到断点时停止。

- j(ump) lineno
设置即将运行的下一行。仅可用于堆栈最底部的帧。它可以往回跳来再次运行代码，也可以==往前跳来跳过不想运行的代码。==

需要注意的是，不是所有的跳转都是允许的 -- 例如，不能跳转到 for 循环的中间或跳出 finally 子句。

3. 断点命令
- b(reak) [([filename:]lineno | function) [, condition]]
> 如果带有 lineno 参数，则在当前文件相应行处设置一个断点。如果带有 function 参数，则在该函数的第一条可执行语句处设置一个断点。行号可以加上文件名和冒号作为前缀，以在另一个文件（可能是尚未加载的文件）中设置一个断点。另一个文件将在 sys.path 范围内搜索。请注意，每个断点都分配有一个编号，其他所有断点命令都引用该编号。


4. 栈操作命令
- w(here)
> 打印堆栈跟踪，在底部显示最近的帧。箭头(>)表示当前帧，它决定了大多数命令的上下文。
- d(own) [count]
> 在堆栈回溯中，将当前帧向下移动 count 级（默认为 1 级，移向更新的帧）。
- u(p) [count]
> 在堆栈回溯中，将当前帧向上移动 count 级（默认为 1 级，移向更老的帧）。

如果第二个参数存在，它应该是一个表达式，且它的计算值为 true 时断点才起作用。

如果不带参数执行，将列出所有中断，包括每个断点、命中该断点的次数、当前的忽略次数以及关联的条件（如果有）。

- interact
启动一个交互式解释器（使用 code 模块），它的全局命名空间将包含当前作用域中的所有（全局和局部）名称。

- q(uit)
退出调试器。 被执行的程序将被中止。

- debug code
在代码中输入一个递归调试器(这是在当前环境中执行的任意表达式或语句)。
Enter a recursive debugger that steps through code (which is an arbitrary expression or statement to be executed in the current environment).

- retval
打印当前函数最后一次返回的返回值
Print the return value for the last return of the current function.
- display
如果表达式的值改变了，每次执行在当前帧停止时显示它的值。
如果没有表达式，列出当前框架的所有显示表达式。

- undisplay
在当前帧中不再显示表达式。如果没有表达式，则清除当前帧的所有显示表达式。

- l(ist) [first[, last]]
列出当前文件的源代码。如果不带参数，则列出当前行周围的 11 行，或继续前一个列表。如果用 . 作为参数，则列出当前行周围的 11 行。如果带有一个参数，则列出那一行周围的 11 行。如果带有两个参数，则列出所给的范围中的代码；如果第二个参数小于第一个参数，则将其解释为列出行数的计数。

当前帧中的当前行用 -> 标记。如果正在调试异常，且最早抛出或传递该异常的行不是当前行，则那一行用 >> 标记。

3.2 新版功能: >> 标记。

- ll | longlist
列出当前函数或帧的所有源代码。相关行的标记与 list 相同。

## py模块安装示例
###  Appium-Python-Client安装
Appium是一个开源的，适用于原生或混合移动应用（ hybrid mobile apps ）的自动化测试工具，
应用WebDriver: JSON wire protocol驱动安卓和iOS移动应用。

**注意事项**

1. 选择了Client/Server的设计模式，Client支持多语言。
2. 扩展了WebDriver的协议，以前的WebDriver API能够直接被继承过来，以前的Selenium（WebDriver）各种语言的binding都可以拿来就用，省去了为每种语言开发一个client的工作量。

通过命令： pip install Appium-Python-Client 进行安装。 

## python 动态导入

### 通过 `importlib.import_module` 进行

`import_module(name, package=None)`
导入一个模块。 参数 `name` 指定了以绝对或相对导入方式导入(如 `pkg.mod` 或 `..mod`)。 如果参数 `name` 使用相对导入的方式来指定(即以`.`开始)，那么 `package` 参数必须设置为对于包名，这个包名作为解析这个包名的锚点 

> 如 `import_module('..mod', 'pkg.subpkg')` 将会导入 pkg.mod

> `import_module()` 函数是一个对 `importlib.__import__()` 进行简化的包装器。 两个函数之间最重要的不同点在于 `import_module()` 返回指定的包或模块 (例如 pkg.mod)，而 `__import__()` 返回最高层级的包或模块 (例如 pkg)。

**注意** 如果动态导入一个自解释器开始执行以来被创建的模块（即创建了一个 Python 源代码文件），为了让导入系统知道这个新模块，可能需要调用 `invalidate_caches()`(用于使查找器存储在 sys.meta_path 中的内部缓存无效)

**注意** python通过 `__init__.py` 文件判断该文件夹是否为一个python包

#### `import_module` 的近似实现

```python
import importlib.util
import sys

def import_module(name, package=None):
    """An approximate implementation of import."""
    absolute_name = importlib.util.resolve_name(name, package)
    try:
        return sys.modules[absolute_name]
    except KeyError:
        pass

    path = None
    if '.' in absolute_name:
        parent_name, _, child_name = absolute_name.rpartition('.')
        parent_module = import_module(parent_name)
        path = parent_module.__spec__.submodule_search_locations
    for finder in sys.meta_path:
        spec = finder.find_spec(absolute_name, path)
        if spec is not None:
            break
    else:
        msg = f'No module named {absolute_name!r}'
        raise ModuleNotFoundError(msg, name=absolute_name)
    module = importlib.util.module_from_spec(spec)
    sys.modules[absolute_name] = module
    spec.loader.exec_module(module)
    if path is not None:
        setattr(parent_module, child_name, module)
    return module
```
### 通过 `spec.loader.exec_module` 进行

`spec.loader.exec_module`导入一个模块，一般和以下函数配套使用

1. `importlib.util.spec_from_file_location` 从文件路径获取一个`ModuleSpec`对象(ModuleSpec用于导入系统相关状态的规范说明)
2. `importlib.util.module_from_spec(ModuleSpec) -> ModuleType` 从一个模块描述对象创建模块

### 一个动态导入并通过pyinstaller打包的示例
```python
import os

# 动态生成一个 Python 文件
def create_module():
    module_code = """
def greet(name):
    return f"Hello, {name}!"
"""
    with open("generated_module.py", "w") as f:
        f.write(module_code)

# 创建模块
create_module()

# 动态导入生成的模块
import importlib.util
import sys
import importlib

module_name = "generated_module"
module_path = "generated_module.py"

spec = importlib.util.spec_from_file_location(module_name, module_path)
generated_module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = generated_module
spec.loader.exec_module(generated_module)

# 使用生成的模块
if __name__ == "__main__":
    name = "World"
    print(generated_module.greet(name))

# 通过以下命令打包
# pyinstaller --onefile -w main.py
```

### reload重新导入的问题
python 的导入库importlib 提供了一种重新导入的方式 `reload`

> 注意:
1. 重新导入需要之前此**模块已被导入**
2. Python 模块的代码会被重新编译并且那个模块级的代码被重新执行，通过重新使用一开始加载那个模块的 loader，定义一个新的绑定在那个模块字典中的名称的对象集合。**扩展模块的 init 函数不会被调用第二次**
3. 与Python中的所有的其它对象一样，旧的对象只有在它们的引用计数为0之后才会被回收
4. 模块命名空间中的名称重新指向任何新的或更改后的对象。而其他旧对象的引用（例如那个模块的外部名称）**不会被重新绑定到引用的新对象的**，并且如果有需要，必须在出现的每个命名空间中进行更新。
5. 一个新模块没有定义在旧版本模块中定义的名称，则将**保留旧版本中的定义**

## py跨平台api

#### Python的os和shutil模块封装了常见的文件和目录操作如copy，cd，mv，rm以及解压等等操作。