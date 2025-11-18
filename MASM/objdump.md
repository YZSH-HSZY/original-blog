# objdump

GNU系列软件, 用于显示目标文件的信息

## 安装

1. 直接使用apt包安装 `apt install binutils-x86-64-linux-gnu`

## 使用

```sh
objdump [options] <obj_file>
    -s, --full-contents      显示所有段部分的完整内容(包括.rodata和.text)
    -d, --disassemble        显示执行段的汇编内容
    -D, --disassemble-all    显示所有段的汇编内容
    -g, --debugging          显示目标文件的调试信息
    -e, --debugging-tags     显示目标文件ctags样式的调试信息
    -f, --file-headers       显示整个文件头的内容
```