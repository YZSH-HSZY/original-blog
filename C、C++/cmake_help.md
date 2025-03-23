# cmake学习笔记

**注意**
- CMakeLists.txt是区分大小写的
- 使用SET指令设置变量,`${<var_name>}`来引用变量,在IF指令中,变量会被自动解引用,无需显示使用`${}`获取
- 指令是大小写无关的,参数和变量是大小写相关的.推荐全部使用大写指令
- 基本指令格式中,`<cmd_name>(<params_1> [params_2 ...])`参数可以带双引号"包裹,cmake会自动去除

## cmake指令

### PROJECT
1. PROJECT可以指定工程名称project_name,并可指定工程支持的语言
`PROJECT (HELLO [CXX] [C] [Java])`
2. **注意** 该指令隐式定义了两个变量,`<projectname>_BINARY_DIR`(等同`PROJECT_BINARY_DIR`) 以及`<projectname>_SOURCE_DIR`(等同`PROJECT_SOURCE_DIR`);这两个变量的值分别为生成的二进制文件(包括可执行文件和库文件)的存放位置,源文件的位置

### SET
SET 指令的语法：
`SET(VAR [VALUE] [CACHE TYPE DOCSTRING [FORCE]])`
设置普通、缓存或环境变量为给定值

> example:
> `set(VAR1 "var1_test" CACHE STRING "Description") `。创建一个名为 `VAR1` 的字符串类型变量，初始值为 `"var1_test"`，存储在 CMake 的缓存中，同时提供了一个描述字符串。

**注意** cmake的变量存在作用域，只可以在它的作用域内访问这个变量。在变量声明末尾添加 `PARENT_SCOPE` 来将它的作用域置定为当前的上一级作用域。

- `CACHE`将变量存储在 CMake 的缓存中(即生成的CMakeCache.txt文件)，这样在后续的 CMake 配置过程中可以保持这个值，并且可以被用户在 CMake GUI 或者命令行中修改。
> 命令行更改: `cmake -DVAR1="new_value" .`

### MESSAGE
MESSAGE 用于向终端输出用户定义的信息
`MESSAGE([SEND_ERROR | STATUS | FATAL_ERROR] "message to display"...)`

- SEND_ERROR,产生错误,生成过程被跳过.
- SATUS,输出前缀为—的信息.
- FATAL_ERROR,立即终止所有 cmake 过程.

### ADD_EXECUTABLE
`ADD_EXECUTABLE(hello ${SRC_LIST})`
定义工程会生成一个文件名为 hello 的可执行文件,相关的源文件是 SRC_LIST 中定义的源文件列表, example1中等同与 `ADD_EXECUTABLE(hello main.c)`

### ADD_LIBRARY
`add_library(<name> [<type>] [EXCLUDE_FROM_ALL] <sources>...)`
```
type:
 - STATIC 链接其他目标时使用的目标文件存档。
 - SHARED 一个动态库，可以由其他目标链接并在运行时加载。
 - MODULE 一个插件，可能不会被其他目标链接，但可以在运行时使用类似 dlopen 的功能动态加载。
 若未设置，则默认值为 STATIC 或 SHARED 基于 BUILD_SHARED_LIBS 变量的值。
```
### ADD_SUBDIRECTORY
`ADD_SUBDIRECTORY(source_dir [output_binary_dir] [EXCLUDE_FROM_ALL])`
向当前工程添加存放源文件的子目录，并可以指定中间二进制和目标二进制存放的位置。
EXCLUDE_FROM_ALL 参数的含义是将这个目录从编译过程中排除

### SUBDIRS
`SUBDIRS(dir1 dir2...)`
这个指令已经不推荐使用。它可以一次添加多个子目录，
并且，即使外部编译，子目录体系仍然会被保存.

### find_package

