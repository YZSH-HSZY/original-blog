### sql查询语句执行顺序
sql查询语句格式：
```
select [all|distincy] <column|expression>
from <table_name|view_name|(子查询)> [, <table_name|view_name|(子查询)>...]  [[inner|outer] join <table_name|view_name|(子查询)> on <join_conditions>]
[where <conditions>]
[group by <column|expression> [having <conditions>]]
[order by <column> [asc|desc]]
[limit <offset> [, <line_number>]]
```
1. from对表进行笛卡儿积连接
2. on对笛卡儿积进行 行过滤
3. join保留on条件过滤的部分表行，以null补全空列
4. where过滤行，不能使用聚集函数和as取别名
5. group by 分组，分组后聚集函数可用于每一个分组,且最终每组只会输出一行记录。**之后语句均可使用select中别名**。
6. having过滤符合表达式的分组

### sql聚集函数
```
count([all|distincy] <column>)
sum([all|distincy] <column>)
avg([all|distincy] <column>)
max([all|distincy] <column>)
min([all|distincy] <column>)
```
**注意** 除`count(*)`外，聚集函数均不处理null值，默认跳过null值。聚集函数只能在select表达式和having表达式中使用。

### UNION 操作符用于合并两个或多个 SELECT 语句的结果集。

请注意，UNION 内部的每个 SELECT 语句必须拥有相同数量的列。列也必须拥有相似的数据类型。同时，每个 SELECT 语句中的列的顺序必须相同。

### if
CASE 字段 WHEN 预期值 THEN 结果1 ELSE 结果2 END

IF(expr,result_true,result_false)

ifnull(expr,result)

### sql大量数据插入优化

1. 批量插入数据，只使用一条insert语句,避免多次建立连接
2. 使用事务插入，避免每次insert时自动事务
3. 使用load命令，`load data local infile {sql_file} into table {table_name} fields terminated by ',' lines terminated by '\n' ;`
> 需要在登录sql用户时使用 `-local-infile` 选项，并且通过 `set global local_infile = 1;` 开启从本地加载文件开关
4. 使用主键顺序插入
