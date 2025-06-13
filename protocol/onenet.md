# OneNet
NMEA OneNet是一个用于海洋电子设备的IP网络标准

参[nmea归档网页](https://web.archive.org/web/20210418034919/https://www.nmea.org/Assets/)

## 专用术语

- CAN(Controller Area Network):
- Headless Device:
- HID(Human Interface Device)
- Mapped
- Native
- NMEA2000 Virtual Device 
- NMEA NAME
- OneNet Application
- OneNet Datagram Service
- OneNet Device 
- OneNet Network
- OneNet Secure Network
- PGN 
- PGN Message
- PGN Virtual Device

## chapter

### 消息传输

> 多播消息
OneNet 的多播地址范围从 `ff02::160` 到 `ff02::16f` , UDP 端口号 `10111` 由 IANA 分配。多播地址范围从`ff02::161`到`ff02::16f`被限制用于未来的 OneNet 分配。

多播消息应从数据报服务端口发送到端口10111和适当的目标多播地址。 在本版本的OneNet标准中，所有多播消
息的目标地址应为ff02::160。

> 单播消息
单播消息应从数据报服务端口发送到目标数据报服务的OneNet应用程序和数据报服务端口的IPv6地址

### Discovery侦测组件
#### 要求
1. 每个OneNet设备应管理一个DNS-SD响应器, 处理多播MDNS消息(响应器检查接受ipv6源地址和本地链路子网是否匹配, 不匹配忽略)
2. 设备提供服用需要广播相关端口
3. 提供OneNet网络上唯一标识的ID
    - `#`被保留,不得使用
    - 格式如`<any>-<number>`
    - 使用时保持持久
4. 提供缓存机制
OneNet程序必须提供id

### 数据报安全

#### 加密PGN消息

> OneNet Encrypted PGN Format:
- `OneNet Fixed Header`: 31 4e 45 54 00 01 00 00(8 bytes=4B SIGNATURE:`1NET`+2B VERSION: `0x0001`+2B MessageSequenceNumber`0x0000`递增)

## OneNet Certification Test Tool

测试程序用于确保应用程序和设备符合NMEA OneNet标准的要求。不涉及设计、构建和测试NMEA OneNet设备的所有方面。相反，目标是确定并提供测试NMEA OneNet标准中特定需求的程序，这些需求对于实现一致和适当的网络行为至关重要。这些测试程序将在NMEA OneNet认证测试(CT)工具中实施。

### 术语
- CT: 认证工具-执行本文件中确定的测试程序的设备组合
- DUT: 测试设备—运行一个或多个OneNet应用程序的OneNet设备或通用计算设备
- PT-n: 测试前信息—手工添加的被测件DUT的产品信息, 由制造商在运行任何认证测试程序之前添加的。索引n标识引用的信息。

### OneNet测试过程

OneNet测试过程是认证测试工具(CT)和一个或多个OneNet应用程序(也称为被测设备DUT)之间的完整交互。测试程序会导致DUT在记录和评估响应报文时从一个已知状态过渡到另一个已知状态。

> 测试程序将包括:
> - 将DUT初始化为已知状态的说明
> - 请求测试DUT的一种或多种方法:
>   * 在OneNet网络上传输特定数据
>   * 在NMEA 2000网络上传输特定数据
>   * 在NMEA 0183串行端口上传输特定数据
>   * 通过手动操作或DUT本身的特定操作
> - 如果不能通过请求达到要求, 用户必须证明DUT符合规范要求
> - 请求和响应记录下来, 然后评估以确定测试程序结果

**测试过程**

> 单个测试过程可能涉及几个步骤，每个步骤可能有一个或多个所需的响应。在某些测试程序中，响应将是视觉或听觉响应，并且需要测试操作员确认该响应的发生。

每个测试过程包括:
- Requirement Under Test(测试要求)
- Preconditions(先决条件)
- Postconditions(后置条件)
- Procedure(过程)