### 图像基本操作
#### 读取图像

使用**cv.imread**()函数读取图像。图像应该在工作目录或图像的完整路径应给出。

**注意** imread方法打开文件时可能存在中文的编码错误，请用英文命名或借助numpy的fromfile方法读取值并解码imdecode(np.fromfile(,dtype=np.uint8))

第二个参数是一个标志，它指定了读取图像的方式。

|值                                 |含义   |
|-----------                        |-----------------------------|
|cv.IMREAD_COLOR(1)                 |将图像调整为 3 通道的 BGR 图像。它是默认标志。|
|cv.IMREAD_GRAYSCALE(0)             |以灰度模式加载图像|
|cv.IMREAD_UNCHANGED(-1)            |保持原格式不变|
|cv2.IMREAD_ANYDEPTH(2)             |当载入的图像深度为 16 位或者 32 位时，就返回其对应的深度图像；否则，将其转换为 8 位图像|
|cv2.IMREAD_ANYCOLOR(4)             |以任何可能的颜色格式读取图像|
|cv2.IMREAD_LOAD_GDAL(8)            |使用 gdal 驱动程序加载图像 8|
|cv2.IMREAD_REDUCED_GRAYSCALE_2     |将图像转换为单通道灰度图像，并将图像尺寸减小 1/2|
|cv2.IMREAD_REDUCED_COLOR_2         |将图像转换为 3 通道 BGR 彩色图像，并将图像尺寸减小 1/2|
|cv2.IMREAD_REDUCED_GRAYSCALE_4     |始终将图像转换为单通道灰度图像，并将图像尺寸减小为原来的 1/4|
|cv2.IMREAD_REDUCED_COLOR_4         |将图像转换为 3 通道 BGR 彩色图像，并将图像尺寸减小为原来的 1/4|
|cv2.IMREAD_REDUCED_GRAYSCALE_8     |将图像转换为单通道灰度图像，并将图像尺寸减小为原来的1/8|
|cv2.IMREAD_REDUCED_COLOR_8         |将图像转换为 3 通道 BGR 彩色图像，并将图像尺寸减小为原来的 1/8|
|cv2.IMREAD_IGNORE_ORIENTATION      |不以 EXIF 的方向为标记旋转图像|

cv.waitKey()是一个键盘绑定函数。其参数是以毫秒为单位的时间。该函数等待任何键盘事件指定的毫秒。如果您在这段时间内按下任何键，程序将继续运行。如果**0**被传递，它将无限期地等待一次敲击键。它也可以设置为检测特定的按键，（其返回键盘对应按键的anscii码）

#### 显示图像
- 函数 cv2.namedWindow(winname)用来创建指定名称的窗口
- 函数 cv2.imshow(winname, mat)用来显示图像,(可以先不创建，直接引用不存在的窗口，opencv会自动创建)
> winname 是窗口名称。
  mat 是要显示的图像。

#### 保存图像
cv2.imwrite( filename:"文件全路径", img:"图像名"[, params:"保存类型参数，可选"] )

### 图像相关概念

#### 图像的基本表示方法
分为二值图像、灰度图像、彩色图像

#### 感兴趣区域（ROI）
在图像处理过程中，我们可能会对图像的某一个特定区域感兴趣，该区域被称为感兴趣区
域（Region of Interest，ROI）。
我们可以使用python切片操作获取ROI，如`face=a[220:400,250:350]`

#### 通道操作
在 RGB 图像中，图像是由 RGB 通道三个通道构成的。需要注意的是，在
OpenCV 中，通道是按照 BGR 通道的顺序存储的。

1. 通道拆分
- 通过索引拆分,[:,:,<0,1,2>]
- 通过函数拆分,cv2.split得到 bgr通道

2. 通道合并

#### 获取图像属性

- shape:返回包含行数、列数、通道数的数组
- size:返回图像的像素数目。其值为“行×列×通道数”.

#### 掩膜/掩码

OpenCV 中的很多函数都会指定一个掩模，也被称为掩码

当使用掩模参数时，操作只会在掩模值为非空的像素点上执行，并将其他像素点的值置为0
> 换而言之，如果指定了mask，那么opencv会将图像矩阵与mask进行按位与操作。

### 图像操作

#### 图像加法

