# cross-toolchain

交叉编译器是指用于在一种架构的计算机上编译出能在另一种架构的计算机上运行的程序的编译器。常见如x86开发主机上编译出适用于ARM架构嵌入式设备的代码。

## 命令规范

交叉编译工具链的命名规范是:
`arch [-vendor] [-os] [-(gnu)eabi]`

- arch : 目标架构，如ARM/MIPS
- vendor： 工具链的提供厂商
- os： 支持的操作系统
- eabi：嵌入式应用二进制接口（Embedded Application Binary Interface）
- arm gcc还分为 是否支持操作系统: 支持(arm-none-linux-eabi-gcc) 或不支持(arm-none-eabi-gcc)
- ABI 和 EABI: ABI(Application Binary Interface (ABI) for ARM); EABI(embed ABI)
**注意** 两者主要区别是，ABI是计算机上的，EABI是嵌入式平台上（如ARM，MIPS等）
- arm-linux-gnueabi-gcc 和 arm-linux-gnueabihf-gcc
    > 两个交叉编译器分别适用于 armel 和 armhf 两个不同的架构,armel 和 armhf 这两种架构在对待浮点运算采取了不同的策略, gcc 的选项 -mfloat-abi 的默认值(soft/softfp/hard)不同, 后两者都要求 arm 里有 fpu 浮点运算单元，soft 与后两者是兼容的，但 softfp 和 hard 两种模式互不兼容）
    > soft: 不用fpu进行浮点计算，即使有fpu浮点运算单元也不用，而是使用软件模式
    > softfp: armel架构（对应的编译器为 arm-linux-gnueabi-gcc ）采用的默认值，用fpu计算，但是传参数用普通寄存器传，这样中断的时候，只需要保存普通寄存器，中断负荷小，但是参数需要转换成浮点的再计算
    > hard: armhf架构（对应的编译器 arm-linux-gnueabihf-gcc ）采用的默认值，用fpu计算，传参数也用fpu中的浮点寄存器传，省去了转换，性能最好，但是中断负荷高