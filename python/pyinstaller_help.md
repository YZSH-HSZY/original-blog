# pyinstaller
pyinstaller是一个python的打包库
[官方文档](https://pyinstaller.org/en/stable/spec-files.html "spec规范文件说明")

## 选项
`-F`
### pyinstaller打包exe文件运行报错
ImportError: DLL load failed while importing win32gui: 找不到指定的模块。

**解决方法:**
在交互式命令行中，导入模块，通过__file__属性找到文件路径，在pyinstaller的spec规范文件中指定位置重新使用`pyinstaller [options] <name.spec>`打包或者直接打包时使用命令行选项指定