- 使用+符
- 使用cv2.add函数(可以传入两张图片或一张图片和调整数字，用于图像的整体调整)
**注意：** +符对于像素合值>255的像素，会进行mod(256)操作。而add函数则取max值255
- 图像加权和cv2.addWeighted(src1, alpha:"对于图像src1的加权系数", src2, beta:"对于图像src2的加权系数", gamma:"必选参数，不能省略，校正量，可为0")
`dst = src1×alpha + src2×beta + gamma。`
**注意：** 加权和 取饱和值（最大值），要求 src1 和 src2 必须大小、类型相同

#### 按位逻辑运算

|函数名              | 基本含义|
|--------------------|-----|
|cv2.bitwise_and()   | 按位与|
|cv2.bitwise_or()    | 按位或|
|cv2.bitwise_xor()   | 按位异或|
|cv2.bitwise_not()   | 按位取反|

#### 位平面分解

**什么是位平面**
例：8 位灰度图中，每一个像素使用 8 位二进制值来表示
`value = 𝑎7 × 27 + 𝑎6 × 26 + 𝑎5 × 25 + 𝑎4 × 24 + 𝑎3 × 23 + 𝑎2 × 22 + 𝑎1 × 21 + 𝑎0 × 20`
通过提取灰度图像像素点二进制像素值的每一比特位的组合，可以得到多个位平面图像。
> $a_7$的权重最高，所构成的位平面与原图像相关性最高，该位平面看起来通常与原图像最类似。

**如何获取位平面**

1．图像预处理
2．构造提取矩阵
3．提取位平面
```
示例：
import cv2
import numpy as np
lena=cv2.imread("lena.bmp",0)
cv2.imshow("lena",lena)
# 获取行，列数
r,c=lena.shape
# 通道数为8，存储8个位平面
x=np.zeros((r,c,8),dtype=np.uint8)
for i in range(8):
 x[:,:,i]=2**i
r=np.zeros((r,c,8),dtype=np.uint8)
for i in range(8):
 r[:,:,i]=cv2.bitwise_and(lena,x[:,:,i])
 mask=r[:,:,i]>0
 r[mask]=255
 cv2.imshow(str(i),r[:,:,i])
cv2.waitKey()
cv2.destroyAllWindows()
```
#### 图像加密与解密

1. 通过按位异或运算可以实现图像的加密和解密
> a：明文，原始数据。
b：密钥。
c：密文，通过 xor(a,b)实现。

$$
由xor(a,b)=c
,则可以得到：
xor(c,b)=a,
xor(c,a)=b
$$

#### 数字水印

**最低有效位LSB(Least Significant Bit)含义**
> 指一个二进制数中的第 0 位（即最低位）。

根据位平面分析可知，最低位平面对图像的影响权重最小，通过最低有效位信息隐藏（将一个需要隐藏的二值图像信息嵌入载体图像的最低有效位，即将载体图像的最低有效位层替换为当前需要隐藏的二值图像，从而实现将二值图像隐藏的目的。）对于载体图像的影响非常不明显，其具有较高的隐蔽性。

上述这种信息隐藏也被称为数字水印，通过该方式可以实现信息隐藏、版权认证、身份认证等功能。

### 色彩空间转换
RGB 图像是一种比较常见的色彩空间类型，除此以外还有一些其他的色彩空间，比较常见的包括 GRAY 色彩空间（灰度图像）、XYZ 色彩空间、YCrCb 色彩空间、HSV 色彩空间、HLS色彩空间、CIEL*a*b*色彩空间、CIEL*u*v*色彩空间、Bayer 色彩空间等。每个色彩空间都有自己擅长的处理问题的领域，因此，为了更方便地处理某个具体问题，就要用到色彩空间类型转换。

**颜色空间的转换都用到了如下约定：**
- 8 位图像值的范围是[0,255]。
- 16 位图像值的范围是[0,65 535]。
- 浮点数图像值的范围是[0.0~1.0]。
**注意：** 
1. 对于线性转换来说，这些取值范围是无关紧要的。但是对于非线性转换来说，输入的 RGB图像必须归一化到其对应的取值范围内，才能获取正确的转换结果。
2. 由于计算过程存在四舍五入，所以转换过程并不是精准可逆的。

#### opencv的转换函数
使用 cv2.cvtColor()函数实现色彩空间的变换
`dst = cv2.cvtColor( src, code [, dstCn] )`
dstCn 是目标图像的通道数。如果参数为默认的 0，则通道数自动通过原始输入图像和code 得到。

#### GRAY色彩空间
GRAY（灰度图像）通常指 8 位灰度图，其具有 256 个灰度级，像素值的范围是[0,255]。

