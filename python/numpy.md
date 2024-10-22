# numpy介绍
## numpy中的数组、向量、矩阵
numpy中array,vertor,matrix虽然可以相互转换，但他们仍是不同的概念，在进行运算时请区分它们。
### N 维数组对象 ndarray

- NumPy 最重要的一个特点是其 N 维数组对象 ndarray，它是一系列同类型数据的集合，以 0 下标为开始进行集合中元素的索引。
- ndarray 对象是用于**存放同类型元素的多维数组**。
- ndarray 中的每个元素在内存中都有**相同存储大小**的区域。
  
#### 创建ndarray
```
np.empty(       np.empty_like(  # 创建空数组，值随机,使用shape指定形状
np.zeros(      np.zeros_like(   # 创建全0数组，使用shape指定形状
np.ones(      np.ones_like(     # 创建全1数组，使用shape指定形状
np.identity(    np.eye(         # identity创建二维单位数组，eye创建二维数组，主对角线填1，可使用参数k偏移填充的对角线
```

#### ndarray的属性

|属性               |说明                   |
|-------------------|-----------------------|
|ndarray.ndim	    |数组的维度数|
|ndarray.shape	    |数组的形状,是一个len==ndim的tuple，对于矩阵，(n行,m列)|
|ndarray.size	    |数组元素的总个数，相当于 .shape 中 各项相乘|
|ndarray.dtype	    |ndarray 对象的元素类型|
|ndarray.itemsize	|ndarray 对象中每个元素的大小，以字节为单位|
|ndarray.flags	    |ndarray 对象的内存信息|
|ndarray.real	    |ndarray元素的实部|
|ndarray.imag	    |ndarray 元素的虚部|
|ndarray.data	    |包含实际数组元素的缓冲区，由于一般通过数组的索引获取元素，所以通常不需要使用这个属性。|

### numpy的矩阵库matlib
NumPy 中包含了一个矩阵库 numpy.matlib，该模块中的函数返回的是一个矩阵，而不是 ndarray 对象。NumPy中一个矩阵是二维的，由 m行（row）n列（column）元素构成。

**注意** ：
1. 区分numpy中矩阵和线性代数中矩阵求解（即向量组）的概念，二者不等同。
2. numpy中矩阵都是二维的

#### 矩阵相乘np.dot和@
在 Python 3.5 之前，使用数组类型的唯一缺点是您必须使用 dot 而不是 * 乘法（约简）两个张量（标量积、矩阵向量乘法等）。从 Python 3.5 开始，您可以使用矩阵乘 @ 法运算符。

## NumPy 广播机制(Broadcast)
广播(Broadcast)是 numpy 对不同形状(shape)的数组进行数值计算的方式， 对数组的算术运算通常在相应的元素上进行。

如果两个数组 a 和 b 形状相同，即满足 a.shape == b.shape，那么 a*b 的结果就是 a 与 b 数组对应位相乘。这要求维数相同，且各维度的长度相同。

## numpy序列化

### 解包
numpy在加载时会自动解包，示例：
- `np.frombuffer(binary_data[start: end], dtype="<u2,(3,)B")`
- `np.frombuffer(binary_data[start: end], dtype=[('name_1, np.uint, (2,)'),(name_2, np.uint)]`

**注意** dtype为字符串时，默认以`f<index>`为元素名，如`f0`

## dtype
|单字符 | 描述                                            |
|-------|------------------------------------------------|
`?`     | boolean                                        |
`b`     | (signed) byte                                  |
`B`     | unsigned byte                                  |
`i`     | (signed) integer                               |
`u`     | unsigned integer                               |
`f`     | floating-point                                 |
`c`     | complex-floating point                         |
`m`     | timedelta                                      |
`M`     | datetime                                       |
`O`     | (Python) objects                               |
`S`/`a` | zero-terminated bytes (not recommended)        |
`U`     | Unicode string                                 |
`V`     | raw data (void)                                |

**注意** 对于字符串来说，你可以通过 `'<(7,)u1'`/`'<S7'`/`'<V7'`进行解包，区别在于使用字节数组`u`/二进制数据`V`时需要调用`tobytes`转换为python的bytes，再decode获取。`S`对于以`0x00`结尾的字节串会自动移除他们。

## C/F顺序与大小端
C/F顺序指的是numpy元素在内存中的存储顺序，而大小端指的是元素的字节在内存中的存储顺序
C order 指的是 Row-major Order（按行存储）
F order 指的是 Column-major Order（按列存储）
小端 指的是 元素的高位存在内存的高位
大端 指的是 元素的高位存在内存的低位
```
example:
一个(2,3),uint16矩阵
[[1,2,3],
 [6,7,8]]
C序小端存储0x01 0x00,0x02 0x00,0x03 0x00,0x06 0x00,0x07 0x00,0x08 0x00
F序大端存储0x00 0x01,0x00 0x06,0x00 0x02,0x00 0x07,0x00 0x03,0x00 0x08
```
## numpy examples

### numpy char字符数组
#### 字符串居中
```
>>> print(np.char.center('Runoob', 20,fillchar = '*'))
*******Runoob*******
```
函数用于将字符串居中，并使用指定字符在左侧和右侧进行填充，不足截断

#### numpy拼接数组
`np.concatenate`
> concatenate((a1, a2, ...), axis=0, out=None, dtype=None, casting="same_kind")
> 延指定轴拼接数组，使用axis指定轴，例：ndarray.shape==(height,width,channels)的三维数组，axis=0默认在ndarray[end]添加(width,channels)
> **数组必须具有相同的形状**，尺寸可不同。 
> axis 数组将沿其指定的轴连接。如果axis为None，则数组在使用前被扁平化(转为一维数组)。默认为0。
> out 如果提供，则存放结果的目的地。形状必须是正确的，与未指定out参数时concatenate返回的形状相匹配。 
> dtype:str 如果提供，目标数组将具有此dtype。不能和out一起提供。