加载外部项目设置
```
find_package(<package> [version] [EXACT] [QUIET] [MODULE]
             [REQUIRED] [[COMPONENTS] [components...]]
             [OPTIONAL_COMPONENTS components...]
             [NO_POLICY_SCOPE])
```         
 `<package>_FOUND` 将设置为指示是否找到包。找到包时，将通过包本身记录的变量和导入目标提供特定于包的信息。如果找不到包，则 QUIET 选项将禁用消息。MODULE 选项将禁用下面记录的第二个签名。如果找不到包，则 REQUIRED 选项将停止处理并显示错误消息。

**注意** 包加载到嵌套作用域中，会定义了以下变量：
`PACKAGE_FIND_NAME`包名
`<package>_FIND_VERSION`提供的完整版本字符串
`<package>_FIND_VERSION_MAJOR`主要版本（如果提供），否则为 0
`<package>_FIND_VERSION_MINOR`次要版本（如果提供），否则为 0
`<package>_FIND_VERSION_PATCH`补丁版本（如果提供），否则为 0
`<package>_FIND_VERSION_TWEAK`tweak version if provided, else 0
`<package>_FIND_VERSION_COUNT`版本组件数，0 到 4

#### find_package搜索路径

1. 在局部缓存中查看以下变量值，使用 NO_CMAKE_PATH 指定是否跳过该步骤
`CMAKE_PREFIX_PATH`(指定查找库、头文件和程序的根目录)
`CMAKE_MODULE_PATH`(指定查找CMake模块即.cmake路径)
`CMAKE_FRAMEWORK_PATH`
`CMAKE_APPBUNDLE_PATH`
2. 在cmake的特定环境变量中搜索，使用 NO_CMAKE_ENVIRONMENT_PATH 指定是否跳过该步骤
`<package>_DIR`
`CMAKE_PREFIX_PATH`
`CMAKE_FRAMEWORK_PATH`
`CMAKE_APPBUNDLE_PATH`
3. 在`PATH`中搜索，以父目录结尾的 /bin 或 /sbin 自动转换为其父目录的路径条目：使用 NO_SYSTEM_ENVIRONMENT_PATH 指定是否跳过该步骤
4. 搜索当前系统的平台文件中定义的 cmake 变量。使用 NO_CMAKE_SYSTEM_PATH 指定是否跳过该步骤
`CMAKE_SYSTEM_PREFIX_PATH`
`CMAKE_SYSTEM_FRAMEWORK_PATH`
`CMAKE_SYSTEM_APPBUNDLE_PATH`

**注意** cmake在搜索路径下查找`<package_name>Config.cmake`或`<package_name>-config.cmake`或`Find<package_name>.cmake`文件
cmake在每个目录prefix下会尝试进行一系列的可能的查找
`<prefix>/                                               `
`<prefix>/(cmake|CMake)/                                 `
`<prefix>/<name>*/                                       `
`<prefix>/<name>*/(cmake|CMake)/                         `
`<prefix>/(lib/<arch>|lib|share)/cmake/<name>*/          `
`<prefix>/(lib/<arch>|lib|share)/<name>*/                `
`<prefix>/(lib/<arch>|lib|share)/<name>*/(cmake|CMake)/`

#### 在CMakeLists.txt文件中配置find_package搜索路径
```cmake
list(APPEND CMAKE_PREFIX_PATH "D:/Qt/Qt5.12.9/5.12.9/mingw73_32/lib/cmake/Qt5")
list(APPEND CMAKE_PREFIX_PATH "D:/Qt/Qt5.12.9/5.12.9/mingw73_32/lib/cmake/Qt5LinguistTools")
```

#### 简易的Find<name>.cmake模块示例
```
FIND_PATH(HELLO_INCLUDE_DIR hello.h /usr/include/hello /usr/local/include/hello)
FIND_LIBRARY(HELLO_LIBRARY NAMES hello PATH /usr/lib /usr/local/lib) 

IF (HELLO_INCLUDE_DIR AND HELLO_LIBRARY)
  SET(HELLO_FOUND TRUE)
ENDIF (HELLO_INCLUDE_DIR AND HELLO_LIBRARY)

IF (HELLO_FOUND)
  IF (NOT HELLO_FIND_QUIETLY)
    MESSAGE(STATUS "Found Hello: ${HELLO_LIBRARY}")
  ENDIF (NOT HELLO_FIND_QUIETLY)

ELSE (HELLO_FOUND)
  IF (HELLO_FIND_REQUIRED)
    MESSAGE(FATAL_ERROR "Could not find hello library")
  ENDIF (HELLO_FIND_REQUIRED)
ENDIF (HELLO_FOUND)
```

