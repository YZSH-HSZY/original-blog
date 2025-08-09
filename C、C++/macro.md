# 宏替换

发生在预处理步骤中, 多层宏

## 预处理相关操作符

### 字符串化运算符 (#)

**C/C++标准支持**

```C
// stringizer.cpp
#include <stdio.h>
#define stringer( x ) printf_s( #x "\n" )
int main() {
   stringer( In quotes in the printf function call ); //printf_s( "In quotes in the printf function call" "\n" );
   stringer( "In quotes when printed to the screen" ); //printf_s( "\"In quotes when printed to the screen\"" "\n" );
   stringer( "This: \"  prints an escaped double quote" ); //printf_s( "\"This: \\\" prints an escaped double quote\"" "\n" );
}
```

### 连接操作符 (##)

**C/C++标准支持**

```c
#define CONCAT(a, b) a##b
char* str = CONCAT("asdf", "adf");  // char* str = "asdfadf";
printf("%d\n", CONCAT(12,34));  // 1234
```

### 字符化运算符(#@)

**非C/C++标准支持(MSVC扩展)**

```c
#define ToChar(x) #@x
char a = ToChar(1);  // char a='1';
char a = ToChar(123s);  // char a='s';
char a = ToChar(12345);  // error, 超过4个字符报错
```

## 嵌套宏的展开

> 多层宏（嵌套宏）的处理顺序遵循预处理器的展开规则

1. 扫描参数: 先完全展开宏的参数（除非参数被#或##操作）
2. 代入宏定义: 将展开后的参数代入宏体
3. 重新扫描: 对替换后的结果再次扫描，展开新出现的宏
4. 递归保护: 如果宏名在展开过程中重复出现，则停止展开

**注意** 字符串化(#)和 拼接(##) 会阻止其操作数被展开

```c
#define STR(x) #x
#define CONCAT(a, b) a##b
#define WRAP(x) STR(CONCAT(x, 123))

WRAP(abc)  // 展开步骤：
           // 1. 先展开CONCAT(abc, 123) → abc123
           // 2. 再展开STR(abc123) → "abc123"

#define TO_STR(x) #x
#define EXPAND_TO_STR(x) TO_STR(x)

#define VERSION 123
TO_STR(VERSION)      // 结果为 "VERSION"（直接字符串化，不展开）
EXPAND_TO_STR(VERSION) // 结果为 "123"（先展开VERSION）
```
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


#### __PRETTY_FUNCTION__ / __func__ / __FUNCTION__

GCC 提供了三个魔法常量用于以字符串形式获取当前函数的名称

- `__func__`是c99标准中的一部分
- `__FUNCTION__` 是 `__func__` 的另一个名称, 为了向后兼容 GCC 的旧版本而提供
- `__PRETTY_FUNCTION__` 在 c 中是 `__func__` 的另一个名称, 在 C++ 中, 被求值为顶级空间字符串(包含函数的签名以及其基本名称)

### Unix/BSD系列

#### __USE_MISC

`/usr/include/features.h`中自定义的宏, 用于定义 `BSD` 和 `System V Unix` 共有的东西

### MSVC系列

#### __FUNCSIG__

## 示例

### 宏使用...修饰函数参数时, 替换后的参数有误括号影响参数传递

`"str"`和`("str")`, 前者时正常字符串, 后者在单参数时无影响, 多参数时传递的是逗号表达式的值(即最后一个参数)