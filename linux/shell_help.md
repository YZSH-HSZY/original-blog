# shell介绍
shell 是一个用 C 语言编写的程序，它是用户使用 Linux 的桥梁。它既是一种命令语言，又是一种程序设计语言。
日常中所说的 shell 通常都是指 shell 脚本，即由shell解释器运行的文本文件。

Linux 的 shell 种类众多，常见的有：
- Bourne shell（/usr/bin/sh或/bin/sh）
- Bourne Again shell（/bin/bash）
- C shell（/usr/bin/csh）
- K shell（/usr/bin/ksh）
- shell for Root（/sbin/sh）

## 变量

变量定义格式: `<var_name>=<value>`

> 变量命名规则: 只包含字母（大小写敏感）、数字和下划线，不能包含其他特殊字符
   1. 不能以数字开头： 变量名不能以数字开头，但可以包含数字
   2. 避免使用 Shell 关键字： 如 if、then、else、fi、for、while 等，以免引起混淆
   3. 使用大写字母表示常量： 习惯上，常量的变量名通常使用大写字母，例如 PI=3.14
   4. 避免使用特殊符号： 尽量避免在变量名中使用特殊符号，因为它们可能与 Shell 的语法产生冲突
   5. 避免使用空格

**注意** 变量名和等号之间不能有空格，这可能和你熟悉的所有编程语言都不一样。

### 获取变量
`$<var_name>`/`${var_name}`, 变量名外面的大括号是可选的, 大括号主要是用于区分变量边界(默认空格分隔)

**注意** 单引号包围的字符串中变量获取无效, 双引号可以

### 只读变量
`readonly <var_name>` 变量定义后使用readonly标识此变量只读

### 删除变量
`unset <variable_name>` 
**注意** unset不能删除只读变量

### 变量类型

- 字符串变量
- 整数变量, 使用 `declare -i ttt=42` 定义
- 数组变量, 分为索引数组/关联数组, `arr=(1 2 3 4 5)`/`declare -A arr && arr["name"]="hello"`
- 环境变量, 操作系统或用户设置的特殊变量
- 特殊变量, 如 `$0` 表示脚本的名称，`$1`/`$2` 等表示脚本的参数, `$#` 表示传递给脚本的参数数量, `$?` 表示上一个命令的退出状态等, `$*` 以一个单字符串显示所有向脚本传递的参数, `$$` 脚本运行的当前进程ID号, `$!` 后台运行的最后一个进程的ID号, `$-` 显示Shell使用的当前选项，与set命令功能相同。

### 一些变量操作示例

- 获取字符串变量长度 `${#string}`/`${#string[0]}`
- 提取子字符串 `${string:1:4}`
- 获取数组变量的长度 `${#arr[*]}`/`${#arr[@]}`
- 获取数组变量的value `${arr[*]}`/`${arr[@]}`
- 获取数组变量的key `${!arr[*]}`/`${!arr[@]}`

## 运算符
shell中的比较运算符 -eq -ne -gt -lt -ge -le 及 == != 与 逻辑 ...

### 判断字符串为空

1. `if [ -z "$vars" ]`
   > -z 判断字符串长度为0
2. 加一个字符串再比较
```sh
if [ X$STR = "X" ]
　　then
　　　　echo "空字符串"
fi
```
3. 直接使用变量判断
```sh
if [ "$variable" ]
then
   echo "非空"
 else
    echo "空"
fi
```

### 与 或操作
[ -o ] 
[] || []
[ -a ]
[] && []

## 流程控制

### for指令
for 命令格式形如: `for var in item1 item2 ... itemN; do command1; command2… done;` 多行如下:
```sh
for var in item1 item2 ... itemN
do
    command1
    command2
    ...
    commandN
done
```

### if指令

> 示例: 
   - `if [ $(ps -ef | grep -c "ssh") -gt 1 ]; then echo "true"; fi`
   - ``

## 函数
> 函数定义如下:
```sh
[ function ] funname [()]
{
   action;
   [return int;]
}
```

**注意** 函数类似于脚本, 其参数可通过 `$#`/`$*`/`$$`/`$!`/`$@`/`$-`/`$?` 调用

## example
```sh
#!/bin/bash
echo "hello"
```
#! 是一个约定的标记，它告诉系统这个脚本需要什么解释器来执行，即使用哪一种 Shell。

### 运行sh文件几种方式

1. 作为可执行程序
`chmod +x ./test.sh`  #使脚本具有执行权限
`./test.sh`  #执行脚本
2. 作为解释器参数
`/bin/sh test.sh`

### 脚本中当前脚本的绝对路径

1. `readlink -f $0`
2. `cd $(dirname $0) && pwd`

### 忽略命令的标准输出和标准错误
`dpkg -l xvfb > /dev/null 2>&1`
