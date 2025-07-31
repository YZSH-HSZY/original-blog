# gdb

GDB调试器用于观测一个程序在执行时"内部"发生了什么或者程序在崩溃时正在做什么

[gdb手册](https://www.sourceware.org/gdb/documentation/)

## 使用

```sh
gdb [options] [executable-file [core-file or process-id]]
gdb [options] --args executable-file [inferior-arguments ...]
```

> 选项
- `--args <executable-file> [args...]` 将可执行文件之后的参数传递给调试程序进程
- `--pid=<PID>` 附加gdb到一个运行线程

## 调试命令

- `n`: 执行下一行程序(之后停止);跳过该行中的任何函数调用
- `ni`: 执行一条指令(汇编级)
- `s`: 执行下一行程序(之后停止);步进该行的任何函数调用
- `si`: 执行一条指令(汇编级)
- `c`: 继续运行程序
- `run [arglist]`: 开始运行程序
- `list [file:]function`:  在程序当前停止位置附近显示程序的文本
- `x/<FMT> <ADDRESS>`: 检查内存, FMT: `<repeat-count><format-letter><size-letter>`; ADDRESS是要检查的内存地址的表达式.
    > Format letters:  `o(octal)`/`x(hex)`/`d(decimal)`/`u(unsigned decimal)`/`t(binary)`/`f(float)`/`a(address)`/`i(instruction)`/`c(char)`/`s(string)`/`z(hex, zero padded on the left)`
    > Size letters: `b(byte, 1 bytes)`/`h(halfword)`/`w(word)`/`g(giant, 8 bytes)`
    > 此命令的作用是: 按照FMT打印指定数量的指定大小的对象, 并按`Format letters`指定的形式显示;如果repeat-count指定的是负数,则从地址开始向后检查内存
    > 默认使用上一次的格式, 默认计数为1, 默认地址是上次操作的地址+1

### 断点
- `b {line_no | function_name}` 设置断点(C级)
- `b *fun_name` 函数断点(汇编级)
- `b ... if i == 9` 条件断点
- `clear {line_no}` 清楚断点
- `info break` 显示所有断点
- `delete {breakpoints num}` 删除指定编号的断点

### 堆栈
- `bt [num]` 显示堆栈信息, 可选项num指定显示的堆栈数
- `frame {index}` 切换堆栈
- `info frame {index}` 打印指定堆栈的详细信息
- `f` 查看当前位于哪一堆栈
- `up {n}` 上移n个栈
- `down {n}` 下移n个栈

### 寄存器

- `info registers` 查看通用寄存器
- `info registers register-name`/`print $register-name` 打印指定寄存器的值
- `info all-registers` 查看所有寄存器(包括浮点向量等)

### 参数

- `set args` 指定运行时参数，例`set args 10 20 30 40 50`
- `show args` 查看设置好的运行参数
- `info locals` 打印当前函数的局部变量

## 示例

### 查看执行链接文件是否存在调试信息

`readelf -S <elf_file> | grep "debug"` 显示各个节头信息(静态库等同)

### gdb调试python扩展

#### 单py文件调试
1. 使用 `gdb python` 开启gdb模式下调试py文件
2. 通过 `b <func_name>` 在c的调用函数名中设置断点
3. `run <py_file>` 开始或重新运行py文件

### gdb以16进制查看
`x/161xb msg`

### gdb调试时出现optimized out或断点与文件行不对应
> 描述: 这一般是由于在gcc编译时会进行一定程度的优化，会更改生成的机器码执行顺序，因此在gdb加载符合表并运行时，会出现非源码跳转的现象，以及变量优化。

> 解决方案: gcc选项-O支持不同级别的优化。使用-O0禁用它们，并使用-S输出程序集。-O3是最高级别的优化。

从gcc 4.8开始，可以使用优化级别的-Og。它支持不会干扰调试的优化，并且是标准编辑-编译-调试周期的推荐默认设置。

若要将程序集的方言更改为英特尔或att，请使用-masm=intel或-masm=att。

您还可以使用-fname手动启用某些优化。

### gdb汇编级调试

> 在gdb启动后通过
 - `set disassemble-next-line on` 开启自动反汇编
 - `layout regs -tui` 显示寄存器和源码视图

### 交叉开发的远程调试
```sh
# 使用同目标架构相同的gdb,开发板上使用`gdbserver :6666 ./program`启动
arm-linux-gnueabihf-gdb ./target_program
(gdb) target remote 192.168.8.32:6666
```

## bug

### 其它平台上编译的程序在另一平台上调试,无法打断点

一般是由于调试信息的源代码路径不匹配导致的
> 解决方案: 
- 编译时重映射调试信息中的路径 `gcc -g -fdebug-prefix-map=/container/path=/host/path -o program source.c`
- 使用gdbserver远程附加调试
