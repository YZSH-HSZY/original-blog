### sqlite
sqlite 是一个轻量的关系型数据库，其引擎不工作在独立的进程上，你可以按应用程序需求进行静态或动态连接。（即使用sqlite应用程序或api打开一个已存在数据库文件.db）

直接使用sqlite3打开一个sqlite命令行，如未指定db则默认连接到内存暂态数据库，可在关闭时保存。

#### slqite命令行帮助

输入的命令可以缩写，sqlite会根据你以输入的命令进行猜测
使用`.help`查看命令帮助信息
```
.auth ON|OFF             显示授权器回调信息
.backup ?DB? FILE        备份 DB( 默认main) 到 FILE
.bail on|off             击出错误后停止.  Default OFF
.binary on|off           打开或关闭二进制输出.  Default OFF
.cd DIRECTORY            将工作目录更改为 DIRECTORY
.changes on|off          显示由 SQL 更改的行数
.check GLOB              Fail if output since .testcase does not match
.clone NEWDB             Clone data into NEWDB from the existing database
.connection [close] [#]  打开或关闭数据库连接
.databases               列出数据库的名称及其所依附的文件。
.dbconfig ?op? ?val?     List or change sqlite3_db_config() options
.dump ?OBJECTS?          将数据库转换为 SQL 内容
.echo on|off             Turn command echo on or off
.eqp on|off|full|...     Enable or disable automatic EXPLAIN QUERY PLAN
.excel                   Display the output of next command in spreadsheet
.exit ?CODE?             Exit this program with return-code CODE
.expert                  EXPERIMENTAL. Suggest indexes for queries
.explain ?on|off|auto?   Change the EXPLAIN formatting mode.  Default: auto
.filectrl CMD ...        Run various sqlite3_file_control() operations
.fullschema ?--indent?   Show schema and the content of sqlite_stat tables
.headers on|off          打开或关表头显示
.help ?-all? ?PATTERN?   Show help text for PATTERN
.import FILE TABLE       Import data from FILE into TABLE
.imposter INDEX TABLE    Create imposter table TABLE on index INDEX
.indexes ?TABLE?         Show names of indexes
.limit ?LIMIT? ?VAL?     Display or change the value of an SQLITE_LIMIT
.lint OPTIONS            Report potential schema issues.
.load FILE ?ENTRY?       Load an extension library
.log FILE|off            Turn logging on or off.  FILE can be stderr/stdout
.mode MODE ?OPTIONS?     Set output mode
.nonce STRING            Suspend safe mode for one command if nonce matches
.nullvalue STRING        Use STRING in place of NULL values
.once ?OPTIONS? ?FILE?   Output for the next SQL command only to FILE
.open ?OPTIONS? ?FILE?   Close existing database and reopen FILE
.output ?FILE?           Send output to FILE or stdout if FILE is omitted
.parameter CMD ...       Manage SQL parameter bindings
.print STRING...         Print literal STRING
.progress N              Invoke progress handler after every N opcodes
.prompt MAIN CONTINUE    Replace the standard prompts
.quit                    Stop interpreting input stream, exit if primary.
.read FILE               Read input from FILE or command output
.restore ?DB? FILE       Restore content of DB (default "main") from FILE
.save ?OPTIONS? FILE     Write database to FILE (an alias for .backup ...)
.scanstats on|off|est    Turn sqlite3_stmt_scanstatus() metrics on or off
.schema ?PATTERN?        显示匹配 PATTREN 的 CREATE 语句
.selftest ?OPTIONS?      Run tests defined in the SELFTEST table
.separator COL ?ROW?     Change the column and row separators
.sha3sum ...             Compute a SHA3 hash of database content
.shell CMD ARGS...       Run CMD ARGS... in a system shell
.show                    显示各种设置的当前值
.stats ?ARG?             Show stats or turn stats on or off
.system CMD ARGS...      Run CMD ARGS... in a system shell
.tables ?TABLE?          List names of tables matching LIKE pattern TABLE
.testcase NAME           开始重定向输出到 "testcase-out.txt"
.testctrl CMD ...        Run various sqlite3_test_control() operations
.timeout MS              Try opening locked tables for MS milliseconds
.timer on|off            打开或关闭 SQL 计时器(即执行sql的时间显示)
.trace ?OPTIONS?         Output each SQL statement as it is run
.version                 Show source, library and compiler versions
.vfsinfo ?AUX?           关于顶级VFS的信息
.vfslist                 列出所有可用的 VFS
.vfsname ?AUX?           打印 VFS 堆栈的名称
.width NUM1 NUM2 ...     设置列输出的最小列宽
```

#### sqlite默认表sqlite_master
每个数据库中存在一张sqlite_master，保存了关于你的数据库表的关键信息。使用`.schema sqlite_master`查看

#### sqlite查看当前的显示设置
```
sqlite> .show
        echo: off
         eqp: off
     explain: auto
     headers: off
        mode: list
   nullvalue: ""
      output: stdout
colseparator: "|"
rowseparator: "\n"
       stats: off
       width:
    filename: t1.da
```
#### sqlite显示表头
`.head on`

#### sqlite设置输出模式

```
.model [csv|column|html|insert|line|list|tabs|tcl]

csv - 逗号分隔值
column - 左对齐的列。
html - HTML 代码
insert - 表的SQL插入语句
line - 每行一个值
list - 以.separator字符串分隔的值
tabs - 制表符分隔的值
tcl - TCL列表元素
```

#### sqlite操作数据库
- 使用`.open test.db`打开或创建一个数据库
- 
- 以.sql文本的形式保存数据库
`sqlite3 testDB.db .dump > testDB.sql`转换整个 testDB.db 数据库的内容到 SQLite 的语句中，并将其转储到 ASCII 文本文件 testDB.sql 中

可以通过简单的方式从生成的 testDB.sql 恢复`sqlite3 testDB.db < testDB.sql`

#### sqlite操作表
- 查看数据库中的所有表 `.tables`
- 创建表,等同mysql操作
```
create table <table_name>(
    <field_name> <type> [column_constraint],
    ...
);
列约束column_constraint有 NOT NULL，PRIMARY KEY(one or more columns)，UNION等
```
- 查看已存在表的创建语句`.schema <table_name>`