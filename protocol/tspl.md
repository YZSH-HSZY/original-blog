# TSPL

TSPL(TSC Printer Command Language) 是一种打印机指令语言, 由台湾 `TSC Printronix` 公司 为其热转印/热敏条码打印机开发的一套指令集或编程语言。

## 指令

### SIZE

设定卷标纸的宽度和长度, 如`SIZE 23 mm, 10 mm`

### GAP

定义两张卷标纸间的垂直间距距离, 如 `GAP 2 mm`

### CLS

用于清除图像缓冲区(image buffer)的数据.

**注意** 此项指令必须置于SIZE指令之后

### DIRECTION

设置打印的方向, 0水平/1垂直, 如 `DIRECTION 1`

### TEXT

打印文本字符串, 语法如下:

`TEXT x,y,"font",rotation,x-multiplication,y-multiplication,"content"`

### BARCODE

绘制一维条码, 如法如下:
`BARCODE x,y,"code type",height,human readable,rotation,narrow,wide,"content"`

**注意** 这里的x/y/height均以dot位单位, (200 DPI: 1 點=1/8 mm, 300 DPI: 1 點=1/12 mm)

### PRINT

设置打印份数和每份重复次数, 如 `PRINT 1,1`

## example

### 打印简易文本和条码的示例
```sh
SIZE 100 mm,50 mm
GAP 2 mm,0
CLS
TEXT 100,50,"TSS24.BF2",0,1,1,"Hello TSPL"
BARCODE 100,100,"128",100,1,0,2,2,"12345678"
PRINT 1
```

### 设置撕纸打印

`SET TEAR ON`