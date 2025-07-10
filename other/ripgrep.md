# ripgrep

基于rust实现的grep, 较快

## options

```sh
    --files  不答应搜索文件内容
    -F/--fixed-strings  禁用正则表达式匹配
    --sort <path>  强制 ripgrep 按文件名对其输出进行排序
    -i/--ignore-case  搜索模式时，忽略大小写差异
    --debug  显示 ripgrep 的调试输出
    -g <GLOB>  包含的文件路径
```

## example

- `rg -F "content" .`
- `rg -g "*.ui" .`