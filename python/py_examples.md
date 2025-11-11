## python示例

### python 标识符和字面值

对字面值求值将返回一个该值所对应类型的对象（字符串、字节串、整数、浮点数、复数）。 对于浮点数和虚数（复数）的情况，该值可能为近似值。 详情参见 字面值。

**所有字面值都对应于不可变数据类型**，因此对象标识的重要性不如其实际值。 多次对具有相同值的字面值求值（不论是发生在程序文本的相同位置还是不同位置）可能得到相同对象或是具有相同值的不同对象。（取决python解释器的实现）

#### 对象、值与类型
对象 是 Python 中对数据的抽象。 Python 程序中的所有数据都是由对象或对象间关系来表示的。 （从某种意义上说，按照冯·诺依曼的“存储程序计算机”模型，**代码本身也是由对象来表示的**。）

每个对象都有各自的标识号、类型和值。一个对象被创建后，它的 标识号 就绝不会改变；你可以将其理解为该对象在内存中的地址。 'is' 运算符可以比较两个对象的标识号是否相同；id() 函数能返回一个代表其标识号的整数。

对象的类型决定该对象所支持的操作 (例如 "对象是否有长度属性？") 并且定义了该类型的对象可能的取值。type() 函数能返回一个对象的类型 (**类型本身也是对象**)。与编号一样，**一个对象的 类型 也是不可改变的。**

####  None、NotImplemented、Ellipsis、False、True
**均为内置常量，只有一种取值。是一个具有此值的单独对象。**
- None 空值
- NotImplemented 无实列，在由双目运算特殊方法（如 `__eq__()`等）返回的特殊值，以表明该运算没有针对其他类型的实现
- Ellipsis 等同省略量字面值...
- False、True 唯二的bool值

#### 序列
一种支持非负整数下标索引的对象，可分为不可变序列和可变序列
- 不可变序列：（字符串str、元组tuple、字节串bytes）
- 可变序列：（列表list、字节数组bytearray）

### class
#### 静态属性、成员属性、静态方法、类方法、成员方法
```
def main():
    class LearnClass:
        static_a = {}  # 静态属性,所有实例只有一个备份
        def __init__(self) -> None:
            self.obj_a = {}
            pass
        def print_id(self):
            print(id(self.static_a),id(self.obj_a))
    a1 = LearnClass()
    a2 = LearnClass()
    a1.print_id()
    a2.print_id()
    a1.static_a.setdefault('xs',23)
    a1.obj_a.setdefault('obja',78)
    print(a2.static_a.get('xs'),a2.obj_a.get('obja'))

output:
    2205038842720 2204998719744
    2205038842720 2205043631088
    23 None
```
静态方法和静态方法和类方法都依附在定义的类，这个类对象上
成员属性和成员方法在实例化对象时创建，依附在实例化对象上

### dict
python的字典是一种哈希表，是根据关键码值(Key value)而直接进行访问的数据结构。也就是说，它通过把关键码值映射到表中一个位置来访问记录，以加快查找的速度。这个映射函数叫做散列函数(哈希函数)，存放记录的数组叫做散列表(哈希表/hash table)。

#### hash冲突解决

**开放定址--二次探针**
python 采用的是开放定址法（open addressing）来解决哈希冲突,其原理是产生哈希冲突时, python 会通过一个二次探测函数 f, 计算下一个候选位置,当下一个位置可用，则将数据插入该位置,如果不可用则再次调用探测函数 f,获得下一个候选位置，因此经过不断探测,总会找到一个可用的位置。

#### 使用 抽取 和 属性引用 获取元素
- 抽取 
例：d[<"key_value">]
一个对象可通过同时定义 `__getitem__() 和 __class_getitem__()` 或其中之一来支持抽取操作。
- 属性引用 
例：d.key
这个产生过程可通过重载 `__getattr__()` 方法来自定义。

### python单行注释和多行注释和文档字符串
Python 使用井号#作为单行注释的符号，多行注释三个单引号'''包裹

### 文件和目录操作

