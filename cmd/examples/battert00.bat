@echo off
setlocal enabledelayedexpansion
:BatteryCheck

echo -----------------start---------------------->>battery_logs.txt

set "start_time=%time:~0,8%"
echo %start_time%开始执行计划任务>>battery_logs.txt

for /f %%i in ('wmic path win32_battery get batterystatus ^| findstr "[0-9]"') do (
	set "battery_status=%%i"
)

set "exec1_time=%time:~0,8%"
echo %exec1_time%执行完获取电池状态任务----%battery_status%>>battery_logs.txt

for /f %%j in ('wmic path win32_battery get EstimatedChargeRemaining ^| findstr "[0-9]"') do (
	set "bat_power=%%j"
)

set "exec2_time=%time:~0,8%"
echo %exec2_time%执行完获取电池电量任务----%bat_power%>>battery_logs.txt

rem set "battery_sign=未充电。"

:: 如果未充电，弹出提示信息

if not "%battery_status%"=="2" (
	msg %USERNAME% /time:1 "未充电。电量：!bat_power!"
)

:: msg %USERNAME% /time:1 "%battery_sign%电量：!bat_power!"


exit /b 0