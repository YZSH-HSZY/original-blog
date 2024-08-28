#### 获取电池充电状态和电量信息

命令详解查看[bat_help](./bat_help.md)

```
@echo off
setlocal enabledelayedexpansion
:BatteryCheck
for /f %%i in ('wmic path win32_battery get batterystatus ^|sed -n 2p') do (
	set "battery_status=%%i"
)
for /f %%j in ('wmic path win32_battery get EstimatedChargeRemaining ^|sed -n 2p') do (
	set "bat_power=%%j"
)
if "!battery_status!" == "2" (
	echo ===========================================
	echo BatteryStatus           :!battery_status!
	echo EstimatedChargeRemaining:!bat_power!
	echo ===========================================
	exit /b 0
) else (
	echo ===========================================
	echo BatteryStatus           :!battery_status!
	echo EstimatedChargeRemaining:!bat_power!
	echo ===========================================
	exit /b 1
)
```

#### cmd 中使用 runas 命令作为管理员执行命令时禁止输入空密码

解决方案为以下 2 种方式之一

1. 为 administrator 设置非空密码
2. cmd 中键入 secpol.msc，然后按 Enter。导航到本地策略，然后导航到安全选项。找到表明“ 帐户：”的策略：将本地帐户的空白密码限制为仅控制台登录。将其设置为禁用。

以下命令为禁用 Windows Update 服务
`runas /user:administrator "sc config wuauserv start=disabled"`

#### cmd 编辑注册表禁用 Windows 更新医生服务（WaaSMedicSvc）服务

```
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WaaSMedicSvc" /v "Start" /t REG_DWORD /d "4" /f

# reg add 帮助信息：
REG ADD KeyName [/v ValueName | /ve] [/t Type] [/s Separator] [/d Data] [/f]
        [/reg:32 | /reg:64]

  KeyName  [\\Machine\]FullKey
           Machine  远程机器名 - 忽略默认到当前机器。远程机器上
                    只有 HKLM 和 HKU 可用。
           FullKey  ROOTKEY\SubKey
           ROOTKEY  [ HKLM | HKCU | HKCR | HKU | HKCC ]
           SubKey   所选 ROOTKEY 下注册表项的完整名称。

  /v       所选项之下要添加的值名称。

  /ve      为注册表项添加空白值名称(默认)。

  /t       RegKey 数据类型
           [ REG_SZ    | REG_MULTI_SZ | REG_EXPAND_SZ |
             REG_DWORD | REG_QWORD    | REG_BINARY    | REG_NONE ]
           如果忽略，则采用 REG_SZ。

  /s       指定一个在 REG_MULTI_SZ 数据字符串中用作分隔符的字符
           如果忽略，则将 "\0" 用作分隔符。

  /d       要分配给添加的注册表 ValueName 的数据。

  /f       不用提示就强行覆盖现有注册表项。

 /reg:32  指定应该使用 32 位注册表视图访问的注册表项。

 /reg:64  指定应该使用 64 位注册表视图访问的注册表项。
```

#### 创建定时任务

```
SCHTASKS /?
    SCHTASKS /Run /?
    SCHTASKS /End /?
    SCHTASKS /Create /?
    SCHTASKS /Delete /?
    SCHTASKS /Query  /?
    SCHTASKS /Change /?
    SCHTASKS /ShowSid /?

:: 创建batteryshow定时任务，每两分钟执行一次
C:\Users\USER\Desktop>schtasks /create /tn "batteryShow" /tr C:\Users\USER\Desktop\dianchi.bat /sc minute /mo 2
SUCCESS: The scheduled task "batteryShow" has successfully been created.

/create 表创建任务
/tn 指定任务名
/tr 指定执行文件路径
/sc 指定执行粒度
/mo 修饰符，指定时间长度

:: 查看创建的任务
C:\Users\USER\Desktop>SCHTASKS /Query  /tn "batteryShow"

Folder: \
TaskName                                 Next Run Time          Status
======================================== ====================== ===============
batteryShow                              2023/7/25 14:36:00     Ready
```

**计划任务相关 bug？**

1. ==不执行 bug== : 手动使用 cmd 命令创建的计划任务，可能默认的条件是在电池充电时执行，可以在计划任务程序管理中更改。
   ![Alt text](imgs/image.png)
2. ==读写文件错误 bug== : 定时脚本写入文件错误，未指定具体的路径，定时脚本路径需全称，操作起始位置也需指定
3. ==权限不够 bug== : 权限拒绝，可以使用最高权限执行
4. ==cmd 不能设置相关参数 bug== : 使用命令创建计划任务时指定相关参数，可以在创建时指定相关配置 xml 文件。（已创建的计划任务 xml 配置在 %SystemRoot%\System32\Tasks 下，不过直接更改不生效--可能需要重启）。示例如下：

```
==> 文件路径中可以加入空格，但需要加上两组引号，
    一组引号用于 CMD.EXE，另一组用于 SchTasks.exe。用于 CMD
    的外部引号必须是一对双引号；内部引号可以是一对单引号或
    一对转义双引号:
    SCHTASKS /Create
        /tr "'c:\program files\internet explorer\iexplorer.exe'
        \"c:\log data\today.xml\"" ...
```

5. ==隐藏计划任务执行 bat 的 cmd 窗口== : 在常规选项中勾选隐藏和不管用户是否登录均执行及不存储密码选项。或者参考
6. ==禁用计划任务服务== : 计划任务相关注册表项位置 HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Schedule

**计划任务学习相关参考**
[windows 计划任务隐藏新姿势分享](https://paper.seebug.org/1464/)
[microsoft window server 参考](https://learn.microsoft.com/zh-cn/windows-server/administration/windows-commands/schtasks-create)

#### 隐藏 cmd 窗口

1. 利用 vb 脚本 `CreateObject("WScript.Shell").Run "cmd /c D:/test.bat",0`
2. 利用计划任务
3. 利用系统服务
4. 编译为 exe 文件
5. 利用 start 命令启动一个单独的窗口以运行指定的程序或命令。可将窗口最小化。
6. 在 bat 文件头中添加如下内容

```
@echo off
if "%1"=="h" goto begin
start mshta vbscript:createobject("wscript.shell").run("""%~nx0"" h",0)(window.close)&&exit
:begin
::以下为正常批处理命令，不可含有pause set/p等交互命令
pause
```
