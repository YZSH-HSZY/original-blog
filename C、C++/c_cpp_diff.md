# c/cpp兼容

## syntax

### struct

- c: `typedef struct` c独有
- cpp: 支持访问控制符修饰`public`, 支持成员方法

## symbol

cpp中存在符号重命名(name mangling), 因此对应c代码需要兼容时需要进行声明:
- 兼容c库链接, 使用 `extern "C" func();`
- 兼容c源码, 使用 `extern "C" {\n#include "header.h" \n}`