# qemu
QEMU 是一个通用的开源机器仿真器和虚拟化器。
> 可以通过 System Emulation(系统仿真)/User Mode Emulation(用户模式仿真)
> - System Emulation: 提供整台机器（CPU、内存和模拟设备）的虚拟模型来运行来os，可完全模拟/也可和虚拟机管理程序配套使用
> - User Mode Emulation: 可启动另一架构CPU编译的程序
> QEMU 还提供了许多独立的命令行实用程序，例如qemu-img用于创建、转换和修改磁盘映像的磁盘映像实用程序

## 术语

### PCI(Peripheral Component Interconnect, 外围设备互连)

PCI是一种计算机总线标准，用于连接计算机主板和外部设备，如显卡、网卡、声卡等。在 X86 硬件体系结构中几乎所有的设备都以各种形式连接到 PCI 设备树上

PCI三个基本组件:
- PCI 设备(device): 符合 PCI 总线标准的设备都可以称之为 PCI 设备，在一个 PCI 总线上可以包含多个 
- PCI 总线(bus): 用以连接多个 PCI 设备与多个 PCI 桥的通信干道
- PCI 桥(bridge): 总线之间的连接枢纽，主要有以下三:
    1. `HOST/PCI bridge`: 也称为 PCI 主桥或者 PCI 总线控制器，用以连接 CPU 与 PCI 根总线，隔离设备地址空间与存储器地址空间，现代 PC 通常还会在其中集成内存控制器，称之为北桥芯片组(North Bridge Chipset)
    2. `PCI/ISA bridge`: 用于连接旧的 ISA 总线，通常还会集成中断控制器(如 i8359A)，称之为南桥芯片组(South Bridge Chipset)
    3. `PCI-to-PCI bridge`: 用于连接 PCI 主总线(Primary Bus)与次总线(Secondary Bus)

## 选项

```sh
Options:
    -machine [type=]name[,prop=value[,...]]
        按名称选择模拟机器。使用-machine help来列出可用的机器
    -nographic
        使用此选项，可以完全禁用图形输出，以便QEMU成为一个简单的命令行应用程序。模拟串口在控制台上被重定向，并与显示器混合（除非在其他地方显式重定向）。因此，您仍然可以使用QEMU调试带有串行控制台的Linux内核。
网络选项:
    -netdev user,id=id[,option][,option][,...]
        配置用户模式主机网络后端，不需要管理员权限即可运行
        可选选项:
            ipv4=on|off and ipv6=on|off
                指定IPv4或IPv6是否启用,如果不指定，则同时启用两个协议
            net=addr[/mask]
                设置网络地址,默认是10.0.2.0/24
            host=addr
                设置IP地址,默认是x.x.x.2
            ipv6-net=addr[/int], 默认fec0::/64
            ipv6-host=addr, 默认xxxx::2
            # hostfwd=[tcp|udp]:[hostaddr]:hostport-[guestaddr]:guestport
    
```

## example

### qemu多台虚拟机互联
```sh
# 首先创建一个桥接网络(宿主机上执行)
sudo ip link add name br0 type bridge
sudo ip link set br0 up
# 启动第一个虚拟机
sudo qemu-system-arm --machine raspi2b --cpu arm1176 \
  -m 1024m --drive format=raw,file=/sdcard/filesystem1.img \
  -netdev tap,id=net0,ifname=tap0,script=no,downscript=no \
  -device usb-net,netdev=net0 \
  --dtb /fat/bcm2709-rpi-2-b.dtb --kernel /fat/kernel7.img \
  --append "rw console=ttyAMA0,115200 root=/dev/mmcblk0p2 rootwait" \
  --no-reboot --display none --serial mon:stdio
...
# 然后将 tap 设备连接到桥接(宿主机上执行)
sudo ip link set tap0 master br0
sudo ip link set tap1 master br0
sudo ip link set tap0 up
sudo ip link set tap1 up
```