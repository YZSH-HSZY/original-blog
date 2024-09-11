# python测试框架
python内置unitest单元测试框架、doctest文档测试框架，也有一些三方的适用于python的测试框架

## unitest
unittest 是受到 JUnit 的启发，与其他语言中的主流单元测试框架有着相似的风格。其支持测试自动化，配置共享和关机代码测试。支持将测试样例聚合到测试集中，并将测试与报告框架独立。

## doctest
doctest 模块寻找像Python交互式代码的文本，然后执行这些代码来确保它们的确就像展示的那样正确运行，有许多方法来使用doctest：
1. 通过验证所有交互式示例仍然按照记录的方式工作，以此来检查模块的文档字符串是否是最新的。
2. 通过验证来自一个测试文件或一个测试对象的交互式示例按预期工作，来进行回归测试。
3. 为一个包写指导性的文档，用输入输出的例子来说明。 取决于是强调例子还是说明性的文字，像 "文本测试 "或 "可执行文档 "的风格。

## pytest
pytest 框架使编写小型、可读测试变得容易，并且可以扩展以支持应用程序和库的复杂功能测试。
**pytest requires**: Python 3.8+ or PyPy3.

(官方文档)[https://docs.pytest.org/en/8.2.x/]

### 使用

1. 测试文件以test_开头（以_test结尾也可以）
2. 测试类以Test开头，并且不能带有 init 方法（class名不满足该条时，将跳过所有成员test方法）
3. 测试函数以test_开头
4. 断言使用基本的assert即可

**注意** 
- pytest 将运行当前目录及其子目录中所有 `test_*.py` 或 `*_test.py` 形式的文件。它遵循标准的测试发现规则。
- pytest 运行指定py文件时，会侦测以test_开头的测试函数(可以使用Test类进行测试函数组管理，通过类属性来进行所有测试函数的初始化)
- 在类class中对测试进行分组时需要注意的一点是，每个测试都有一个唯一的类实例。让每个测试共享相同的类实例将非常不利于测试隔离，并且会促进不良的测试实践。

#### setup/teardown控制测试环境
```python
def setup_module():
    print("=====整个.py模块开始前只执行一次=====")

def teardown_module():
    print("=====整个.py模块结束后只执行一次=====")

def setup_function():
    print("===每个函数级别用例开始前都执行setup_function===")

def teardown_function():
    print("===每个函数级别用例结束后都执行teardown_function====")

class TestCase():
    def setup_class(self):
        print("====整个测试类开始前只执行一次setup_class====")

    def teardown_class(self):
        print("====整个测试类结束后只执行一次teardown_class====")

    def setup_method(self):
        print("==类里面每个用例执行前都会执行setup_method==")

    def teardown_method(self):
        print("==类里面每个用例结束后都会执行teardown_method==")

    def setup(self):
        print("=类里面每个用例执行前都会执行setup=")

    def teardown(self):
        print("=类里面每个用例结束后都会执行teardown=")
```

#### 异常抛出测试
1. 断言抛出异常
```python
def f():
    raise SystemExit(1)
def test_mytest():
    with pytest.raises(SystemExit):
        f()
```
2. 断言异常组包含指定异常
`assert excinfo.group_contains(RuntimeError)`

#### 跳过指定测试
```python
@pytest.mark.skip(reason='跳过原因')
def test_connect():
    pass
```
> 也可指定跳过条件如 `@pytest.mark.skipif(conn.__version__ < '0.2.0', reason='not supported until v0.2.0')`

#### 指定测试用例顺序

1. 通过pytest-ordering包，对于同一指定顺序，按先后执行
```python
@pytest.mark.run(order=1)
def test_first():
    print("用例test_first")
    time.sleep(1.5)
# 指定在哪一个函数之后运行
@pytest.mark.run(after='test_fist')
def test_2():
    pass
```
2. 通过`Collection hooks`是pytest的一个特性，允许在测试用例收集阶段进行自定义操作。可以通过实现`pytest_collection_modifyitems`钩子来控制测试用例的执行顺序。

#### pytest测试符号意义

- `.` 表测试完成
- `s` 表测试被跳过(SKIPPED)

### 选项

#### 显示print输出
使用选项 `-s` 作为捕获输出快捷键

#### 移除pytest测试开始输出部分
使用选项 `-q` 或 `--quit` 仅显示测试结果

#### 显示可用的内置测试工具/函数参数
1. `pytest --fixtures ` 显示可用测试工具/函数参数
2. `pytest --fixtures -v` 显示所有测试工具（包含隐藏，即带前导_）

```python
# content of test_tmp_path.py
def test_needsfiles(tmp_path):
    print(tmp_path)
    assert 0
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, dash_br, dash_duo, dash_duo_mp, dash_multi_process_server, dash_process_server, dash_thread_server, dashjl, dashjl_server, dashr, dashr_server, diskcache_manager, doctest_namespace, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.
```
### 固件fixtures
固件可以直接定义在各测试脚本中，其他测试函数可以直接在参数中传递固件，pytest将会自动调用固件并将结果赋给固件参数
```python
@pytest.fixture()
def postcode():
    return '010'
```
> 如果想要固件fixtures复用,pytest使用文件 conftest.py 集中管理固件,作用域为其所在的目录和子目录. pytest会自动调用conftest.py

#### fixtures的前后处理
使用python的yield将fixtures转化为一个生成器,yield前的代码部分会在测试前执行,yield后的部分则在测试结束后执行.

#### fixtures的作用域
使用fixtures可以抽离出重复的工作以方便复用,为了更精细化控制固件,可以使用作用域来进行指定固件的使用范围.

在定义固件时,通过 `scope` 参数声明作用域,可选项有:

- `function`: 函数级,每个测试函数都会执行一次固件;
- `class`: 类级别,每个测试类执行一次,所有方法都可以使用;
- `module`: 模块级,每个模块执行一次,模块内函数和方法都可使用;
- `session`: 会话级,一次测试只执行一次,所有被找到的函数和方法都可用.

**注意** 对类使用作用域,需要使用 `pytest.mark.usefixtures` 装饰器,函数和方法即可使用该装饰器(也可使用传递参数)

#### fixtures自动执行
固件自动执行，可以在定义时指定 autouse 参数

#### 查看固件执行顺序
使用 `--setup-show` 选项

### pytest的Configuration配置文件

配置文件位于仓库的根目录中,子目录下的测试文件也会共享同一配置文件。

使用 `pytest -h` 显示已安装插件注册的命令行和配置文件设置

**注意** 可以在子目录下创建自己的`pytest.ini`和`conftest.py`文件以覆盖根目录配置。或者使用`--ignore`选项：在运行pytest时，忽略特定的文件或目录。

#### pytest.ini

**注意** pytest.ini文件优先于其他文件，即使为空也是如此。

##### 在ini配置文件中设置额外的命令行选项
`addopts = --setup-show --html=./report/report.html --self-contained-html`

### 在测试失败时进入pdb
`pytest -x --pdb` # 第一次失败时下降到 PDB，然后结束测试会话
`pytest --pdb --maxfail=3` # 前三次失败都下降到 PDB

### pytest测试报告（htmlReport）
安装`pytest-html`
使用`pytest --html=./report/report.html`指定输出测试报告位置

#### 将样式保存到html文件中
使用选项 `--self-contained-html`

#### 流式生成测试报告（即在每一个测试完成后生成，而不是全部完成后在生成）
```ini
[pytest]
generate_report_on_test = True
```