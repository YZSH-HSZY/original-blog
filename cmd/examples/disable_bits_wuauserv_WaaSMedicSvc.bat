:: 停止window更新相关服务
runas /profile /env /user:administrator "sc stop WaaSMedicSvc"

runas /profile /env /user:administrator "sc stop wuauserv"

runas /profile /env /user:administrator "sc stop bits"

:: 以管理员身份禁用window医生服务,需解决禁止输入空密码问题
runas /profile /env /user:administrator "reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WaaSMedicSvc /v Start /t REG_DWORD /d 4 /f"

:: 禁用bits服务
runas /profile /env /user:administrator "sc config bits start=disabled"
:: disabled为禁用，demand为手动

:: 禁用window更新服务
runas /profile /env /user:administrator "sc config wuauserv start=disabled"

