:: ֹͣwindow������ط���
runas /profile /env /user:administrator "sc stop WaaSMedicSvc"

runas /profile /env /user:administrator "sc stop wuauserv"

runas /profile /env /user:administrator "sc stop bits"

:: �Թ���Ա��ݽ���windowҽ������,������ֹ�������������
runas /profile /env /user:administrator "reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WaaSMedicSvc /v Start /t REG_DWORD /d 4 /f"

:: ����bits����
runas /profile /env /user:administrator "sc config bits start=disabled"
:: disabledΪ���ã�demandΪ�ֶ�

:: ����window���·���
runas /profile /env /user:administrator "sc config wuauserv start=disabled"

