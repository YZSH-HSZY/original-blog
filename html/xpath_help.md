## xpath

### 在浏览器console中使用xpath定位
1. 绝对定位
`$x("/html/body/table")`
2. 相对定位
`$x(//<xpath_expression>)`

属性选择@
not()
contains()
normalize-space 定位时忽略空格
parent:: 父元素定位
child:: 子元素定位
preceding-sibling:: 上一个兄弟
following-sibling:: 下一个兄弟
descendant:: 后代元素
ancestor:: 祖先元素定位