# BMP
Windows 的图形设备接口(GDI)，在 Windows 1.0 开始便支持位图。但此时的位图并不是上方所说的BMP，而是"GDI位图对象"，也被称为"设备相关位图"(Device-dependent bitmap，DDB)。

到了20世纪80年代中期，微软与IBM合作开发的操作系统 OS/2 1.1 版本中定义了 DIB 格式，这就是起源处。OS/2 1.1 于 1988 年发布，是第一个拥有像 Windows 一样的图形用户界面(Presentation Manager, PM)的 OS/2 版本。PM包含一套图形编程接口，其中定义了位图的格式。

Windows 3.0(1990年发布)引入"设备无关位图"的概念(Device-independent bitmap，DIB)，这时才被称作DIB。从这可以看出DIB是在GDI位图对象(DDB)之后才出现的。DIB包含了自身的颜色表，显示每个像素位怎样对应到RGB颜色，DIB能被显示在任何点阵输出设备上。唯一的问题是DIB的颜色经常必须被转换为设备实际能处理的颜色。DDB与DIB在某些方面存在一定联系，如它们之间可以相互转换，只不过会丢失一些数据。因此两者不能相互代替，且DDB在Windows上至今仍占据着重要地位，特别当你很在乎性能时。

Windows 3.0 还包含了最初DIB格式的一个变形，也就是文章前半部分所介绍的版本。它最后成为了Windows环境下的标准。之后的 Windows 95，Windows NT 4.0 以及后来的 Windows 98，Windows NT 5.0 又在此基础上做了一些改进，诞生出 V4，V5 两个版本。目前DIB共 5 个版本。

DIB文件的扩展名是BMP，但在极个别的情况下也可以是DIB。ICON(图标)和CUR(光标)也是DIB文件，只不过有一些微小的不同。程序可将DIB文件除去开始的 14 个字节(文件头)外，整个载入到一块连续的内存区域中，这也被称为"紧凑DIB格式的位图"(Packed-DIB Format)。 


## BMP文件结构
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
    * `biCompression(4bytes)`: 压缩类型(0: 无压缩，1: RLE-8，2: RLE-4，3: BITFIELDS)
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
    * **注意** BMP图像格式中，像素数据以"自下而上"，"从左至右" 顺序存储

**注意** BMP文件格式有多种变体，包括OS/2 BMP、Windows BMP和OS X BMP等。这些变体之间的差异主要在于文件头和信息头的格式
**注意** 如果BMP的 `biWidth*biHeight*biBitCount/8 != biSizeImage`, 一般是将每行的像素存储字节扩大为4的倍数, 计算公式如: 

$$ RowLength = 4 * \lfloor \frac{biWidth*biBitCount + 31}{32} \rfloor $$
$$ biSizeImage = RowLength * biHeight $$

## BMP压缩类型
- 0: 无压缩（BI_RGB）
- 1: RLE8 压缩（8 位位图）
- 2: RLE4 压缩（4 位位图）
- 3: BITFIELDS 压缩（16 位或 32 位位图）
通过 -compress None，ImageMagick 会将压缩方式设置为 0（无压缩）。

