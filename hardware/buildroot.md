# buildroot
Buildroot 是一个简单、高效且易于使用的工具，通过交叉编译生成嵌入式 Linux 系统。
它可以将一个BSD系统的各部分集成到一起，从而简化嵌入式linux开发。
> 包括工具链toolchain、rootfs、kernel、引导加载程序bootloader等

**注意** buildroot构建的根文件系统, 相较于busybox更全, 并且可以直接使用

[buildroot主页](https://buildroot.org/)

## External toolchain 

- 查看交叉工具链使用的linux headers版本 `grep -r "LINUX_VERSION_CODE" /opt/gcc-linaro-5.3.1-2016.05-x86_64_arm-linux-gnueabi`
> 输出如下: `/opt/gcc-linaro-5.3.1-2016.05-x86_64_arm-linux-gnueabi/arm-linux-gnueabi/libc/usr/include/linux/version.h:#define LINUX_VERSION_CODE 262144`
> 其中 `262144` 及为linux headers版本, 计算方法如下:
> 主版本号 (M): `LINUX_VERSION_CODE >> 16 & 0xFF`
> 次版本号 (m): `LINUX_VERSION_CODE >> 8 & 0xFF`
> 补丁版本号 §: `LINUX_VERSION_CODE & 0xFF`

- 判断toolchain版本, `/opt/gcc-linaro-5.3.1-2016.05-x86_64_arm-linux-gnueabi/bin/arm-linux-gnueabi-gcc -v` 
- 判断toolchain使用的是libc还是uclibc, `strings -a /opt/gcc-linaro-5.3.1-2016.05-x86_64_arm-linux-gnueabi/bin/arm-linux-gnueabi-gcc | grep -i "uclibc"` 有输出一般为uclibc

