# 控制台信号处理

## example

### SetConsoleCtrlHandler 函数

```c
BOOL WINAPI SetConsoleCtrlHandler(
  _In_opt_ PHANDLER_ROUTINE HandlerRoutine,
  _In_     BOOL             Add
);
// HandlerRoutine [in, optional]
// 应用程序定义的要添加或删除的 HandlerRoutine 函数的指针
// - Add [in]
// 如果此参数为 TRUE，则添加处理程序；如果 FALSE，则删除处理程序。
```

调用进程的处理程序函数列表中添加或删除应用程序定义的 HandlerRoutine 函数。
确定调用进程是否忽略 Ctrl+C 信号