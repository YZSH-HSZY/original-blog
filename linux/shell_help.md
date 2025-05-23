# shell介绍
shell 是一个用 C 语言编写的程序，它是用户使用 Linux 的桥梁。它既是一种命令语言，又是一种程序设计语言。
日常中所说的 shell 通常都是指 shell 脚本，即由shell解释器运行的文本文件。

Linux 的 shell 种类众多，常见的有：
- Bourne shell（/usr/bin/sh或/bin/sh）
- Bourne Again shell（/bin/bash）
- C shell（/usr/bin/csh）
- K shell（/usr/bin/ksh）
- shell for Root（/sbin/sh）

## 快捷键
> 光标移动
   - `Ctrl + a`: 移到命令行首
   - `Ctrl + e`: 移到命令行尾
   - `Ctrl + f`: 按字符前移（右向）
   - `Ctrl + b`: 按字符后移（左向）
   - `Alt + f`: 按单词前移（右向）
   - `Alt + b`: 按单词后移（左向）
   - `Ctrl + x`: 在命令行首和光标之间移动
> 删除
   - `Ctrl + u`: 从光标处删除至命令行首
   - `Ctrl + k`: 从光标处删除至命令行尾
   - `Ctrl + w`: 从光标处删除至字首
   - `Alt + d`: 从光标处删除至字尾
   - `Ctrl + d`: 删除光标处的字符
   - `Ctrl + h`: 删除光标前的字符
> 复制粘贴
   - `Ctrl + y`: 粘贴至光标后
- `Alt + c`: 从光标处更改为首字母大写的单词
- `Alt + u`: 从光标处更改为全部大写的单词
- `Alt + l`: 从光标处更改为全部小写的单词
- `Ctrl + t`: 交换光标处和之前的字符
- `Alt + t`: 交换光标处和之前的单词
- `Alt + Backspace`: 与 Ctrl + w 相同类似，分隔符有些差别

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


### 环境变量
`echo $var_name` 查看环境变量值
`export` 查看全部环境变量

`export PATH=PATH:/bin` 向环境变量中添加值
注意：使用此方法更改的环境变量仅当前终端、当前用户有效，窗口关闭即失效

`.bashrc`或`.bash_profile` 配置文件，在末尾添加一行`export PATH=PATH:/bin`
对当前用户有效，永久生效

配置`/etc/bashrc或/etc/profile或/etc/environment` 文件
对所有用户有效

### declare

> Options:
- `-a`: 声明变量为索引数组
- `-A`: 声明变量为关联数组
- `-i`: 声明变量为整数
- `-r`: 声明变量为只读
- `-x`: 将变量导出为环境变量
- `-g`: 在函数内部使用时,将变量声明为全局变量
- `-l`: 将变量值转为小写
- `-u`: 将变量值转为大写
- `-n`: 将变量声明为引用(Bash 4.3及以上版本)
- `-p`: 显示变量的属性和值

> 这些选项可以组合使用

### 一些变量操作示例

- 获取字符串变量长度 `${#string}`/`${#string[0]}/${#@}`
- 提取子字符串 `${string:1:4}`
- 获取数组变量的长度 `${#arr[*]}`/`${#arr[@]}`
- 获取数组变量的value `${arr[*]}`/`${arr[@]}`
- 获取数组变量的key `${!arr[*]}`/`${!arr[@]}`
- 数组变量添加 `arr+=("new")`/`arr[$index]="new";index=$((index+1))`

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

> 示例: 
   - `for i in $(seq 1 10); do echo $i; done`
   - `for i in {1..10}; do echo $i; done`
   - `for ((i=1; i<=10; i++)); do echo $i; done`

### if指令

> 示例: 
   - `if [ $(ps -ef | grep -c "ssh") -gt 1 ]; then echo "true"; fi`
   - `if <list>; then <list>; [ elif <list>; then <list>; ] ... [ else <list>; ] fi`

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

### 获取数组下标

可以通过`${!array[@]}`获取数组的所有下标，然后使用`for`循环遍历这些下标。以下是一个示例：

```bash
array=("apple" "banana" "cherry")

# 遍历数组下标
for index in "${!array[@]}"; do
  echo "Index: $index, Value: ${array[$index]}"
done
```