## BMP版本
BMP共有V1/V2/V3/V4/V5五个版本,通过 `bmp_info_header` 的 `biSize` 字段区分
```c
// =================================================
// OS/2 V1
// GDI 支持: OS/2 及 Windows 3.0 以上的 Windows 版本
// =================================================
typedef struct tagBITMAPCOREHEADER { // 12 字节
  DWORD bcSize;
  WORD  bcWidth;
  WORD  bcHeight;
  WORD  bcPlanes;
  WORD  bcBitCount;
} BITMAPCOREHEADER, FAR *LPBITMAPCOREHEADER, *PBITMAPCOREHEADER;



// =================================================
// OS/2 V2
// GDI 支持: !∑(°ω° )
// =================================================
typedef struct tagBITMAPCOREHEADER2 { // 64 字节

};



// =================================================
// Windows V3
// GDI 支持: Windows 3.0 以上的Windows版本
// =================================================
typedef struct tagBITMAPINFOHEADER { // 40 字节
  DWORD  biSize;
  LONG   biWidth;
  LONG   biHeight;
  WORD   biPlanes;
  WORD   biBitCount;
  DWORD  biCompression;
  DWORD  biSizeImage;
  LONG   biXPelsPerMeter;
  LONG   biYPelsPerMeter;
  DWORD  biClrUsed;
  DWORD  biClrImportant;
} BITMAPINFOHEADER, FAR *LPBITMAPINFOHEADER, *PBITMAPINFOHEADER;



// =================================================
// Windows V4
// GDI 支持: Windows 95/NT 4 以上的 Windows 版本
// =================================================
typedef struct { // 108 字节
  DWORD        bV4Size;
  LONG         bV4Width;
  LONG         bV4Height;
  WORD         bV4Planes;
  WORD         bV4BitCount;
  DWORD        bV4V4Compression;
  DWORD        bV4SizeImage;
  LONG         bV4XPelsPerMeter;
  LONG         bV4YPelsPerMeter;
  DWORD        bV4ClrUsed;
  DWORD        bV4ClrImportant;
  DWORD        bV4RedMask;   // 红色遮罩
  DWORD        bV4GreenMask; // 绿色遮罩
  DWORD        bV4BlueMask;  // 蓝色遮罩
  DWORD        bV4AlphaMask; // 阿尔法遮罩
  DWORD        bV4CSType;    // 色彩空间类型
  CIEXYZTRIPLE bV4Endpoints; // XYZ值
  DWORD        bV4GammaRed;  // 红色伽马值
  DWORD        bV4GammaGreen;// 绿色伽马值
  DWORD        bV4GammaBlue; // 蓝色伽马值
} BITMAPV4HEADER, FAR *LPBITMAPV4HEADER, *PBITMAPV4HEADER;



// =================================================
// Windows V5
// GDI 支持: Windows 98/2000 及其新版本
// =================================================
typedef struct { // 124 字节
  DWORD        bV5Size;
  LONG         bV5Width;
  LONG         bV5Height;
  WORD         bV5Planes;
  WORD         bV5BitCount;
  DWORD        bV5Compression;
  DWORD        bV5SizeImage;
  LONG         bV5XPelsPerMeter;
  LONG         bV5YPelsPerMeter;
  DWORD        bV5ClrUsed;
  DWORD        bV5ClrImportant;
  DWORD        bV5RedMask;
  DWORD        bV5GreenMask;
  DWORD        bV5BlueMask;
  DWORD        bV5AlphaMask;
  DWORD        bV5CSType;
  CIEXYZTRIPLE bV5Endpoints;
  DWORD        bV5GammaRed;
  DWORD        bV5GammaGreen;
  DWORD        bV5GammaBlue;
  DWORD        bV5Intent;      // 渲染意图
  DWORD        bV5ProfileData; // 颜色配置数据或文件名(偏移量)
  DWORD        bV5ProfileSize; // 内嵌数据或文件名的大小
  DWORD        bV5Reserved;    // 保留
} BITMAPV5HEADER, FAR *LPBITMAPV5HEADER, *PBITMAPV5HEADER; 
```
## example

### bmp 24 bit to 16 bit

> magick 7
`magick .\det_icons_2\H01_4.bmp -define bmp:format=bmp4 -compress none -define bmp:subtype=rgb565 H01_4.bmp`
`magick input.bmp -depth 16 -compress none output.bmp`

> magick 6
- 8bit bmp-->16bit bmp: `convert-im6.q16 pre_icon/T042_5.bmp -define bmp:format=bmp3 -define bmp:compression=0 -define bmp:subtype=rgb565 -type truecolor ./TT.bmp`

- 4bit bmp-->16bit bmp: `ffmpeg -i pre_icon/T007_2.bmp -pix_fmt rgb565 ./T007_2.bmp`

> 使用greenfish图标编辑器: **注意** 1.4版本的位深度转换无效,请使用更高版本(如4.4)

[greenfish软件下载页](https://greenfishsoftware.org/gfie.php)