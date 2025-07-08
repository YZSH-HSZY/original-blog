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