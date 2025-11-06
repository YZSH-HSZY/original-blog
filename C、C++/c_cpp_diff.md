# c/cpp兼容

## syntax

### struct

- c: `typedef struct` c独有
- cpp: 支持访问控制符修饰`public`, 支持成员方法

### struct initial
```c
struct Point {
    int x;
    int y;
    int z;
};
// C99及以上支持, 可以不按顺序初始化
struct Point p1 = {.x = 1, .y = 2, .z = 3};
struct Point p2 = {.y = 5};  // x和z自动初始化为0
// C++20及以上支持, 必须按顺序初始化
Point p1 = {.x = 1, .y = 2, .z = 3};
Point p2 = {.y = 5};  // x和z保持未初始化
```

## symbol

cpp中存在符号重命名(name mangling), 因此对应c代码需要兼容时需要进行声明:
- 兼容c库链接, 使用 `extern "C" func();`
- 兼容c源码, 使用 `extern "C" {\n#include "header.h" \n}`