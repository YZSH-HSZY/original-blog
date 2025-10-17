## 描述

记录一些qt开发时产生的问题

### 多线程相关

#### 子线程何时发送finish信号

1. 当线程的事件循环退出时发射 finished 信号
```cpp
void QThread::run() {
    // ... 线程初始化
    exec();  // 进入事件循环
    // 当 exec() 返回时，发射 finished 信号
}
```
2. 手动调用 `quit`/`exit`
```cpp
_m_thread->quit();
_m_thread->exit(0);
```
3. 重写run方法并退出
```cpp
void MyThread::run() {
    // 做一些工作...
    // 函数返回时自动发射 finished
}
```
4. 对象删除导致的连接断开

**总结** QThread默认在exec中开启事件循环, 当循环中还有事件时, QThread不会自动退出