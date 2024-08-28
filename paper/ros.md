# ROS
## 安装
(官方安装教程noteic)[https://wiki.ros.org/cn/noetic/Installation/Ubuntu]

ubuntu ros仓库 key设置(ros官方将key托管在https://github.com/ros/rosdistro.git)
可以使用该命令从镜像获取`curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -`


## ros术语描述

### 节点
一个ros节点代表一个可独立运行的程序，是使用ROS API相互通信的处理过程（即功能模块）。

### 节点管理器
节点管理器：ROS节点管理器（后简称master）作为中间节点工作，帮助在不同的ROS节点之间建立连接。
**注意** ros2中使用roscore服务重新来替代节点管理器

### 话题
在两个ROS节点之间通信和交换ROS消息的方法之一称为ROS话题。话题是使用ROS消息交换数据的命名总线。

### 服务
服务是另一种通信方法，其功能类似于话题。话题使用发布或订阅交互，而服务使用请求或回复方法。

### 数据包
数据包是ROS提供的一个有效工具，用于记录和回放ROS话题（模拟一个过程中的数据传输）。当开展机器人相关研究时，可能有些情况下我们需要在没有实际硬件的情况下工作。使用rosbag，我们可以记录传感器数据，并将数据包文件复制到其他计算机上，通过回放来检查数据以及应用程序的执行结果。

### roscore服务程序
roscore向节点提供连接信息，当一个新节点出现时，向他提供（与他订阅同一个消息主题的节点）建立点对点连接的必要信息。
### Gazebo开源机器人模拟器
与ROS紧密集成的开源机器人模拟器之一是Gazebo（http://gazebosim.org）。Gazebo是一个动态的机器人模拟器，提供了对各种各样的机器人模型和传感器的广泛支持。
使用`gazebo --help`查看是否已安装

#### URDF (Unified Robot Description Format, 统一机器人描述格式)
它是一种用于描述机器人和其他机械系统的标准化文件格式。URDF 文件可以使用各种编程语言编写，并且可以使用各种工具来读取和修改它们。 

### DDS
DDS是OMG定义的标准。它是一种发布–订阅传输技术，类似于ROS-1中使用的技术。与ROS-1不同，DDS实现了一种分布式发现系统技术，可以帮助两个或多个DDS程序在不使用master的情况下相互通信。

### tf树、fixed frame

ros话题下发布的坐标数据均匀一个frame_id的标识，表示该坐标点位于哪一个坐标系下。如果想要在rviz下查看对应数据，需要话题中数据的坐标系能够通过tf树变换得到；

tf树存放坐标系之间的相对转换关系

## ros命令

### rosrun
`rosrun <package_name> <cmd> [args...]`

### roslaunch
`roslaunch <package_name> <launch_file>`
用于自动启动一系列ros节点的命令行工具，与rosrun有点像（但roslaunch操作launch文件而不是节点）

### launch文件

是以`<launch>`包裹的xml文件,内置了一系列启动节点和参数的描述。

**注意** `params标签`是设置在ros的参数服务器上，可以通过rosparam命令获取。而`arg标签`仅在launch文件内有效，用于代替重复重新的数据。也可以作为局部参数（定义在include内部）传递给include_launch文件，通过`$(arg <arg_naem>)`获取，注意：传递的局部参数必须显示声明使用`<arg name=<arg_naem> />`，否则报unused错误，也不能重复定义（即添加value属性,可以有default属性）

`rosparams标签`可以从yaml文件中加载参数。
`node标签`用于启动节点，pkg和type属性唯一指定一个可执行文件，name为对应namespace下节点的命名。

**注意** `remap标签`用于ns和name的重映射，如下
```launch
<node name="test_name" pkg="test_launch" type="test_name.py" ns="temp" output="screen" >
    <!-- <remap from="data" to="/no_prefix_mapping"/> -->
    <remap from="/pub/full_test/data" to="/pub/have_prefix_mapping"/>
    <remap from="pub_loacl_data" to="remap_pub_local"/>
    <remap from="/sub/test/data" to="/sub/have_prefix_mapping"/>
    <remap from="sub_loacl_data" to="remap_sub_local"/>
</node>
```

```test_name.py
self.str_pub = rospy.Publisher("/pub/full_test/data", String, queue_size=10) 
self.str_pub2 = rospy.Publisher("pub_loacl_data", String, queue_size=10) 
self.str_sub = rospy.Subscriber("/sub/test/data", String, self.callback) 
self.str_sub2 = rospy.Subscriber("sub_loacl_data", String, self.callback) 
```
对应topic为
```
d:\all_projects>rostopic list
/pub/have_prefix_mapping
/rosout
/rosout_agg
/sub/have_prefix_mapping
/temp/remap_pub_local
/temp/remap_sub_local
```

### rqt_plot话题可视化
rqt_plot程序（http://wiki.ros.org/rqt_plot）是一个用于绘制ROS话题形式的标量值的工具。我们可以在话题框中提供话题名称，并将相应话题的变量数据绘制出来。

### rqt_graph节点可视化
rqt_graph（http://wiki.ros.org/rqt_graph），是一个ROS GUI工具，能够以可视化的形式展示ROS节点之间的相互连接关系，

### RViz三维可视化工具
RViz（http://wiki.ros.org/rviz）是ROS提供的三维可视化工具之一，可以将ROS话题和参数中的数值以二维或三维的形式可视化。RViz主要用于各类数据的可视化，如机器人模型、机器人三维变换数据（TF）、点云、激光和图像数据，以及其他各种不同的传感器数据。

**注意** rviz通过话题可视化数据时，需要指定frame_id坐标系名，可以通过`rosrun rqt_tf_tree rqt_tf_tree`查看所有可以互相转换的坐标系名。

### rospack
```
USAGE: rospack <command> [options] [package]
  Allowed commands:
    help
    depends           [package] (alias: deps)
    export [--deps-only] --lang=<lang> --attrib=<attrib> [package]
    find [package]  # 找到包所在位置
    list            # 列出所有包
    plugins --attrib=<attrib> [--top=<toppkg>] [package]
    profile [--length=<length>] [--zombie-only]
    rosdep  [package] (alias: rosdeps)
    vcs  [package]

 If [package] is omitted, the current working directory
 is used (if it contains a package.xml or manifest.xml).
```
### rostopic

1. `rostopic list`显示当前所有活动话题
`rostopic list -v`显示当前所有活动话题的详细信息

```
C:\Windows\System32>rostopic list -v

Published topics:
 * /tf_static [tf2_msgs/TFMessage] 1 publisher
Subscribed topics:
 * /tf_static [tf2_msgs/TFMessage] 1 subscriber
```
2. `rostopic info <topic_name>`查看通过指定topic话题相互通信的双方的信息：
3. `rostopic type <topic_name>`列出topic_name主题的数据类型，我们这里使用的自定义的话题通信消息文件是person.msg文件：
4. `rostopic echo <topic_name>`输出话题的消息,可以指定选项-n控制输出消息次数
5. `rostopic find <msg_name>`输出使用该消息的活动话题


### rosnode
C:\Windows\System32>rosnode help
rosnode is a command-line tool for printing information about ROS Nodes.

Commands:
        rosnode ping    test connectivity to node
        rosnode list    list active nodes
        rosnode info    print information about node
        rosnode machine list nodes running on a particular machine or list machines
        rosnode kill    kill a running node
        rosnode cleanup purge registration information of unreachable nodes

Type rosnode <command> -h for more detailed usage, e.g. 'rosnode ping -h'


### rosmsg
`rosmsg show <msg_name>`查看信息定义

### nodelet
多进程共用shared_ptr实现零拷贝通信,一般用于图像和点云数据传输(而不是ros默认的xml-rpc协议)


## example

#### 查看ros版本
使用`roscore`启动服务,会自动输出ros版本信息;分别为ros参数rosdistro和rosversion

#### 编译指定软件包
`catkin_make -DCATKIN_WHITELIST_PACKAGES=<pkg_name,...>`

#### 调试编译
`catkin_make -DCMAKE_BUILD_TYPE=Debug`

#### 查看tf树

生成TF树pdf `rosrun tf view_frames`
gui查看对应TF树 `rosrun rqt_tf_tree rqt_tf_tree`


#### 查看保存的map
ros标准格式的map地图由 `*.pgm`和`*.yaml`两文件构成，可以被ROS导航框架中的map_server节点直接调用。

- 其中.pgm文件本质是一张图片，可以直接使用图片查看器打开。
.yaml 保存的是地图的元数据信息，用于描述图片，内容格式如下: 
```
image: /home/wheeltec/wheeltec_robot/src/turn_on_wheeltec_robot/map/WHEELTEC.pgm  # pgm资源路径，可以是绝对路径也可以是相对路径。
resolution: 0.050000  # 图片分片率(单位: m/像素)。
origin: [-17.800000, -16.800000, 0.000000]  # 地图中左下像素的二维姿势，为（x，y，偏航），偏航为逆时针旋转（偏航= 0表示无旋转）。
negate: 0  # 是否应该颠倒 白色/黑色对应空闲/障碍物 的语义（默认值0，即白色对应空闲）
occupied_thresh: 0.65  # 占用概率大于此阈值的像素被视为完全占用。
free_thresh: 0.196  # 占用率小于此阈值的像素被视为完全空闲。
```
- map_server 中障碍物计算规则:
> 地图中的每一个像素取值在 [0,255] 之间，白色为 255，黑色为 0，该值设为 x；
> map_server 会将像素值作为判断是否是障碍物的依据，首先计算比例p = (255 - x) / 255.0，即白色为0，黑色为1 (如果negate为true，则p = x / 255.0)
> 根据步骤2计算的比例判断是否是障碍物，如果 p > occupied_thresh 那么视为障碍物，如果 p < free_thresh 那么视为无物。

#### 查看包和可执行文件位置

- 对于手动编译安装的包，你可以使用自带的rospack命令查看，并在对应的cmakelists文件查看编译的可执行文件安装路径 `rospack find <pkg_name>`
- 对与直接安装的二进制文件，可以通过catkin_find查看
```
wheeltec@wheeltec:~$ catkin_find rtabmap_ros
/opt/ros/melodic/include/rtabmap_ros
/opt/ros/melodic/lib/rtabmap_ros
/opt/ros/melodic/share/rtabmap_ros
```

## ros工作空间
可以创建多个工作空间，但ros同一时刻只支持一个工作空间运行。因此如果你使用docker搭建的ros环境，那么你应该使用tmux之类的终端复用器来打开多个窗口（而使用docker exec进入容器，需要重新配置一下ros命令的环境，并配置同一个docker网络）

### 目录结构
最顶层的catkin工作空间，它是整个ROS工程中层次最高的概念。

工作空间也就是管理和组织ROS工程项目文件的地方。其下主要的一级目录有四个：

- src：源空间
- build：编译空间
- devel：开发空间
- install：安装空间
其中，

最顶层的工作空间（可以任意命名）和 src （必须为src）文件夹是需要自己创建；
build 和 devel 文件夹由 `catkin_make` 命令自动创建；
install 文件夹由 `catkin_make install` 命令自动创建。
catkin 是 ROS 定制的编译构建系统，是对CMake的扩展，对ROS这样大体量的工程有更好的支持，同时也简化了操作。

**注意** 使用`catkin_make`编译之前一定要回到最顶层的工作空间。
**注意** 如果src中源代码改变了，需要使用`catkin_make clean`清理后在重新编译。

#### CMakeLists文件

##### find_package和catkin_package

```
## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
)
```
find_package 是 cmake 中常见的宏，用于加载 catkin 宏和指定对其他 ROS 功能包的依赖关系。
catkin_package 宏是 catkin 的宏之一，声明要传递给依赖项目的内容，生成 cmake 配置文件。也就是说它对**依赖于此功能包的其他功能包**来说具有重要作用。

#### src：源空间
存放功能包（package）。

功能包是ROS文件系统中组织程序文件的基本单元，也就是catkin编译的基本单元。
一个 package 下**必须包含CMakeLists.txt 和 package.xml 两个文件** 

CMakeLists.txt 文件中规定了功能包的编译规则，包括指定功能包名称，指定编译依赖项，指定要编译的源文件，指定要添加的消息格式文件/服务格式文件/动作格式文件，指定生成的消息/服务/动作，指定头文件搜索目录，指定链接库搜索目录，指定生成的静态链接库文件，指定需要链接的库文件，指定编译生成的可执行文件以及路径等等。
package.xml 文件定义了功能包的属性信息，包括包名，版本号，作者，编译依赖和运行依赖等。
另外，

include 和 src 分别存放头文件（*.h）和源程序文件（*.c/*.cpp等）；
scripts 存放脚本文件（比如Python文件 *.py，shell文件 *.sh）；
launch 存放 launch文件（*.launch），用于批量运行多个可执行文件；
config 存放配置文件（*.yaml等）；
此外，还有自定义的通信格式文件，包括消息（*.msg）、服务（*.srv）以及动作（*.action）。

#### build：编译空间
存放CMake和catkin的缓存信息、配置信息和其他中间文件。

#### devel：开发空间
存放编译后生成的目标文件，包括头文件、动态&静态链接库、可执行文件等。

#### install：安装空间
即开发完成后的安装包。

## ros example (自动驾驶模拟)


海龟机器人测试
`roscore`
`rosrun turtlesim turtlesim_node`
`rosrun turtlesim turtle_teleop_key`

旧
melodic
sudo apt-get install ros-kinetic-yocs-cmd-vel-mux ros-kinetic-dwa-local-planner ros-kinetic-hector-mapping



`qt.qpa.xcb: could not connect to display :0`
主机运行`xhost +`授权
### 问题

- 找不到JointTrajectoryController，报错如下：
Could not load controller, JointTrajectoryController does not exist
`sudo apt-get install ros*controller*`

- process has died [pid 20978, exit code 255, cmd /opt/ros/melodic/lib/gazebo_ros/gzserver -e ode /home/aditya/catkin_ws/src/my_simulations/world/empty_world.world __name:=gazebo __log:=
```
killall gzserver 
killall gzclient
```


- 进行Velodyne Simulator仿真时，gazebo或rviz自动退出并报错
```
Segmentation fault (core dumped)
[gazebo_gui-3] escalating to SIGTERM
```
- 解决方案：
  1. 虚拟机vmware，请确保分配的内存>=8G
  2. 在终端设置`export SVGA_VGPU10=0`或关闭虚拟机3d图形加速
> 其实，当更改SVGA_VGPU10变量时，其实只是在告诉系统OpenGL版本，尝试两种选择，然后看看哪个更适合。如果要使用此选项避免每次启动终端时都设置此变量，只需将此命令添加到.bashrc中即可。

### python 使用opencv报错
`Failed to load module "canberra-gtk-module"`
解决方案: 使用dpkg查看包`libcanberra-gtk-module`和`libcanberra-gtk3-module`是否已安装

### opencv输出警告信息
警告信息: `Couldn't connect to accessibility bus: Failed to connect to socket /tmp/dbus-fndjZZehMN: Connection refused`
`Failed to load module "canberra-gtk-module"`
解决方案: 通常你可以忽视他,或者在[到stackexchange查看该问题解决方案](https://unix.stackexchange.com/questions/230238/x-applications-warn-couldnt-connect-to-accessibility-bus-on-stderr)
如设置`export NO_AT_BRIDGE=1`忽视该警告


## ORB-SLAM仿真
[ORB-SLAM仿真博客](https://blog.csdn.net/qinqinxiansheng/article/details/115266992)

[机器人操作系统入门-MOOC课程代码示例](https://github.com/DroidAITech/ROS-Academy-for-Beginners)


(rosdep下载失败)[https://blog.csdn.net/qq_30267617/article/details/115028689]

### OBR-SLAM2构建报错

- 问题:`OpenCV > 2.4.3 not found.`
> 使用`pkg-config opencv --libs --cflags`查看opencv是否在全局包路径中
> 注意: opencv4版本之后，默认配置是不生成opencv.pc,需要在cmake的时候可以先配置一下： 
`cmake -D WITH_TBB=ON -D WITH_EIGEN=ON -D OPENCV_GENERATE_PKGCONFIG=ON  -D BUILD_DOCS=ON -D BUILD_TESTS=OFF -D BUILD_PERF_TESTS=OFF -D BUILD_EXAMPLES=OFF  -D WITH_OPENCL=OFF -D WITH_CUDA=OFF -D BUILD_opencv_gpu=OFF -D BUILD_opencv_gpuarithm=OFF -D BUILD_opencv_gpubgsegm=O -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local .`

**注意** `-D OPENCV_GENERATE_PKGCONFIG=ON`必须，用于生成opencv.pc文件

### ROS-Academy-for-Beginners运行orb-slam问题

## 轮趣科技小车

### 小车测试
收到之后测试，建议先看 【1.小车硬件介绍与遥控教程视频】。

------------------基础学习---------------------
如果您的控制相关基础比较薄弱，建议先看【 4.电机控制基础视频教程】。
如果您有一定的智能小车的基础，可以直接看【2.ROS小车视频教程】。
如果您觉得看视频比较费时间，可以直接看【3.ROS开发手册】。

【2.STM32底层开发与ROS功能教程】文件夹下的【3.ROS应用视频教程】，有快速使用教程，按照该教程可以100%顺利使用ROS，并且有ROS方面必须明白的知识讲解，是学习ROS必看的教程。
用户自行DIY搭建软件硬件环境、移植、更新源码时如果遇到问题，根目录下的【常见问题与BUG解决教程.pdf】与【3.ROS开发手册】文件夹下的【1.Ubuntu配置教程.pdf】基本都会有解决方案。

--------------------ROS开发手册怎么看------------------
如果您对ubuntu没有很多概念，建议先看 【1.Ubuntu配置教程】和【4.ROS极简概念基础】，
然后看一下【2.STM32运动底盘开发手册】，以对小车的底层部分有一个充分的认识，
最后的重点是【3.ROS开发教程】，这个建议大概过一遍之后，再边看边操作。

--------------------其他-----------------------
之后的手册建议按需查看，默认资料包里面没有放镜像文件，因为文件比较大，如有需要可随时联系我们。
有任何技术问题、售后问题请随时联系我们，必要时可联系我们远程给您操作，祝您一切顺利。
关注公众号可以获取资料更新通知哦，公众号：WHEELTEC。

### 小车ros版本
```
NAME="Ubuntu"
VERSION="18.04.5 LTS (Bionic Beaver)"

PARAMETERS
 * /rosdistro: melodic
 * /rosversion: 1.14.13
```


设备 USB\VID_0BDA&PID_B812\123456 在启动时出现问题。

驱动程序名称: netrtwlanu.inf
类 GUID: {4d36e972-e325-11ce-bfc1-08002be10318}
服务: RtlWlanu
低层筛选程序: 
高层筛选程序: vwifibus
问题: 0x0
问题状态: 0xC00000E5