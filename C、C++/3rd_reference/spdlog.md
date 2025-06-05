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