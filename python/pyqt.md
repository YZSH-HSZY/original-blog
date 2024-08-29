## pyqt

### qt资源管理系统

为了防止打包发布pyqt程序时丢失资源文件，qt推出了`qt资源管理系统`。与直接读取资源文件相比，qt资源管理系统可以对资源进行组管理并使用资源别名提高程序健壮性，借助资源编译rcc可以将资源文件编译进可执行文件中。如
```python
QPixmap("Icons/Python_icon.ico")  # 直接读取资源文件
QPixmap(":/<资源组名>/<资源文件别名>")  # 借助qt资源管理系统读取资源文件
```

- Qt 资源系统（The Qt Resource System）是一种独立于平台的资源管理器，用于在应用程序的可执行文件中存储二进制文件。对 PyQt 而言，这意味着在 Python 代码中直接以二进制形式存储图标、QSS、长文本翻译等资源文件。使用 Qt 资源管理系统可以有效防止资源文件丢失，对于需要打包发布 的 PyQt 程序尤其实用。

- Qt 资源集合文件（Qt Resource Collection File）一般以 .qrc 作为扩展名保存，故简称 .qrc 文件。其文件格式基于 XML，用于将文件系统（硬盘）中的资源文件与 Qt 应用程序关联起来。.qrc 还可以实现为资源分组、设置别名、等功能。

#### qt资源系统的使用

在项目中使用 Qt 资源系统，大致分为三个步骤：
1. 编写 .qrc 文件;
2. 使用 rcc 编译资源;
3. 导入与使用;

##### qrc文件

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

##### rcc编译

Qt 提供了 Resource Compiler Command Tool（简称 rcc），用于在构建过程中将资源嵌入 Qt 应用程序。对于 PyQt，也有对应版本的 rcc 工具，用于将 .qrc 中指定的资源文件数据编译至 Python 对象。

- 使用`pyrcc5`命令 或 `python -m PyQt5.pyrcc_main`运行脚本生成对应资源编译后的py文件
- 生成后的py文件内容包含：
qt_resource_data - 资源文件内容数据
qt_resource_name - 资源文件名称
qt_resource_struct - 资源结构
还有两个函数 qInitResources() 与 qCleanupResources()，分别对应向 Qt 中注册资源与清理资源。
- 在生成的ui文件中会自动import所需的qrc文件(如果ui中使用了qrc中的资源)

### 使用designer设计界面ui文件

designer是qt为了简化界面设计而推出的一款类原型设计工具，你可以直接在designer中设计需要的应用程序原型并预览，保存并生成需要的界面布局ui文件。

- ui文件是一个xml文件，其内以标签的形式定义了样式的布局，可以通过以下方式使用:
  1. `loadUiType(uifile, from_imports=False, resource_suffix='_rc'， import_from='.') ->(表单类，基类)`
  > `loadUiType`会加载Qt Designer .ui文件并返回生成的表单类和Qt基类。
  > Uifile是以.ui为后缀的文件或类似文件的对象。可以选择设置From_imports来生成相对导入语句。目前，这只适用于资源模块的导入。resource_suffix是附加到.ui文件中指定的任何资源文件的basename后的后缀，用于创建pyrcc4从资源文件生成的Python模块的名称。默认值是'_rc'，也就是说，如果.ui文件指定了一个名为foo的资源文件。那么对应的Python模块是foo_rc。Import_from可选地设置为相对导入语句使用的包。默认值是'.'。

  2. pyuic5编译生成ui布局的py文件，`pyuic5 <ui_file> -o <output_py>`




### pyqt集成的工具
pyuic5、pyrcc5、pylupdate5

- pyuic5自动转换ui文件到py类文件 `pyuic5 <ui_file> -o <output_py_file>`
  - pyuic5 等同 `python -m PyQt5.uic.pyuic`
- pyrcc5自动转换qrc文件到py文件
    - pyrcc5 等同 `python -m PyQt5.pyrcc_main`
- pylupdate5
  - pylupdate5 等同 `python -m PyQt5.pylupdate_main`

除此之外还有：Qt设计师Designer、Qt助手assistant、Qt国际化工具lupdate等

### qt界面分类