### target_link_libraries
`target_link_libraries(<target> ... <item>... ...)`
指定链接目标时和其依赖项时要使用的库或标志

### target_link_options
```m
target_link_options(<target> [BEFORE]
  <INTERFACE|PUBLIC|PRIVATE> [items1...]
  [<INTERFACE|PUBLIC|PRIVATE> [items2...] ...])
```
向可执行文件、共享库或模块库目标的链接步骤添加选项。

### target_include_directories
```sh
target_include_directories(<target> [SYSTEM] [AFTER|BEFORE]
   <INTERFACE|PUBLIC|PRIVATE> [items1...]
   [<INTERFACE|PUBLIC|PRIVATE> [items2...] ...])
```
将头文件包含目录添加到目标

### link_directories

`link_directories([AFTER|BEFORE] directory1 [directory2 ...])`
添加链接器将在其中查找库的目录

### link_libraries
```
link_libraries([item1 [item2 [...]]]
  [[debug|optimized|general] <item>] ...)
```
将库链接到以后添加的所有目标

### 控制指令

#### IF

IF指令语法格式:
```sh
IF(expression)
  # THEN section.
  COMMAND1(ARGS ...)
  COMMAND2(ARGS ...)
  ...
ELSE(expression)
  # ELSE section.
  COMMAND1(ARGS ...)
  COMMAND2(ARGS ...)
  ...
ENDIF(expression)
```

## cmake变量

