# 介绍
此文章存储内存越界相关调试方法

## Example

### 编译启用AddressSanitizer检测内存错误

- `gcc --version | grep "sanitizer"`查看编译器是否支持AddressSanitizer
- 直接编译 `g++ -fsanitize=address -g -o <prog> <source_file>`
- 在cmake中开启支持
```c
if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    target_compile_options(${PROJECT_NAME} PRIVATE -fsanitize=address -fno-omit-frame-pointer)
    target_link_options(${PROJECT_NAME} PRIVATE -fsanitize=address)
endif(CMAKE_BUILD_TYPE)
```
- 在qmake中开启支持
```
# 开启全局asan分析
QMAKE_CXXFLAGS +=  -g -O0
QMAKE_LFLAGS += -fsanitize=address

# 对指定文件设置asan分析
df_desc.cpp {
    QMAKE_CXXFLAGS += -fsanitize=address
}
```
- msvc中使用 `/fsanitize=address`选项, 需要安装了 `C++ AddressSanitizer` 组件, 如: `cl /fsanitize=address /Zi med.cpp /link /DEBUG`

**注意**
    - AddressSanitizer主要检测内存访问错误(泄漏检测默认是关闭的)
    - Windows 上的 ASan 主要是移植版，功能不如 Linux/macOS 上的完整