# spdlog

cpp实现的快速日志库

[spdlog官方文档](https://github.com/gabime/spdlog/wiki)

## USAGE

### spdlog日志等级

```cpp
enum level_enum : int {
    trace = SPDLOG_LEVEL_TRACE,
    debug = SPDLOG_LEVEL_DEBUG,
    info = SPDLOG_LEVEL_INFO,
    warn = SPDLOG_LEVEL_WARN,
    err = SPDLOG_LEVEL_ERROR,
    critical = SPDLOG_LEVEL_CRITICAL,
    off = SPDLOG_LEVEL_OFF,
    n_levels
};
```

## EXAMPLE

### 字符串以hex格式打印

通过内部提供的 `spdlog::to_hex` 方法(头文件 `#include "spdlog/fmt/bin_to_hex.h"`)
`spdlog::default_logger()->debug("error: parse msg: {} failed", spdlog::to_hex(revc_msg));`

```c
// format flags:
// {:X} - print in uppercase.
// {:s} - don't separate each byte with space.
// {:p} - don't print the position on each line start.
// {:n} - don't split the output into lines.
// {:a} - show ASCII if :n is not set.
```

> **注意** 
> - `spdlog::to_hex` 支持类似容器的参数, `char*`需转为`std::string`