### cmake内置变量
参[cmake官方文档](https://cmake.org/cmake/help/latest/manual/cmake-variables.7.html)

#### cmake常用变量

- `PROJECT_SOURCE_DIR`，`PROJECT_BINARY_DIR`参PROJECT指令
- `EXECUTABLE_OUTPUT_PATH`指定最终的目标二进制的位置(不包含编译生成
的中间文件)
- `LIBRARY_OUTPUT_PATH`指定最终的共享库的位置(不包含编译生成
的中间文件)
- `CMAKE_CURRENT_SOURCE_DIR` cmake当前正在处理的源目录的完整路径(即CMakeLists.txt所在目录)
- `CMAKE_CURRENT_LIST_FILE` cmake当前正在处理的 listfile 的完整路径
- `CMAKE_CURRENT_LIST_DIR` cmake当前正在处理的 listfile 的完整目录
- `CMAKE_CURRENT_LIST_LINE` 正在处理的当前文件的行号

> 区别
> `CMAKE_CURRENT_SOURCE_DIR`和`CMAKE_CURRENT_LIST_DIR`: 前者执行正在处理的CMakeLists文件路径, 后者在 `include` 时指向当前listfile路径

## cmake函数

- `string(TOUPPER <str> <out_var>)` 字符串转为大写
- `get_filename_component(<var> <FileName> <mode> [BASE_DIR <dir>] [CACHE])` 获取完整文件名的特定组件

## cmake选项

```sh
Options:
  -B <path-to-build> 
    CMake将用作构建目录根目录的路径(不存在将自动创建)
  -S <path-to-source>
    要构建的CMake项目的根目录路径
```

以下是一下命令行指定source和target目录的示例:

|Command Line             |Source Dir   |Build Dir      |
|-------------------------|-------------|---------------|
|`cmake -B build`         |cwd          |build          |
|`cmake -B build src`     |src          |build          |
|`cmake -B build -S src`  |src          |build          |
|`cmake src`              |src          |cwd            |
|`cmake build (existing)` |loaded       |build          |
|`cmake -S src`           |src          |cwd            |
|`cmake -S src build`     |src          |build          |
|`cmake -S src -B build`  |src          |build          |

上述用于指定源树和构建树的样式可以混合使用。用l -S或-B指定的路径总是分别被分类为源树或构建树。使用普通参数指定的路径根据其内容和前面给出的路径类型进行分类。如果只给出了一种类型的路径，则使用当前工作目录（cwd）作为另一种类型的路径。例如:

#### 内部构建和外部构建

1. 内部构建指在源工程代码目录下进行构建,未创建一个指定的build目录,这时构建过程中的临时文件均会输出到工程目录下,污染代码环境。
**注意** cmake可以通过执行脚本运行一些额外的任务并生成一些临时文件，但cmake没法判断临时文件是哪些，因此在clean时无法自动清理这些文件。

2. 外部构建:创建一个build目录，将临时文件和构建输出的makefile文件输出到build目录

## cmake调试

- `message(STATUS "MY_VARIABLE=${MY_VARIABLE}")` 使用message指令打印变量
- `include(CMakePrintHelpers)` `cmake_print_variables(MY_VARIABLE)` 通过内置模组CMakePrintHelpoers打印变量

## cmake工程操作示例

### 工程清理
`make clean`对构建结果进行清理

### cmake编译配置(选择编译器和编译目标架构)

x86 用32位的编译器编译出32位程序
x64 用64位的编译器编译出64位程序
x86_x64 用32位的编译器编译出64位程序
x64_x86 用64位的编译器编译出32位程序

### cmake指定二进制文件的输出目录

```cmake
# PROJECT_BINARY_DIR当前所有二进制文件输出目录,设置不生效

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)

# 指定可执行程序输出目录,未设置设置build type时不生效
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_DEBUG 	${publish_bin_debug})
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_RELEASE 	${publish_bin_release})

# 指定静态库文件输出目录,未设置设置build type时不生效
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY_DEBUG 	${publish_lib_debug})
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY_RLEASE 	${publish_lib_release})

# 源文件拷贝
file(COPY ${CMAKE_CURRENT_SOURCE_DIR}/include/udp/udp_interface.h DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/publish/x64/include)
```

**注意** 设置要放在函数 `add_library` 或者 `add_executable` 之前

### cmake查找依赖和输出文件执行路径问题

建议如果实在找不到<name>Config.cmake文件，自己写个Find<name>.cmake文件放到CMAKE_MOUDLE_PATH指定的目录中，自己指定生成的头文件目录名和共享库路径名.

<name>_DIR，可以定义这个变量，最优先到这个目录下查询<name>Config.cmake文件.
CMAKE_PREFIX_PATH, CMAKE_FRAMEWORK_PATH, CMAKE_APPBUNDLE_PATH.
根据PATH，因为PATH都是以bin或sbin结尾，所以自动退回上级到lib | share的cmake目录中查找<name>Config.cmake文件.

**注意** 在自己电脑上编译通过后，只要不移动共享库文件，即使移动可执行文件，也照样可以执行，因为链接库的绝对路径已经编译到可执行文件中了.

**注意** 如果链接库移动了，位置变了，把此时的路径加入到LD_LIBRARY_PATH变量中，运行时会自动到这些路径中去查找的.

### example1-简易CMakeLists.txt示例
```
PROJECT (HELLO [CXX] [C] [Java])  # 指定工程名称,并可指定工程支持的语言
SET(SRC_LIST main.c)  # 
MESSAGE(STATUS "This is BINARY dir " ${HELLO_BINARY_DIR})
MESSAGE(STATUS "This is SOURCE dir "${HELLO_SOURCE_DIR})
ADD_EXECUTABLE(hello SRC_LIST)
```

### cmake配置debug类型




## cmake常见问题

### cmake如何确定使用gcc编译还是g++编译
1. 通过在 `project` 中指定的项目语言langages
2. 通过 `add_executable` 或 `add_library` 中，源文件的后缀名 `.cpp` 对应g++，`.c` 对应gcc
