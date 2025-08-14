# jsonpath

一种类似xpath操作xml文档的表达式语言

## Usage

- `$` 表示文档的根元素
- `@` 表示文档的当前元素
- `.node_name 或 ['node_name']` 匹配下级节点
- `[index]` 检索数组中的元素
- `[start:end:step]` 支持数组切片语法
- `*` 作为通配符，匹配所有成员
- `..` 子递归通配符，匹配成员的所有子元素
- `(<expr>)` 使用表达式
- `?(<boolean expr>)` 进行数据筛选

## Example

- `jsonpath.jsonpath(fs,"$..PGNs[?(@.Type=='Mixed')]")`, 选择PGNs的对象数组中,Type字段为Mixed的