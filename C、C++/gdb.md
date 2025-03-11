# gdb

GDB调试器目的是观测一个程序在执行时"内部"发生了什么或者程序在崩溃时正在做什么

[gdb手册](https://www.sourceware.org/gdb/documentation/)

## 使用

```sh
gdb [options] [executable-file [core-file or process-id]]
gdb [options] --args executable-file [inferior-arguments ...]
```

> 选项
- `--args` 将参数传递给可执行文件

## 调试命令

- `n`: 执行下一行程序(之后停止);跳过该行中的任何函数调用
- `ni`: 执行一条指令(汇编级)
- `s`: 执行下一行程序(之后停止);步进该行的任何函数调用
- `si`: 执行一条指令(汇编级)
- `c`: 继续运行程序
- `run [arglist]`: 开始运行程序
- `list [file:]function`:  在程序当前停止位置附近显示程序的文本

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

- set args 指定运行时参数，例set args 10 20 30 40 50
- show args 查看设置好的运行参数。 

## 示例

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