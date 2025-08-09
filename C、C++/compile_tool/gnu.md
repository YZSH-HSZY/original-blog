# GCC/G++

## gcc/g++使用

### gcc/g++区别
gcc适用于c语言编译器,g++适用于c++/c编译。我们常使用的gcc/g++命令是一系列命令的集合，包括cc/cpp的预处理、gcc/g++的编译、as的汇编、ld的链接等。

### gcc/g++查看默认的include搜索位置
` $(g++ --print-prog-name=cc1plus) -v`
```
(debug) ubuntu@yzsh:~/debug/Python-3.12.3$ `g++ --print-prog-name=cc1plus` -v
ignoring nonexistent directory "/usr/lib/gcc/x86_64-linux-gnu/9/include-fixed"
ignoring nonexistent directory "/usr/lib/gcc/x86_64-linux-gnu/9/../../../../x86_64-linux-gnu/include"
#include "..." search starts here:
#include <...> search starts here:
 /usr/include/c++/9
 /usr/include/x86_64-linux-gnu/c++/9
 /usr/include/c++/9/backward
 /usr/lib/gcc/x86_64-linux-gnu/9/include
 /usr/local/include
 /usr/include
End of search list.
```
### gcc/g++指定头文件、库文件搜索路径

- 首先会从当前目录寻找所需要的文件，一般是用户自定义的文件。
- 根据 -I 参数指定的头文件路径来搜索头文件,-L搜索库文件。
- 从环境变量C_INCLUDE_PATH、CPLUS_INCLUDE_PATH、OBJC_INCLUDE_PATH、LIBRARY_PATH、LD_LIBRARY_PATH 中寻找所需要的文件
- 从内定目录`/usr/include、/usr/local/include、/lib、/usr/lib、/usr/local/lib`（这是gcc程序编译时确定的）中寻找所需要的文件。


- 在编译命令中通过编译选项指定搜索路径
```
-I ( i 的大写)  ：指定头文件路径（相对路径或觉得路径，建议相对路径）
-i               ：指定头文件名字 (一般不使用，而是直接放在**.c 文件中通过#include<***.h> 添加)
-L              ：指定连接的动态库或者静态库路径（相对路径或觉得路径，建议相对路径）
-l (L的小写)    ：指定需要链接的库的名字（例如：编译链接静态库文件libc.a，使用`-lc `选项，gcc在指定库文件名时，查找库文件会自动在lib_name添加前缀"lib"和后缀".a"/".so"）。

**注意**：如果链接路径下同时有动态库和静态库，那优先链接动态库。可以显示指定库文件全名-l:lib***.a；-static选项指定链接静态库。
```

- 通过环境变量指定搜索路径
1. `C_INCLUDE_PATH、CPLUS_INCLUDE_PATH、OBJC_INCLUDE_PATH`中寻找所需要的头文件
2. `LIBRARY_PATH` 中寻找所需要的静态库
3. `LD_LIBRARY_PATH`中寻找所需要的动态库，也用于可执行文件运行时加载动态库。
4. `LD_PRELOAD` 定义在程序运行前优先加载的动态链接库

### gcc/g++ 选项
|选项|描述              |
|---|-----------------|
|`-c`            | 只激活预处理,编译,和汇编(但不会链接),也就是他只把程序做成obj文件,此时生成的.obj文件不可直接运行,只在其他文件编译时会用到|
|`-E`            | 只进行预处理，输出.i文件|
|`-S`            | 预处理、编译，不汇编和链接，输出.s文件|
|`-fverbose-asm`            | 在生成的汇编代码中添加额外的注释信息，使其更具可读性|
|`-o <file_name>`| 指定输出文件名|
|`-static`            | 阻止与共享库的链接(在支持动态链接的系统上),其他系统上选项不起作用|
|`-shared`            | 创建共享库|
|`-pie`            | Produce a dynamically linked  position independent executable, 生成一个包含动态链接点的独立可执行文件|
|`-fPIC`| Position Independent Code，位置无关代码|
|`-O<no>`| 开启指定程度的优化选项, 会更改生成机器码相对位置|
|`-nostdinc`|不要在标准系统目录中搜索头文件; 只搜索用 `-I`/`-iquote`/`-isystem`/`-idirafter`选项明确指定的目录(以及当前文件的目录)|
|`-nostdinc++`|不要在特定c++的标准目录中搜索头文件, 但仍然要搜索其他标准目录(此选项在构建c++库时使用)|
|`-undef`|不要预定义任何特定于系统或特定于gcc的宏;标准的预定义宏仍然是定义的|
|`-D name[=definition]`|将name预定义为宏, 默认定义为1|

### gcc优化设置
gcc选项-O支持不同级别的优化。使用-O0禁用它们，并使用-S输出程序集。-O3是最高级别的优化。

从gcc 4.8开始，可以使用优化级别的-Og。它支持不会干扰调试的优化，并且是标准编辑-编译-调试周期的推荐默认设置。

若要将程序集的方言更改为英特尔或att，请使用-masm=intel或-masm=att。

您还可以使用-fname手动启用某些优化。

### 参考使用的c/c++默认标准

- 查看指定的默认c版本 `gcc -E -dM - </dev/null | grep "STDC_VERSION"`
- 查看指定的默认cpp版本 `g++ -dM  -E -x c++ /dev/null | grep -F __cplusplus`

### 查看编译器是否支持指定的c/c++标准

- `gcc -std=gnu11 -E -dM - </dev/null | grep "STDC_VERSION"`
- `g++ -std=gnu++17 -dM  -E -x c++ /dev/null | grep -F __cplusplus`

## gnu内建函数

### __builtin_expect
GCC 中的一个内建函数，用于优化程序中的分支预测, 如:
```c
if (__builtin_expect(expr, 0)){
   func1();
} else{
   func1();
}
```
> 上述片段期望表达式expr的值为0, 因此期望执行func2函数, 此时生成的汇编代码优化中JMP跳转期望执行次数少的部分.以进行多分支的预测优化


## gcc扩展

[csdn-c编译器特定扩展](https://blog.csdn.net/2301_76151015/article/details/144235226)
[csdn-宏__VA_ARGS__](https://blog.csdn.net/q2519008/article/details/80934815)

## ld链接器

**注意** Linux/Unix中链接的注意事项
1. 顺序也也会影响链接结果, 链接器从左到右解析依赖
2. 静态库(.a)的链接, 只链接当前未解析的符号

> example
> - 对于有循环依赖的库, 使用`--start-group` 和 `--end-group`包裹链接库, 让链接器反复扫描组内的库,直到所有符号解析完成