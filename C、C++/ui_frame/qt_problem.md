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

#### 在子线程中访问ui对象一定报错吗?

不一定，主要取决于qt有没有做线程检查
- 直接调用: 如果方法涉及UI操作（如text(), value()等），几乎肯定会报错
- 安全方式: 使用invokeMethod或信号槽可避免线程问题
- 只读数据: 如果只是获取简单数据成员且不涉及GUI，可能不会立即报错，但仍不建议这样做


#### 在QT事件循环未启动时操作QObject对象有问题吗？

### MVD相关

#### paint事件中, save/restore 方法作用以及paint内部是实时更新ui的吗？

> 参 `QT` 源码: 
- `save() {...new status create...d->states.push_back(d->state);...}` 创建一个当前状态的新状态并将呢新状态放到状态栈中
- `restore() {...d->states.pop_back();d->state = d->states.back();...}` 丢弃save创建的新状态,并恢复至保存时的状态

#### `setData`/`property` 存储自定义数据的区别

- `setData/data` 一般用于模型项相关类, 以 `Qt::ItemDataRole (int)` 为键, 性能较高, 常用于模型数据存储
- `setProperty/property` 一般用于 `QObject` 派生类, 以字符串作为key, 性能相对较低, 常用于动态属性、样式表、通用数据存储

## bug

### QMetaObject::invokeMethod: No such method

对于非槽函数来讲需要通过 `Q_INVOKABLE` 宏定义函数在元对象中可以调用, 在声明时添加即可