
[intel开发手册下载](https://www.intel.cn/content/www/cn/zh/support/articles/000006715/processors.html)
[wiki x86调用约定](https://en.wikipedia.org/wiki/X86_calling_conventions)

## x86汇编文件结构

> `section`: 所有x86_64的汇编文件有三种section
    - `.data`: 该section下定义的所有变量,在汇编之前,编译器会完成所有相关变量指向对应内存位置的值的替换
    - `.bss`: 该section,为某些功能的使用而分配内存,和.data section有些类似
    - `.text`: 该section,主要定义程序运行的逻辑和各种的系统调用
> `label:`: 标签用于标记代码的一部分。在编译时，编译将计算标签在内存中的位置。每次使用标签的名称后，该名称将被编译器替换为内存中的位置。
> `_start:` 此标签对所有程序都至关重要。当您编写程序并稍后执行时，它首先在"_start"的位置执行。如果链接器找不到"_start"标签，则会抛出错误。
> `global:`: 当希望链接器能够知道某个标签的地址时，使用global关键字。 生成的目标文件将包含指向global的每个标签的链接。

## x86指令

###### CMP指令

CMP(比较)指令，从目的操作数中减去源操作数的隐含减法操作，并且不修改任何操作数。
指令格式：
```CMP 目的操作数, 源操作数```

>基于无符号数比较的跳转
>助记符	说明
>JB	小于跳转
>JNB	不小于跳转
>JNBE	不小于或等于跳转
>JA	大于跳转
>JNA	不大于跳转
>JNAE	不大于或等于跳转

## 示例

### linux下查看objdump反汇编的代码

一个简易的示例c代码如下:
```c
#include <unistd.h>

int main(){
    write(1, "# ", 2);
    return 0;
}
```
> 生成intel格式的汇编码 `objdump -M intel -D mm.out > mm.S`, 其中main的部分如下:
```s
0000000000001149 <main>:
    1149:       f3 0f 1e fa             endbr64 
    114d:       55                      push   rbp
    114e:       48 89 e5                mov    rbp,rsp
    1151:       ba 02 00 00 00          mov    edx,0x2
    1156:       48 8d 35 a7 0e 00 00    lea    rsi,[rip+0xea7]        # 2004 <_IO_stdin_used+0x4>
    115d:       bf 01 00 00 00          mov    edi,0x1
    1162:       e8 e9 fe ff ff          call   1050 <write@plt>
    1167:       b8 00 00 00 00          mov    eax,0x0
    116c:       5d                      pop    rbp
    116d:       c3                      ret    
    116e:       66 90                   xchg   ax,ax
```
```
caller:
    ; make new call frame
    ; (some compilers may produce an 'enter' instruction instead)
    push    ebp       ; save old call frame
    mov     ebp, esp  ; initialize new call frame
    ; push call arguments, in reverse
    ; (some compilers may subtract the required space from the stack pointer,
    ; then write each argument directly, see below.
    ; The 'enter' instruction can also do something similar)
    ; sub esp, 12      : 'enter' instruction could do this for us
    ; mov [ebp-4], 3   : or mov [esp+8], 3
    ; mov [ebp-8], 2   : or mov [esp+4], 2
    ; mov [ebp-12], 1  : or mov [esp], 1
    push    3
    push    2
    push    1
    call    callee    ; call subroutine 'callee'
    add     esp, 12   ; remove call arguments from frame
    add     eax, 5    ; modify subroutine result
                      ; (eax is the return value of our callee,
                      ; so we don't have to move it into a local variable)
    ; restore old call frame
    ; (some compilers may produce a 'leave' instruction instead)
    mov     esp, ebp  ; most calling conventions dictate ebp be callee-saved,
                      ; i.e. it's preserved after calling the callee.
                      ; it therefore still points to the start of our stack frame.
                      ; we do need to make sure
                      ; callee doesn't modify (or restore) ebp, though,
                      ; so we need to make sure
                      ; it uses a calling convention which does this
    pop     ebp       ; restore old call frame
    ret               ; return
```
### System V AMD64 ABI

- System V AMD64 ABI 的调用约定在 Solaris、Linux、FreeBSD、macOS 上得到遵循，并且是 Unix 和类 Unix作系统中的事实标准。
- x86-64 上的 OpenVMS 呼叫标准基于 System V ABI，具有向后兼容性所需的一些扩展。
- 前六个整数或指针参数在寄存器 `RDI`/`RSI`/`RDX`/`RCX`/`R8`/`R9` 中
- 传递(`R10` 在嵌套函数的情况下用作静态链指针)，而 `XMM0`/`XMM1`/`XMM2`/`XMM3`/`XMM4`/`XMM5`/`XMM6`/`XMM7` 用于第一个浮点参数。
- 与 Microsoft x64 调用约定一样，添加的参数在堆栈上传递。
- 最大 64 位的整数返回值存储在 `RAX` 
- 最大 128 位的值存储在 `RAX` 和 `RDX` 
- 浮点返回值同样存储在 `XMM0` 和 `XMM1` 
- 较宽的 YMM 和 ZMM 寄存器用于传递和返回较宽的值，以代替 XMM（如果存在）

|参数类型|寄存器|
|----|----|
|Integer/pointer arguments 1–6|RDI, RSI, RDX, RCX, R8, R9|
|Floating point arguments 1–8|XMM0 – XMM7|
|Excess arguments|Stack|
|Static chain pointer|R10|