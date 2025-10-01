# nvidia

## 术语

### nvcc

### CUDA(Compute Unified Device Architecture, 统一计算设备架构)

NVIDIA 公司推出的一种并行计算平台和编程模型, 允许开发者使用一种类似于 C/C++ 的语言，直接利用 NVIDIA 的 GPU（图形处理器）来进行通用计算，而不仅仅是渲染图形

## cuda编译器

### 安装


## 示例

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