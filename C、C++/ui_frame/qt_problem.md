# 描述

记录一些qt开发时产生的问题

### 信号/槽相关

#### 事件如何接受自定义类型的信号, 原理是什么?

- `.h` 中完成信号注册 `Q_DECLARE_METATYPE(stCustomType);`
- 执行代码中进行元类型的注册 `qRegisterMetaType<stCustomType>("stCustomType");`

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

**注意** 连接start信号的槽执行完毕, 不代表QThread完成
**总结** QThread默认在exec中开启事件循环, 当循环中还有事件时, QThread不会自动退出

#### QMetaObject::invokeMethod是如何确保方法多线程安全的?

- 通过 Qt 的事件循环和线程间通信机制实现的, 每个QT线程都有自己的`Event Loop`(一般主线程事件循环有QApplication::exec()启动, 其他线程由 `QThread::exec` 启动)
- 每个 `QObject` 都有一个线程关联性，表示其"属于"哪个线程。当对象被创建时，就与创建它的线程关联
- `Queued Connection`(队列连接), 使用 `Qt::QueuedConnection` 或 `Qt::AutoConnection(different thread)`时，方法调用会被封装成一个事件并投递到目标对象所在线程的事件队列中

> 内部流程大概如:
* `QMetaObject::invokeMethod(q_obj, func, connect_way [, Q_ARG(type, arg)...])` 
* 封装为一个 `QMetaCallEvent` 事件, `QMetaCallEvent *event = new QMetaCallEvent(slotIdx, receiver, parameters...);`
* 投递事件到目标线程所属的事件队列 `QCoreApplication::postEvent(receiver, event);`
* 目标线程的事件循环从队列中获取事件并执行方法调用

## bug

### QMetaObject::invokeMethod: No such method

对于非槽函数来讲需要通过 `Q_INVOKABLE` 宏定义函数在元对象中可以调用, 在声明时添加即可