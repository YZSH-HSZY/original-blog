# nvidia

## 术语

### nvcc


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