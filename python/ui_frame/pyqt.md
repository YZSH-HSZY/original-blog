# pyqt

[github pyqt5示例](https://github.com/PyQt5/PyQt)

## qt资源管理系统

为了防止打包发布pyqt程序时丢失资源文件，qt推出了`qt资源管理系统`。与直接读取资源文件相比，qt资源管理系统可以对资源进行组管理并使用资源别名提高程序健壮性，借助资源编译rcc可以将资源文件编译进可执行文件中。如
```python
QPixmap("Icons/Python_icon.ico")  # 直接读取资源文件
QPixmap(":/<资源组名>/<资源文件别名>")  # 借助qt资源管理系统读取资源文件
```

- Qt 资源系统（The Qt Resource System）是一种独立于平台的资源管理器，用于在应用程序的可执行文件中存储二进制文件。对 PyQt 而言，这意味着在 Python 代码中直接以二进制形式存储图标、QSS、长文本翻译等资源文件。使用 Qt 资源管理系统可以有效防止资源文件丢失，对于需要打包发布 的 PyQt 程序尤其实用。

- Qt 资源集合文件（Qt Resource Collection File）一般以 .qrc 作为扩展名保存，故简称 .qrc 文件。其文件格式基于 XML，用于将文件系统（硬盘）中的资源文件与 Qt 应用程序关联起来。.qrc 还可以实现为资源分组、设置别名、等功能。

### qt资源系统的使用

在项目中使用 Qt 资源系统，大致分为三个步骤：
1. 编写 .qrc 文件;
2. 使用 rcc 编译资源;
3. 导入与使用;

#### qrc文件

```xml
<RCC>
  <qresource [prefix=<group_name>]>
    <file [alias=<alias_name>]>img/logo_text.png</file>
    <file>img/my.ico</file>
    <file>img/qt.png</file>
  </qresource>
</RCC>
```
**注意**
- 资源文件的路径相对于`.qrc`文件,是相对路径
- 在qresource标签内使用前缀prefix进行分组
- 在file内为使用alias属性为资源创建别名

#### rcc编译

Qt 提供了 Resource Compiler Command Tool（简称 rcc），用于在构建过程中将资源嵌入 Qt 应用程序。对于 PyQt，也有对应版本的 rcc 工具，用于将 .qrc 中指定的资源文件数据编译至 Python 对象。

- 使用`pyrcc5`命令 或 `python -m PyQt5.pyrcc_main`运行脚本生成对应资源编译后的py文件
- 生成后的py文件内容包含：
qt_resource_data - 资源文件内容数据
qt_resource_name - 资源文件名称
qt_resource_struct - 资源结构
还有两个函数 qInitResources() 与 qCleanupResources()，分别对应向 Qt 中注册资源与清理资源。
- 在生成的ui文件中会自动import所需的qrc文件(如果ui中使用了qrc中的资源)

## 使用designer设计界面ui文件

designer是qt为了简化界面设计而推出的一款类原型设计工具，你可以直接在designer中设计需要的应用程序原型并预览，保存并生成需要的界面布局ui文件。

- ui文件是一个xml文件，其内以标签的形式定义了样式的布局，可以通过以下方式使用:
  1. `loadUiType(uifile, from_imports=False, resource_suffix='_rc'， import_from='.') ->(表单类，基类)`
  > `loadUiType`会加载Qt Designer .ui文件并返回生成的表单类和Qt基类。
  > Uifile是以.ui为后缀的文件或类似文件的对象。可以选择设置From_imports来生成相对导入语句。目前，这只适用于资源模块的导入。resource_suffix是附加到.ui文件中指定的任何资源文件的basename后的后缀，用于创建pyrcc4从资源文件生成的Python模块的名称。默认值是'_rc'，也就是说，如果.ui文件指定了一个名为foo的资源文件。那么对应的Python模块是foo_rc。Import_from可选地设置为相对导入语句使用的包。默认值是'.'。

  2. pyuic5编译生成ui布局的py文件，`pyuic5 <ui_file> -o <output_py>`

### designer使用示例

#### 设置stylesheet
每个继承qwidget的控件，在designer中均具有stylesheet属性，你可编写样式表来达到自定义的显示效果

#### 设置控件的自定义属性
1. 选择控件
2. 在属性编辑器中，找到"动态属性"（Dynamic Properties）部分
3. 点击"新建"按钮
4. 输入属性名和值

## QSS
QSS为qt支持的stylesheet, 类似于css

### 选择器
QSS支持的选择器常见类型有以下几种:
1. 通配选择 `* {color: red;}`
2. 类型选择(控件的继承基类) `QLabel {font-size: 16pt;}`
3. 类选择(控件的类型) `.QLabel {font-size: 16pt;}`
4. id选择(控件的objectname) `#temp {font-size: 12px;}`
5. 属性选择(控件的objectname) `QLabel[attr="x"] {font-size: 12px;}`
6. 后代选择 `QTabWidget QLabel {font-size: 12px;}`
7. 子选择器 `QbWidget>QLabel {font-size: 12px;}`

## pyqt集成的工具
pyuic5、pyrcc5、pylupdate5

- pyuic5自动转换ui文件到py类文件 `pyuic5 <ui_file> -o <output_py_file>`
  - pyuic5 等同 `python -m PyQt5.uic.pyuic`
- pyrcc5自动转换qrc文件到py文件
    - pyrcc5 等同 `python -m PyQt5.pyrcc_main`
- pylupdate5
  - pylupdate5 等同 `python -m PyQt5.pylupdate_main`

除此之外还有：Qt设计师Designer、Qt助手assistant、Qt国际化工具lupdate等

## qt界面分类

Qt的界面大概分为以下3大类：
1. 主窗口 `QMainWindow`
> 主窗口类，具有特定的布局和功能。包含菜单栏、工具条，菜单、工具下方的空白区域是主部件区域，使用`QMainWindow`，可以快速地构建具有标准布局和功能的应用程序主界面。可以通过`setCentralWidget`接口为`QMainWindow` 设置主部件。
2. 对话框 `QDialog`
> 对话框类，通常用于实现一些特定的功能或操作。有最大化、最小化、关闭按钮，有模态、非模态之分(模态对话框会打断用户的当前操作流程/非模态对话框则不会打断用户操作)。一般用作其他部件的子部件。不能嵌入到其他窗体中。
3. 控件 `QWidget`
> `QWidget`是所有具有可视界面类的基类，也是`QDialog`和`QMainWindow`的基类。这意味着选择`QWidget`创建的界面可以支持各种界面组件，并可以嵌入到其他窗体中。每个窗口部件都是矩形，并且它们按Z轴顺序排列。没有指定父容器时，`QWidget`可作为独立的窗口。常用于开发应用程序的主体部分，或者是作为其他更复杂界面元素的容器。

### QMainWindow组件

`QMainWindow`用于创建主窗口应用程序,包含菜单栏 (QMenuBar)、工具栏 (QToolBar)、状态栏 (QStatusBar)、中央窗口部件 (Central Widget)、停靠窗口 (Dock Widgets)、工具窗口 (Tool Windows)


#### QStatusBar和QToolBar和QMenuBar的区别
1. `QStatusBar`：
- 主要用于显示应用程序的状态信息。
- 通常位于窗口的底部，可以用来显示提示信息、进度条或其他状态相关的信息。
- 适合短暂的信息展示，比如“文件已保存”或“正在加载...”。

2. `QToolBar`：
- 提供一组工具按钮，通常用于快速访问常用功能或命令。
- 可以放置在窗口的顶部、底部或侧边，用户可以自定义工具栏的布局。
- 工具栏中的按钮可以是图标、文本或两者的组合，适合频繁使用的操作，比如“新建”、“打开”、“保存”等。

3. `QMenuBar`：
- 用于创建菜单，通常位于窗口的顶部。
- 包含多个菜单项，每个菜单项可以展开显示子菜单。
- 适合组织应用程序的功能，用户可以通过菜单访问各种命令和选项，比如“文件”、“编辑”、“帮助”等。
  

## qt信号和槽机制
qt使用信号和槽机制来替代传统ui编程的事件和callback操作，

1. 使用connect宏实现信号-槽开发,(qt5以下版本)
2. 使用connect函数实现信号-槽开发。
3. 使用lambda函数实现信号-槽开发。

**注意** 信号一般定义到类属性上，作为类属性的时候，信号是一个`unbound signal`，只有在将信号作为类实例的属性引用时，`PyQt5` 才会自动将实例绑定到信号以创建绑定信号`bound signal`，才能调用`connecet`、`disconnect`、`emit`方法。

### pyqtSignal创建

`PyQt5.QtCore.pyqtSignal(types[, name[, revision=0[, arguments=[]]]])`

- `types` – 定义 C++ 信号签名的类型。每个类型可能是 Python 类型对象，也可能是 C++ 类型名称的字符串。或者，每个可能是类型参数的序列。在这种情况下，每个序列定义了不同信号重载的签名。第一个重载将是默认的。
- `name` – 信号的名称。如果省略，则使用类属性的名称。这只能作为关键字参数给出。
- `revision` – 用于向 QML 导出的信号的修订。这只能作为关键字参数给出。
- `arguments` – 信号的参数序列，该序列被导出到 QML。这只能作为关键字参数给出。

> 当定义了类型types时，在通过emit触发信号时，需要进行相应的参数传递.如果以列表的形式给出则支持重载，如：`pyqtSignal([int], [str])`

### pyqt槽函数

- 内置槽函数,如`close`等
- 运行时连接函数(具有动态开销),`object.signal.connect(func)`
- 装饰器`@pyqtSlot()`自动连接,装饰函数名格式为`on_<obj_name>_<signal_name>`
    > 前提是`QtCore.QMetaObject.connectSlotsByName(QObject)`已执行

### pyqt重载信号的连接
`sign_name[int, str].connect(slot)`

## 事件循环机制

qt使用事件驱动模型的来进行ui逻辑和数据处理的分离,对于

## gui模块

Qt GUI模块提供了用于窗口系统集成、事件处理、OpenGL和OpenGL ES集成、2D图形、基本成像、字体和文本的类。这些类由Qt的用户界面技术在内部使用，但也可以直接使用，例如使用低级OpenGL ES图形API编写应用程序。 

> Qt GUI模块中最重要的类是`QGuiApplication`和`QWindow`。想要在屏幕上显示内容的Qt应用程序必须使用他们。
> - QGuiApplication 包含主事件循环，在其中处理和调度来自窗口系统和其他源的所有事件。它还处理应用程序的初始化和终结。
> - QWindow 类表示基础窗口系统中的一个窗口。它提供了许多虚拟功能来处理来自窗口系统的事件 （QEvent），例如触摸输入、曝光、焦点、击键和几何更改。

### 2D Graphics
Qt GUI模块还包含2D图形、图像、字体和高级排版的类。

1. 2D图形：使用曲面类型`QSurface::RasterSurface`创建的QWindow可以与`QBackingStore`和`QPainter`（Qt高度优化的2D矢量图形API）结合使用。`QPainter` 支持绘制线条、多边形、矢量路径、图像和文本。有关详细信息，请参阅绘制系统和栅格窗口示例。
2. 图像：Qt可以使用`QImage`和`QPixmap`类加载和保存图像。默认情况下，Qt支持最常见的图像格式，包括JPEG和PNG等。用户可以通过 `QImageIOPlugin` 类添加对其他格式的支持。有关详细信息，请参阅读取和写入图像文件。
3. 字体和高级排版：Qt 中的排版是通过 `QTextDocument` 完成的，它使用 `QPainter` API 和 Qt 的字体类（主要是 `QFont`）。应用程序更喜欢低级 API `QRawFont` 和 `QGlyphRun` 等类去处理文本和字体。

### 硬件加速
Qt的硬件渲染接口是使用硬件加速图形API的抽象，例如OpenGL、OpenGL ES、Direct3D、Metal和Vulkan。

与直接使用 OpenGL 或 Vulkan 渲染到 QWindow 的方法相比，`QRhi` 和其它相关类提供了一个可移植的、跨平台的 3D 图形和计算 API，并辅以着色器调节和转译管道。这样一来，应用程序就可以避免直接依赖单个 API，在某些情况下，还可以避免依赖特定于供应商或平台的 3D API。

### 3d矩阵和矢量
Qt GUI模块还包含一些数学类，以帮助进行与3D图形相关的最常见数学运算。这些类包括 QMatrix4x4、QVector2D、QVector3D、QVector4D 和 QQuaternion。

## QT内部的MVC模型
QT内部有一套专门的显示数据界面的MVC封装,即Model-View-Delegate(模型-视图-代理)

## 示例

### 让部件填充QWidget

1. 对于`QMainWindow`可以通过`setCentralWidget`设置中心控件
2. 对于`QWidget`可以指定控件的大小策略Size Policies
3. 或者为控件添加一个布局管理器(如: 垂直布局QVBoxLayout)，此时会使用布局指定的大小策略

**注意** `QMainWindow` 和 `QWidget` 的填充方法略有区别，注意区分！

**注意** 填充本质上是将部件的布局显示托管给布局管理器，如果你发现部分Widget无法跟随窗口扩大而扩大，请检查该部件有无部件管理器(区分`layout.addWidget`和构造方法`layout(parent=widget)`)

### 使用`QProcess`调用子进程调用py脚本,而不是`subprocess.Popen`

- 通过`subprocess.Popen`调用py脚本,如果需要和子进程进行交互时,极为麻烦,如下:
```python
# 通过文件做输出的桥接终端,因为
#   1. 模拟io中StringIO和BinaryIO均无fileno操作,实例化Popen会报错
#   2. 直接使用subprocess.PIPE有阻塞问题(process.stdout.readable()判断有无缓存值失效)
out_fp = open(join(UiShow.exec_file_path, CACHE_DIR, f'out_{self.txt}.txt'), 'wb')
self.process = subprocess.Popen(
    ['python', 'Get_SPI_BOOT.py'],
    stdin=subprocess.PIPE, stdout=out_fp.fileno(), stderr=out_fp.fileno())
# 在另一部分通过QTimer轮询文件内容,并传递部件显示
with open(join(UiShow.exec_file_path, CACHE_DIR, f'out_{self.txt}.txt'), 'rb') as fp:
    self.ptr_source_item.listWidget().show_widget.sig_port_get_stdout.emit(
        self.txt, fp.read().decode('gbk'))
```
- 直接使用`QProcess`创建子进程就较为方便,

**注意** 使用QProcess与子进程进行交互，在捕获子进程的输出时，请在子进程中调用sys.stdout.flush()

### QAction介绍

QAction是一个Qt中用于描述菜单项的类，一个QAction对象可以关联多个菜单项，例如同一个QAction对象可以关联主菜单、工具栏、context菜单三种菜单项。

QAction对象提供了一些有用的信号，如`triggered`信号，`toggled`信号等，通过connect信号槽可以实现菜单项的逻辑处理。

QAction对象在pyqt中可以通过`QAction`构造函数创建，例如`QAction("Open", self)`，也可以使用`QMenu.addAction`方法创建菜单项，例如`menu.addAction("Open")`。

QAction对象可以设置图标、文本、状态等属性，例如`action.setIcon(QIcon("open.png"))`、`action.setText("Open File")`、`action.setCheckable(True)`等。

**QAction对象可以在多个菜单中共享相同的逻辑处理**，例如在主菜单、工具栏、-context菜单中共享同一个QAction对象。

#### QAction和ToolButton

在QToolbar中可以通过addAction添加QAction对象，也可以通过addWidget添加ToolButton对象，通过ToolButton的defaultAction()可以获取对应的QAction对象

### 设置`QComboBox`下拉列表的提示文本

1. 通过设置`QComboBox`为可编辑并使用lineEdit设置提示文本
```python
combo_box.setEditable(True) 
combo_box.lineEdit().setPlaceholderText("Search")
```
2. 通过`QAbstractProxyModel`托管`QComboBox`的数据model
```python
def copy_combo_box_model(combo_box: QComboBox) -> QStandardItemModel:
    model_copy = QStandardItemModel()
    model = combo_box.model()
    for i in range(model.rowCount()):
        for j in range(model.columnCount()):
            item = model.item(i, j)
            item_copy = QStandardItem(item.text())
            item_copy.setData(item.data())
            model_copy.setItem(i, j, item_copy)
    return model_copy
class ProxyModel(QAbstractProxyModel):

    """ 代理model，用于给一个model添加一个提示行 """

    def __init__(self, model, placeholderText='---', parent=None):
        super().__init__(parent)
        self._placeholderText = placeholderText
        self.setSourceModel(model)
        
    def index(self, row: int, column: int, parent: QModelIndex = ...) -> QModelIndex:
        return self.createIndex(row, column)

    def parent(self, index: QModelIndex = ...) -> QModelIndex:
        return QModelIndex()

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return self.sourceModel().rowCount()+1 if self.sourceModel() else 0

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return self.sourceModel().columnCount() if self.sourceModel() else 0

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole) -> Any:
        if index.row() == 0 and role == Qt.DisplayRole:
            return self._placeholderText
        elif index.row() == 0 and role == Qt.EditRole:
            return None
        else:
            return super().data(index, role)

    def mapFromSource(self, sourceIndex: QModelIndex):
        return self.index(sourceIndex.row()+1, sourceIndex.column())

    def mapToSource(self, proxyIndex: QModelIndex):
        return self.sourceModel().index(proxyIndex.row()-1, proxyIndex.column())

    def mapSelectionFromSource(self, sourceSelection: QItemSelection):
        return super().mapSelectionFromSource(sourceSelection)

    def mapSelectionToSource(self, proxySelection: QItemSelection):
        return super().mapSelectionToSource(proxySelection)
    
    def headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.DisplayRole):
        if not self.sourceModel():
            return None
        if orientation == Qt.Vertical:
            return self.sourceModel().headerData(section-1, orientation, role)
        else:
            return self.sourceModel().headerData(section, orientation, role)

    def removeRows(self, row: int, count: int, parent: QModelIndex = ...) -> bool:
        return self.sourceModel().removeRows(row, count -1)
```

### 借助python的属性描述符更改uic自动生成的文件
```python
class PropertyQListWidget:
    def __init__(self, name = None):
        self._store = None
        self._store_name = name
        pass
    def __get__(self, instance, cls):
        # print(locals())
        # print(self._store)
        if self._store is not None: 
            # print('having')
            return self._store
        # print('not having')
        pass
    def __set__(self, instance, set_value):
        # print(locals())
        self._store = set_value
        if isinstance(set_value, QListWidget):
            if self._store_name == 'all_ports':
                self._store = ShowPortListDragListWidget(set_value.parent())
            elif self._store_name == 'living_example':
                self._store = ShowInfoDropListWidget(set_value.parent())
            else: return

            if set_value.parent() is not None:
                set_value.close()
            del set_value
            pass
        # print('self._store', end='')
        # print(self._store)
        pass
```

### QDoubleSpinBox更改值响应，仅在完成输入后触发(避免每次输入时触发槽操作)

- 使用 `editingFinished` 信号，此时只会在按下回车或者失去焦点时，触发事件槽
- 使用 `valueChanged` 信号，通过 `setKeyboardTracking(False)` 禁用输入时按键追踪

### QTimer的计时方式

以下是一个简易的QTimer示例
```python
self._time = QTimer()
self._time.start(1000)
self._time.setSingleShot(False)  # 设置是否仅触发一次
def p():
    print(datetime.now(), int(QThread.currentThreadId()), "timer")
    time.sleep(3)
self._time.timeout.connect(p)
```
**注意** 定时器start指定的时间计时是在对应的timeout槽函数执行完毕后开始计时,因此这段代码每4s执行一次

### 继承QThread和moveToThread的区别

采用moveToThread方式，会开一个子线程事件循环，此对象的相应方法可在另一线程中执行

**注意** moveToThread托管的对象存在线程上下文, 如果实例化时在ui线程绑定sig和slot, 那么对应的槽函数将会在ui线程而非子线程中进行。
**注意** 子线程在同一个时刻只执行一个耗时的操作，如果有多个耗时的操作同时执行，仍然会阻塞在子线程中。

```python
import sys
import threading
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from yaml import emit

class AsyncThread(QObject):
    sig_t = pyqtSignal()
    finished = pyqtSignal()
    EXIT_SIGN: bool = False

    def __init__(self):
        super().__init__()
        # self.sig_t.connect(self.mock_sleep_btn)  # 在此处绑定信号,对应槽在ui线程中执行

    def async_task(self):
        self.sig_t.connect(self.mock_sleep_btn)
        # 循环执行时时，其他子线程触发事件被阻塞在事件循环队列里(如mock_sleep_btn)
        while True:
            if self.EXIT_SIGN: 
                self.finished.emit()  # 此信号不提交,子线程的不会自动退出(即quit调用和扩展权交给子线程事件循环的finished信号触发)
                break
        
            print(int(QThread.currentThreadId()), "async_task", threading.get_ident())
            time.sleep(1)
    
    def mock_sleep_btn(self):
        print("mock_sleep_btn", int(QThread.currentThreadId()), threading.get_ident())
        time.sleep(3)
        print("mock_sleep_btn end")

class MovetoThreadPage(QMainWindow):
    sig_j = pyqtSignal()

    def __init__(self, parent=None):
        super(MovetoThreadPage, self).__init__(parent)
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        v = QVBoxLayout(self.centralWidget())
        btn = QPushButton('按钮')
        btn2 = QPushButton('按钮2')
        v.addWidget(btn)
        v.addWidget(btn2)

        print('ui thread id is: ', int(int(QThread.currentThreadId())), threading.get_ident())
        self._thread = QThread()
        self.async_thread = AsyncThread()
        self.async_thread.moveToThread(self._thread)
        # self.async_thread.sig_t.connect(self.async_thread.mock_sleep_btn)
        self.sig_j.connect(self.async_thread.sig_t.emit)
        self._thread.started.connect(self.async_thread.async_task)
        self._thread.finished.connect(self.slot_finish_thread)
        self._thread.finished.connect(self.async_thread.deleteLater)
        self._thread.finished.connect(self._thread.deleteLater)
        # self.async_thread.finished.connect(self._thread.quit)
        self._thread.start()


        # btn.clicked.connect(self.async_thread.sig_t.emit)
        btn.clicked.connect(self.slot_btn_click)
        btn2.clicked.connect(self.slot_btn2_click)

    def slot_finish_thread(self):
        print("thread end", int(QThread.currentThreadId()), threading.get_ident())
    
    def slot_btn2_click(self):
        AsyncThread.EXIT_SIGN = True
        
    def slot_btn_click(self):
        print("click btn thread is: ", int(QThread.currentThreadId()), threading.get_ident())
        self.async_thread.sig_t.emit()  # 在子线程中绑定时,等待子线程事件循环处理(即async_task停止)
        # self.async_thread.mock_sleep_btn()  # 在ui线程中执行
        # self.sig_j.emit()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_widget = MovetoThreadPage()
    main_widget.show()
    sys.exit(app.exec())
```

### 注册全局异常hook,以在程序异常退出时提示用户
```python
def exception_handler(exc_type, exc_value, exc_traceback):
    logging.getLogger('UI').error("Uncaught exception", 
            exc_info=(exc_type, exc_value, exc_traceback))
    QMessageBox.critical(None, 'Error', 
        f'Uncaught exception: {exc_type.__name__}: {exc_value}')

sys.excepthook = exception_handler
```

## qt内部视图变换

### 2d视图变换QGraphicsView

Graphics View图形视图框架主要由三部分组成
1. 视图对象(View) 对应着QGraphicsView类
2. 场景对象(Scene) 对应着QGraphicsScene类
3. 元素对象(Item) 对应着QGraphicsItem类


> Items是一个具体的事物,必须实现paint()接口和boundingRect()接口，paint()负责对元素进行绘制，boundingRect()会返回绘制的图形的边界
> Scene是一个全局的场景,其中定位不会变更,理论上可以无限大。但受限于滚动条,其通过view展示的部分可以通过view.translate变更
> View是软件的用户查看scene的窗口,显示一部分场景scene,用户可以通过view操作可见的item
> 均以左上角为原点

#### QGraphicsItem对象

##### 元素paint的调用
当我们需要自定义绘制图形项，可以重写paint函数来定义场景中如何渲染。可以控制图形项的外观，包括颜色、形状、纹理等。

#### 事件处理顺序
1. 鼠标按下事件 (`mousePressEvent`):
   - 首先在 `QGraphicsView` 中调用。
   - 然后在 `QGraphicsScene` 中调用。
   - 最后在具体的 `QGraphicsItem` 中调用（如果鼠标位置在某个项上）。

2. 鼠标移动事件 (`mouseMoveEvent`):
   - 处理顺序与鼠标按下事件相同。


#### 显示大小示例
`setTransform` 只会更改view,对scene中size无影响,仅有视图的显示效果
`setScale` 会更改QGraphicsItem的大小,同步影响view和scene中显示效果

#### 使用Transform变换item同步更改view和scene中显示

**注意** mapRect的计算方向为右乘(点*矩阵)，例: `QTransform(1,0,0,0,1.5,0,10,20,1).mapRect(QRectF(0,0,6,6))`的结果为`QRectF(10.0, 20.0, 6.0, 9.0)`

**注意** `QPoint`和`QRect`存在四舍五入

#### method
|函数|描述|
|----|----|
|QGraphicsView.translate(dx, dy) |Translates the current view transformation by (dx , dy ).|

#### 子元素QGraphicsItem鼠标事件QGraphicsSceneMouseEvent的pos和scenePos的区别
`pos` 获取的是子元素相对与自身绘制区域`boundingRect`的位置，而`scenePos`则获取的是`QGraphicsItem`所在场景的位置(类似与相对位置)


#### bug

##### 继承于QGraphicsItem的元素，重写paint的绘制更新问题
> 问题描述: 继承于QGraphicsItem的元素，重写paint添加其他绘制项，在场景移动更新时存在旧轨迹并且调用自身`update`或所在场景`update`无效
> 解决方案: 确保绘制的额外图形在绘制区域`boundingRect`中

##### QGraphicsView的更新模式
QGraphicsView的一个属性ViewportUpdateMode，可以通过`setViewportUpdateMode(QGraphicsView::ViewportUpdateMode mode)`设定

> 有五种模式:
- `QGraphicsView::FullViewportUpdate` 全视口更新
- `QGraphicsView::MinimalViewportUpdate` 最小更新
- `QGraphicsView::SmartViewportUpdate` 智能选择
- `QGraphicsView::BoundingRectViewportUpdate` Bounding内更新
- `QGraphicsView::NoViewportUpdate` 不更新
其中默认为QGraphicsView::MinimalViewportUpdate，也就是上例中我们没有进行设置的情况。事实上除了设置为`FullViewportUpdate` 其余四种在超出`BoundingRect`均会有拖尾现象

##### item点击显示的区域框
`shape`/`boundingRect`

##### scene和view中前景绘制drawForeground问题
`def drawForeground(self, painter: QPainter, rect: QRectF):`

##### 自定义boundingRect时item缩放定位偏差问题

##### item的transform默认为E，鼠标拖动item其transform不更新

##### 鼠标位置获取及坐标转换
`QGraphicsTextItem` 鼠标事件的位置相对于自身，请使用`mapToScene`变换到场景scene坐标系
mouseevent转发时注意区分事件的处理对象，不同范围获取的鼠标位置点显示有差异

##### 对view应用Transform变换时平移向量translate无显示效果

1. 在初始化时设置`self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)`启用视图拖放
2. 通过[qtbase仓库qgraphicsview文件](https://github.com/qt/qtbase/blob/v5.12.9/src/widgets/graphicsview/qgraphicsview.cpp)中`ScrollHandDrag`的处理逻辑，自己实现视图移动逻辑



### 鼠标位置获取
1. 相对位置, `event.pos()`
2. 绝对位置，`QCursor.pos()` / `event.globalPos()`
`
#### 鼠标位置变换
1. `main_widget.mapToGlobal`
2. `main_widget.mapFromGlobal`

#### 实例

> 问题描述: 以下代码中，内部部件不能填充整个窗口
```python
class Ui_Form(object):      
    def setupUi(self, Form):      
        Form.setObjectName("Form")
        Form.resize(400, 334)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # self.gridLayoutWidget.setGeometry(QtCore.QRect(80, 140, 160, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)

        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.listView = QtWidgets.QListView(self.gridLayoutWidget)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 2, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        ...
```
> 解决方案:
`gridLayoutWidget` 的大小策略设置为 `QSizePolicy.Policy.Expanding`，但没有设置其几何形状，因此它可能没有
正确扩展以填充整个窗口。为了解决这个问题，可以尝试以下几个步骤：
1. 设置 `gridLayoutWidget` 的几何形状：确保 `gridLayoutWidget` 的几何形状能够填充整个 `Form`。你可以使用 `setGeometry` 方法，或者更好的是使用布局管理器来自动处理大小。

2. 使用布局管理器：将 `gridLayoutWidget` 添加到 `Form` 的布局中，而不是手动设置几何形状。可以在 `setupUi` 方法中添加以下代码：
```python
  self.verticalLayout = QtWidgets.QVBoxLayout(Form)
  self.verticalLayout.addWidget(self.gridLayoutWidget)
```

3. 确保 `gridLayout` 的行和列扩展：在 `gridLayout` 中，确保添加的控件的行和列能够扩展。你可以使用 `setRowStretch` 和 `setColumnStretch` 方法。

### 设置layout的比例
1. 在designer中设置 `layoutstretch` 属性，为给布局管理的其他控件设置比例大小
2. 使用控件 `Spacer` 来分割其他显示控件
3. 设置layout的`addStretch`方法添加一个可伸缩的空白控件
4. 使用layout的`setStretch(2, 1)`来给第二个控件设置比例，同一的代码表示

**注意** `Spacer`弹性控件 和 `addStretch`添加的空白控件的区别：
- 弹性控件与其他显示控件计算比例在layoutstretch中相同占用
- 空白控件只计算空白区域的比例占用

### 使用QLibrary加载dll
```python
lib = QLibrary(r"CDFPSK.dll")

# lib.load():判断加载成功与否
```

### View与Widget

`View` 和 `Widget` 是两个概念，主要用于展示数据和创建用户界面元素。视图（View）侧重于显示数据，而窗口部件（Widget）则侧重于用户交互，可操纵性更强。

- View
> **视图（View）本身不包含数据，而是通过模型（Model）来获取和展示数据**
> Qt提供了多个视图类，如列表QListView、表格QTableView和树形结构QTreeView等，用于以不同方式呈现数据。

- Widget
> 窗口部件（Widget）是Qt中的基本GUI控件，用于创建用户界面的各种元素，如按钮、文本框等。
> **窗口部件(Widget)能够直接与用户交互，并可以包含其他窗口部件或视图。**
> `QWidget` 是Qt中所有窗口部件的基类，其他窗口部件如`QLineEdit`、`QPushButton`等都是其子类。


以 `QListView` 和 `QListWidget` 为例子，前者是一个通用的视图类，后者是一个直接的列表型窗口部件。

#### QListView和QListWidget
视图

##### QListWidget自定义QListWidgetItem进行元素显示

1. 定义一个继承`QWidget`的类，用于自定义显示`QListWidgetItem`，如下所示：
```python
class CustemItem(QWidget):
    store_item_mapping_custem: Dict[str, 'CustemItem'] = {}
    def __init__(self, source_item: QtWidgets.QListWidgetItem, sign: bool = False, 
            parent: QWidget = None) -> None:
        super().__init__(parent)
        self.ptr_source_item = source_item
        self.__class__.store_item_mapping_custem[source_item.text()] = self
        if sign:
            self.ptr_source_item.setBackground(Qt.GlobalColor.green)
        else:
            self.ptr_source_item.setBackground(Qt.GlobalColor.red)

    def change_sign(self, sign: bool):
        if sign:
            self.ptr_source_item.setBackground(Qt.GlobalColor.green)
        else:
            self.ptr_source_item.setBackground(Qt.GlobalColor.red)

    pass
```
2. 在`QListWidget`添加元素时，以string为默认item的key，调用setItemWidget设置item样式
```python
def add_listitem(revc: str, sign: bool):
    # self.listWidget.geta
    all_items = []
    for i in range(self.listWidget.count()):
        all_items.append(self.listWidget.item(i).text())
    if revc not in all_items: 
        a = QtWidgets.QListWidgetItem(revc)
        self.listWidget.addItem(a)
        self.listWidget.setItemWidget(a, CustemItem(a, False))
    else:
        CustemItem.store_item_mapping_custem[revc].change_sign(sign)
```

#### QListWidget设置item项大小
```python
the_lw_width = self.living_example.size().width()
    the_lw_height = self.living_example.size().height()
    all_lwitem_count = self.living_example.count()
    for i in reversed(range(all_lwitem_count)):
        self.living_example.item(i).setSizeHint(QSize(
            the_lw_width // all_lwitem_count, 
            the_lw_height // all_lwitem_count
        ))
```

#### QListWidget删除item项
```python
p = self.living_example.takeItem(i)
del p
# 或者通过removeItemWidget方法
self.living_example.removeItemWidget(self.living_example.item(i))
```

#### QListWidgetItem的drag和drop事件

- `dragEnterEvent`, 当外部item进入QListWidget区域时触发（只有在这里接收acceptProposedAction，才会触发之后的dragMoveEvent和dragLeaveEvent）
- `dragLeaveEvent`, 当外部item拖放进来然后离开QListWidget区域时触发
- `dragMoveEvent`, 当外部item拖放进来QListWidget区域时并移动时触发
- `dropEvent`, 当外部item拖放进来QListWidget区域时触发


**注意** `startDrag`会接管move事件，这是之后的move事件均不会被`mouseMoveEvent`捕获

#### 手动设置QDrag开启拖曳动画


### 一个自动消失的提示label

1. 通过自定义Widget实现,在QWidget内添加一个QLabel控件，并通过定时器QTimer的timeout事件插槽实现定时销毁
```python
class ReminderWidget(QWidget):
    """ 显示提示信息,自动销毁 """
    def __init__(self, text: str) -> None:
        super().__init__(main_widget)
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        self.setupUi()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.label.setText(text)
        self.label.setStyleSheet('background-color: red;')
        self.label.adjustSize()

        self.resize(self.label.size())
        self.move(main_widget.size().width()//2 - self.size().width()//2, 0)

        timer = QTimer(self)
        timer.start(1500)  # 1.5秒后
        timer.setSingleShot(True)  # 仅触发一次
        timer.timeout.connect(self.dest)
        # connect(timer, SIGNAL(timeout()), this, SLOT(onTimeupDestroy()))
    
    def dest(self):
        sys.stdout.write('定时器到时...\n')
        print('定时器到时...')
        sys.stdout.write(str((main_widget.size().width(), main_widget.size().height())) + '\n')
        sys.stdout.write(str((self.size().width(), self.size().height())) + '\n')
        sys.stdout.write(str((self.label.size().width(), self.label.size().height())) + '\n')
        self.destroy(True, True)
        self.close()
        del self
    
    def setupUi(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
```
2. 让该部件跟随显示文本内容扩展，通过设置Qlabel的adjustSize让该标签的大小自动根据内容确定，并将父控件的大小resize为Qlabel的大小，即可

**注意** 给提示部件需要设置主窗口才能显示

### 一个基本的SDI(single document interface, 单文档界面)
```python
# demo.py
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 314)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 110, 54, 20))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "hello"))
```
```python
# run.py
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import sys
import demo

