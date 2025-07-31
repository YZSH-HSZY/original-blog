# objdump

GNU系列软件, 用于显示目标文件的信息

## 安装

1. 直接使用apt包安装 `apt install binutils-x86-64-linux-gnu`

## 使用

```sh
objdump [options] <obj_file>
    -s, --full-contents      显示所有段部分的完整内容(包括.rodata和.text)
```