#### TODO
`fileno()` 方法本身并不是全局不冲突的，因为它返回的是与特定文件对象关联的文件描述符，而不是全局唯一的标识符。
不过，在同一进程中，文件描述符在一定范围内是唯一的，直到你关闭文件对象。

#### 目录操作
```
os.mkdir(),os.makedirs()                    # 创建目录

os.mkdir(            # 创建一层目录，
os.makedirs(             # 创建多层级目录  

os.getcwd()，os.path.abspath('.')           # 获取当前工作目录
os.chdir(path)                              # 更改工作目录

os.removedirs(          # 递归删除所有空目录，深度优先搜素
shutil.rmtree(          # 递归删除所有文件和目录
```
##### os.path.realpath与os.path.abspath区别
realpath会返回软链接文件指向的实际地址
abspath则会返回软链接所在位置的绝对路径

#### 复制或移动或重命名文件
```
shutil.copy($file_path, $dir_path) # 复制文件
shutil.move($file_path, $dir_path) # 移动到另外一个文件夹中
shutil.move($file_path, $new_file_path) # 重命名为新的绝对路径
```

#### open各文件打开模式
```
'r'	open for reading (default)
'w'	open for writing, truncating the file first（首先截断文件）
'x'	create a new file and open it for writing（若文件存在，则报错）
'a'	open for writing, appending to the end of the file if it exists
'b'	binary mode
't'	text mode (default)
'+'	open a disk file for updating (reading and writing)
注意：'r+'与'w+'的区别，'w+'会截断文件，即擦除原有内容。
读写模式下，你可以使用file对象的seek函数更改文件指针位置。
'U'	universal newline mode(通用换行模式) (deprecated 已弃用)
```
#### window下文件存在但python使用open打开报错

**window 11中默认不启用长路径**
Windows 启用长路径支持
打开注册表编辑器：regedit
找到如下路径：HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSytem
找到如下键值：LongPathsEnabled
将值修改为1：默认是0，不启用。

### python脚本编写帮助

#### python 脚本处理输入参数
你可能会手动的处理 sys.argv 或者使用 getopt 模块。但是，使用argparse模块，将会减少很多冗余代码，
底层细节argparse 模块已经帮你处理了。你可能还会碰到使用 optparse 库解析选项的代码。
尽管 optparse 和 argparse 很像，但是后者更先进，因此在新的程序中你应该使用它。

**argparse处理未知选项参数**
1. 使用`args, unknown = parser.parse_known_args()` 而不是`args = parser.parse_args()` 来解析选项
2. 如果您想使用剩余的部分，可以使用parser.add_argument('args', nargs=argparse.REMAINDER)将它们放入新的参数中。

#### python调用外部命令，模拟交互输入

##### 使用内置subprocess模块
`subprocess.check_output(['cmd','arg1','arg2'])`
默认情况下， check output() 仅仅**返回输入到标准输出的值**。如果你需要同时收集标准输出和错误输出，使用 stderr 参数,例：
`subprocess.check_output(['cmd','arg1','arg2'], stderr=subprocess.STDOUT, timeout=5)`

通常来讲，命令的执行不需要使用到底层 shell 环境（比如 sh、 bash）。一个字符
串列表会被传递给一个低级系统命令，比如 os.execve() 。如果你想让命令被一个
shell 执行，传递一个字符串参数，并设置参数 shell=True . 有时候你想要 Python 去
执行一个复杂的 shell 命令的时候这个就很有用了，比如管道流、 I/O 重定向和其他特
性。

如果需要对子进程做更复杂的交互，比如给它发送输入，可以采用另外一种方法。
这时候可直接使用 subprocess.Popen 类。例如：
```python
# Launch a command with pipes
p = subprocess.Popen(['wc'],
    stdout = subprocess.PIPE,
    stdin = subprocess.PIPE)
# Send the data and get the output
stdout, stderr = p.communicate(text)
# To interpret as text, decode
out = stdout.decode('utf-8')
err = stderr.decode('utf-8')
```

subprocess 模块对于依赖 TTY 的外部命令不合适用。例如，你不能使用它来自动化一个用户输入密码的任务（比如一个 ssh 会话）。
这时候，你需要使用到第三方模块了，比如基于著名的 expect 家族的工具（pexpect 或类似的）

