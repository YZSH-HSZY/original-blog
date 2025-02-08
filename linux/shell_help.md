## shell介绍
shell 是一个用 C 语言编写的程序，它是用户使用 Linux 的桥梁。它既是一种命令语言，又是一种程序设计语言。
日常中所说的 shell 通常都是指 shell 脚本，即由shell解释器运行的文本文件。

Linux 的 shell 种类众多，常见的有：
- Bourne shell（/usr/bin/sh或/bin/sh）
- Bourne Again shell（/bin/bash）
- C shell（/usr/bin/csh）
- K shell（/usr/bin/ksh）
- shell for Root（/sbin/sh）

## 变量

只包含字母、数字和下划线： 变量名可以包含字母（大小写敏感）、数字和下划线 _，不能包含其他特殊字符。
不能以数字开头： 变量名不能以数字开头，但可以包含数字。
避免使用 Shell 关键字： 不要使用Shell的关键字（例如 if、then、else、fi、for、while 等）作为变量名，以免引起混淆。
使用大写字母表示常量： 习惯上，常量的变量名通常使用大写字母，例如 PI=3.14。
避免使用特殊符号： 尽量避免在变量名中使用特殊符号，因为它们可能与 Shell 的语法产生冲突。
避免使用空格

**注意** 变量名和等号之间不能有空格，这可能和你熟悉的所有编程语言都不一样。

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
## example
```sh
#!/bin/bash
echo "hello"
```
#! 是一个约定的标记，它告诉系统这个脚本需要什么解释器来执行，即使用哪一种 Shell。

### 运行sh文件几种方式
1. 作为可执行程序
chmod +x ./test.sh  #使脚本具有执行权限
./test.sh  #执行脚本
2. 作为解释器参数
/bin/sh test.sh