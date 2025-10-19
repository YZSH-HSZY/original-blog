# sqlite
sqlite 是一个轻量的关系型数据库，其引擎不工作在独立的进程上，你可以按应用程序需求进行静态或动态连接。（即使用sqlite应用程序或api打开一个已存在数据库文件.db）

直接使用sqlite3打开一个sqlite命令行，如未指定db则默认连接到内存暂态数据库，可在关闭时保存。

## sqlite commandline interface

### slqite命令行帮助

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

### sqlite默认表sqlite_master
每个数据库中存在一张sqlite_master，保存了关于你的数据库表的关键信息。使用`.schema sqlite_master`查看

### sqlite查看当前的显示设置
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
### sqlite显示表头
`.head on`

### sqlite设置输出模式

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

### sqlite操作数据库
- 使用`.open test.db`打开或创建一个数据库
- 
- 以.sql文本的形式保存数据库
`sqlite3 testDB.db .dump > testDB.sql`转换整个 testDB.db 数据库的内容到 SQLite 的语句中，并将其转储到 ASCII 文本文件 testDB.sql 中

可以通过简单的方式从生成的 testDB.sql 恢复`sqlite3 testDB.db < testDB.sql`

### sqlite操作表
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

## sqlite函数

### 字符串函数

- `substr({string}, {start_idx(Increment from 1)}, [substring_length])`: 获取指定子字符串
- `{string1} || {string2}`: 拼接字符串

## sqlite事务和锁

事务（Transaction）具有四个标准属性，通常根据首字母缩写为 ACID：
原子性（Atomicity）、一致性（Consistency）、隔离性（Isolation）、持久性（Durability）

### sqlite事务使用示例
```sql
-- 开始事务处理。
BEGIN TRANSACTION

-- 保存更改，或者可以使用 END TRANSACTION 命令。
COMMIT or END TRANSACTION

-- 回滚所做的更改。
ROLLBACK
```

### sqlite锁状态
SQLite数据库文件有5种锁的状态。一个线程只有在拥有低级别的锁的时候，才能获取更高一级的锁。

- UNLOCKED：表示数据库此时并未被读写。
- SHARED：表示数据库可以被读取。可以同时被多个线程拥有。一旦某个线程持有SHARED锁，就没有任何线程可以进行写操作。
- RESERVED：表示准备写入数据库。RESERVED锁最多只能被一个线程拥有，此后它可以进入PENDING状态。
- PENDING：表示即将写入数据库，正在等待其他读线程释放SHARED锁。一旦某个线程持有PENDING锁，其他线程就不能获取SHARED锁。这样一来，只要等所有读线程完成，释放SHARED锁后，它就可以进入EXCLUSIVE状态了。
- EXCLUSIVE：表示它可以写入数据库了。进入这个状态后，其他任何线程都不能访问数据库文件。因此为了并发性，它的持有时间越短越好。

**注意** sqlite的锁为文件锁，一旦加锁，整个数据库均会被加锁

> SQLite就是靠这5种类型的锁，巧妙地实现了读写线程的互斥。同时也可看出，写操作必须进入EXCLUSIVE状态，此时并发数被降到1，这也是SQLite被认为并发插入性能不好的原因。另外，read-uncommitted和WAL模式会影响这个锁的机制。在这2种模式下，读线程不会被写线程阻塞，即使写线程持有PENDING或EXCLUSIVE锁。

### sqlite查看锁模式
`PRAGMA locking_mode;` 该命令将返回锁定模式的值，例如 `NORMAL` 表示使用默认的锁定模式。

## sqlite优化操作

### 全文搜索(FTS)虚拟表

语句示例: `create virtual table[main].[place_name] using[fts3](t_name text, obj_idx integer)`
```sh
using[fts3] - 指定使用FTS3(全文搜索)虚拟表模块
    FTS3是SQLite的全文搜索引擎扩展模块
    它提供了高效的文本搜索功能
```
> 特点:
1. 专门优化用于文本搜索
2. 支持高效的全文搜索查询(使用MATCH操作符)
3. 自动维护内容索引
4. 支持词干提取、前缀搜索等高级功能
5. 不直接支持某些标准SQL功能(如外键约束)

> 常用于地名搜索、文档搜索等场景

## SQlite-C API

> example:
```c
const char *select_sql = "SELECT id, name, age FROM users WHERE age > ?;";
rc = sqlite3_prepare_v2(db, select_sql, -1, &stmt, NULL);
if (rc != SQLITE_OK) {
    fprintf(stderr, "准备查询语句失败: %s\n", sqlite3_errmsg(db));
    return 1;
}
    
// 绑定参数并查询
sqlite3_bind_int(stmt, 1, 28);
    
while ((rc = sqlite3_step(stmt)) == SQLITE_ROW) {
    int id = sqlite3_column_int(stmt, 0);
    const char *name = (const char*)sqlite3_column_text(stmt, 1);
    int age = sqlite3_column_int(stmt, 2);
    
    printf("ID: %d, Name: %s, Age: %d\n", id, name, age);
}

// 清理资源
sqlite3_finalize(stmt);
sqlite3_close(db);
```
### sqlite3_open 

### sqlite3_prepare/sqlite3_prepare16

sqlite语句编译, 将要执行的语句编译成字节码
> 注意
- 首选`sqlite3_prepare_v2`接口, `sqlite3_prepare`是遗留接口, 避免使用, `sqlite3_prepare_v3`具有额外参数prepFlags选项用于特殊用途
- 首选UTF-8接口, UTF-16是将UTF-16的输入转换为UTF-8, 然后调用UTF-8的接口
> 参数
- `db`: 先前成功调用`sqlite3_open`/`sqlite3_open_v2`/`sqlite3_open16`获取的 `数据库连接`, 数据库连接必须没有被关闭
- `zSql`: 是要编译、编码的语句
- `nByte`: 参数为负，则读取zSql到第一个零终结, 正则是从zSql读取的字节数, 0则没有准备生成语句
- `pzTail`: 如果不为NULL, 则`*pzTail`左指向`zSql`中未编译的部分. (因为`sqlite3_prepare_v2`默认只编译一条语句, 多语句时有用)
- `*ppStmt`: 左指向一个编译好的`准备好的语句`，使用 `sqlite3_step()` 执行, 如果错误, 则`*ppStmt`为空, 使用`sqlite3_finalize`删除编译后的SQL语句
- 成功, `sqlite3_prepare` 系列返回 `SQLITE_OK`, 否则返回错误码
```c
SQLITE_API int sqlite3_prepare_v2(
  sqlite3 *db,            /* Database handle */
  const char *zSql,       /* SQL statement, UTF-8 encoded */
  int nByte,              /* Maximum length of zSql in bytes. */
  sqlite3_stmt **ppStmt,  /* OUT: Statement handle */
  const char **pzTail     /* OUT: Pointer to unused portion of zSql */
);
```

## sqlite error示例及解决办法

### 多线程使用同一对象错误
> 错误信息: `sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread.，`
> 解决方案:
> 1. 连接时使用 check_same_thread 参数，`sqlite3.connect('example.db', check_same_thread=False)`
> 2. 为每个线程使用独立的对象并通过锁进行同步
> 3. 使用 `sqlalchemy` orm框架，如下:
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
# 创建数据库引擎
engine = create_engine('sqlite:///example.db')
# 创建 scoped_session
Session = scoped_session(sessionmaker(bind=engine))
with Session() as session:
    ...
# 在程序结束时移除所有会话
Session.remove()
```