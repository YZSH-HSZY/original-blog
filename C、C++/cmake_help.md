## cmake学习笔记

**注意**
- CMakeLists.txt是区分大小写的
- 使用SET指令设置变量,`${<var_name>}`来引用变量,在IF指令中,变量会被自动解引用,无需显示使用`${}`获取
- 指令是大小写无关的,参数和变量是大小写相关的.推荐全部使用大写指令
- 基本指令格式中,`<cmd_name>(<params_1> [params_2 ...])`参数可以带双引号"包裹,cmake会自动去除
- 建议如果实在找不到<name>Config.cmake文件，自己写个Find<name>.cmake文件放到CMAKE_MOUDLE_PATH指定的目录中，自己指定生成的头文件目录名和共享库路径名.

<name>_DIR，可以定义这个变量，最优先到这个目录下查询<name>Config.cmake文件.
CMAKE_PREFIX_PATH, CMAKE_FRAMEWORK_PATH, CMAKE_APPBUNDLE_PATH.
根据PATH，因为PATH都是以bin或sbin结尾，所以自动退回上级到lib | share的cmake目录中查找<name>Config.cmake文件.

注意1：在自己电脑上编译通过后，只要不移动共享库文件，即使移动可执行文件，也照样可以执行，因为链接库的绝对路径已经编译到可执行文件中了.
注意2：如果链接库移动了，位置变了，把此时的路径加入到LD_LIBRARY_PATH变量中，运行时会自动到这些路径中去查找的.

文章知识点与官方知识档案匹配，可进一步学习相关知识
OpenCV技能树首页概览25179 人正在系统学习中


#### 内部构建和外部构建

1. 内部构建指在源工程代码目录下进行构建,未创建一个指定的build目录,这时构建过程中的临时文件均会输出到工程目录下,污染代码环境。
**注意** cmake可以通过执行脚本运行一些额外的任务并生成一些临时文件，但cmake没法判断临时文件是哪些，因此在clean时无法自动清理这些文件。

2. 外部构建:创建一个build目录，将临时文件和构建输出的makefile文件输出到build目录

#### example1
```
PROJECT (HELLO [CXX] [C] [Java])  # 指定工程名称,并可指定工程支持的语言
SET(SRC_LIST main.c)  # 
MESSAGE(STATUS "This is BINARY dir " ${HELLO_BINARY_DIR})
MESSAGE(STATUS "This is SOURCE dir "${HELLO_SOURCE_DIR})
ADD_EXECUTABLE(hello SRC_LIST)
```
### cmake指令

#### PROJECT
1. PROJECT可以指定工程名称project_name,并可指定工程支持的语言
`PROJECT (HELLO [CXX] [C] [Java])`
2. **注意** 该指令隐式定义了两个变量,`<projectname>_BINARY_DIR`(等同`PROJECT_BINARY_DIR`) 以及`<projectname>_SOURCE_DIR`(等同`PROJECT_SOURCE_DIR`);这两个变量的值分别为生成的二进制文件(包括可执行文件和库文件)的存放位置,源文件的位置

#### SET
SET 指令的语法：
`SET(VAR [VALUE] [CACHE TYPE DOCSTRING [FORCE]])`

#### MESSAGE
MESSAGE 用于向终端输出用户定义的信息
`MESSAGE([SEND_ERROR | STATUS | FATAL_ERROR] "message to display"...)`

- SEND_ERROR,产生错误,生成过程被跳过.
- SATUS,输出前缀为—的信息.
- FATAL_ERROR,立即终止所有 cmake 过程.

#### ADD_EXECUTABLE
`ADD_EXECUTABLE(hello ${SRC_LIST})`
定义工程会生成一个文件名为 hello 的可执行文件,相关的源文件是 SRC_LIST 中定义的源文件列表, example1中等同与 `ADD_EXECUTABLE(hello main.c)`

#### ADD_LIBRARY
`add_library(<name> [<type>] [EXCLUDE_FROM_ALL] <sources>...)`
```
type:
 - STATIC 链接其他目标时使用的目标文件存档。
 - SHARED 一个动态库，可以由其他目标链接并在运行时加载。
 - MODULE 一个插件，可能不会被其他目标链接，但可以在运行时使用类似 dlopen 的功能动态加载。
 若未设置，则默认值为 STATIC 或 SHARED 基于 BUILD_SHARED_LIBS 变量的值。
```
#### ADD_SUBDIRECTORY
`ADD_SUBDIRECTORY(source_dir [output_binary_dir] [EXCLUDE_FROM_ALL])`
向当前工程添加存放源文件的子目录，并可以指定中间二进制和目标二进制存放的位置。
EXCLUDE_FROM_ALL 参数的含义是将这个目录从编译过程中排除

#### SUBDIRS
`SUBDIRS(dir1 dir2...)`
这个指令已经不推荐使用。它可以一次添加多个子目录，
并且，即使外部编译，子目录体系仍然会被保存.

#### find_package

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

##### find_package搜索路径

1. 在局部缓存中查看以下变量值，使用 NO_CMAKE_PATH 指定是否跳过该步骤
`CMAKE_PREFIX_PATH`
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

**注意** cmake在搜索路径下查找`<package_name>Config.cmake`或`Find<package_name>.cmake`文件
cmake在每个目录prefix下会尝试进行一系列的可能的查找
`<prefix>/                                               `
`<prefix>/(cmake|CMake)/                                 `
`<prefix>/<name>*/                                       `
`<prefix>/<name>*/(cmake|CMake)/                         `
`<prefix>/(lib/<arch>|lib|share)/cmake/<name>*/          `
`<prefix>/(lib/<arch>|lib|share)/<name>*/                `
`<prefix>/(lib/<arch>|lib|share)/<name>*/(cmake|CMake)/`

#### target_link_libraries
`target_link_libraries(<target> ... <item>... ...)`
指定链接目标时和其依赖项时要使用的库或标志

#### target_link_options
```
target_link_options(<target> [BEFORE]
  <INTERFACE|PUBLIC|PRIVATE> [items1...]
  [<INTERFACE|PUBLIC|PRIVATE> [items2...] ...])
```
向可执行文件、共享库或模块库目标的链接步骤添加选项。


### camke常用变量

- `PROJECT_SOURCE_DIR`，`PROJECT_BINARY_DIR`参PROJECT指令
- `EXECUTABLE_OUTPUT_PATH`指定最终的目标二进制的位置(不包含编译生成
的中间文件)
- ` LIBRARY_OUTPUT_PATH`指定最终的共享库的位置(不包含编译生成
的中间文件)


##### 工程清理
`make clean`对构建结果进行清理

##### cmake编译配置(选择编译器和编译目标架构)

x86 用32位的编译器编译出32位程序
x64 用64位的编译器编译出64位程序
x86_x64 用32位的编译器编译出64位程序
x64_x86 用64位的编译器编译出32位程序


### cmake常见问题

#### cmake如何确定使用gcc编译还是g++编译
1. 通过在 `project` 中指定的项目语言langages
2. 通过 `add_executable` 或 `add_library` 中，源文件的后缀名 `.cpp` 对应g++，`.c` 对应gcc

#### cmake指定二进制文件的输出目录

```cmake
# PROJECT_BINARY_DIR当前所有二进制文件输出目录,设置不生效

set(CMAKE_RUNTIME OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
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