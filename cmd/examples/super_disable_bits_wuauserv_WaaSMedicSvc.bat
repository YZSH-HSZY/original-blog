:: ֹͣwindow������ط���
sc stop WaaSMedicSvc

sc stop wuauserv

sc stop bits

:: �Թ���Ա��ݽ���windowҽ������,������ֹ�������������
reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WaaSMedicSvc /v Start /t REG_DWORD /d 4 /f

:: ����bits����
sc config bits start=disabled
:: disabledΪ���ã�demandΪ�ֶ�

:: ����window���·���
sc config wuauserv start=disabled