class UiShow(QDialog, demo.Ui_Form):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # MainWindow = QMainWindow()
    widget = UiShow()
    widget.show()

    sys.exit(app.exec())
```

## qt帮助文档
qt内置了一系列工具，用于帮助开发者将使用说明内建到应用中。如:
- `assistant`
- `qhelpgenerator`用于将qhp文件转为qch文件(或者将qhcp文件转为qhc文件)，生成压缩后内容
- `qcollectiongenerator`用于将qhcp文件转为qhc文件，生成压缩后内容集合(该工具在qt5.15版本中已弃用，存在包含图片时不显示bug)

### 开发内建文档流程

1. 准备需要显示的帮助文档(html/md格式,md需要转换为html格式)
2. 准备qhp文件，包含基本的content显示和link以及包含的文件
3. 准备qhcp文件，包含需要转换qhp文件及输出文件和注册的qcp文件集合
4. 通过`qhelpgenerator`处理qhcp文件，生成qch文件和qhc文件
5. 注册qhc文件到assistant中查看显示格式问题
6. 在qt应用中使用`QHelpEngine`和`QTabWidget`显示qhc帮助文档

### `qhp`/`qhcp`/`qch`/`qhc`文件

1. `qhp(Qt Help Project)`，`qch(Qt Compressed Help)`，qch是html的压缩文件，把多个的html压缩之后变为qch
2. `qhcp(Qt Help Collection Project)`，`qhc(Qt Help Collection)`。qhcp用于将多个qch文件collection起来，形成一个定制化的Assistant，并在之后注册到assistant里

#### qhp文件编写格式
```xml
<?xml version="1.0" encoding="UTF-8"?>
<QtHelpProject version="1.0">
    <namespace>org.qt-project.examples.simpletextviewer</namespace>
    <virtualFolder>doc</virtualFolder>
    <filterSection>
        <toc>
            <section title="Simple Text Viewer" ref="index.html">
                <section title="Find File" ref="findfile.html">
                    <section title="File Dialog" ref="filedialog.html"/>
                    <section title="Wildcard Matching" ref="wildcardmatching.html"/>
                    <section title="Browse" ref="browse.html"/>
                </section>
                <section title="Open File" ref="openfile.html"/>
            </section>
        </toc>
        <keywords>
            <keyword name="Display" ref="index.html"/>
            <keyword name="Rich text" ref="index.html"/>
        </keywords>
        <files>
            <file>index.html</file>
            <file>images/wildcard.png</file>
        </files>
    </filterSection>