Qt的界面大概分为以下3大类：
1. 主窗口 `QMainWindow`
> 主窗口类，具有特定的布局和功能。包含菜单栏、工具条，菜单、工具下方的空白区域是主部件区域，使用`QMainWindow`，可以快速地构建具有标准布局和功能的应用程序主界面。可以通过`setCentralWidget`接口为`QMainWindow` 设置主部件。
2. 对话框 `QDialog`
> 对话框类，通常用于实现一些特定的功能或操作。有最大化、最小化、关闭按钮，有模态、非模态之分(模态对话框会打断用户的当前操作流程/非模态对话框则不会打断用户操作)。一般用作其他部件的子部件。不能嵌入到其他窗体中。
3. 控件 `QWidget`
> `QWidget`是所有具有可视界面类的基类，也是`QDialog`和`QMainWindow`的基类。这意味着选择`QWidget`创建的界面可以支持各种界面组件，并可以嵌入到其他窗体中。每个窗口部件都是矩形，并且它们按Z轴顺序排列。没有指定父容器时，`QWidget`可作为独立的窗口。常用于开发应用程序的主体部分，或者是作为其他更复杂界面元素的容器。


### qt信号和槽机制
qt使用信号和槽机制来替代传统ui编程的事件和callback操作，

1. 使用connect宏实现信号-槽开发。
2. 使用connect函数实现信号-槽开发。
3. 使用lambda函数实现信号-槽开发。

### gui模块

Qt GUI模块提供了用于窗口系统集成、事件处理、OpenGL和OpenGL ES集成、2D图形、基本成像、字体和文本的类。这些类由Qt的用户界面技术在内部使用，但也可以直接使用，例如使用低级OpenGL ES图形API编写应用程序。 

> Qt GUI模块中最重要的类是`QGuiApplication`和`QWindow`。想要在屏幕上显示内容的Qt应用程序必须使用他们。
> - QGuiApplication 包含主事件循环，在其中处理和调度来自窗口系统和其他源的所有事件。它还处理应用程序的初始化和终结。
> - QWindow 类表示基础窗口系统中的一个窗口。它提供了许多虚拟功能来处理来自窗口系统的事件 （QEvent），例如触摸输入、曝光、焦点、击键和几何更改。

#### 2D Graphics
Qt GUI模块还包含2D图形、图像、字体和高级排版的类。

1. 2D图形：使用曲面类型`QSurface::RasterSurface`创建的QWindow可以与`QBackingStore`和`QPainter`（Qt高度优化的2D矢量图形API）结合使用。`QPainter` 支持绘制线条、多边形、矢量路径、图像和文本。有关详细信息，请参阅绘制系统和栅格窗口示例。
2. 图像：Qt可以使用`QImage`和`QPixmap`类加载和保存图像。默认情况下，Qt支持最常见的图像格式，包括JPEG和PNG等。用户可以通过 `QImageIOPlugin` 类添加对其他格式的支持。有关详细信息，请参阅读取和写入图像文件。
3. 字体和高级排版：Qt 中的排版是通过 `QTextDocument` 完成的，它使用 `QPainter` API 和 Qt 的字体类（主要是 `QFont`）。应用程序更喜欢低级 API `QRawFont` 和 `QGlyphRun` 等类去处理文本和字体。

#### 硬件加速
Qt的硬件渲染接口是使用硬件加速图形API的抽象，例如OpenGL、OpenGL ES、Direct3D、Metal和Vulkan。

与直接使用 OpenGL 或 Vulkan 渲染到 QWindow 的方法相比，`QRhi` 和其它相关类提供了一个可移植的、跨平台的 3D 图形和计算 API，并辅以着色器调节和转译管道。这样一来，应用程序就可以避免直接依赖单个 API，在某些情况下，还可以避免依赖特定于供应商或平台的 3D API。

#### 3d矩阵和矢量
Qt GUI模块还包含一些数学类，以帮助进行与3D图形相关的最常见数学运算。这些类包括 QMatrix4x4、QVector2D、QVector3D、QVector4D 和 QQuaternion。

## QT内部的MVC模型
QT内部有一套专门的显示数据界面的MVC封装,即Model-View-Delegate(模型-视图-代理)

## 示例

### 让部件填充QWidget

1. 对于`QMainWindow`可以通过`setCentralWidget`设置中心控件
2. 对于`QWidget`可以指定控件的大小策略Size Policies
3. 或者为控件添加一个布局管理器(如: 垂直布局QVBoxLayout)，此时会使用布局指定的大小策略

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
