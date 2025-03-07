## 寄存器
寄存器由于兼容性,同一个寄存器可以使用不同的位数 `rax(64bit)/eax(32bit)/ax(16bit)/ah(8bit)/al(8bit)` 

### 通用寄存器
广义寄存器有两种概念，逻辑上的和物理上的，分别是架构相关寄存器（architectural register）和物理寄存器（physical register）。前者是指令集（ISA）提供给编译器可见的，相当于API接口规范，一共16个通用寄存器；后者是硬件上实际设计的，软件领域不直接接触。最新的CPU可能有上百个实际的物理寄存器。当然了，对软件开发人员来说，我们只需要关注逻辑上的通用寄存器。

## AT&T 与 Intel 汇编语法对比

1. 寄存器命名原则
   - **AT&T**: `%eax`
   - **Intel**: `eax`
2. 源/目的操作数顺序
   - **AT&T**: `movl %eax, %ebx` （将 `eax` 的值移动到 `ebx`）
   - **Intel**: `mov ebx, eax` （将 `eax` 的值移动到 `ebx`）
3. 常数/立即数的格式
   - **AT&T**: 
   > `movl $_value, %ebx` （将 `_value` 的地址移动到 `ebx`）
   > `movl $0xd00d, %ebx` （将立即数 `0xd00d` 移动到 `ebx`）
   - **Intel**:
   >  `mov eax, _value` （将 `_value` 的地址移动到 `eax`）
   > `mov ebx, 0xd00d` （将立即数 `0xd00d` 移动到 `ebx`）
4. 操作数长度标识
   - **AT&T**: `movw %ax, %bx`  （将 16 位的 `ax` 移动到 `bx`）
   - **Intel**: `mov bx, ax`  （将 16 位的 `ax` 移动到 `bx`）
5. 寻址方式
   - **AT&T**: `immed32(basepointer, indexpointer, indexscale)`  
     例如：`movl 0x10(%eax, %ebx, 4), %ecx`（将 `[eax + ebx * 4 + 0x10]` 处的值移动到 `ecx`）
   - **Intel**: `[basepointer + indexpointer × indexscale + imm32]`  
     例如：`mov ecx, [eax + ebx * 4 + 0x10]`（将 `[eax + ebx * 4 + 0x10]` 处的值移动到 `ecx`）

**总结**
> AT&T 语法:
> - 寄存器前缀：`%`
> - 立即数前缀：`$`
> - 操作数顺序：源操作数在前，目标操作数在后。
> - 寻址方式：`immed32(basepointer, indexpointer, indexscale)`
> Intel 语法：
> - 寄存器前缀：无
> - 立即数前缀：无
> - 操作数顺序：目标操作数在前，源操作数在后。
> - 寻址方式：`[basepointer + indexpointer × indexscale + imm32]`