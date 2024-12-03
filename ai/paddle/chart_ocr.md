# chart_ocr
这是一个海图识别的项目，用于将海图遥感图像中的数据使用ocr、det之类的模型识别处理，并结合矢量数据格式（如shp等），分割为不同的图层，进一步在qgis中进行处理，并将图层合成为海图机可以直接使用的dat数据。

关键词: paddleocr/paddledet/shp/qgis/pyqt5

```python
# 更改模型的输入尺寸
import onnxfile_path = './my.onnx'
model = onnx.load(file_path)
#model.graph.input[0].type.tensor_type.shape.dim[0].dim_param = '?'
model.graph.output[0].type.tensor_type.shape.dim[2].dim_param = '?'
model.graph.output[0].type.tensor_type.shape.dim[3].dim_param = '?'
onnx.save(model, './my_dynamic.onnx') 
```

## bug

### version `GLIBCXX_3.4.30' not found
> 问题描述: 在导入paddleocr时，报错`libstdc++.so.6: version GLIBCXX_3.4.30 not found`,但是更改`from paddleocr import PaddleOCR`导入语句的位置至第一行,此问题不会出现
> 解决方案: 这种情况是c++的运行时库缺少符号`GLIBCXX_3.4.30`,并且运行环境注入有延时(即虚拟环境和系统环境不一致),按以下步骤排查:
1. 使用 `find / -name "libstdc++.so"` 查找所有的运行时库
2. 使用 `strings /home/miniconda3/lib/libstdc++.so.6 | grep "GLIBCXX_3.4.30"` 查看是否支持指定的GLIBCXX版本
3. 对于conda环境使用 `conda install conda-forge::libstdcxx-ng` 更新libstdc++版本

**注意** libstdcxx和libstdcxx-ng的区别, libstdcxx-ng是一个新的C++标准库实现，它是由LLVM项目开发的，是libstdcxx的一个重写版本，更好的与LLVM的集成。
