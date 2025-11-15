
## 参考文档

- [cpp新特性介绍网站](https://www.apiref.com/cpp-zh/cpp/11.html)

## c/cpp编译原理相关

### 头文件预处理

```
#define OPEN_AUTH 0   //宏定义
//...

#ifdef OPEN_AUTH   //判断宏是否定义
    // do A ...
#else
    // do B ...
#endif

#undef OPEN_AUTH    //取消宏变量设置
```
c/c++编译器在处理include文件时，会将所有定义的宏给包含到源代码中。
在源程序编译之前，会对源代码进行预处理，将宏替换为对应宏代码体

## window 平台相关

### window 下的静态库 lib 和动态库 dll 文件

工作中有时候因为分工合作的原因需要让别人调用自己写的代码去完成某项功能，但是又不想让别人看到具体的实现过程，只是提供一个函数 API 形式的接口供别人调用。 1.库类型共有两种：

> （1）库包含了函数所在的 DLL 文件和文件中函数位置的信息（入口），代码由运行时加载在进程空间中的 DLL 提供，称为动态链接库 DLL(dynamic link library)
> （2）库包含函数实现代码，在编译时直接将代码加入程序当中，称为静态链接库 LIB(static link library)。

2.程序在编译链接时有两种方式：

> （1）静态链接，链接器从静态链接库获取被引函数体，连同程序代码生成可执行文件。
> （2）动态链接，链接器声明使用动态链接库，允许生成的可执行模块（.dll 文件或.exe 文件）包含在运行时定位 DLL 函数的可执行代码所需的信息

### cl
window下编译工具, 参[msvc笔记](./compile_tool/msvc.md)

### dumpbin

二进制文件转储程序 (DUMPBIN.EXE), 参[dumpbin笔记](../MASM/dumpbin.md)

### lib

查看 .lib 静态库的归档文件
`lib /list <lib_file>`

### window下编译动态库问题

#### 添加宏，输出函数表

定义宏如下:`#define DLL_API __declspec(dllexport)`
在需要导出的函数声明处，为函数添加该定义

在 Windows 平台上，如果你想在编译时自动为所有函数添加 `__declspec(dllexport)` 标志，可以通过以下几种方法实现：

1. 使用宏定义

你可以在头文件中定义一个宏，根据编译条件来自动添加 `__declspec(dllexport)` 或 `__declspec(dllimport)`。例如：

```cpp
#ifdef MYLIBRARY_EXPORTS
#define MYLIBRARY_API __declspec(dllexport)
#else
#define MYLIBRARY_API __declspec(dllimport)
#endif
```

然后在你的函数声明中使用这个宏：

```cpp
MYLIBRARY_API void myFunction();
```

2. 使用 CMake 处理导出宏

如果你使用 CMake，可以在 CMakeLists.txt 中定义一个编译选项，来控制导出宏的定义。例如：

```cmake
add_library(MyLibrary SHARED mylibrary.cpp)

# 定义导出宏
target_compile_definitions(MyLibrary PRIVATE MYLIBRARY_EXPORTS)
```

然后在你的代码中使用上述宏定义：

```cpp
#ifdef MYLIBRARY_EXPORTS
#define MYLIBRARY_API __declspec(dllexport)
#else
#define MYLIBRARY_API __declspec(dllimport)
#endif

MYLIBRARY_API void myFunction();
```

3. 使用 `__declspec(dllexport)` 的默认设置

如果你希望所有函数都默认导出，可以在库的实现文件中使用 `__declspec(dllexport)`，并在头文件中使用 `__declspec(dllimport)`。例如：

```cpp
// mylibrary.h
#ifdef MYLIBRARY_EXPORTS
#define MYLIBRARY_API __declspec(dllexport)
#else
#define MYLIBRARY_API __declspec(dllimport)
#endif

MYLIBRARY_API void myFunction();
```

```cpp
// mylibrary.cpp
#define MYLIBRARY_EXPORTS
#include "mylibrary.h"

void myFunction() {
    // 实现
}
```

4. 使用 `#pragma` 指令

在某些情况下，你也可以使用 `#pragma` 指令来控制导出。例如：

```cpp
#pragma warning(disable : 4251) // 禁用警告
#pragma export
```

## C/C++项目示例

### 查看多文件中宏

1. 使用 `gcc -E <c_file>` 进行预处理宏替换
缺点:在输出的处理后的文件中定位具体位置较为麻烦
2. 使用gcc扩展 `#pragma message ("message the DEFINE_VALUE is:" DEFINE_VALUE)`
缺点:只能对字符串宏进行输出,其他形式的宏不能通过`#pragma message`预处理指令输出
3. 静态断言_Static_assert，在c11及以上版本可用
4. printf函数直接输出
缺点:需确定宏替换后的类型,在宏未生效时易报错

example:
```C
#include <stdio.h>
#define DEFINE_VALUE 9
#define DEFINE_VALUE_STR "9" 
#pragma message ("message the DEFINE_VALUE is:" DEFINE_VALUE_STR)
_Static_assert(DEFINE_VALUE == 9, "error");
int main(){
    printf("Hello");
    printf("%x", DEFINE_VALUE );
    return 0;
}
```
预处理后输出:
```C
# 5 "test_define.c"
#pragma message ("message the DEFINE_VALUE is:" "9")
# 5 "test_define.c"

# 7 "test_define.c"
_Static_assert(9 == 9, "error");
int main(){
    printf("Hello");
    printf("%x", 9 );
    return 0;
}
```

### 跨平台编译auto工具
1. autoscan (autoconf): 扫描源代码以搜寻普通的可移植性问题，比如检查编译器，库，头文件等，生成文件configure.scan,它是configure.ac的一个雏形。
`your source files --> [autoscan*] --> [configure.scan] --> configure.ac`

2. aclocal (automake):根据已经安装的宏，用户定义宏和acinclude.m4文件中的宏将configure.ac文件所需要的宏集中定义到文件 aclocal.m4中。aclocal是一个perl 脚本程序，它的定义是：`aclocal - create aclocal.m4 by scanning configure.ac`

user input files   optional input     process          output files
================   ==============     =======          ============

                    acinclude.m4 - - - - -.
                                          V
                                      .-------,
configure.ac ------------------------>|aclocal|
                 {user macro files} ->|       |------> aclocal.m4
                                      `-------'


3. autoheader(autoconf): 根据configure.ac中的某些宏，比如cpp宏定义，运行m4，生成config.h.in


user input files    optional input     process          output files
================    ==============     =======          ============

                    aclocal.m4 - - - - - - - .
                                             |
                                             V
                                     .----------,
configure.ac ----------------------->|autoheader|----> autoconfig.h.in
                                     `----------'


4. automake: automake将Makefile.am中定义的结构建立Makefile.in，然后configure脚本将生成的Makefile.in文件转换 为Makefile。如果在configure.ac中定义了一些特殊的宏，比如AC_PROG_LIBTOOL，它会调用libtoolize，否则它 会自己产生config.guess和config.sub


user input files   optional input   processes          output files
================   ==============   =========          ============

                                     .--------,
                                     |        | - - -> COPYING
                                     |        | - - -> INSTALL
                                     |        |------> install-sh
                                     |        |------> missing
                                     |automake|------> mkinstalldirs
configure.ac ----------------------->|        |
Makefile.am  ----------------------->|        |------> Makefile.in
                                     |        |------> stamp-h.in
                                 .---+        | - - -> config.guess
                                 |   |        | - - -> config.sub
                                 |   `------+-'
                                 |          | - - - -> config.guess
                                 |libtoolize| - - - -> config.sub
                                 |          |--------> ltmain.sh
                                 |          |--------> ltconfig
                                 `----------'



5. autoconf:将configure.ac中的宏展开，生成configure脚本。这个过程可能要用到aclocal.m4中定义的宏。


user input files   optional input   processes          output files
================   ==============   =========          ============

aclocal.m4 ,autoconfig.h.in - - - - - - -.
                                         V
                                     .--------,
configure.ac ----------------------->|autoconf|------> configure


6. ./configure的过程

                                           .-------------> [config.cache]
     configure* --------------------------+-------------> config.log
                                          |
              [config.h.in] -.            v            .--> [autoconfig.h]
                             +-------> config.status* -+                   
              Makefile.in ---'                         `-->   Makefile




7. make过程

      [autoconfig.h] -.
                     +--> make* --->  程序
       Makefile   ---'

### 查看可执行文件运行平台
`readelf -h <exec_file_path>`

### 查看so文件需要的动态库
`ldd <so_file_path>`
`readelf -d <file_path>`

### 查看.a文件的架构
1. `ar x libcrypto.a; file *.o | head -n 1` 解压后查看
2. `readelf -h libcrypto.a | grep 'Class\|Machine'`
3. `objdump -f libcrypto.a | grep architecture`

### 查看so文件中字符串用于判断是否支持指定版本
`strings <so_file_path>`

### 查看归档文件.a中包含的所有目标文件

`ar -t your_library.a        # 列出库中包含的所有.o文件`

### 查看符号表

使用 `nm` 列出obj目标文件中的符号
```sh
# 输出符号类型描述
- A 在每个符号信息的前面打印所在对象文件名称
- C 输出demangle过了的符号名称
- D 打印动态符号
- l 使用对象文件中的调试信息打印出所在源文件及行号
- n 按照地址/符号值来排序
- u 打印出那些未定义的符号
```

### c调用cpp函数

**注意事项**
1. g++编译器会将cpp文件中定义的函数进行符号重命名，因此c通过定义的函数名链接cpp的库文件，要想使 C++ 中的函数名称具有 C 链接（编译器不会破坏名称），则被c调用的c++函数需要用extern "C"标识
2. 若c++函数中使用了c++的库，比如`iostream`，`#include<iostream>`只能写在cpp源文件中，不能写在.h文件中.h文件由gcc编译器处理，它无法处理c++的头文件进行预处理，将抛出未定义错误。

## BUG

### .h文件实现函数时在编译时报多重定义

> 问题描述: 在.h文件中做到

### static/extern/inline共用的编译错误

- C中，extern和static是两个关键字，其作用是相互矛盾的。extern用于声明一个变量或函数是在其他文件中定义的，而static用于限制变量或函数的作用域，使其只能在声明它的文件中访问。
    > 如果此时以dll的形式导出，则会报 `invalid use of ‘static’ in linkage specification`

#### static和inline关键字

- static
> 在C语言中，函数默认情况下是global的。函数名前的static关键字使它们变成静态。不同于C语言其他的global的函数，访问static函数被限制到声明它们的文件。因此，当我们要限制对函数的访问时，我们让它们static。此外，在不同的文件中可以允许存在拥有相同函数名的static函数。
- inline
> inline是c99的特性。在c99中，inline是向编译器建议，将被inline修饰的函数以内联的方式嵌入到调用这个函数的地方（类似与宏定义，不过inline函数，编译器会检查参数传递和返回类型是否一致）。而编译器会判断这样做是否合适，以此最终决定是否这么做。

写在头文件的`static inline`函数可以在编译器未将inline函数内联时，不会报重复定义错误。

**注意** 因为编译器对inline函数的处理存在差异，因此你应该注意这点。
内联是编译器在编译时进行的代码替换，因此代码块之类的运行时确定的值无法返回。
宏替换发送在预处理阶段，而内联发生在编译时。

### 链接一个三方库时出现未定义符号

使用 `nm -U <archived_file>` 查看所有未定义符号, 之后根据此符号判断缺失库

> 常见依赖库判断方法:
- 看到pthread_开头的符号 → 需要-lpthread
- 看到crypto_开头的符号 → 需要-lcrypto
- 看到ssl_开头的符号 → 需要-lssl
- 看到z_开头的符号 → 需要-lz

## 工程示例

### 头文件相关处理

#### 防止多重包含

在 `.h` 中组合添加如下代码:
```h
#pragma once
#ifndef MY_HEADER
#define MY_HEADER
// ... 代码 ...
#endif
```

> `#pragma once` 不是标准的一部分(属于编译器扩展), 受不同编译器的实现影响(GNU/Clang/MSVC均支持)

### 内存对齐相关

> 内存对齐是指编译器将数据存储在内存中时, 要求数据的起始地址必须是某个值的倍数, 以提高内存访问效率。这个值称为对齐边界(Alignment Boundary)。对齐边界通常是最大数据类型的大小，例如，整型数据的对齐边界是4字节，双精度浮点数的对齐边界是8字节
> 结构体中的内存对齐是指在结构体中成员变量所占用的内存空间的排列方式. 这是由编译器自动进行的处理.
> 受编译器实现差异, 不同编译器不同平台表现形式不同. 一般是按结构体中最大的数据类型进行每个变量的对齐, 不足部分填充字节以保证结构体中的成员变量按照对齐方式排列, 从而提高程序的运行效率

> Example:
```c
struct Example {
    short b:7;
    short c:9;
    int i;
    char a;
};
printf("Sizeof Example: %zu\n", sizeof(struct Example));  // Sizeof Example: 12
```

**如何在解析字节时取消字节填充**
1. `#pragma pack(push, 1)  // 1 字节对齐（无填充）` 支持MSVC/GCC/Clang
2. `struct __attribute__((packed)) PackedExample` 支持(GCC/Clang)

### 依赖管理相关

#### linux下使用pkg-config查看包是否存在
`pkg-config opencv --libs --cflags`

#### 使用pkg-config管理C/C++编译选项

使用pkg-config获取库/模块的所有编译相关的信息

- 可以设置`PKG-CONFIG-PATH`环境变量指定pkg-config额外搜索pc文件路径
- 可以使用`pkg-config --variable pc_path pkg-config`查看pkg-config built-in search path(默认搜索路径)。
> `pkg-config --print-variables pkg-config`查看指定包中定义的变量，其中pkg-config中变量pc_path为pkg-config的默认搜索路径，在编译安装时确认。
**注意** 你可以通过环境变量 `PKG_CONFIG_LIBDIR` 来覆盖默认搜索pc文件路径。
- example:
> `pkg-config --cflags --libs opencv`,--cflags选项列出opencv头文件路径，--libs选项列出库文件以及附加链接库路径

#### window下安装pkg-config

1. 直接使用choco安装`choco install pkgconfiglite`
2. 下载pkg-config及其依赖库：
```
pkg-config_0.26-1_win32.zip
glib_2.28.8-1_win32.zip
gettext-runtime_0.18.1.1-2_win32.zip
    extract 文件bin/pkg-config.exe，放到MinGW\bin
    extract 文件bin/intl.dll to MinGW\bin
    extract 文件bin/libglib-2.0-0.dll to MinGW\bin
```

### 运行时的堆栈处理

1. glibc中的backtrace函数
2. gcc内置函数__builtin_return_address
3. 三方库libunwind

> Example:
```c
printf("%p,%p\n", __builtin_return_address(0), __builtin_return_address(1));

const int size = 200;
void *buffer[size];
char **strings;
​
int nptrs = backtrace(buffer, size);
printf("backtrace() returned %d address\n", nptrs);
​
// backtrace_symbols函数不可重入, 可以使用backtrace_symbols_fd替换
strings = backtrace_symbols(buffer, nptrs);
if (strings) {
    for (int i = 0; i < nptrs; ++i) {
        printf("%s\n", strings[i]);
    }
    free(strings);
}
```

### cpp/c联合编程中static函数的处理

> static限制函数的作用域为他自身的文件, 其他文件无法访问
> 在cpp中想要访问.c中static函数,可以通过对普通函数进行extern "C"来间接调用(这也是Cpp/C之间桥接的一种方式)

### 强制内联

> 因为inline是一个向编译器推荐的标准, 编译器不一定会将此函数在编译时展开, 因此在一些希望类宏替换的原地展开操作可以使用强制内联, 如下所示:

```c
#ifdef _MSC_VER_ // for MSVC
#define forceinline __forceinline
#elif defined __GNUC__ // for gcc on Linux/Apple OS X
#define forceinline __inline__ __attribute__((always_inline))
#else
#define forceinline
#endif
```