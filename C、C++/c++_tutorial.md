# C++

## 定义

- 函数指针 `int (*function_pointer)(int, int);`

## 关键字

### explicit

主要用于防止构造函数的隐式类型转换，提高代码的安全性和可读性。

基本作用
explicit关键字用于修饰类的构造函数，表示该构造函数必须显式调用，不能用于隐式转换。

    Point p1(1, 2);       // 正确：显式调用
    Point p2 = {1, 2};    // 错误：explicit阻止列表初始化隐式转换
    drawPoint({1, 2});    // 错误：explicit阻止隐式转换

    nm -u your_library.a列出静态库中所有未定义的符号(标记为U)
    ar -t your_library.a        # 列出库中包含的所有.o文件
nm your_library.a | grep 'U' # 查看所有未定义符号

常见依赖库判断方法
看到pthread_开头的符号 → 需要-lpthread

看到crypto_开头的符号 → 需要-lcrypto

看到ssl_开头的符号 → 需要-lssl

看到z_开头的符号 → 需要-lz

### decltype

检查实体的声明类型，或表达式的类型和值类别(从C++11开始)

> Example:
```cpp
int i = 33;
decltype(i) j = i * 2;  // j类型为int
decltype((i)) j = i;  // j类型为int&

auto f = [](int a, int b) -> int
{
    return a * b;
};

decltype(f) g = f; // lambda 的类型是独有且无名
i = f(2, 2);
j = g(3, 3);
```

**注意** decltype在获取lambda函数类型时必须使用(因为lambda类型独有且无名)