**tty是什么？**
在 Linux 或 UNIX 中，TTY 变为了一个抽象设备。有时它指的是一个物理输入设备，例如串口，有时它指的是一个允许用户和系统交互的虚拟 TTY
在大多数 发行版 中，你可以使用以下键盘快捷键来得到 TTY 屏幕
CTRL + ALT + F1 – 锁屏
CTRL + ALT + F2 – 桌面环境
CTRL + ALT + F3 – TTY3
CTRL + ALT + F4 – TTY4
CTRL + ALT + F5 – TTY5
CTRL + ALT + F6 – TTY6
在ubuntu中你可以使用tty查看当前连接的tty编号
```
ubuntu@VM-12-17-ubuntu:~$ tty
/dev/pts/1
ubuntu@VM-12-17-ubuntu:~$ who
ubuntu   pts/0        2023-08-08 15:44 (111.183.9.68)
ubuntu   pts/1        2023-08-08 16:09 (111.183.9.68)
```

##### pexpect模块

**注意** pexpect工作在Unix-like系统,如果你需要在window上使用它,请安装WinPexpect

在讲解Pexpect之前，我们需要先了解一下Expect这个脚本语言，它是由TCL语言实现的，主要用于人机交互式对话的自动化控制，可以用来完成ssh、ftp、telnet等命令行程序的自动化交互。Pexpect其实就是一个用Python语言实现的类Expect功能的模块，通过它就可以在Python中完成Expect所完成的功能。

示例--通过python启动docker服务
```python
import pexpect
s=pexpect.spawn('systemctl start docker')       #实例化spawn类
s.sendline('<user_password>')                   #发送字符串，末尾添加换行，与send()不添加换行对应
'''
expect(pexpect.EOF)期望匹配pexpect进程结束异常，如果没匹配成功则会抛出异常，可以通过匹配异常，让异常不在终端显示。
返回0，表匹配成功
'''
s.expect(pexpect.EOF)
s.before.decode()                               #参考下文before/after/match
s.close()

```

before/after/match：当expect()匹配到关键字之后，系统会自动给这三个变量赋值，通过这三个变量可以获取子程序运行输出。 before：保存了到匹配到关键字为止，缓存里面已有的所有数据。也就是说如果缓存里缓存了100个字符的时候匹配到了关键字，那before就是除了匹配到的关键字之外的所有字符。 after：保存了匹配到了关键字。 * match：保存的是匹配到的正则表达式的实例，和上面的after相比一个是匹配到的字符串，一个是匹配到的正则表达式实例。

