# micropython

## 直接下载固件

[micropython官方下载页](https://micropython.org/download/ESP32_GENERIC_S3/)

**注意** 防止干扰写入时先擦除 `esptool.py --chip esp32s3 --port /dev/ttyACM0 erase_flash`
**注意** 全bin文件写入地址为0x0,如 `esptool.py --chip esp32s3 --port /dev/ttyACM0 write_flash -z 0 board-20210902-v1.17.bin`

## 编译安装
从[micropython官方中获取代码仓库](https://github.com/micropython/micropython/tree/v1.23.0)
[micropython官方build教程](https://github.com/micropython/micropython/wiki/Build-Troubleshooting)
[micropython文档编译构建教程](http://micropython.com.cn/en/latet/develop/gettingstarted.html)

1. 编译micropython交叉编译工具
```sh
cd mpy-cross
make
```
2. `make BOARD=... submodules`初始化子模块,BORARD指定固件运行的开发板类型
> 对于esp32-s2来说，BOARD=ESP32_GENERIC_S2
3. 编译micropython固件 `make`

## 交会解释器repl模式

1. 普通模式 normal REPL, CTRL-B
2. 原始模式 raw REPL, CTRL-A 
3. 粘贴模式 paste mode, CTRL-E

默认为普通模式，此时包含自动缩进、自动补全，在进行代码粘贴时，可能会影响解释内容。此时可以进入粘贴模式

### 示例

#### esp32s2

`(base) ubuntu@DESKTOP-UAS0QBB:~/micropython-1.23.0/ports/esp32$ make BOARD=ESP32_GENERIC_S2 -j8`

##### flash program

`/home/ubuntu/.espressif/python_env/idf5.0_py3.12_env/bin/python ../../../../../esp/v5.0.6/esp-idf/components/esptool_py/esptool/esptool.py -p /dev/ttyUSB0 -b 460800 --before default_reset --after hard_reset --chip esp32s2  write_flash --flash_mode dio --flash_size 4MB --flash_freq 80m 0x1000 build-ESP32_GENERIC_S2/bootloader/bootloader.bin 0x8000 build-ESP32_GENERIC_S2/partition_table/partition-table.bin 0x10000 build-ESP32_GENERIC_S2/micropython.bin`