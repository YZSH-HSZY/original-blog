# signal

记录一些程序中使用的信号机制(Linux/Unix)及其对应在Window上的事件处理

## Usage

> **Linux/Unix**
```c
#include <signal.h>
typedef void (*sighandler_t)(int);
//  Success return point to self. On failure, it returns SIG_ERR, and errno is set to indicate the error.
sighandler_t signal(int signum, sighandler_t handler);
```
> `signal` 将信号 `signum` 的处置设置为`handler`, 支持`SIG_IGN`/`SIG_DFL`或程序自定义的函数(信号处理程序)的地址
> 如果将信号signum传递给进程，则会发生以下情况之一:
> * 如果配置为`SIG_IGN`，则忽略该信号
> * 如果处置设置为`SIG_DFL`，则默认动作伴随信号发生(参考 signal(7))
> * 如果配置被设置为一个函数，那么配置被重置为`SIG_DFL`，或者阻塞信号，然后调用处理程序带信号数参数，返回时解除阻塞

**注意** `SIGKILL` and `SIGSTOP` 不能捕获或忽略

> **Window**
```c
// return value: TRUE(表事件已处理)/FLASE(表事件未处理)
typedef BOOL (__stdcall *Handler)(DWORD CtrlType);
SetConsoleCtrlHandler(Handler, TRUE);    // 控制台事件

// return value: EXCEPTION_EXECUTE_HANDLER(终止程序)/EXCEPTION_CONTINUE_SEARCH(继续处理, 在链式异常处理时有用)/EXCEPTION_CONTINUE_EXECUTION(继续执行)
typedef LONG (WINAPI *PTOP_LEVEL_EXCEPTION_FILTER)(
    _In_ struct _EXCEPTION_POINTERS *ExceptionInfo
    );
SetUnhandledExceptionFilter(PTOP_LEVEL_EXCEPTION_FILTER);    // 异常事件
```

## 名称示意


|Linux/Unix signal  |Windows exception code	                |desc          |
|-------------------|---------------------------------------|--------------|
|SIGSEGV	        |EXCEPTION_ACCESS_VIOLATION	            |内存访问违规   |
|SIGFPE	            |EXCEPTION_INT_DIVIDE_BY_ZERO	        |除零错误       |
|SIGILL	            |EXCEPTION_ILLEGAL_INSTRUCTION	        |非法指令       |
|SIGABRT	        |EXCEPTION_NONCONTINUABLE_EXCEPTION	    |不可继续异常   |
|SIGINT             |CTRL_C_EVENT                           |Ctrl+C        |
|SIGTERM            |CTRL_SHUTDOWN_EVENT                    |终止信号,系统关机/注销| 
|SIGHUP             |CTRL_CLOSE_EVENT                       |控制台关闭     |
|......             |CTRL_BREAK_EVENT                       |Ctrl+Break    |
|......             |CTRL_LOGOFF_EVENT                      |用户登出       |

## Example

> Linux/Unix
```cpp
#include <signal.h>
static void ProcessExit(int sig) {
    ...
}
signal(SIGINT, ProcessExit);  // 处理程序退出

static void OnwaCrashHandler(int sig) {
    ...
}
signal(SIGSEGV, CrashHandler);  // 只处理段错误
signal(SIGABRT, CrashHandler);  // 只处理中止信号
signal(SIGFPE, CrashHandler);   // 只处理浮点异常
```

> Window
```cpp
LONG WINAPI ExceptionHandler(EXCEPTION_POINTERS* ExceptionInfo) {
    switch (ExceptionInfo->ExceptionRecord->ExceptionCode) {
        case EXCEPTION_ACCESS_VIOLATION:
            // 对应 SIGSEGV
            break;
        case EXCEPTION_INT_DIVIDE_BY_ZERO:
            // 对应 SIGFPE
            break;
        case EXCEPTION_ILLEGAL_INSTRUCTION:
            // 对应 SIGILL
            break;
        default:
            break;
    }
    
    // 生成堆栈跟踪
    GenerateStackTrace(ExceptionInfo);
    return EXCEPTION_EXECUTE_HANDLER;
}
// Windows风格 - 处理所有未处理异常
SetUnhandledExceptionFilter(ExceptionHandler);  // 处理所有异常
```