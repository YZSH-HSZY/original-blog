### bat 变量类型

> 1. %0~9，表示接收的命令参数，其中%0 指运行的命令名称
> 2. %*，获取接受的所有参数从1~n

%~1	去除前后引号
%~f1	f 指的是 fully qualified path，即扩展成完整路径。
%~d1	d 指的是 drive letter only，即路径只保留盘符
%~p1	p 指的是 path only，即去掉盘符和文件名。
%~n1	n 指定是 file name only , 即只保留文件名。
%~x1	x 指的是 file name extension only, 即只保留后缀名
%~s1	s 指的是 full qualified path that contains names only.
即指的是
%~a1	a 指的是 file attribute，即文件属性，ls -l 那种 rwxd 之类的
%~t1	t 指的是 date and time of file,即文件更新时间。
%~z1	z 值得是 size，即文件大小。
%~$PATH:1	从PATH中搜索完全符合的第一个路径。
%~dp1,%~nx1	上面的组合

> 3. %i，%%i。用于 for 循环，cmd 下使用%i 表所取的变量，bat 下用%%i。格式如下
>
> FOR %variable IN (set) DO command [command-parameters]
>
> 其中 for 变量为单一字母，分大小写和全局的变量；
> 而且，不能同时使用超过 52 个[for 详情](#cmd "转到for命令")
>
> 3.%variable%,取出变量的值,例：[示例](#variable3)
>
> 4.!variable!,延时环境变量扩展，开启延时环境变量扩展在 bat 中使用，若未开启则类似%variable%。set a=0 后执行`set a=1&echo %a%`，结果为 0.
> bat 执行一行时进行预处理，%a%处理为 0，再执行。
> 使用`setlocal enabledelayedexpansion`命令开启延时环境变量扩展。执行`set a=1&echo !a!`，结果为 1

<p id='variable3'></p>
```
set a=1 
echo %a%
set /p b=   
/P 命令行开关允许将变量数值设成用户输入的一行输入。读取输入
行之前，显示指定的 promptString。
set /a a=%a%+1
echo %a%
```

#### 延迟变量扩展

bat解释器在遇到复合语句时，会将其当做一条语句。这时解释器在对复合语句中的变量进行替换时，会一次性将所有用到的变量进行替换，**因此如果你在复合语句中更改变量值并在之后使用该变量，你会发现变量还是原来值**

这个时候需要启用延迟变量扩展来告诉bat解释器，将复合语句一条条解释。

### <p id="cmd">for 命令</p>

```
FOR /F ["options"] %variable IN (file-set) DO command [command-parameters]
FOR /F ["options"] %variable IN ("string") DO command [command-parameters]
FOR /F ["options"] %variable IN ('command') DO command [command-parameters]
```

> 1.处理文件时,（）中为文件集合 file-set,会打开文件

`FOR /F "eol=; tokens=2,3* delims=, " %i in (myfile.txt do @echo %i %j %k`

> 会分析 myfile.txt 中的每一行，忽略以分号打头的那些行，将
> 每行中的第二个和第三个符号传递给 for 函数体，用逗号和/或
> 空格分隔符号。请注意，此 for 函数体的语句引用 %i 来
> 获得第二个符号，引用 %j 来获得第三个符号，引用 %k
> 来获得 ==第三个符号后的所有剩余符号== 。对于==带有空格的文件名==，你需要用双引号将文件名括起来。为了用这种方式来使
> 用双引号，还需要使用 usebackq 选项，否则，双引号会
> 被理解成是用作定义某个要分析的字符串的。

> 还可以在相邻字符串上使用 FOR /F 分析逻辑，方法是，
> 用单引号将括号之间的 file-set 括起来。这样，该字符
> 串会被当作一个文件中的一个单一输入行进行解析。

> 最后，可以用 FOR /F 命令来分析命令的输出。方法是，将
> 括号之间的 file-set 变成一个==反括字符串==。该字符串会
> 被当作命令行，传递到一个子 CMD.EXE，其输出会被捕获到
> 内存中，并被当作文件分析。如以下例子所示:

> `` FOR /F "usebackq delims==" %i IN (`set`) DO @echo %i //会枚举当前环境中的环境变量名称。 ``

> 2.处理字符串时，使用""括起来。 3.使用命令结果时，用''括起来。
> 例如：for /f %i in ('dir /a-d /b .\*') do echo %i
> 输出当前目录以.起始的文件

### if 和 else 和 else if 

```
rem 在这种写法可读性好，也能执行多语句，但兼容性不太好
if "!battery_status!"=="2" (
	msg %USERNAME% /time:1 "充电中。电量：!bat_power!"
) else (
	msg %USERNAME% /time:1 "未充电。电量：!bat_power!"
)
if "!battery_status!"=="2" (msg %USERNAME% /time:1 "充电中。电量：!bat_power!") else (msg %USERNAME% /time:1 "未充电。电量：!bat_power!")
```
**注意** 如果else换行,需要在前一个`)` 后接 `^` 转义符

### bat示例

#### bat将命令结果输出到空设备

`echo u >nul 2>nul`
将标准输出和错误输出均输出到nul空设备

#### bat获取上一条命令执行结果

1. 通过 `%errorlevel%` 变量获取上一条命名执行成功与否，注意延时变量问题
2. 通过 `&&` 和 `||` 组合命令起到根据命令执行结果分别执行的效果,如 `echo 0 && (echo success) || echo error`

**注意** `echo` 和 `call` 不会改变errorlevel，如果想在call调用的脚本中获取退出码，可以使用 `exit /b <code>` 

#### bat退出脚本

```
exit [/b] [code]
退出当前cmd或批处理脚本
选项:
	/b 		指定退出当前批处理脚本，而不是cmd。如果从批处理脚本外部执行，它将退出cmd
	code 	指定一个数字数字。如果指定了/B，则设置ERRORLEVEL为该数。如果退出cmd，则使用该数字设置进程退出代码。
```

#### 使用`@echo off`关闭命令回显

- 如果你希望在执行bat脚本时，命名行cmd不显示当前执行命令，你可以使用echo off关闭命令回显
**注意** echo off只能关闭之后命令的回显表示，如果你想要`echo off`也不显示，可以使用@符让命令在后台运行