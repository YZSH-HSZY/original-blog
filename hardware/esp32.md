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

## esptool使用
esptool 是用于乐鑫单片机的一个串行工具，用来通信和flash代码到esp单片机上。可用于esp的擦除、下载固件(bin->mcu)、提取固件(mcu->bin)等
```sh
usage: esptool [-h]
  [--chip {auto,esp8266,esp32,esp32s2,esp32s3beta2,esp32s3,esp32c3,esp32c6beta,esp32h2beta1,esp32h2beta2,esp32c2,esp32c6,esp32h2,esp32p4}]
  [--port PORT] [--baud BAUD] [--before {default_reset,usb_reset,no_reset,no_reset_no_sync}]
  [--after {hard_reset,soft_reset,no_reset,no_reset_stub}] [--no-stub] [--trace]
  [--override-vddsdio [{1.8V,1.9V,OFF}]] [--connect-attempts CONNECT_ATTEMPTS]
  {load_ram,dump_mem,read_mem,write_mem,write_flash,run,image_info,make_image,elf2image,read_mac,chip_id,flash_id,read_flash_status,write_flash_status,read_flash,verify_flash,erase_flash,erase_region,merge_bin,get_security_info,version}
```
**注意** window上，对于python3.8以下的版本，安装esptool时注册的脚本为esptool.py; 而以上版本为esptool.exe

### esptool使用示例

1. 从mcu下载代码到本地 `esptool --port <com_name> read_flash 0x0 0x400000 source_bin.bin`
2. 擦除mcu `esptool --chip esp32s2 --port <com_name> erase_flash --force`
3. 拷贝mcu上flash数据 `esptool --chip esp32s2 --port COM20 read_flash 0x0 0x400000 <output_bin>`
4. 下载代码到mcu `esptool --chip esp32s2 -b 115200 -p <com> --before default_reset --after hard_reset write_flash -z  --flash_mode dio  --flash_freq 80m --flash_size 4MB 0x1000 program/bootloader.bin 0x20000 program_path 0xA000 program/partition-table.bin 0xF000 program/ota_data_initial.bin`
5. 查看mcu信息 `esptool --chip esp32s3 --port COM21 chip_id`
6. 查看flash大小 `esptool --chip esp32s3 --port COM21 flash_id`

## espefuse

### espefuse使用示例

- 查看板子信息 `espefuse --port <com_name> summary`
- 
## ESP32加密模式

**注意** 不同版型的加密标志位不同

1. 烧写密钥
2. 烧写明文程序
3. 启用加密模式
4. 后续烧写加密后的程序

[乐鑫-esp32s2加解密文档](https://docs.espressif.com/projects/esp-idf/zh_CN/release-v5.0/esp32s2/security/flash-encryption.html#id17)

### esp32s2的SPI_BOOT_CRYPT_CNT标志位

此SPI_BOOT_CRYPT_CNT标志位默认为0b000,只能设置三次(3个bit位各置为1), 其中0b001和0b111表示加密状态, 0b000和0b011表示解密状态

> 设置SPI_BOOT_CRYPT_CNT比特位命令 `espefuse.py [--port <chip_serial_name>] burn_efuse SPI_BOOT_CRYPT_CNT`

### ESP32加密分类

1. 开发模式
2. 生产模式

**注意** 可以在开机打印信息中`[0;33mW (748) flash_encrypt: Flash encryption mode is DEVELOPMENT (not secure)[0m`查看,或者通过`espefuse -p <port> summary`获取加密项SPI_BOOT_CRYPT_CNT

### ESP32加解密工具

`espsecure encrypt_flash_data -a 0x20000 -k key.bin --aes_xts -o hello_encrypt.bin no_flash_encrypt_hello_example\hello_world.bin`

`espsecure decrypt_flash_data -k key.bin  -o not_encrypt_KC2W.bin -a 0x20000 ESP32_KC2W.bin`

## bug

### can't open port
- 检查usb端口的权限 `ll /dev/ttyUSB0`
- 通过udev为usb端口创建别名并设置权限
- 将当前用户添加至dialout组
