# cuda(Compute Unified Device Architecture, 统一计算设备架构)

NVIDIA CUDA是一种并行计算平台和编程模型，可以在 NVIDIA GPU 上运行的程序。NVIDIA提供了linux上的cuda工具包 `nvidia-cuda-toolkit`

nvidia-cuda-toolkit 为创建高性能、GPU 加速的应用程序提供了一个开发环境。可以在 GPU 加速的嵌入式系统、桌面工作站、企业数据中心、基于云的平台和超级计算机上开发、优化和部署应用程序。包括 GPU 加速的库、调试和优化工具、C/C++ 编译器和运行时库。

## cuda环境搭建

1. 下载cuda工具包， `sudo apt install nvidia-cuda-toolkit`
2. 查看显卡类型名 `sudo lspci | grep "nvidia"`
3. 查看NVIDIA驱动是否成功安装
   - `sudo apt install nvidia-settings`
   - `nvidia-settings`
   - 显示错误消息即未安装，参nvidia驱动安装
4. 查看显卡版本, `nvidia-smi`(此命令只有安装nvidia显卡驱动后才具备)

## nvidia驱动安装

确保安装了 `nvidia-cuda-toolkit` 工具
1. 下载 [nvidia官方驱动下载](https://www.nvidia.cn/geforce/drivers)，选择lspci查看的显卡类型
2. 禁用系统自带的显卡驱动nouveau

- 查看nouveau模块是否存在
```sh
lsmod|grep "nou"
nouveau              3096576  4
mxm_wmi                12288  1 nouveau
drm_gpuvm              45056  1 nouveau
drm_exec               12288  2 drm_gpuvm,nouveau
gpu_sched              61440  1 nouveau
drm_ttm_helper         12288  1 nouveau
ttm                   110592  2 drm_ttm_helper,nouveau
drm_display_helper    237568  1 nouveau
i2c_algo_bit           16384  1 nouveau
video                  73728  1 nouveau
wmi                    28672  4 video,wmi_bmof,mxm_wmi,nouveau
```
- 备份`/etc/modprobe.d/blacklist.conf`，并在末尾添加如下：
```conf
blacklist nouveau
options nouveau modeset=0
```
- 更新initramfs镜像文件 `sudo update-initramfs -u`，会生成类似`/boot/initrd.img-6.8.0-47-generic`文件
- 重启系统
- 检查nouveau是否禁用 `lsmod|grep "nou"`无输出

3. 关闭图形模式，进入tty
   - 进入tty `sudo telinit 3`, 使用 `sudo telinit 5` 可重新打开图形模式
4. 禁用 x-window 服务
   - 查看x-window服务状态 `service gdm3 status`
   - 关闭x-window服务 `sudo service gdm3 stop`
5. 进入下载的nvidia驱动目录下，添加执行权限 `chmod u+x <nvidia_program.run>`，以root权限执行，需选项`-no-opengl-files`/`–no-x-check`
**注意** `sudo ./NVIDIA-Linux-x86_64-384.59.run –no-x-check -no-nouveau-check -no-opengl-files`
–no-opengl-files：表示只安装驱动文件，不安装OpenGL文件。这个参数不可省略，否则会导致登陆界面死循环
–no-x-check：表示安装驱动时不检查X服务
–no-nouveau-check：表示安装驱动时不检查nouveau，非必需
-Z, --disable-nouveau：禁用nouveau。此参数非必需，因为之前已经手动禁用了nouveau
--compat32-libdir 添加32位兼容，非必需
6. 使用 `nvidia-smi` 查看驱动版本，cuda版本，gpu进程信息，tty下gpu进程无，可使用`sudo telinit 5`开启xorg服务进入图形模式

**注意** 安装完成后，如果需要更新xorg.conf配置文件，参`/usr/share/doc/NVIDIA_GLX-1.0/README.txt`

## CUDNN(CUDA Deep Neural Network library, CUDA深度神经网络库)

cudnn 是一种由 NVIDIA 开发的深度学习库，它提供了一系列的 GPU 加速算法和函数，用于实现深度神经网络的训练和推理。

[cudnn安装官方文档](https://developer.nvidia.com/cudnn-downloads)

### 安装步骤
```sh
wget https://developer.download.nvidia.com/compute/cudnn/9.5.1/local_installers/cudnn-local-repo-ubuntu2404-9.5.1_1.0-1_amd64.deb
sudo dpkg -i cudnn-local-repo-ubuntu2404-9.5.1_1.0-1_amd64.deb
sudo cp /var/cudnn-local-repo-ubuntu2404-9.5.1/cudnn-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cudnn
```

### 查看cudnn版本

- 查看cudnn有无安装 `find /usr -name "cudnn.h"`
- 查看cudnn版本 `grep -i "CUDNN_MAJOR" -r /usr/include`

## CUDA 教程

[简易cuda学习笔记](./cuda_tutorial.md)