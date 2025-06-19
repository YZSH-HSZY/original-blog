# snippets 代码片段设置

[官方配置文档](https://code.visualstudio.com/docs/editor/userdefinedsnippets)

## 一些使用示例

- `${TM_FILENAME/([A-Z]+)([a-z]*)\\.?([a-z]*)/${1:/upcase}${2:/upcase}_${3:/upcase}/g}` 转换文件名`BasePGN.hpp` 为 `BASE_PGN_HPP`, 适用于hpp文件的防重定义头