## dumpbin

Microsoft COFF 二进制文件转储程序 (DUMPBIN.EXE) 显示有关通用对象文件格式 (COFF) 二进制文件的信息

> 示例:
- 查看每个文件的段节(可用于查看文件架构) `dumpbin /HEADERS <obj_file>`
- 库导出的符号(一般用于对外接口) `dumpbin /EXPORTS  ImagePack.exe`
- 二进制文件希望导入的符号(一般用于外部函数定义) `dumpbin /IMPORTS Qt5Network.dll | findstr /i "SSL"`
- obj文件内部符号 `dumpbin /SYSBOLS <obj_file>`
- 查看二进制文件的依赖库 `dumpbin /dependents <execable_file>`