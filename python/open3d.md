## 矩阵变换中概念

### 左手坐标系和右手坐标系
### 旋转角度正负确定
### 旋转矩阵和平移向量和旋转向量
### 齐次坐标
### 内旋和外旋
### 偏航角rpy和欧拉角euler（静态欧拉角和动态欧拉角）
### 四元数

## open3d介绍
Open3D 是一个开源库，支持快速开发处理 3D 数据的软件。Open3D 前端在 C++ 和 Python 中公开了一组精心挑选的数据结构和算法。后端经过高度优化，并设置为并行化。

[官方文档](http://www.open3d.org/docs/release)

open3d中可视化的坐标轴为右手坐标系，z轴指向前方，y轴指向上方，x轴指向右方
### open3d安装
open3d和open3d-python，这两个都是open3d的官方库，open3d-python是0.7及以前版本的名字，0.8及以后的版本名字是open3d。
直接使用`pip install open3d`安装即可

### open3d的核心功能
|功能                                                    |中文对应   |
|--------------------------------------------------------|-------|
|3D data structures                                      | 3D 数据结构 |
|3D data processing algorithms                           | 3D数据处理算法|
|Scene reconstruction                                    | 场景重建 |
|Surface alignment                                       | 曲面对齐 |
|3D visualization                                        | 3D 可视化 |
|Physically based rendering (PBR)                        | 基于物理的渲染 （PBR）|
|3D machine learning support with PyTorch and TensorFlow | PyTorch 和 TensorFlow 的 3D 机器学习支持|
|GPU acceleration for core 3D operations                 | 用于核心 3D 操作的 GPU 加速|
|Available in C++ and Python                             | 支持 C++ 和 Python|

### open3d数据结构

#### 点云 pointcloud
在open3d的几何模块geometry中

##### 点云操作(读取/绘制/计算凸包)

read_point_cloud 从文件中读取点云。它尝试根据扩展名对文件进行解码。有关支持的文件类型列表，请参阅文件 IO。

draw_geometries 可视化点云。使用鼠标/触控板从不同的视点查看几何图形。

paint_uniform_color 将所有点绘制为统一的颜色。颜色在 RGB 空间中，[0， 1] 范围。

使用open3d.geometry.PointCloud.compute_convex_hull方法计算凸包，你也可以使用python的科学计算scipy包中的ConvexHull计算凸包

### open3d常见名词解释
#### ICP（Iterative Closest Point）
icp(迭代最近点)是一种点云配准算法，可以将两个点云进行对齐.

#### 投影、模型、视图矩阵与相机内参外参的区别
在计算机图形学中，投影、模型、视图矩阵以及相机的内参和外参是常用的概念，它们在渲染和相机模拟中起着重要的作用。下面是它们的区别： 

1. 投影矩阵（Projection Matrix）：投影矩阵是将三维场景投影到二维屏幕上的变换矩阵。它定义了视锥体的形状和大小，包括透视投影和正交投影等不同类型。透视投影用于产生透视效果，而正交投影则保持物体在远近平行投影的效果。 
 
2. 模型矩阵（Model Matrix）：模型矩阵是将模型从局部坐标系变换到世界坐标系的变换矩阵。它用于描述模型的位置、旋转和缩放等变换操作。通过将模型矩阵与顶点坐标相乘，可以将模型从局部坐标系变换到世界坐标系。 
 
3. 视图矩阵（View Matrix）：视图矩阵是将场景从世界坐标系变换到相机坐标系的变换矩阵。它描述了相机的位置和朝向，用于模拟相机的观察视角。通过将视图矩阵与顶点坐标相乘，可以将场景从世界坐标系变换到相机坐标系。 
 
4. 相机的内参和外参（Camera Intrinsic and Extrinsic Parameters）：相机的内参是指相机的内部参数，包括焦距、主点位置和像素尺寸等。它们描述了相机的成像特性和像素坐标系。相机的外参是指相机的外部参数，包括相机的位置和朝向等。它们描述了相机在世界坐标系中的位置和朝向。 
 
相机的内参和外参与投影、模型、视图矩阵的关系在于，通过相机的内参和外参，可以计算出相机的视图矩阵和投影矩阵。视图矩阵将场景从世界坐标系变换到相机坐标系，而投影矩阵将场景从相机坐标系投影到屏幕坐标系。这两个矩阵的乘积即为最终的变换矩阵，用于将模型从局部坐标系经过视图变换和投影变换后投影到屏幕上。

### open3d数据集
```
open3d下载的数据集在以下目录，其中download存放下载的压缩包，extract存放解压后文件
%USERPROFILE%\open3d_data\download\DemoICPPointClouds\<name>.zip
%USERPROFILE%\open3d_data\extract\DemoICPPointClouds
```
[数据集下载镜像](https://hub.nuaa.cf/isl-org/open3d_downloads/releases?page=1)
|  o3d的dataset示例 |  说明 |
|---|---|
|DemoColoredICPPointClouds|包含两个ply格式的点云|
|DemoCropPointCloud|包含一个点云和cropped.json|
|DemoFeatureMatchingPointClouds|两个点云分割和对应的FPFH和L32D特性|
|DemoICPPointClouds|包含三个二进制pcd格式的点云|
|DemoPoseGraphOptimization|2个json文件|
|SampleFountainRGBDImages SampleFountainRGBD法师|33个彩色和深度图像|
|SampleNYURGBDImage|NYU_color.ppm和NYU_depth.pgm|
|SampleRedwoodRGBDImages|5组彩色深度图像|
|SampleSUNRGBDImage|SUN_color.jpg和SUN_depth.png|
|SampleTUMRGBDImage|TUM_color.png和TUM_depth.png|

## open3d模块

### geometry(几何模块)

常见几何体有pointcloud点云、lineset线集
LineSet 在 3D 中定义一组线集合。一般用于在点云中显示对应部分。

#### 各示例
各工具类示例如下：
```
o3d.geometry.All                                  o3d.geometry.OctreeLeafNode(
o3d.geometry.Average                              o3d.geometry.OctreeNode(
o3d.geometry.AxisAlignedBoundingBox              o3d.geometry.OctreeNodeInfo
o3d.geometry.Color                                o3d.geometry.OctreePointColorLeafNode
o3d.geometry.DeformAsRigidAsPossibleEnergy       o3d.geometry.OrientedBoundingBox
o3d.geometry.FilterScope                         o3d.geometry.PointCloud
o3d.geometry.Gaussian3                            o3d.geometry.Quadric
o3d.geometry.Gaussian5                            o3d.geometry.RGBDImage
o3d.geometry.Gaussian7                            o3d.geometry.SimplificationContraction
o3d.geometry.Geometry                            o3d.geometry.Smoothed
o3d.geometry.Geometry2D                          o3d.geometry.Sobel3dx
o3d.geometry.Geometry3D                          o3d.geometry.Sobel3dy
o3d.geometry.HalfEdge                            o3d.geometry.Spokes
o3d.geometry.HalfEdgeTriangleMesh                o3d.geometry.TetraMesh
o3d.geometry.Image                               o3d.geometry.TriangleMesh
o3d.geometry.ImageFilterType                     o3d.geometry.Vertex
o3d.geometry.KDTreeFlann                         o3d.geometry.Voxel
o3d.geometry.KDTreeSearchParam                   o3d.geometry.VoxelGrid
o3d.geometry.KDTreeSearchParamKNN                o3d.geometry.get_rotation_matrix_from_quaternion
o3d.geometry.KDTreeSearchParamRadius             o3d.geometry.get_rotation_matrix_from_xyz
o3d.geometry.LineSet                             o3d.geometry.get_rotation_matrix_from_xzy
o3d.geometry.MeshBase                            o3d.geometry.get_rotation_matrix_from_yxz
o3d.geometry.Normal                               o3d.geometry.get_rotation_matrix_from_yzx
o3d.geometry.Octree                              o3d.geometry.get_rotation_matrix_from_zxy
o3d.geometry.OctreeColorLeafNode                 o3d.geometry.get_rotation_matrix_from_zyx
o3d.geometry.OctreeInternalNode                  o3d.geometry.keypoint
o3d.geometry.OctreeInternalPointNode
```

#### TriangleMesh(三角网格)
三角形网格包含顶点和三角形。三角形网格类将属性数据存储在键值映射中。有两种映射:顶点属性映射和三角形属性映射。
可以使用`TriangleMesh.vertices`属性获取所有顶点，
### camera(相机模块)

PinholeCameraIntrinsic固定的针孔相机
PinholeCameraIntrinsic class 存储内部相机矩阵以及图像高度和宽度

#### 相机的各矩阵或向量含义

内部矩阵(也叫内参（intrinsic matrix）决定相机的投影属性)，外部矩阵(也叫外参（extrinsic matrix）决定相机的位置和朝向)，旋转矩阵，平移向量

1. 外部矩阵也叫外参，是用于将世界坐标系的点转换到相机坐标系中。
> 外参包含旋转矩阵，平移向量，根据世界坐标系变换相机坐标系所采取的算法不同，计算方式有所差异。
> 相机外参是一个4x4的矩阵 ，其作用是将世界坐标系的点变换到相机坐标系下。我们也把相机外参叫做world-to-camera (w2c)矩阵。(注意用的是4维的齐次坐标)
> 相机外参的逆矩阵被称为camera-to-world (c2w)矩阵，其作用是把相机坐标系的点变换到世界坐标系。
2. 内部矩阵也叫内参，是用于将相机坐标系中的对象转换到投影平面中
> 相机的内参矩阵将相机坐标系下的3D坐标映射到2D的图像平面，这里以针孔相机(Pinhole camera)为例介绍相机的内参矩阵K：
> 内参矩阵K包含4个值，其中fx和fy是相机的水平和垂直焦距（对于理想的针孔相机，fx=fy）。焦距的物理含义是相机中心到成像平面的距离，长度以像素为单位。cx和cy是图像原点相对于相机光心的水平和垂直偏移量。cx，cy有时候可以用图像宽和高的1/2近似:
```
NeRF run_nerf.py有这么一段构造K的代码
if K is None:
    K = np.array([
        [focal, 0, 0.5*W],
        [0, focal, 0.5*H],
        [0, 0, 1]
    ])
```

注意：接下来的介绍假设矩阵是列矩阵(column-major matrix)，变换矩阵左乘坐标向量实现坐标变换（这也是OpenCV/OpenGL/NeRF里使用的形式）。

相机外参


相机外参的逆矩阵被称为camera-to-world (c2w)矩阵，其作用是把相机坐标系的点变换到世界坐标系。因为NeRF主要使用c2w，这里详细介绍一下c2w的含义。c2w矩阵是一个4x4的矩阵，左上角3x3是旋转矩阵R，右上角的3x1向量是平移向量T。有时写的时候可以忽略最后一行
**齐次坐标系**
在进行平移变换时，需要将各变换向量使用齐次坐标系表示，使用3*3矩阵只能表示旋转和缩放操作，而扩充到4d齐次空间则可以统一表示平移。旋转、缩放操作。

### visualization(可视化模块)
一般是在快速预览单个pcd时使用。
```
{
	"class_name" : "ViewTrajectory",
	"interval" : 29,
	"is_loop" : false,
	"trajectory" : 
	[
		{
			"boundingbox_max" : [ 3.9607717990875244, 2.4249000549316406, 2.5536561012268066 ],
			"boundingbox_min" : [ 0.55078125, 0.83203125, 0.55859375 ],
			"field_of_view" : 60.0,
			"front" : [ 0.42646335124247764, -0.19388430316588381, -0.88348055271913883 ],
			"lookat" : [ 2.2557765245437622, 1.6284656524658203, 1.5561249256134033 ],
			"up" : [ 0.38557113665728643, -0.84459766566235372, 0.37146962424202523 ],
			"zoom" : 0.69999999999999996
		}
	],
	"version_major" : 1,
	"version_minor" : 0
}
```
示例：
```
#创建窗口对象
vis = o3d.visualization.Visualizer()
#设置窗口标题
vis.create_window(window_name="kitti")

# 创建一个坐标轴的网格
# create_coordinate_frame工厂函数，创建一个坐标框架网格。坐标系将以“原点”为中心。x、y、z轴将分别呈现为红色、绿色和蓝色箭头。
# size:坐标系的大小
# origin:坐标系的原点
coord_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(size=1.0, origin=[0, 0, 0])
# 将坐标轴添加到可视化窗口
vis.add_geometry(coord_frame)
```

### 可视化的gui模块
gui内置了一系列的按键别名，可通过`print(gui.<任一按键大写英文名，如ENTER>.__doc__)`查看`Names of keys. Used by KeyEvent.key ...`。**注意**: 如果是一些特殊按键，如CTRL之类的，可以通过gui.KeyModifier获取别名。
也可通过gui的各种ui控件来制作较为精美的ui界面效果。

**设置回调函数处理事件**
使用`set_on_mouse(self,Callable[[gui.MouseEvent], int])`或`set_on_key(`来为ui容器或控件添加交互事件并设置回调时，回调函数必须返回EventCallbackResult.IGNORED, EventCallbackResult.HANDLED, or EventCallbackResult.CONSUMED.
> `IGNORED`表示事件处理程序忽略了事件，小部件将正常处理事件
> `HANDLED`表示事件处理程序处理了事件，但小部件仍将正常处理事件。这在扩展基本功能时非常有用
> `CONSUMED`表示事件处理程序消耗了事件，事件处理停止，小部件将不再处理该事件。这在替换func时很有用

#### 小ui控件
```
gui.Label       gui.RadioButton     gui.Widget      gui.FileDialog
...
```
#### 按键事件KeyEvent
```
>>> gui.KeyEvent.
gui.KeyEvent.DOWN      gui.KeyEvent.UP        gui.KeyEvent.key       gui.KeyEvent.type
gui.KeyEvent.Type(     gui.KeyEvent.is_repeat gui.KeyEvent.mro(
```
#### 鼠标事件MouseEvent

**注意** 在open3d自定义的事件回调处理函数中，鼠标事件中down和move不能同时触发（或许可以手动抛出事件？）
```
>>> gui.MouseEvent.
gui.MouseEvent.BUTTON_DOWN       gui.MouseEvent.WHEEL             gui.MouseEvent.mro(              gui.MouseEvent.x
gui.MouseEvent.BUTTON_UP         gui.MouseEvent.buttons           gui.MouseEvent.type              gui.MouseEvent.y
gui.MouseEvent.DRAG              gui.MouseEvent.is_button_down(   gui.MouseEvent.wheel_dx
gui.MouseEvent.MOVE              gui.MouseEvent.is_modifier_down( gui.MouseEvent.wheel_dy
gui.MouseEvent.Type(             gui.MouseEvent.modifiers         gui.MouseEvent.wheel_is_trackpad
```
### utility(工具模块)
各工具类示例如下：
```
o3d.utility.Debug                    o3d.utility.Vector2dVector          o3d.utility.Warning
o3d.utility.DoubleVector            o3d.utility.Vector2iVector          o3d.utility.get_verbosity_level
o3d.utility.Error                    o3d.utility.Vector3dVector          o3d.utility.random
o3d.utility.Info                     o3d.utility.Vector3iVector          o3d.utility.reset_print_function
o3d.utility.IntVector               o3d.utility.Vector4iVector          o3d.utility.set_verbosity_level
o3d.utility.Matrix3dVector          o3d.utility.VerbosityContextManager
o3d.utility.Matrix4dVector          o3d.utility.VerbosityLevel
```
1. 其中比较常用的是Vector<列数，类似与numpy的reshape((-1,列数))><数据类型，i值int32，d值float64>Vector 类