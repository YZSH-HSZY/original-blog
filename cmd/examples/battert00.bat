@echo off
setlocal enabledelayedexpansion
:BatteryCheck

echo -----------------start---------------------->>battery_logs.txt

set "start_time=%time:~0,8%"
echo %start_time%��ʼִ�мƻ�����>>battery_logs.txt

for /f %%i in ('wmic path win32_battery get batterystatus ^| findstr "[0-9]"') do (
	set "battery_status=%%i"
)

set "exec1_time=%time:~0,8%"
echo %exec1_time%ִ�����ȡ���״̬����----%battery_status%>>battery_logs.txt

for /f %%j in ('wmic path win32_battery get EstimatedChargeRemaining ^| findstr "[0-9]"') do (
	set "bat_power=%%j"
)

set "exec2_time=%time:~0,8%"
echo %exec2_time%ִ�����ȡ��ص�������----%bat_power%>>battery_logs.txt

rem set "battery_sign=δ��硣"

:: ���δ��磬������ʾ��Ϣ

if not "%battery_status%"=="2" (
	msg %USERNAME% /time:1 "δ��硣������!bat_power!"
)

:: msg %USERNAME% /time:1 "%battery_sign%������!bat_power!"


exit /b 0