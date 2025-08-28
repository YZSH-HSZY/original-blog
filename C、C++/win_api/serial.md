# WIN-API 串口编程

> 参考文档:
- [dcb结构参考](https://learn.microsoft.com/en-us/windows/win32/api/winbase/ns-winbase-dcb)

## 易混淆点

### window串口描述结构体DCB的构建

- `BYTE StopBits;        /* 0,1,2 = 1, 1.5, 2` DCB的停止位参数是用0代表1位停止位

**注意** 停止位提供帧之间的分隔和同步, 因此有时双方协商的停止位不一致数据不一定出错, 但发送方传输频率一旦过高则大概率导致数据错误

## example

### 串口和socket共同监听

1. 使用WaitForMultipleObjects组合等待
```c
HANDLE waitHandles[2];
int waitHandlesCount = 0;
WSAEVENT sockEvent = WSACreateEvent();
if(ENABLE_READER) {
    WSAEventSelect(reader_socket, sockEvent, FD_READ | FD_CLOSE);
    waitHandles[waitHandlesCount++] = sockEvent;
}
OVERLAPPED ov = {0};
char comBuf[1024];
if(ENABLE_SIMULATOR) {
    ov.hEvent = CreateEvent(NULL, TRUE, FALSE, NULL);
    ReadFile(simulator_handle, comBuf, sizeof(comBuf), NULL, &ov);
    waitHandles[waitHandlesCount++] = ov.hEvent;
}

while(RUN_SIGN) {
    DWORD result = WaitForMultipleObjects(waitHandlesCount, waitHandles, FALSE, 200);
    if(waitHandlesCount == 1 && ENABLE_SIMULATOR && result == WAIT_OBJECT_0) {
        result = WAIT_OBJECT_0 + 1;
    }
    switch (result) {
        case WAIT_OBJECT_0:
            WSANETWORKEVENTS events;
            WSAEnumNetworkEvents(reader_socket, sockEvent, &events);
            if (events.lNetworkEvents & FD_READ) {
                // read socket data
                // recvfrom ...
            }
        break;
    
        case WAIT_OBJECT_0 + 1:
            DWORD bytesRead;
            GetOverlappedResult(simulator_handle, &ov, &bytesRead, TRUE);
            // handle serial data ...
            memset(comBuf, 0, sizeof(comBuf));
            ReadFile(simulator_handle, comBuf, sizeof(comBuf), NULL, &ov);
            break;
        
        case WAIT_FAILED:
            ERROR_PRINT("WaitForMultipleObjects failed");
            break;
        }
}
```

2. 使用I/O完成端口统一管理
3. 使用WSAAsyncSelect模拟消息驱动

|方案	                     |优点	                       |缺点|
|---------------------------|-----------------------------|----|
|WaitForMultipleObjects	    |实现简单，适合少量句柄	        |扩展性差，最多64个句柄|
|I/O完成端口	             |高性能，可扩展性好	            |实现复杂，需要多线程|
|WSAAsyncSelect	            |适合GUI程序	                   |仅适用于Windows GUI程序|