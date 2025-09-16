## dumpbin

Microsoft COFF(Common Object File Format) 二进制文件转储程序 (DUMPBIN.EXE) 显示有关通用对象文件格式 (COFF) 二进制文件的信息

> 示例:
- 查看每个文件的段节(可用于查看文件架构) `dumpbin /HEADERS <obj_file>`
- 库导出的符号(一般用于对外接口) `dumpbin /EXPORTS  ImagePack.exe`
- 二进制文件希望导入的符号(一般用于外部函数定义) `dumpbin /IMPORTS Qt5Network.dll | findstr /i "SSL"`
- obj文件内部符号 `dumpbin /SYMBOLS <obj_file>`
- 查看二进制文件的依赖库 `dumpbin /dependents <execable_file>`


### COFF SYMBOL TABLE

使用 `dumpbin /symbols <obj>` 查看COFF文件的符号表, 每行数据如下:
- 索引值: 符号表的索引号
- 值/地址: 符号在节内的偏移量
- 符号位置
- 存储类型
- 符号类型: `External`(外部可见的, 可被其他目标文件或库看到和链接)/`Static`(文件局部:静态, 只在当前目标文件内部使用, 链接器会忽略它), 
- 符号名