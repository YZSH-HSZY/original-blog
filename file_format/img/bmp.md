# BMP
BMP（Bitmap）是一种图像文件格式，文件结构如下：

- `file_header(14 bytes)`
    * `bfType(2 bytes)`: 文件类型，必须为 `BM(0x424d)`
    * `bfSize(4 bytes)`: 文件大小(bytes)
    * `bfReserved1(2 bytes)`: 保留字段，必须为0
    * `bfReserved2(2 bytes)`: 保留字段，必须为0
    * `bfOffBits(4 bytes)`: 图像数据偏移量(bytes)，一般为54
- `bmp_info_header(40 bytes)`
    * `biSize(4bytes)`: 信息头大小(bytes)
    * `biWidth(4bytes)`: 图像宽度(像素)
    * `biHeight(4bytes)`: 图像高度(像素)
    * `biPlanes(2bytes)`: 颜色平面数，必须为1
    * `biBitCount(2bytes)`: 每像素位数(1、4、8、16、24或32)
    * `biCompression(4bytes)`: 压缩类型(0: 无压缩，1: RLE-8，2: RLE-4)
    * `biSizeImage(4bytes)`: 图像数据大小(bytes)
    * `biXPelsPerMeter(4bytes)`: 水平分辨率(像素/米)
    * `biYPelsPerMeter(4bytes)`: 垂直分辨率(像素/米)
    * `biClrUsed(4bytes)`: 颜色表中使用的颜色数
    * `biClrImportant(4bytes)`: 重要颜色数
- `颜色表(optional)`
    * **注意** 如果biBitCount小于16，则颜色表是必须的
    * 颜色表中的每个颜色由一个RGBQUAD结构表示
- `图像数据`
    * 数据按行存储，行尾可能有填充字节以使行长度为4的倍数
    * **注意** BMP图像格式中，像素数据以自下而上的格式存储

**注意** BMP文件格式有多种变体，包括OS/2 BMP、Windows BMP和OS X BMP等。这些变体之间的差异主要在于文件头和信息头的格式