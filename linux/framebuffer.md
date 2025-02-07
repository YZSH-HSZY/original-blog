# FrameBuffer
FrameBuffer帧缓冲驱动, 是linux抽象出一个fb设备来供用户态进程实现直接写屏. 是对显卡硬件的一层抽象，可以看作是一个显示内存的映射

[参野火fb文档](https://doc.embedfire.com/linux/rk356x/linux_base/zh/latest/linux_app/framebuffer/framebuffer.html)

## 查看fb设备
1. `ls /dev/fb*`
2. `cat /proc/fb`


## bug

### linux上无/dev/fb设备

> 通过以下方法尝试解决:
- 检查linux内核是否开启fb设备支持功能 `lsmod | grep "fb"`, 尝试重新编译内核或尝试以下其他方法
    > 下载内核代码; `make menuconfig` 配置内核编译选项, 开启 `Device Drivers->Graphics Support-->Support for frame buffer devices`; 安装内核 `make install`, 安装模块 `make moudels_install`; 制作initrd镜像(为boot loader初始化的内存盘); 修改/boot/grub/meun.lst配置菜单
- 手动创建字符设备 `mknod /dev/fb0 c 29 0 && mknod /dev/fb1 c 29 1`
- 修改内核启动参数 使用 `sudo grep "spl" /boot/grub/grub.cfg` 查看splash行, 将之后的 `$vt_handof` 换为 `vga=0x315`