## 常见工具

### Kvaser CAN

[驱动及SDK下载](https://www.kvaser.com/download/)

> 提供`canlib` API支持 `C/C++/Python/Java/.NET`
> 支持 CAN FD、J1939、LIN
> 开发工具: Kvaser CANKing、Kvaser Memorator

### Peak CAN

[驱动及SDK下载](https://www.peak-system.com/Drivers.523.0.html)

> 提供` PCAN-Basic` API 支持 `C/C++/C#/Python`
> 支持 CAN FD、J1939、XCP
> 开发工具: PCAN-View、PCAN-Explorer

### National Instruments (NI) CAN

[驱动及SDK下载](https://www.ni.com/en-us/support/downloads/drivers/download.ni-can.html)

## 软件模拟CAN设备

### linux

Linux 内核原生支持虚拟 `CAN(vcan)`

> 加载vcan模块,并创建一个虚拟vcan设备
```sh
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0
```

> 使用`can-utils`测试
```sh
candump vcan0  # 接收数据
cansend vcan0 123#11223344  # 发送数据
```

### window

window上的can设备软件模拟,需要相应工具实现

- PEAK PCAN-View Simulator
> PEAK 提供的 PCAN-View 软件支持 虚拟 CAN 通道（如 PCAN Simulated）
- Kvaser Virtual CAN Driver
> Kvaser 的 Kvaser Virtual CAN Driver 可创建虚拟设备（需安装 Kvaser SDK）

### python-can

使用 python-can 的 虚拟总线

[python-can虚拟接口文档](https://python-can.readthedocs.io/en/stable/virtual-interfaces.html)