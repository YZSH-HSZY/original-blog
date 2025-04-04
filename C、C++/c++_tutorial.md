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