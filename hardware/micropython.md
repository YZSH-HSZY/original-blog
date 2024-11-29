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
2. 构建基于unix的micropython，他可在本机测试micropython，避免部署到机器上测试
```sh
cd ports/unix
make submodules
make
```
**注意** 对于子模块缺少的现象，可使用git submodule手动添加
3. 对于具有多类型版本的型号，使用 `make BOARD=... submodules`初始化子模块,BORARD指定固件运行的开发板类型
> 对于esp32-s2来说，BOARD=ESP32_GENERIC_S2
4. 编译micropython固件 `make`

**注意** 编译unix需先编译依赖子模块，对于子模块嵌套的现象，可使用 `git submodule update --init --recursive` 全部获取

## 交会解释器repl模式

1. 普通模式 normal REPL, CTRL-B
2. 原始模式 raw REPL, CTRL-A 
3. 粘贴模式 paste mode, CTRL-E

默认为普通模式，此时包含自动缩进、自动补全，在进行代码粘贴时，可能会影响解释内容。此时可以进入粘贴模式

## 示例

### esp
文件结构:
```sh
ports/esp32
    ├── boards                          # 此目录存放不同型号的单片机配置(编译时指定的类型可从此目录查看)
    ├── main_esp32
    ├── main_esp32c3
    ├── main_esp32s2
    ├── main_esp32s3
    ├── managed_components
    └── modules                         # 此目录存放自定义的mpy内建模块(包括_boot.py文件)
```
#### PWM示例
```py
def esp_python_pwm_example():
    pwm0 = PWM(Pin(0))         # create PWM object from a pin
    freq = pwm0.freq()         # get current frequency (default 5kHz)
    pwm0.freq(1000)            # set PWM frequency from 1Hz to 40MHz

    duty = pwm0.duty()         # get current duty cycle, range 0-1023 (default 512, 50%)
    pwm0.duty(256)             # set duty cycle from 0 to 1023 as a ratio duty/1023, (now 25%)

    duty_u16 = pwm0.duty_u16() # get current duty cycle, range 0-65535
    pwm0.duty_u16(2**16*3//4)  # set duty cycle from 0 to 65535 as a ratio duty_u16/65535, (now 75%)

    duty_ns = pwm0.duty_ns()   # get current pulse width in ns
    pwm0.duty_ns(250_000)      # set pulse width in nanoseconds from 0 to 1_000_000_000/freq, (now 25%)

    pwm0.deinit()              # turn off PWM on the pin

    pwm2 = PWM(Pin(2), freq=20000, duty=512)  # create and configure in one go
    print(pwm2)                               # view PWM settings
    print("The PWM2 keep..., please close in exit.")
```
**注意** 根据精度要求选择duty设置方式

#### esp32s2

`(base) ubuntu@DESKTOP-UAS0QBB:~/micropython-1.23.0/ports/esp32$ make BOARD=ESP32_GENERIC_S2 -j8`

##### flash program

`/home/ubuntu/.espressif/python_env/idf5.0_py3.12_env/bin/python ../../../../../esp/v5.0.6/esp-idf/components/esptool_py/esptool/esptool.py -p /dev/ttyUSB0 -b 460800 --before default_reset --after hard_reset --chip esp32s2  write_flash --flash_mode dio --flash_size 4MB --flash_freq 80m 0x1000 build-ESP32_GENERIC_S2/bootloader/bootloader.bin 0x8000 build-ESP32_GENERIC_S2/partition_table/partition-table.bin 0x10000 build-ESP32_GENERIC_S2/micropython.bin`

#### esp32s3

`(base) ubuntu@DESKTOP-UAS0QBB:~/micropython-1.23.0/ports/esp32$ make BOARD=ESP32_GENERIC_S3 -j8`

#####  ESP32_GENERIC_S3-20240602-v1.23.0官网固件启动
```sh
ESP-ROM:esp32s3-20210327
Build:Mar 27 2021
rst:0x1 (POWERON),boot:0x8 (SPI_FAST_FLASH_BOOT)
SPIWP:0xee
mode:DIO, clock div:1
load:0x3fce3810,len:0xf8c
load:0x403c9700,len:0xb3c
load:0x403cc700,len:0x2dd4
entry 0x403c989c
MicroPython v1.23.0 on 2024-06-02; Generic ESP32S3 module with ESP32S3
Type "help()" for more information.
>>> 
```

##### flash program

build后输出如下,其中指定了flash方式
```sh
Creating esp32s3 image...
Merged 3 ELF sections
Successfully created esp32s3 image.
Generated /home/ubuntu/work/esp/micropython-1.23.0/ports/esp32/build-ESP32_GENERIC_S3/micropython.bin

Project build complete. To flash, run this command:
/home/ubuntu/miniconda3/envs/esp_py312/bin/python ../../../../../esp/v5.0.6/esp-idf/components/esptool_py/esptool/esptool.py -p (PORT) -b 460800 --before default_reset --after no_reset --chip esp32s3  write_flash --flash_mode dio --flash_size 8MB --flash_freq 80m 0x0 build-ESP32_GENERIC_S3/bootloader/bootloader.bin 0x8000 build-ESP32_GENERIC_S3/partition_table/partition-table.bin 0x10000 build-ESP32_GENERIC_S3/micropython.bin
```
