# esp32
ESP32是乐鑫(Espressif Systems)推出的一个基于XMOS XS2微处理器的低功耗微控制器单片系统（SoC），具有Wi-Fi、蓝牙5.0、BLE等无线通信功能。ESP32具有丰富的外设接口，可以满足各种物联网应用场景的需求。

[乐鑫产品介绍](https://www.espressif.com.cn/zh-hans/products/modules)

[乐鑫开发文档](https://docs.espressif.com/projects/esp-idf/zh_CN/v4.2.3/esp32/)

## esp32开发环境vscode in wsl搭建

[参官方文档](https://github.com/espressif/vscode-esp-idf-extension/blob/master/docs/tutorial/basic_use.md)

1. 依赖库安装 `sudo apt-get install git wget flex bison gperf python3 python3-pip python3-setuptools cmake ninja-build ccache libffi-dev libssl-dev dfu-util`
2. 下载esp-idf仓库`git clone -b v5.2.3 --recursive https://github.com/espressif/esp-idf.git`(可以在第4步,有vscode引导)
3. 通过install脚本设置环境`cd ~/esp/esp-idf && ./install.sh esp32s2`
4. 安装vscode扩展esp-idf-extension

### vscode中esp32开发设置文件

[参官方vscode设置文件](https://github.com/espressif/vscode-esp-idf-extension/blob/master/docs/SETTINGS.md)

> 常见设置项:
```json
// .vscode/settings.json
{
  "C_Cpp.intelliSenseEngine": "default",
  "idf.adapterTargetName": "esp32s2",
  "idf.port": "/dev/ttyUSB0",  // 设备端口,window下使用idf.portWin
  "idf.openOcdConfigs": [
    "board/esp32s2-kaluga-1.cfg"
  ],  // OpenOCD的配置文件,相对于OPENOCD_SCRIPTS文件夹
  "idf.flashType": "UART", // DFU, UART or JTAG
  "idf.flashBaudRate": "115200",  //Flash烧写速率
  "idf.monitorBaudRate": "115200",  //未设置则使用sdkconfig中CONFIG_ESP_CONSOLE_UART_BAUDRATE项
}
```

## ESP32-S2-SOLO-U开发示例

开发板型号: `ESP32-S2-DevKitC-1`
模组: `ESP32-S2-SOLO-U`
介绍: ESP32-S2-SOLO-U 集成 ESP32-S2，是通用型 Wi-Fi MCU 模组，功能强大，具有丰富的外设接口，与 ESP32-WROOM 系列模组 Pin 角兼容。可用于可穿戴电子设备、智能家居等场景。
备注: 已停产
