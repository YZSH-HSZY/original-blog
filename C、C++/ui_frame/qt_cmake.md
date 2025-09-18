# use qt in cmake

## usage

### use in qt5

- 开启`CMAKE_AUTOUIC`自动转换ui文件到h文件
```sh
set(CMAKE_AUTOUIC ON)
add_executable(t t.cpp t.ui t.h)
```
- 使用`qt_wrap_ui`将给定的ui进行转换
```sh
set(SOURCES t.cpp)
qt_wrap_ui(SOURCES CxNMEA2000Display.ui)
add_executable(tree_test ${SOURCES})
```

## 注意事项

- qt5/qt6的cmake有所不同, 主要是在qt6中添加了更多的cmake宏
- qt5-cmake中qrc文件需要添加到 `add_execable` 中,否则不会编译
- `qt5.12.8`中, 没有 `qt_wrap_ui` 只有 `qt5_wrap_ui`

### cmake在构建和源码目录分开时, qt_autouic错误

需要设置AUTOUIC的搜索路径 `set(CMAKE_AUTOUIC_SEARCH_PATHS ${CMAKE_CURRENT_LIST_DIR}/ui)`
默认在构建目录下查找

## example

### 一个简易的cmake-qt demo

```c
cmake_minimum_required(VERSION 3.18)
project(test_qt)
cmake_policy(SET CMP0028 NEW)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)
find_package(Qt5 COMPONENTS Core REQUIRED)
# find_package(Qt5Core REQUIRED)  # will find Qt5CoreConfig.cmake file

message(STATUS "Qt5_DIR: ${Qt5_DIR}; Qt5Core_DIR: ${Qt5Core_DIR}")
include_directories(.)
include_directories(${Qt5Core_INCLUDE_DIRS})
include_directories(../..)

set(SOURCES_FILES test.cpp)

if(MSVC)
    add_executable(test_exe ${SOURCES_FILES})
else()
    add_executable(test_exe ${SOURCES_FILES})
endif()

target_link_libraries(test_exe PRIVATE Qt5::Core)
```

### 一套cmake支持qt5/6

> 参考文档:
- [qt-兼容qt5/6](https://doc.qt.io/qt-6/zh/cmake-qt5-and-qt6-compatibility.html)