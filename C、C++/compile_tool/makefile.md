# makefile

[gun-makefile手册](https://www.gnu.org/software/make/manual/make.html)

## makefile 编写rules

简单的makefile具有如下所示的rule形式:

```makefile
target ... : prerequisites ...
    recipe
    ...
    ...
```
- target: 目标通常是由程序生成的文件的名称;包括可执行文件或目标文件,也可以是要执行的动作作的名称, 例如 `clean`
- prerequisite: 先决条件是用作创建目标的输入的文件。一个目标通常依赖于多个文件
- recipe: 配方是 make 执行的动作。一个配方可以有多个命令，要在同一行上或在`\`拼接的多行上。**注意**每行recipe的开头是一个制表符.可以通过 `.RECIPEPREFIX` 变量设置为替代字符

> make 根据创建或更新目标的先决条件执行配方。规则还可以说明如何以及何时执行动作

## make 执行流程

默认情况下，make 从第一个目标开始（不是名称以 `.` 开头的目标，除非它们还包含一个或多个 `/`）。称为默认目标。（目标是使 最终努力更新。 可以使用 命令行参数或`.DEFAULT_GOAL`变量覆写

## makefile函数

### 文件名函数

#### wildcard

Usage: `$(wildcard pattern)`

Describe: 参数模式是一个文件名模式, 通常包含通配符(如shell文件名模式),结果是一个以空格分隔的匹配模式的现有文件名列表

> wildcard支持的通配符包括`*`/`?`/`[...]`, 使用`\`取消通配符的特殊含义