# qmake
qmake是其他官方支持的快平台构建工具, 从项目文件.pro中的信息生成 Makefile

> 参考文档
> - [qt官方qmake文档](https://doc.qt.io/qt-6/qmake-manual.html)

## qmake变量

[qmake内置变量](https://doc.qt.io/qt-6/qmake-variable-reference.html#sources)

> example:
- `QMAKE_PROJECT_DEPTH = 0`: 控制 子项目(subprojects) 的处理深度,默认会递归处理项目中的所有子项目(通过 SUBDIRS 指定的项目), `0 时`, qmake 不会处理任何子项目(处理当前的 `.pro` 文件)

## qmake选项

- `-o <file>`: 指定输出MakeFile文件名

## 示例

### qmake添加宏定义

- `DEFINES += __LOG_DEBUG__` 
- `QMAKE_CFLAGS += "-DMY_MACRO"`
- `qmake QMAKE_CFLAGS+="-DMY_MACRO"`
- `qmake DEFINES+=\\\\\\'NETWORK_CARD_NAME=\\\\\\\"eth2\\\\\\\"\\\\\\' DEFINES+=ONLY_USE_LOCAL_ADDRESS DiscoveryComponent.pro`

### qmake设置构建类型

- `CONFIG += debug`
- `BUILD_TYPE = debug`
- `qmake BUILD_TYPE=debug`

### 指定构建输出目录

- 在pro文件中设置
```make
Release:DESTDIR = release
Release:OBJECTS_DIR = release/.obj
Release:MOC_DIR = release/.moc
Release:RCC_DIR = release/.rcc
Release:UI_DIR = release/.ui

Debug:DESTDIR = debug
Debug:OBJECTS_DIR = debug/.obj
Debug:MOC_DIR = debug/.moc
Debug:RCC_DIR = debug/.rcc
Debug:UI_DIR = debug/.ui

# 复用代码指定
release: DESTDIR = build/release
debug:   DESTDIR = build/debug

OBJECTS_DIR = $$DESTDIR/.obj
MOC_DIR = $$DESTDIR/.moc
RCC_DIR = $$DESTDIR/.qrc
UI_DIR = $$DESTDIR/.ui
```
- 在构建目录中生成
```sh
mkdir build
cd build
qmake ../path/to/MyProject.pro
```