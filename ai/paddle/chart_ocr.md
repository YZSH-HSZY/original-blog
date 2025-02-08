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

## train dataset prepare
本项目基于paddledet目标检测框架，使用其内置的yolox模型训练框架进行部署模型的训练

paddledet 原生支持 COCO/VOC 数据集, 其他数据集格式需要进行相应转换. 

### coco数据集
Microsoft COCO数据集(Microsoft Common Objects in Context)，由微软于2014年出资标注。

COCO数据集是一个大型的、丰富的物体检测，分割和字幕数据集。这个数据集以 场景理解scene understanding 为目标，主要从复杂的日常场景中截取，图像中的目标通过精确的 分割segmentation 进行位置的标定。图像包括91类目标，328,000影像和2,500,000个label。目前为止语义分割的最大数据集，提供的类别有80 类，有超过33 万张图片，其中20 万张有标注，整个数据集中个体的数目超过150 万个。

#### COCO数据格式介绍

COCO数据标注是将所有训练图像的标注都存放到一个json文件中。数据以字典嵌套的形式存放。

> json文件中包含以下key：
- info，表示标注文件info。
- licenses，表示标注文件licenses。
- images，表示标注文件中图像信息列表，每个元素是一张图像的信息。如下为其中一张图像的信息：
```python
{
    'license': 3,                       # license
    'file_name': '000000391895.jpg',    # file_name
     # coco_url
    'coco_url': 'http://images.cocodataset.org/train2017/000000391895.jpg',
    'height': 360,                      # image height
    'width': 640,                       # image width
    'date_captured': '2013-11-14 11:18:45', # date_captured
    # flickr_url
    'flickr_url': 'http://farm9.staticflickr.com/8186/8119368305_4e622c8349_z.jpg',
    'id': 391895                        # image id
}
```
- annotations，表示标注文件中目标物体的标注信息列表，每个元素是一个目标物体的标注信息。如下为其中一个目标物体的标注信息：
```python
{

    'segmentation':             # 物体的分割标注
    'area': 2765.1486500000005, # 物体的区域面积
    'iscrowd': 0,               # iscrowd
    'image_id': 558840,         # image id
    'bbox': [199.84, 200.46, 77.71, 70.88], # bbox [x1,y1,w,h]
    'category_id': 58,          # category_id
    'id': 156                   # image id
}
```
#### 查看COCO标注文件
```python
import json
import jsonpath
coco_anno = json.load(open('./annotations/instances_train2017.json'))

# coco_anno.keys
print('\nkeys:', coco_anno.keys())
# 查看类别信息
print('\n物体类别:', coco_anno['categories'])
# 查看所有类别名
print('\n所有类别名:', jsonapth.jsonpath(coco_anno, "$.categories..name"))
# 查看一共多少张图
print('\n图像数量：', len(coco_anno['images']))
# 查看一共多少个目标物体
print('\n标注物体数量：', len(coco_anno['annotations']))
# 查看一个标注对象的信息
print('\n查看一个标注对象的信息：', coco_anno['annotations'][0])
```

### labelme to coco
```python
python x2coco.py --dataset_type labelme --json_input_dir ./output/json/ \
--image_input_dir ./output/img/ \
--output_dir ./cocome/ \
--train_proportion 0.8 \
--val_proportion 0.2 \ 
--test_proportion 0.0
```

## train environment 搭建

### 查看服务器上cuda api版本
cuda api分为 Driver API(驱动api) 和 Running API(运行时api) 两种
1. 使用 `nvidia-smi` 查看 Driver API版本(最大支持Running API版本)
2. 使用 `nvcc -v` 查看 Running API版本

### 查看服务器上cudnn版本
cudnn是NVIDIA 开发的深度学习库
1. 查看cudnn有无安装 `find /usr -name "cudnn.h"`
2. 查看cudnn版本 `grep -i "CUDNN_MAJOR" -r /usr/include`

### 一种相对稳定的paddle依赖链
```py
paddle2onnx               1.2.6
paddledet                 2.6.0
paddlelabel               1.0.1
paddleocr                 2.7.0
paddlepaddle-gpu          2.6.1.post120
```
**注意** `nvcc --version` 中 cuda版本 V12.0.140

## bug

### version `GLIBCXX_3.4.30' not found
> 问题描述: 在导入paddleocr时，报错`libstdc++.so.6: version GLIBCXX_3.4.30 not found`,但是更改`from paddleocr import PaddleOCR`导入语句的位置至第一行,此问题不会出现
> 解决方案: 这种情况是c++的运行时库缺少符号`GLIBCXX_3.4.30`,并且运行环境注入有延时(即虚拟环境和系统环境不一致),按以下步骤排查:
1. 使用 `find / -name "libstdc++.so"` 查找所有的运行时库
2. 使用 `strings /home/miniconda3/lib/libstdc++.so.6 | grep "GLIBCXX_3.4.30"` 查看是否支持指定的GLIBCXX版本
3. 对于conda环境使用 `conda install conda-forge::libstdcxx-ng` 更新libstdc++版本

**注意** libstdcxx和libstdcxx-ng的区别, libstdcxx-ng是一个新的C++标准库实现，它是由LLVM项目开发的，是libstdcxx的一个重写版本，更好的与LLVM的集成。
