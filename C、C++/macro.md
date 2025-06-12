# 宏替换

## 预定义宏

### GNU系列

#### __VA_ARGS__

标识符__VA_ARGS__只能出现在在参数中使用省略号符号的类函数宏的替换列表中

> example:
```c
#define debug(...) fprintf(stderr, __VA_ARGS__)
#define showlist(...) puts(#__VA_ARGS__)
#define report(test, ...) ((test) ? puts(#test) : printf(__VA_ARGS__))
debug("Flag");
debug("X = %d\n", x);
showlist(The first, second, and third items.);
report(x>y, "x is %d but y is %d", x, y);
// results in
fprintf(stderr, "Flag");
fprintf(stderr, "X = %d\n", x);
puts("The first, second, and third items.");
((x>y) ? puts("x>y") : printf("x is %d but y is %d", x, y));
```

> 使用 `##__VA_ARGS__` 在`__VA_ARGS__`为空时, 移除前置逗号(为编译器扩展)

|特性	            |C 标准	            |C++ 标准	    |说明                           |
|-------------------|------------------|---------------|------------------------------|
|`__VA_ARGS__`	    |C99 起支持	        |C++11 起支持	|基本可变参数宏                  |
|`,##__VA_ARGS__`	|非标准	            |非标准	        |GNU 扩展（但主流编译器均支持）   |
|`__VA_OPT__`	    |C23 起支持	        |C++20 起支持	|标准化的零参数处理方式           |


## 示例

### 宏使用...修饰函数参数时, 替换后的参数有误括号影响参数传递

`"str"`和`("str")`, 前者时正常字符串, 后者在单参数时无影响, 多参数时传递的是逗号表达式的值(即最后一个参数)