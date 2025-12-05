# nvidia

## 术语

### nvcc

### CUDA(Compute Unified Device Architecture, 统一计算设备架构)

NVIDIA 公司推出的一种并行计算平台和编程模型, 允许开发者使用一种类似于 C/C++ 的语言，直接利用 NVIDIA 的 GPU（图形处理器）来进行通用计算，而不仅仅是渲染图形

## cuda编译器

### 安装


## 示例

### 查看服务器上cuda api版本

cuda api分为 Driver API(驱动api;底层接口) 和 Running API(运行时api;高级接口基于Driver API构建) 两种
1. 使用 `nvidia-smi` 查看 `Display Driver API `版本(图形驱动)和 `CUDA Driver` 版本 (最大支持 `Running API` 版本)
2. 使用 `nvcc --version` 查看 `Running API` 版本

### 系统内核升级造成的nvidia驱动失效

```sh
# 查看当前驱动
ls /usr/src | grep nvidia
# 清理当前有问题的驱动
sudo dkms remove nvidia/555.58.02 --all

# 查看可用的驱动版本
ubuntu-drivers devices

# 安装推荐的驱动版本(即 ubuntu-drivers devices 列出的带有 recommended 标记的驱动)
sudo ubuntu-drivers install

# 或者安装特定版本（通常较新的版本兼容性更好）
sudo apt install nvidia-driver-560  # 或更新版本

sudo reboot
nvidia-smi
```

### NVIDIA驱动版本不匹配修复

```sh
# 查看当前安装的驱动
dpkg -l | grep nvidia
ls -la /usr/lib/x86_64-linux-gnu/libnvidia-ml.so*

# 查看内核实际加载的nvidia版本
cat /proc/driver/nvidia/version 

# 查看系统预期加载的nvidia版本
sudo modinfo nvidia | grep version

# 如果两这不一致, 一般是由于自动更新导致的, 查看initrd
ls -la /boot/initrd.img*
# 如果存在多个并且当前使用的`uname -r` 为/boot/initrd.img.old, 则为内核自动更新导致的

# 1. 尝试使用旧版本内核
sudo vim  /etc/default/grub
# 添加 GRUB_DEFAULT="1>2"

# 1>2释义如下
    # 0: Ubuntu
    # 1: Advanced options for Ubuntu
    # 2: Windows Boot Manager
    # 3: UEFI Firmware Settings
# 1 Advanced options for Ubuntu
# 对应的内核参 /boot/grub/grub.cof 中 menuentry 项, 从 0 开始
sudo update-grub
```