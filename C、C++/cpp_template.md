# template

定义类/函数/类型的系列
```
template-declaration:
    template < template-parameter-list > declaration
template-parameter-list:
    template-parameter
    template-parameter-list , template-parameter
declaration:
    - 声明或定义一个函数或类
    - 定义类模板或嵌套在类模板中的成员函数/成员类/静态数据成员
    - 定义类或类模板的成员模板
    - 别名声明
```

**注意** 模板参数列表的 `>` 可能连续出现,会覆盖`>>`操作符

```cpp
template<int i> class X { /* ... */ };
template<class T> class Y { /* ... */ };
X< 1>2 > x1; // syntax error
X<(1>2)> x2; // OK
Y<X<1>> x3; // OK, same as Y<X<1> > x3;
Y<X<6>>1>> x4; // syntax error
Y<X<(6>>1)>> x5; // OK
```