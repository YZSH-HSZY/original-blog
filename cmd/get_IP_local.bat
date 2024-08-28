@echo off
rem 借助临时文件设置变量
ipconfig|findstr /R /i /c:"^[^ipv]*192\.168">ipLocal.txt
set /p ipValue=<ipLocal.txt
rem 去除ip中空格
set ipValue=%ipValue: =%
rem 将ip中剪切到剪切板，不使用echo的换行输出
set /p="ftp://%ipValue%:2121/mixia_Download/com_android/" <nul | clip
rem set /p="ftp://%ipValue%:2121/mixia_Download/com_android/" <nul | clip
:: 弹出消息弹窗，提示用户
msg %USERNAME% /time:1 "%ipValue%已复制"

:: 在本地hosts缓存中，将ip与domain绑定
echo %ipValue% yzsh.fun > C:\Windows\System32\drivers\etc\hosts

:: 删除临时文件
del ipLocal.txt
rem pause>nul
rem echo %aset%
rem time /t | set /P oeb=
rem set /P oea=|time /t
rem @echo off
rem echo "txt">ls1.txt
rem time/t >ls1.txt