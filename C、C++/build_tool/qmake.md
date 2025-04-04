# qmake
qmake是其他官方支持的快平台构建工具, 从项目文件.pro中的信息生成 Makefile

> 参考文档
> - [qt官方qmake文档](https://doc.qt.io/qt-6/qmake-manual.html)

## qmake变量

[qmake内置变量](https://doc.qt.io/qt-6/qmake-variable-reference.html#sources)


## 示例

### qmake添加宏定义

- `DEFINES += __LOG_DEBUG__` 
- `QMAKE_CFLAGS += "-DMY_MACRO"`
- `qmake QMAKE_CFLAGS+="-DMY_MACRO"`

### qmake设置构建类型

- `CONFIG += debug`
- `BUILD_TYPE = debug`
- `qmake BUILD_TYPE=debug`