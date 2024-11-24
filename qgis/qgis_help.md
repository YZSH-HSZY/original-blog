# qgis介绍
QGIS 是一个开源的地理信息系统（GIS）软件，它提供了一套功能强大的工具和插件，用于处理和可视化地理数据。具备跨平台能力，可以在 Windows、Linux 和 macOS 上运行。

[qgis github仓库](https://github.com/qgis/QGIS)

## QGIS/OSGeo4W/GDAL区别
- OSGeo4W（Windows开源地理空间基金会，Open Source Geospatial Foundation for Windows）是一个开源地理信息系统（GIS）软件套件，它提供了一组适用于 Windows 操作系统的开源 GIS 工具。如 GDAL、GRASS、QGIS、GRASS GIS、PostGIS、MapServer 等。
- GDAL（地理空间数据抽象库，Geospatial Data Abstraction Library）是一个开源的地理信息系统（GIS）数据访问库，它提供了一套通用的 API，用于读取、写入和操作各种地理空间数据格式。包括 Shapefile、GeoTIFF、PostGIS、ESRI 格式等。
- QGIS 是一个跨平台的应用程序，可以在 Windows、Linux 和 macOS 上运行

## qgis的python环境

[参独立脚本使用qgis](https://docs.qgis.org/2.18/en/docs/pyqgis_developer_cookbook/intro.html#run-python-code-when-qgis-starts)

**注意** 在qgis的python控制台内，通过自动封装的 `iface` 访问 QGIS API 接口、操作当前可见图层。

## qgis中特定名称介绍
在QGIS中，"layer"（图层）和"feature"（要素）是两个重要的概念，它们在地理信息系统中扮演着关键角色。

### 图层(Layer)
图层是QGIS中用于组织和管理地理数据的基本单位。每个图层可以包含不同类型的地理数据（即多个要素），例如：

- **矢量图层**：包含点、线和多边形等几何形状，通常用于表示地理特征（如城市、道路、湖泊等）。
- **栅格图层**：由像素组成，通常用于表示连续的数据（如卫星影像、高程数据等）。
- **表格图层**：可以是属性表，存储与地理特征相关的属性信息。

图层可以在地图视图中叠加显示，用户可以通过不同的样式和符号化方式来调整图层的可视化效果。

### 要素(Feature)
要素是图层中的单个地理实体。每个要素都有其几何形状（如点、线或多边形）和相关的属性数据。例如，在一个表示城市的矢量图层中，
每个城市就是一个要素，包含其位置（几何形状）和属性（如城市名称、人口、面积等）。

要素的主要特点包括：

- **几何形状**：定义要素在空间中的位置和形状。
- **属性数据**：与要素相关的描述性信息，通常以表格形式存储。

### shp

ESRI Shapefile（shp），或简称shapefile，是美国环境系统研究所公司（ESRI）开发的空间数据开放格式。目前，该文件格式已经成为了地理信息软件界的开放标准，这表明ESRI公司在全球的地理信息系统市场的重要性。Shapefile也是重要的交换格式，能够在ESRI与其他公司的产品之间进行数据互操作。

Shapefile文件用于描述几何体对象：点、折线与多边形。例如，Shapefile文件可以存储井、河流、湖泊等空间对象的几何位置。除了几何位置，shp文件也可以存储这些空间对象的属性，例如河流的名字、城市的温度等等。

包含以下几种：
1. `.shp` 文件：存储几何数据（点、线、面）。
2. `.shx` 文件：存储几何数据的索引，便于快速访问。
3. `.dbf` 文件：存储与几何数据相关的属性信息，以表格形式呈现，通常为dBASE格式。
4. `.prj` 文件：包含坐标系统和投影信息。
5. `.sbn` 和 `.sbx` 文件：用于空间索引，提升空间查询效率。
6. `.cpg` 文件：用于指定字符编码。

## qgis的python插件和python应用脚本

- 在python插件中，通过qgis自动封装的 `iface: qgis._gui.QgisInterface` 访问 QGIS API 接口。
- 在独立python脚本中，通过 `QgsProject().instance()` 的唯一单例对象获取当前工程。

### pyqgis的环境设置
使用OSGeo4W套件`QGIS-OSGeo4W-3.22.13-3.msi`安装QGIS时,在安装目录下存在`OSGeo4W.bat`，内有各个环境设置的命令(使用`o-help`查看可用脚本)，以及`QGIS\bin` 下存在python的环境设置`python-qgis-ltr.bat`(QGIS 3.0.0以上)/`python-qgis.bat`(QGIS 2.0.0)

### pyqgis插件使用messageBar和statusBar的示例
```python
widget = iface.messageBar().createMessage("Global Error Marker"," Downloading errors from data base . . .")
prgBar = QProgressBar()
prgBar.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)
prgBar.setValue(0)
prgBar.setMaximum(10000)           
widget.layout().addWidget(prgBar)
iface.messageBar().pushWidget(widget, Qgis.MessageLevel.Warning)

errCount=0
for i in range(1,10000):
   errCount += 1
   prgBar.setValue(i)


iface.messageBar().clearWidgets()
iface.mapCanvas().refresh()
iface.messageBar().pushMessage('xs',Qgis.Critical)
#iface.statusBarIface().showMessage('xs')
#iface.statusBarIface().clearMessage()
```

### pyqgis 提供iface获取选择feature
```python
canvas: QgsMapCanvas = iface.mapCanvas()  # 获取指向地图画布的pointer,等同iface.activeLayer
cLayer: QgsVectorLayer = canvas.currentLayer()  # 获取当前操作层
count = cLayer.selectedFeatureCount()  # 获取选中的features数
features = cLayer.selectedFeatures  # 获取选中的features

# 创建一个 memory layer，包含选择的features
temp_layer = layer.materialize(QgsFeatureRequest().setFilterFids(layer.selectedFeatureIds()))
# 获取指定层的目标字段
result = QgsVectorLayerUtils.getValues(temp_layer, "your_field")[0]
```

### qgis插件安装位置
- QGIS3: `C:\Users\admin\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins`
- QGIS2: `C:\Users\admin\.qgis2\python\plugins`

### qgis插件2to3迁移
[参官方迁移文档](https://github.com/qgis/QGIS/wiki/Plugin-migration-to-QGIS-3)

### qgis3插件开发

[官方插件开发文档](https://www.osgeo.cn/qgisdoc/docs/pyqgis_developer_cookbook/plugins/plugins.html#getting-started)

#### 环境准备
1. 确保OSGeo4W-QGIS3工作正常
2. 安装插件`Plugin Builder 3`(用于创建一个QGIS插件模板，作为插件开发的起点)和`Plugin Reloader`(重新加载选定的插件,仅对Python插件开发有用)
3. 编写一些配置信息，完成模板生成
4. 安装pbt工具， `pip install pb_tool`

#### 插件目录介绍
典型的插件目录包括以下文件：
- `metadata.txt`: required -包含插件网站和插件基础设施使用的一般信息、版本、名称和其他一些元数据。
- `__init__.py`: required -插件的起点。它必须有 classFactory() 方法，并且可以具有任何其他初始化代码。
- `mainPlugin.py`: core code -插件的主要工作代码。包含有关插件操作和主代码的所有信息。
- `form.ui`: for plugins with custom GUI -Qt Designer创建的图形用户界面。
- `form.py`: compiled GUI -将上面描述的form.ui翻译成Python。
- `resources.qrc`: optional -由Qt Designer创建的.xml文档。包含指向在图形用户界面窗体中使用的资源的相对路径。
- `resources.py`: compiled resources, optional -将上述.qrc文件转换为Python。

##### 默认文件示例
- `__init__.py` 文件
```python
def classFactory(iface):
  from .mainPlugin import TestPlugin
  return TestPlugin(iface)

# any other initialisation needed
```
- `mainPlugin.py` 主要工作代码
```python
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtWidgets import *

# initialize Qt resources from file resources.py
from . import resources

class TestPlugin:

  def __init__(self, iface):
    """ 这可以访问QGIS界面 """
    # save reference to the QGIS interface
    self.iface = iface

  def initGui(self):
    """ 在加载插件时调用 """
    # create action that will start plugin configuration
    self.action = QAction(QIcon("testplug:icon.png"),
                          "Test plugin",
                          self.iface.mainWindow())
    self.action.setObjectName("testAction")
    self.action.setWhatsThis("Configuration for test plugin")
    self.action.setStatusTip("This is status tip")
    self.action.triggered.connect(self.run)

    # add toolbar button and menu item
    self.iface.addToolBarIcon(self.action)
    self.iface.addPluginToMenu("&Test plugins", self.action)

    # connect to signal renderComplete which is emitted when canvas
    # rendering is done
    self.iface.mapCanvas().renderComplete.connect(self.renderTest)

  def unload(self):
    """ 在卸载插件时调用 """
    # remove the plugin menu item and icon
    self.iface.removePluginMenu("&Test plugins", self.action)
    self.iface.removeToolBarIcon(self.action)

    # disconnect form signal of the canvas
    self.iface.mapCanvas().renderComplete.disconnect(self.renderTest)

  def run(self):
    # create and show a configuration dialog or something similar
    print("TestPlugin: run called!")

  def renderTest(self, painter):
    # use painter for drawing to map canvas
    print("TestPlugin: renderTest called!")
```

## 内置算法外部调用
[参qgis官方文档](https://docs.qgis.org/3.34/en/docs/user_manual/processing/console.html)
[自定义算法示例](https://github.com/gacarrillor/pyqgis_scripts/tree/master/pyqgis_custom_processing_algorithm_standalone)
[算法介绍](https://docs.qgis.org/3.22/zh-Hans/docs/user_manual/processing_algs/qgis/vectorgeometry.html#qgisdissolve)

### pyqgis交会shell调用
```python
import processing  # 导入处理部分(注意和qgis.processing区分)
from processing.core.Processing import Processing
Processing.initialize()
# 查看所有算法
for alg in QgsApplication.processingRegistry().algorithms():
    print(alg.id(), "->", alg.displayName())

# Add our own algorithm provider
from example_algorithm_provider import ExampleAlgorithmProvider
provider = ExampleAlgorithmProvider()
QgsApplication.processingRegistry().addProvider(provider)

# Run our custom algorithm
layer = QgsVectorLayer("/docs/geodata/bogota/ideca/Loca.shp", "layer", "ogr")
params = {'INPUT': layer}
print("RESULT:", processing.run("my_provider:my_algorithm", params)['OUTPUT'])
```
**注意** 请检查processing模块的位置在独立的apps插件目录中，区分qgis下processing
**注意** 可使用 `processing.algorithmHelp("native:multiparttosingleparts")` 查看算法帮助信息

### 命令行接口
qgis 提供一个名为 `QGIS Processing Executor` 的工具，允许直接从命令行运行 Processing 算法和模型（内置或由插件提供），而无需启动 QGIS Desktop 本身。

使用 `qgis_process --help` 查看相应帮助信息

**注意** 对于不带窗口管理器的系统（例如无头服务器），请设置变量`export QT_QPA_PLATFORM=offscreen`

## 使用示例

### 通过工具箱检查矢量几何有效性
1. 在 视图-->面板-->工具箱中，打开dockwidget面板，搜索检查几何有效性运行算法
2. 查看生成的图层，在属性表中获取提示信息

### 查看几何体顶点
选择几何体所在layer-->进入编辑模式-->在工具条中选择顶点工具-->在几何体上右键查看

## bug示例

### Normalized/laundered field name
> 问题描述:
为一个要素Feature添加属性并写入矢量文件shp时，出现警告 `Normalized/laundered field name`
> 解决方案:
属性名称不能超过 10 个字符,请使用短名称

### 使用 layer 添加的属性丢失
> 问题描述:
使用`QgsVectorLayer.addAttribute`，添加一个属性字段时，在结果中属性不出现
> 解决方案:
查看`addAttribute`的描述文档可知，`Add an attribute field (but does not commit it).QgsVectorLayer.addAttribute are only valid for layers in which edits have been enabled`,只有通过 `startEditing` 开启图层的编辑模式，并在添加后`commitChanges`提交才有效。

### 使用QgsVectorFileWriter保存shp文件后，通过QgsVectorLayer打开，之后添加要素类型警告
> 解决方案:
每个图层仅能保存一种类型的要素，在`QgsVectorFileWriter`构造时，指定geometryType确定，之后通过QgsVectorLayer打开之前调用 `del`

### pyqgis载入图层后，脚本移除图层并删除文件报错
> 一种尝试的解决方案:
```python
project.removeMapLayer(layer.id())
QgsVectorFileWriter.deleteShapeFile(remove_path)
```
**注意** 此方案不一定生效,推荐在脚本中使用子进程分别处理

### pyqgis写入shp文件时，报文件不是一个目录
此问题在重新覆写一个已加载的图层文件时报错，怀疑此部分异常错误提示有bug，同样重开一个进程解决
`QgsVectorFileWriter.writeAsVectorFormat(save_lay, save_name, "utf-8", save_lay.crs(), "ESRI Shapefile")`