匹配输出：
\x1b[1;31m==== AUTHENTICATING FOR org.freedesktop.systemd1.manage-units ===\r\n
\x1b[0mAuthentication is required to start 'docker.service'.\r\n
Authenticating as: ubuntu\r\n
Password: \r\n
\x1b[1;31m==== AUTHENTICATION COMPLETE ===\r\n
\x1b[0m

**interact()方法**
interact()表示将终端控制权交给用户（或者说将标准输入交给用户）。通常情况下Pexpect会接管所有的输入和输出，如果需要用户介入完成部分工作的时候，interact()就派上用场了。

```
# 让出控制权给用户
process.interact()
# 通过设置escape_character的值定义返回码，当用户输入此值后，会将控制权重新交给pexpect
process.interact(escape_character='\x1d', input_filter=None, output_filter=None)
```

### asyncio模块
asyncio使用事件循环驱动的协程实现并发。
[asyncio官方文档](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.create_task)
async & awit 关键字在Python3.5版本中正式引入，基于他编写的协程代码其实就是 上一示例 的加强版，让代码可以更加简便。

Python3.8之后 @asyncio.coroutine 装饰器就会被移除，推荐使用async & awit 关键字实现协程代码。

### re模块

#### 正则表达式语法

- `(?P<name>…)`
与常规的圆括号类似，但分组所匹配到了子字符串可通过符号分组名称 name 来访问。 分组名称必须是有效的 Python 标识符，并且在 bytes 模式中它们只能包含 ASCII 范围内的字节值。 每个分组名称在一个正则表达式中只能定义一次。 一个符号分组同时也是一个编号分组，就像这个分组没有被命名过一样。

命名组合可以在三种上下文中引用。如果样式是 `(?P<quote>['"]).*?(?P=quote)` （也就是说，匹配单引号或者双引号括起来的字符串)：

**注意** 在 `(?P=quote)` 中引用的分组只能匹配定义时所捕获的具体字符串,而不是定义的正则表达式

|引用组合 "quote" 的上下文|引用方法|
|------------------------|-------|
|在正则式自身内|`(?P=quote)` 或 `\1`|
|处理匹配对象 m|`m.group('quote')` 或 `m.end('quote')` (等)|
|传递到 `re.sub()` 里的 `repl` 参数中| `\g<quote>` 或 `\g<1>` 或 `\1`

**注意** 在 3.12 版本发生变更: 在 bytes 模式中，分组 name 只能包含 ASCII 范围内的字节值 (b'\x00'-b'\x7f')。

#### 正则表达式标志

- `re.A` / `re.ASCII`, 使 \w, \W, \b, \B, \d, \D, \s 和 \S 执行仅限 ASCII 匹配而不是完整的 Unicode 匹配
- `re.M`/`re.MULTILINE`: 指定之后, 模式字符 `^` 将匹配字符串的开始和每一行的开头(紧随在换行符之后); 而模式字符 `$` 将匹配字符串的末尾和每一行的末尾(紧接在换行符之前); 默认下, `^` 只匹配字符串的开头, `$` 只匹配字符串的末尾(如果末尾存在换行则匹配在换行之前)
- `re.S`/`re.DOTALL`: 使 `.` 匹配任意字符, 包括换行符, 无此标志则默认匹配除换行之外的字符
- `re.U`/`re.UNICODE`: 在 Python 3 中, str 模式默认将匹配 Unicode 字符, 此选项多余, 仅用于向下兼容

### 格式化字符串的规格
```py
format_spec     ::=  [[fill]align][sign]["z"]["#"]["0"][width][grouping_option]["." precision][type]
fill            ::=  <any character>
align           ::=  "<" | ">" | "=" | "^"
sign            ::=  "+" | "-" | " "
width           ::=  digit+
grouping_option ::=  "_" | ","
precision       ::=  digit+
type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
```
**注意** sign仅对数字有效，'z' 选项浮点类型有效(负0转换到正0，3.11添加)
**注意** 未显式给出对齐方式，width 字符的 '0'字符将为数字类型启用保留正负号的零填充

### python程序退出机制
1. 在交互式py解释器中，会自动导入site模块，内置quit()和exit()函数，其退出操作仅抛出SystemExit异常
2. 在sys模块中，存在sys.exit函数，引发一个 SystemExit 异常，表示打算退出解释器。接受一个表退出状态的整数，在大多数系统要求该值的范围是 0--127，否则会产生不确定的结果。
3. os._exit 以状态码 n 退出进程，不会调用清理处理程序，不会刷新 stdio，等等。只应在 os.fork() 所生成的子进程中使用。(在不同平台上可能不可用)
4. atexit(退出处理器),定义了清理函数的注册和取消注册函数. 被注册的函数会在解释器正常终止时执行. atexit 会按照注册顺序的==逆序==执行

### python脚本中使用pip安装包
要知道我们可以使用`python -m pip install <packages_name>`安装需要的包，本质上就是调用pip模块的__main__脚本,我们可以查看pip模块的__init__文件，发现在我们导入pip时，提供了一个main方法
```
# pip的__init__.py
def main(args: Optional[List[str]] = None) -> int:
    """This is an internal API only meant for use by pip's own console scripts.

    For additional details, see https://github.com/pypa/pip/issues/7498.
    """
    from pip._internal.utils.entrypoints import _wrapper

    return _wrapper(args)
```

这个方法和使用python -m选项时调用__main__文件中执行是一致的
```
# pip的__main__.py
if __name__ == "__main__":
    # Work around the error reported in #9540, pending a proper fix.
    # Note: It is essential the warning filter is set *before* importing
    #       pip, as the deprecation happens at import time, not runtime.
    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, module=".*packaging\\.version"
    )
    from pip._internal.cli.main import main as _main
    sys.exit(_main())
```
pip._internal.cli.main文件内容
```
# pip._internal.cli.main方法
def main(args: Optional[List[str]] = None) -> int:
    """This is preserved for old console scripts that may still be referencing
    it.

    For additional details, see https://github.com/pypa/pip/issues/7498.
    """
    from pip._internal.utils.entrypoints import _wrapper

    return _wrapper(args)
```
    
```
import pip
pip.main(['install',win10toast'])
```

### python类型提示
使用typing模块中类型进行的类型声明，可以在python文件运行时会进行类型检查，若不匹配则会抛出TypeError错误，或者进行静态检查发现代码错误、获取代码智能提示等

**注意** ：普通的python类型如list，dict等，在typing模块中为首字母大写的驼峰命名。

#### Type Annotations与Type Comments的区别
Type Annotations类型注解形如
```
def func(a:int) -> None:
    pass
```

Type Comments以文档字符串的形式出现，一般在python2版本不支持类型注解时使用，形如
```
# 该comments遵循google规范
def func(a:int) ->None:
    """_summary_ 
    
    Args:
        a (int): _description_
    """
    pass
```
#### Union联合类

`Union[<python_type>,...]`,表数据类型只能为[]中列出的类型

#### 为模块二进制扩展pyd编写存根pyi文件

这里推荐一个`pybind11_stubgen`和`mypy`工具，可以自动生成pyi文件，结合vscode的Pylance可以为python二进制扩展提供代码提示功能。如open3d、opencv之类的库。
[pybind11_stubgen](https://hub.nuaa.cf/sizmailov/pybind11-stubgen)

如：`python -m pybind11_stubgen open3d`
会在工作目录的生成stubs文件夹，其内存放分析open3d生成的存根文件，复制到模块安装目录获取提示。

#### mypy验证py文件hint正确性

mypy检查你的 program.py 文件并打印出它发现的任何错误。其将**静态地检查**你的代码：这意味着它将在不运行您的代码的情况下检查错误，就像 linter 一样。

> 如果你使用其他三方库，并且三方库已有类型声明，mypy会通过它包含的类型提示来类型检查您对该库的使用情况。

**注意** 如果第三方库没有类型提示，你可以通过python官方维护的存根集合typeshed来获取库的纯存根文件。如：`python3 -m pip install types-PyYAML types-requests`。发行版的存根包通常被命名为 `types-<distribution>` 。并且**分发名称可能与您导入的包的名称不同**。例如， types-PyYAML 包含包的 yaml 存根。

##### mypy相关的其他工具
|工具           |   用途                    |
|--------------|---------------------------|
|使用mypy      |     如果你只想要类型检查py代码文件|
|使用 stubgen 或 pyright --createstub 代替  |       生成存根        |
|使用 monkeytype|  根据运行应用程序或测试套件生成存根(即在大型项目中，运行时收集类型信息)|
|使用 retype 或 libcst |    将存根应用于代码以生成内联类型（即根据pyi文件添加py文件中Type Annotations）|
|使用 stubtest|    进行自动存根测试（即存在py文件和对应pyi文件，检查pyi文件的正确性）     |

> LibCST 在抽象语法树 （AST） 和传统具体语法树 （CST） 之间创建折衷方案。通过仔细地重新组织和命名节点类型和字段，我们创建了一个外观和感觉都像 AST 的无损 CST。可以重新更改源代码文件。(libcst文档)[https://libcst.readthedocs.io/en/latest/why_libcst.html]

### python字节码
CPython 使用一个基于栈的虚拟机。使用三种类型的栈：

1. 调用栈(call stack)。这是运行 Python 程序的主要结构。它为每个当前活动的函数调用使用了一个东西 —— "帧(frame)"，栈底是程序的入口点。每个函数调用推送一个新的帧到调用栈，每当函数调用返回后，这个帧被销毁。
2. 计算栈(evaluation stack) （也称为 数据栈(data stack)）。这个栈就是 Python 函数运行的地方，运行的 Python 代码大多数是由推入到这个栈中的东西组成的，操作它们，然后在返回后销毁它们。
3. 块栈(block stack)。它被 Python 用于去跟踪某些类型的控制结构：循环、try / except 块、以及 with 块，全部推入到块栈中，当你退出这些控制结构时，块栈被销毁。这将帮助 Python 了解任意给定时刻哪个块是活动的，比如，一个 continue 或者 break 语句可能影响的块。


#### 使用dis.dis反汇编python对象
dis.dis用于 反汇编类、方法、函数和其他编译过的对象

> 代码对象在**函数**中可以以属性 __code__ 来访问，并且携带了一些重要的属性：
- co_consts 是存在于函数体内的任意实数的元组
- co_varnames 是函数体内使用的包含任意本地变量名字的元组
- co_names 是在函数体内引用的任意非本地名字的元组

```
31           0 LOAD_GLOBAL              0 (print)
            2 LOAD_CONST               1 ('parent new size')
            4 CALL_FUNCTION            1
            6 POP_TOP
```
- LOAD_GLOBAL 0：告诉 Python 通过 co_names （它是 print 函数）的索引 0 上的名字去查找它指向的全局对象，然后将它推入到计算栈
- LOAD_CONST 1：带入 co_consts 在索引 1 上的字面值，并将它推入（索引 0 上的字面值是 None，它表示在 co_consts 中，因为 Python 函数调用有一个隐式的返回值 None，如果没有显式的返回表达式，就返回这个隐式的值 ）。
- CALL_FUNCTION 1：告诉 Python 去调用一个函数；它需要从栈中弹出一个位置参数，然后，新的栈顶将被函数调用。

**注意** 原始的字节码是非人类可读格式的字节串，你可以在代码对象上的co_code 属性查看。如果想要尝试手工反汇编一个函数时，你可以使用 dis.opname 查看字节码指令名和16进制表示字节值的对应关系。如：
```
# FooParent 的 __new__方法字节码如下
FooParent.__new__.__code__.co_code
b't\x00d\x01\x83\x01\x01\x00t\x01\x83\x00\xa0\x02|\x00\xa1\x01}\x03d\x02|\x03_\x03|\x03S\x00'
# 使用dis.dis反汇编得到
0 LOAD_GLOBAL              0 (0)
2 LOAD_CONST               1 (1)
4 CALL_FUNCTION            1
6 POP_TOP
8 LOAD_GLOBAL              1 (1)
10 CALL_FUNCTION            0
12 LOAD_METHOD              2 (2)
14 LOAD_FAST                0 (0)
16 CALL_METHOD              1
18 STORE_FAST               3 (3)
20 LOAD_CONST               2 (2)
22 LOAD_FAST                3 (3)
# 对应测试
chr(dis.opname.index('LOAD_GLOBAL'))
't'
dis.opname[ord('d')]
'LOAD_CONST'
```

#### 使用inspect/__code__获取函数的code解析函数属性

```python
import inspect

def my_function(a, b, c=None):
    pass
# 获取函数的参数
params = inspect.signature(my_function).parameters
params = my_function.__code__.co_varnames
print(params)
```

### 元类type
python中元类用于控制类的创建。

#### 示例

##### 元类__call__实现单例
```python
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
```

### 属性描述符和@property
可以查看一下 `@property` 的参考原型, `property`也具有`__get__`/`__set__`方法, 是由cpython内置实现的属性描述符

## 魔法方法(特殊方法)

> 参考资源:
- [py特殊方法文档](https://docs.python.org/zh-cn/3.9/reference/datamodel.html)

## 异常处理
python中异常可分为系统退出异常和普通异常(非致命)

- `BaseException` 是所有异常的共同基类。其中的一个子类 `Exception` ，是所有非致命异常的基类。其他非 `Exception` 的子类异常通常不被处理，因为它们被用来指示程序应该终止。列如: 由 `sys.exit()` 引发的 `SystemExit` ，以及当用户希望中断程序时引发的 `KeyboardInterrupt` 
- `Exception` 可以被用作通配符，捕获（几乎）一切。然而，好的做法是，尽可能具体地说明我们打算处理的异常类型，并允许任何意外的异常传播下去。

## warn警告处理
1. 使用filterwarnings对警告进行拦截处理，如下:
```python
import warnings
warnings.filterwarnings('error')  # 将警告转为error
warnings.filterwarnings('ignore')  # 忽略警告
```
2. 使用warnings提供的捕获上下文管理处理 ` warnings.catch_warnings(record=True)` 
3. 在python运行时加入 `-W` 选项指定过滤器

## logging日志

### 使用 dictconfig
`logging.config.dictconfig` 用于从字典获取日志记录配置

> 示例如下:
```py
dictConfig = {
    'version': 1,
    'disable_existing_loggers': False,  # 是否要禁用任何现有的非根日志记录器
    'incremental': False,  # 是否在现有配置上新增
    'formatters': {
        'console': {
            'format': '%(asctime)s-%(name)s-%(lineno)s-%(levelname)s: %(message)s'
        },
        'thread': {
            'format': '%(asctime)s-%(thread)d-%(threadName)s-%(name)s-%(lineno)s-%(levelname)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'task_record': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': join(LOG_OUTPUT_DIR, 'task_record.log'),
            'mode': 'w',
            'encoding': 'utf-8',
            "formatter": "thread",
            'delay': True  # 延时写入(可以在目录不存在时完成配置)
        },
    },
    "root": {
        "level": "DEBUG",  # handler中的level会覆盖掉这里的level
        "handlers": ["console"],
    },
    'loggers': {
        '': {
            'handlers': ['default', 'file'],
            'level': 'DEBUG',
            'propagate': True  # 日志记录器的传播设置, True为传播到更高级别
        }
    }
}
```

## 多进程通信 IPC(Inter Process Communication)

### 多进程分类
1. 上下文进程
2. 独立父子进程

### 多进程创建方式

1. `subprocess` 模块
2. `pyqt`的`QProcess`
3. `multiprocessing`
4. `os`系统调用

### 消息传递方式

1. window下管道文件 `win32pipe.CreateNamedPipe`
2. posix下fifo，`os.mkfifo()`
3. socket套接字

### window管道
Windows 中，命名管道的名称是全局唯一的，因此无论你在什么文件路径下使用相同的管道名称 `\\.\pipe\my_pipe`，它们都会指向同一个命名管道。

**关键点**
1. **全局唯一性**：命名管道的名称是全局唯一的。当你创建一个命名管道时，使用的名称在系统范围内是唯一的。这意味着，任何进程都可以通过相同的名称连接到该管道，与工作路径无关

2. **路径格式**：命名管道的名称通常以 `\\.\pipe\` 开头，后面跟着管道的名称。这个格式告诉 Windows 这是一个命名管道，而不是一个文件路径。

3. **连接到管道**：如果两个不同的进程都使用 `\\.\pipe\my_pipe` 来连接，那么它们实际上是在连接同一个管道。这使得进程间通信变得简单，因为你可以在多个进程之间共享同一个管道

#### window管道其他操作
使用 `win32pipe.PeekNamedPipe` 函数来检查管道中是否有数据可读

### 示例
```python
import signal
import socket
from selectors import DefaultSelector, EVENT_READ
from http.server import HTTPServer, SimpleHTTPRequestHandler

interrupt_read, interrupt_write = socket.socketpair()

def handler(signum, frame):
    print('Signal handler called with signal', signum)
    interrupt_write.send(b'\0')
signal.signal(signal.SIGINT, handler)
interrupt_write.fileno()

def serve_forever(httpd):
    sel = DefaultSelector()
    sel.register(interrupt_read, EVENT_READ)
    sel.register(httpd, EVENT_READ)

    while True:
        for key, _ in sel.select():
            if key.fileobj == interrupt_read:
                interrupt_read.recv(1)
                return
            if key.fileobj == httpd:
                httpd.handle_request()

print("Serving on port 8000")
httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
serve_forever(httpd)
print("Shutdown...")
```

## 报错信息示例
```python
import matplotlib.pyplot as plt
int() argument must be a string, a bytes-like object or a number, not 'KeyboardModifie
```
> 请升级到 mpl >=3.6.2 或将 pyside 降级到 <6.4.0。