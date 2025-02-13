# qemu_mock
此文件记录使用qemu模拟硬件开发板的笔记

> 参考文档:
    - [quard_star_tutorial](https://quard-star-tutorial.readthedocs.io/zh-cn/latest/)
    - [ctf-qemu](https://ctf-wiki.org/pwn/virtualization/qemu/)

## develop env

```Dockerfile
FROM ubuntu:x64_20.04
MAINTAINER qgq nothing@example.com
ENV LANG=en_US.utf8 \
    TZ=Asia/Shanghai \
    DEBIAN_FRONTEND=noninteractive
VOLUME /qemu_mock
RUN apt update && \
    apt install -y ninja-build pkg-config libglib2.0-dev && \
    apt install -y libpixman-1-dev libgtk-3-dev libcap-ng-dev libattr1-dev && \
    apt install -y libsdl2-dev device-tree-compiler bison flex gperf intltool && \
    apt install -y mtd-utils libpulse-dev libalsa-ocaml-dev libsdl2-dev libslirp-dev
CMD /bin/bash
```
- 容器构建: `docker build -t qemu_mock_ubuntu:v0.1 .`
- 运行开发容器: `docker run -it --name qemu_dev -v /home/smartwork/work/qemu_mock:/qemu_mock qemu_mock_ubuntu:v0.1`
- 下载qemu-6.0.0源码: `wget https://download.qemu.org/qemu-6.0.0.tar.xz && tar -xf qemu-6.0.0.tar.xz`
- 编译qemu: `./configure --prefix=$(pwd)/output/qemu --target-list=riscv64-softmmu --enable-gtk  --enable-virtfs --disable-gio --enable-debug`

```sh
--prefix=<path>: 指定install位置
--enable-kvm: 开启 kvm 支持
--target-list=<device_framework_name>: 指定要编译的 CPU 架构，这里指定为 riscv64-softmmu 即表示我们要编译 risc 架构的 64 位 CPU
--enable-debug: 启用qemu调试支持
--enable-<feature>: 启用指定feature支持
--disable-<feature>: 警用指定feature支持, 使用 `./configure --help` 查看可选feature
```