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
在安装的

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
