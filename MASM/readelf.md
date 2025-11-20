# readelf

显示ELF(执行链接文件)信息

## 选项
```sh
    -s --syms            显示符号表, 如果符号有与相关联的版本信息, 也会显示出来, 如 foo@VER_1, 无版本的符号项默认使用 foo@@VER_2
     --symbols           An alias for --syms
     --dyn-syms          Display the dynamic symbol table
     --lto-syms          Display LTO symbol tables
     --sym-base=[0|8|10|16] 
                         Force base for symbol sizes.  The options are 
                         mixed (the default), octal, decimal, hexadecimal.
    
```

## example

- 查看可执行文件运行平台: `readelf -h <exec_file_path>`
- 查看so文件需要的动态库: `readelf -d <file_path>`
- 查看是否存在调试信息(静态库等同):`readelf -S <elf_file> | grep "debug"`