# libstdc++

实现c++翻译的库实现, 不同编译器有不同实现, 对c++标准的支持也有所不同

**注意**
> GCC/libstdc++/glibc的区别
- `GCC (GNU Compiler Collection)`: 一个编译器, 用于将 C/C++ 源代码编译成机器代码
- `libstdc++-v3`: 包含C++ 标准库实现, 提供语言特性、语法分析、代码生成等功能
- `glibc (GNU C Library)`: C 标准库实现, 提供 POSIX API、C 标准库函数、系统调用封装等

> gcc编译器源码包含libstdc++实现

## 目录结构

```sh
gcc-13.2.0/
├── gcc/                    # 编译器前端
│   ├── cp/                 # C++ 前端 (最重要的目录)
│   │   ├── parser.cc       # C++ 解析器
│   │   ├── typeck.cc       # 类型检查
│   │   └── decl.cc         # 声明处理
│   └── c-family/           # C/C++ 通用代码
├── libstdc++-v3/           # C++ 标准库
│   ├── include/            # 标准头文件
│   │   ├── bits/           # 实现细节
│   │   └── ext/            # GNU 扩展
│   ├── src/                # 标准库实现
│   │   ├── c++98/          # C++98 组件
│   │   ├── c++11/          # C++11 新特性
│   │   └── c++17/          # C++17 新特性
│   └── libsupc++/          # 语言支持
└── libgcc/                 # 运行时库
```

```sh
libstdc++-v3/
├── include/                    # 所有头文件
│   ├── bits/                  # 实现细节头文件
│   │   ├── vector.tcc         # vector 实现
│   │   ├── list.tcc           # list 实现
│   │   ├── deque.tcc          # deque 实现
│   │   ├── stringfwd.h        # string 前向声明
│   │   └── ...
│   ├── std/                   # 标准头文件
│   │   ├── vector             # vector 主头文件
│   │   ├── list               # list 主头文件
│   │   ├── string             # string 主头文件
│   │   ├── memory             # 智能指针
│   │   └── ...
│   ├── ext/                   # GNU 扩展
│   │   ├── pb_ds/             # Policy-Based Data Structures
│   │   ├── throw_allocator.h  # 测试用分配器
│   │   └── ...
│   └── backward/              # 兼容旧代码
├── src/                       # 运行时实现
│   ├── c++98/                 # C++98 组件
│   │   ├── locale_init.cc     # 本地化初始化
│   │   ├── localename.cc      # 地区名称
│   │   └── ...
│   ├── c++11/                 # C++11 新特性
│   │   ├── chrono.cc          # 时间库
│   │   ├── condition_variable.cc # 条件变量
│   │   ├── thread.cc          # 线程支持
│   │   └── ...
│   ├── c++17/                 # C++17 特性
│   ├── c++20/                 # C++20 特性
│   └── filesystem/            # 文件系统
├── libsupc++/                 # 语言运行时支持
│   ├── eh_alloc.cc            # 异常处理内存分配
│   ├── eh_throw.cc            # 异常抛出
│   ├── vec.cc                 # 向量异常
│   ├── new_op.cc              # new 操作符
│   └── ...
├── testsuite/                 # 测试套件
│   ├── 17_intro/              # 标准符合性测试
│   ├── 20_util/               # 工具类测试
│   ├── 23_containers/         # 容器测试
│   ├── 25_algorithms/         # 算法测试
│   └── ...
└── doc/                       # 文档
```

## input/output library

### File-based streams

`<fstream>` 定义4个类模板和8个类型, 将流缓冲区和文件关联起来, 用于协助读写文件

```cpp
template <class charT, class traits = char_traits<charT> > class basic_filebuf;
typedef basic_filebuf<char> filebuf;
typedef basic_filebuf<wchar_t> wfilebuf;

template <class charT, class traits = char_traits<charT> > class basic_ifstream;
typedef basic_ifstream<char> ifstream;
typedef basic_ifstream<wchar_t> wifstream;

template <class charT, class traits = char_traits<charT> > class basic_ofstream;
typedef basic_ofstream<char> ofstream;
typedef basic_ofstream<wchar_t> wofstream;

template <class charT, class traits = char_traits<charT> > class basic_fstream;
typedef basic_fstream<char> fstream;
typedef basic_fstream<wchar_t> wfstream;
```

> `basic_filebuf` 将文件视为字节的源或接受器, 在使用大小字符集的环境中, `basic_filebuf`对象会将多字节序列转换为宽字节序列

#### File open modes

|binary|in |out |trunc |app|stdio equivalent|
|------|---|----|------|---|----------------|
|      |   | +  |      |   |      "w"       |
|      |   | +  |      | + |      "a"       |
|      |   |    |      | + |      "a"       |
|      |   | +  |  +   |   |      "w"       |
|      | + |    |      |   |      "r"       |
|      | + | +  |      |   |      "r+"      |
|      | + | +  |  +   |   |      "w+"      |
|      | + | +  |      | + |      "a+"      |
|      | + |    |      | + |      "a+"      |
|  +   | + |    |      |   |      "wb"      |
|  +   | + |    |      | + |      "ab"      |
|  +   |   |    |      | + |      "ab"      |
|  +   |   | +  |  +   |   |      "wb"      |
|  +   | + |    |      |   |      "rb"      |
|  +   | + | +  |      |   |      "r+b"     |
|  +   | + | +  |  +   |   |      "w+b"     |
|  +   | + | +  |      | + |      "a+b"     |
|  +   | + |    |      | + |      "a+b"     |

>  `(mode & ios_base::ate) != 0`, 文件定位到末尾, 如 `std::fseek(file,0,SEEK_END)`