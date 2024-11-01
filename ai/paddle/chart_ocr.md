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