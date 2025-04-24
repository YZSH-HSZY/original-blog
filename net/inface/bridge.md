# 桥接网卡

## Usage

- 添加桥接网卡
> * 使用`iproute2`的ip命令 `ip link add name br0 type bridge`; 启用网卡`ip link set br0 up`
> * 使用`bridge-utils`的brctl命令 `brctl addbr br0`; 启用网卡`ip link set br0 up`
> 两者最终都调用 Linux 内核的桥接模块(bridge.ko)，功能无本质差异
> iproute2 是内核推荐的现代工具，直接通过 netlink 接口操作，而 bridge-utils 是旧版工具

**注意** br0用于将多个网卡连接起来, 可以理解为交换机, 还需多个tap网卡给虚拟机桥接使用, 并将多个tap网卡的master设置为br0, 从而可以使多个虚拟机组成网络互访
**注意** 桥接网卡至少需要一个设备(如 tap0 或物理网卡)加入

- 添加虚拟机使用的网卡, 一般以tap命名
> qemu为例, 以root身份和选项 `-netdev tap,id=net0,ifname=tap0,script=no,downscript=no -device usb-net,netdev=net0 ` 会自动创建tap0网卡, 之后设置桥接网卡并开启即可
- 接入桥接网卡并开启物理网卡
> * `sudo ip link set tap1 master br0`接入桥接网卡
> * `sudo ip link set tap1 up`开启物理网卡
- 使用 `bridge link` 查看桥接链接

## BUS

### VboxManage使用桥接网络无法配置

桥接网卡至少需要一个物理设备, 而VboxManage使用的桥接网络是通过驱动加入的(不会创建对应的物理设备), 因此你需要手动创建物理网卡(如tap0), 并将其加入到桥接网卡(如br0)组成桥接网络, 然后让VBoxManage的虚拟机连接到此物理网卡(tap0), 才可以正确配置桥接网络