</QtHelpProject>

```

#### qhcp文件编写格式
```xml
<?xml version="1.0" encoding="UTF-8"?>
<QHelpCollectionProject version="1.0">
    <assistant>
        <title>Software Help Document</title>
        <applicationIcon>images/handbook.png</applicationIcon>
        <cacheDirectory>QtProject/SimpleTextViewer</cacheDirectory>
        <startPage>qthelp://{qhp_namespace}/{qhp_virtualFolder}/USAGE_DOCUMENT.html</startPage>
        <aboutMenuText>
            <text>About Software Help Viewer</text>
        </aboutMenuText>
        <aboutDialog>
            <file>about.txt</file>
            <icon>images/handbook.png</icon>
        </aboutDialog>
        <enableDocumentationManager>false</enableDocumentationManager>
        <enableAddressBar>false</enableAddressBar>
        <enableFilterFunctionality>false</enableFilterFunctionality>
    </assistant>
    <docFiles>
        <generate>
            <file>
                <input>HELP.qhp</input>
                <output>HELP.qch</output>
            </file>
        </generate>
        <register>
            <file>HELP.qch</file>
        </register>
    </docFiles>
</QHelpCollectionProject>
```

**注意** 调用`qhelpgenerator`处理qhcp文件时，也会处理generate中的文件
**注意** `qhelpgenerator`处理时，不能覆盖写，已存在输出文件会报错

## bug

### pyqt界面闪烁、黑屏

在pyqt 5.7以下中，可以通过以下带代码尝试解决，5.15.9不起作用
```python
QtCore.QCoreApplication.setAttribute(Qt.ApplicationAttribute.AA_UseSoftwareOpenGL, True)
QGuiApplication.setAttribute(Qt.ApplicationAttribute.AA_UseSoftwareOpenGL, True)
QApplication.setAttribute(Qt.ApplicationAttribute.AA_UseSoftwareOpenGL, True)

QtCore.QCoreApplication.setAttribute(Qt.ApplicationAttribute.AA_UseDesktopOpenGL, True)
QGuiApplication.setAttribute(Qt.ApplicationAttribute.AA_UseDesktopOpenGL, True)
QApplication.setAttribute(Qt.ApplicationAttribute.AA_UseDesktopOpenGL, True)

QtCore.QCoreApplication.setAttribute(Qt.ApplicationAttribute.AA_UseOpenGLES, True)
QGuiApplication.setAttribute(Qt.ApplicationAttribute.AA_UseOpenGLES, True)
QApplication.setAttribute(Qt.ApplicationAttribute.AA_UseOpenGLES, True)
```

**注意** 如果是使用designer设计界面包含listwidget时，出现的元素项拖曳闪烁。可以参考重写相应方法，自己实现元素拖曳效果。

### designer中对象查看器widget上总存在禁用标志

一般是由于未选定控件的布局管理器,可以右键在布局中选择layout