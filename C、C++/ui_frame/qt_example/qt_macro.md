## qt相关宏设置

- `Q_UNUSED(oldState);` 抑制参数未使用时编译器产生的警告
- `QT_BEGIN_NAMESPACE/QT_END_NAMESPACE` 用于兼容编译时指定了qt命名空间的库, 默认在全局命名空间
- `Q_DECL_DEPRECATED_X("message")` 编译时弃用标记, 定义在类/方法上