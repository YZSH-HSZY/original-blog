# nmake

## example

### nmake多进程编译

`nmake` 本身没有像 `GUN Make` 那样在命令行中中直接指定多任务编译, 只能通过 `cl` 编译器的 `/MP` 选项指定, 因此大部分需要更改makefile文件, 添加 `/MP` 标志

### nmake默认制作的目标

nmake 的默认制造目标是它遇到的第一个目标

> 与 `GNU Make` 不同, `nmake` 没有像 `.DEFAULT_GOAL` 这样的特殊变量来显式地设置默认目标
> 在命令行中键入 `nmake` 而不指定任何目标时，它会从当前目录的 `Makefile` 中读取规则. 然后，它会选择它遇到的第一个"制造目标"作为默认目标来执行