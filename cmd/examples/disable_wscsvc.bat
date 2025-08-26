@REM 禁用Security Center安全扫描工具

reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\wscsvc /v Start /t REG_DWORD /d 4 /f