当图像由 RGB 色彩空间转换为 GRAY 色彩空间时，其处理方式如下：
<center>Gray = 0.299 · 𝑅 + 0.587 · 𝐺 + 0.114 · 𝐵</center>

上述是标准的转换方式，也是 **OpenCV 中使用的转换方式**有时，也可以采用简化形式完成转换：

<center>Gray = (𝑅 + 𝐺 + 𝐵)/3</center>

当图像由 GRAY 色彩空间转换为 RGB 色彩空间时，最终所有通道的值都将是相同的，其处理方式如下：
<center>𝑅,G,B = (Gray,Gray,Gray)</center>

#### XYZ色彩空间
由CIE（International Commission on Illumination）定义的，是一种更便于计算的色彩空间，它可以与 RGB 色彩空间可通过矩阵变换相互转换。

计算公式请自行查阅。

#### YCrCb色彩空间

人眼视觉系统（HVS，Human Visual System）对颜色的敏感度要低于对亮度的敏感度。
传统的 RGB 色彩空间内，RGB 三原色具有相同的重要性，但是忽略了亮度信息。

YCrCb 色彩空间中，Y 代表光源的亮度，色度信息保存在 Cr 和 Cb 中，其中，Cr 表示红色分量信息，Cb 表示蓝色分量信息。

#### HSV色彩空间
RGB 是从硬件的角度提出的颜色模型，在与人眼匹配的过程中可能存在一定的差异，HSV色彩空间是一种面向视觉感知的颜色模型。
HSV 色彩空间从心理学和视觉的角度出发，指出人眼的色彩知觉主要包含三要素：色调（Hue，也称为色相）、饱和度（Saturation）、亮度（Value）

> 色调指光的颜色，饱和度是指色彩的深浅程度，亮度指人眼感受到的光的明暗程度。
> 在 HSV 色彩空间中，色调 H 的取值范围是[0,360]。8 位图像内每个像素点所能表示的灰度级有 2^8=256 个，所以在 8 位图像内表示 HSV 图像时，要把色调的角度值映射到[0,255]范围内。
> **注意** ：在 OpenCV 中，可以直接把色调的角度值除以 2，得到[0,180]之间的值.

#### HLS色彩空间
HLS 色彩空间包含的三要素是色调 H（Hue）、光亮度/明度 L（Lightness）、饱和度 S（Saturation）。

#### CIEL*a*b*色彩空间
CIEL*a*b*色彩空间是均匀色彩空间模型，它是面向视觉感知的颜色模型。

CIEL*a*b*色彩空间中的 L*分量用于表示像素的亮度，取值范围是[0,100]，表示从纯黑到纯白；a*分量表示从红色到绿色的范围，取值范围是[-127,127]；b*分量表示从黄色到蓝色的范围，取值范围是[-127,127]。

#### alpha 通道

RGB 色彩空间三个通道的基础上，还可以加上一个 A 通道，也叫 alpha 通道，表示透明度。这种 4 个通道的色彩空间被称为 RGBA 色彩空间，PNG 图像是一种典型的 4 通道图像。

alpha 通道的赋值范围是[0, 1]，或者[0, 255]，表示从透明到不透明。

### 图像变换
几何变换是指将一幅图像映射到另外一幅图像内的操作。

根据OpenCV 函数的不同，将映射关系划分为缩放、翻转、仿射变换、透视、重映射等。

#### 通过inRange函数锁定特定值
对颜色的锁定一般通过HSV空间处理，因为HSV空间只有一个通道与颜色相关。
```
dst = cv2.inRange( src, lowerb, upperb )
式中：
- dst 表示输出结果，大小和 src 一致。
- src 表示要检查的数组或图像。
- lowerb 表示范围下界。
- upperb 表示范围上界。
返回src对于掩码mask
```

#### 缩放
```
dst = cv2.resize( src, dsize[, fx[, fy[, interpolation]]] )
式中：
- dst 代表输出的目标图像，该图像的类型与 src 相同，其大小为 dsize（当该值非零时），
或者可以通过 src.size()、fx、fy 计算得到。
- src 代表需要缩放的原始图像。
- dsize 代表输出图像大小。
- fx 代表水平方向的缩放比例。
- fy 代表垂直方向的缩放比例。
- interpolation 代表插值方式

注意：目标图像的大小可以通过“参数 dsize”或者“参数 fx 和 fy”二者之一来指定
```