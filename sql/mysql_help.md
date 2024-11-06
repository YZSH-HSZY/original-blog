## mysql
mysql包括server、client、connect-driver等几个组成部分，你在安装时可以根据需要只安装对应部分。

#### mysql安装（windows）

下载地址：[官网下载](https://downloads.mysql.com/archives/installer/ "mysql for windows下载地址")

#### mysql安装（linux）
mysql-client-core-8.0
mysql-server-core-8.0
...

#### mysql设置初始密码
mysql安装后默认密码为空，你需要使用如下命令设置初始密码
`mysqladmin -u root password "new_password";`
-u选项指定user，即mysql使用用户

#### mysql更改密码
mysql更改密码与设置初始密码命令相似
``mysql admin -u root -p password "new_password"``
- mysql交互模式下（设置user表需对应权限）
`update mysql.user set password=password(<passwd>) where user="root";`

#### 无密码`mysql -u root -p`登录时报错
使用 `sudo` 命令或以root用户运行

#### mysql创建用户
`create user 'user01'@'localhost' identified by 'user01';`

#### 查看当前用户
`select current_user();`
`select user();`

#### mysql字符集
ASCII: 简称 latin1
UNICODE: 简称 ucs2

#### mysql类型显示转换
CAST(expr as type) # 类型转换
CAST('1' AS UNSIGNED) # 字符串转换
CAST(timestamp_value AT TIME ZONE timezone_specifier AS DATETIME[(precision)])  # 日期转换
CONVERT(expr USING transcoding_name) # 更改编码字符集
CONVERT(expr,type) # 类型转换

#### count带条件计数
利用`count(<columns_name>)`会忽视null值的特性，
可以通过以下几种方式完成满足条件的行计数
1. `count(status != 'completed' or null)`
2. `count(if(status != 'completed', 1, null))`
3. `count(case when status != 'completed' then 1 else null end)`
**注意** 必须带 or null或条件不成立时为null值

#### 保留有效数字
convert(count(status != 'completed' or null)/count(*),Decimal(10,2)) as "Cancellation Rate"
format(,2)
round()
truncate()

#### mysql正则匹配
rlike 
REGEXP [BINARY]
BINARY 使得匹配区分大小写

## mysql函数

### 日期函数
|函数名|描述|例子|
|-----|----|---|
|ADDDATE(d,n)|	计算起始日期 d 加上 n 天的日期|SELECT ADDDATE("2017-06-15", INTERVAL 10 DAY);->2017-06-25|
|ADDTIME(t,n)|	n 是一个时间表达式，时间 t 加上时间表达式 n	|
添加 1天 2 小时, 10 分钟, 5 秒:SELECT ADDTIME("2020-06-15 09:34:21", "1 2:10:5"); -> 2020-06-16 11:44:26|
|CURDATE()|	返回当前日期	||
|CURRENT_DATE()|	返回当前日期	|SELECT CURRENT_DATE();-> 2018-09-19|
|CURRENT_TIME|	返回当前时间	|SELECT CURRENT_TIME();-> 19:59:02|
|CURRENT_TIMESTAMP()|	返回当前日期和时间	|SELECT CURRENT_TIMESTAMP()-> 2018-09-19 20:57:43|
|CURTIME()|	返回当前时间	|SELECT CURTIME();-> 19:59:02|
|DATE()|	从日期或日期时间表达式中提取日期值	|SELECT DATE("2017-06-15"); -> 2017-06-15|
|DATEDIFF(d1,d2)|	计算日期 d1->d2 之间相隔的天数	|SELECT DATEDIFF('2001-01-01','2001-02-02')-> -32|
|DATE_ADD(d，INTERVAL expr type)|	计算起始日期 d 加上一个时间段后的日期，type 值可以是：MINUTE DAY WEEK MONTH YEAR|SELECT DATE_ADD("2017-06-15", INTERVAL 10 DAY);-> 2017-06-25|
|DATE_FORMAT(d,f)|	按表达式 f的要求显示日期 d	|SELECT DATE_FORMAT('2011-11-11 11:11:11','%Y-%m-%d %H:%i:%s')-> 2011-11-11 11:11:11|
|DATE_SUB(date,INTERVAL expr type)|	函数从日期减去指定的时间间隔|SELECT OrderId,DATE_SUB(OrderDate,INTERVAL 2 DAY) AS OrderPayDate FROM Orders|
|DAY(d)|	返回日期值 d 的日期部分	|SELECT DAY("2017-06-15"); -> 15|

#### mysql时间与本地时间不对应

1. 使用 `show variables like "%time_zone%";` 查看当前时区
```
mysql> show variables like "%time_z%";
+------------------+--------+
| Variable_name    | Value  |
+------------------+--------+
| system_time_zone | EST    |
| time_zone        | SYSTEM |
+------------------+--------+
```
1. 通过以下设置配置
set global time_zone = '+8:00'; ##修改mysql全局时区为北京时间，即我们所在的东8区
set time_zone = '+8:00'; ##修改当前会话时区
flush privileges; #立即生效

### mysql 中变量的生命周期

1. 修改 `my.ini` 配置文件，如果要设置全局变量最简单的方式是在 `my.ini` 文件中直接写入变量配置。重启数据库服务就可以使全局变量生效。
```
vim /etc/my.cnf ##在[mysqld]区域中加上
default-time_zone = '+8:00'
/etc/init.d/mysqld restart ##重启mysql使新时区生效
```
2. 不修改配置文件的基础上，使用关键字global设置全局变量 `set global autocommit=1;`
> 使用此方法对global全局变量的设置仅对于新开启的会话才是有效的，对已经开启的会话不生效。
3. 在MySQL中要修改会话（session）变量，可以使用session关键字，如：`set session autocommit=1;`
> 使用此方法对global全局变量的设置仅对于新开启的会话才是有效的，对已经开启的会话不生效。 

**注意** 对变量设置global作用区，在mysql服务重启之后，数据库的配置又会重新初始化，因此global变量会失效。对应需要永久设置的变量，可以在 `my.ini` 中设置。

## mysql内置函数
### MySQL 字符串函数
|函数       |	描述    |
|-----------|----------------------------------------------|
|CHAR_LENGTH(s) |返回字符串的字符数|
|length(s)      |返回字符串的字节数|
|CONCAT(s1,s2...sn)|	字符串 s1,s2 等多个字符串合并为一个字符串|
|SUBSTR(s, start, length)|	从字符串 s 的 start 位置(从1开始计数)截取长度为 length 的子字符串|
|LOCATE(sub_s, full_s)|	判断sub_s在full_s中位置(从1开始)，未找到为0|

### MySQL 日期函数
|函数       |	描述    |
|-----------|----------------------------------------------|
|CURRENT_DATE()	  |返回当前日期|
|CURRENT_TIME	    |返回当前时间|
|CURRENT_TIMESTAMP()	|返回当前日期和时间|
|DATEDIFF(d1,d2)	|计算日期 d1->d2 之间相隔的天数(d1-d2)|


## mysql备份与恢复

### 冷备份

#### mysqldump
mysqldump 是 MySQL 提供的用于备份和导出数据库的命令行工具。

mysqldump 是 mysql 用于转存储数据库的实用程序。它主要产生一个 SQL 脚本，其中包含从头重新创建数据库所必需的SQL命令等。

**注意** 使用 mysqldump 导出数据需要使用 `--tab` 选项来指定导出文件所在的目录，必须是可写的。
##### mysqldump用法
```sh
Usage: mysqldump [OPTIONS] database [tables]
OR     mysqldump [OPTIONS] --databases [OPTIONS] DB1 [DB2 DB3...]
OR     mysqldump [OPTIONS] --all-databases [OPTIONS]
```

1. 导出整个数据库 `mysqldump -u root -p mydatabase > mydatabase_backup.sql`
2. 导出特定表 `mysqldump -u {username} -p {password} [-h {hostname}] {database_name} [table_name] > output_file.sql` 
3. 导出数据库结构,如果只想导出数据库结构而不包括数据，可以使用 --no-data 选项 `mysqldump -u {username} -p {password} [-h {hostname}] --no-data {database_name} > output_file.sql`
4. 导出压缩文件,将导出的数据进行压缩，以减小文件大小 `mysqldump -u {username} -p {password} [-h {hostname}] {database_name} | gzip > output_file.sql.gz`

### 将查询结果导出到文件

`SELECT ... INTO OUTFILE 'file_name'`形式的SELECT可以把被选择的行写入一个文件中
**注意** 输出不能是一个已存在的文件。防止文件数据被篡改。

### 从sql文件中恢复数据库
`mysql -u root -p database_name < dump.sql`

## mysql data_type数据类型

### 数值类型
MySQL 支持所有标准 SQL 数值数据类型。
包括严格数值数据类型(INTEGER、SMALLINT、DECIMAL 和 NUMERIC)，以及近似数值数据类型(FLOAT、REAL 和 DOUBLE PRECISION)。

**注意** INT等同INTEGER，DEC等同DECIMAL

BIT数据类型保存位字段值，并且支持 MyISAM、MEMORY、InnoDB 和 BDB表。

作为 SQL 标准的扩展，MySQL 也支持整数类型 TINYINT、MEDIUMINT 和 BIGINT。下面的表显示了需要的每个整数类型的存储和范围。

### 日期和时间类型
DATETIME、DATE、TIMESTAMP、TIME和YEAR
> 每个时间类型有一个有效值范围和一个"零"值，当指定不合法的MySQL不能表示的值时使用"零"值。
> TIMESTAMP类型有专有的自动更新特性

|类型|	大小( bytes)|	范围|	格式|	用途|
|--------------|-------------|--|--|--|
|DATE|	3|	1000-01-01/9999-12-31|	YYYY-MM-DD|	日期值|
|TIME|	3|	'-838:59:59'/'838:59:59'|	HH:MM:SS|	时间值或持续时间|
|YEAR|	1|	1901/2155|	YYYY|	年份值|
|DATETIME|	8|	'1000-01-01 00:00:00' 到 '9999-12-31 23:59:59'|	YYYY-MM-DD hh:mm:ss|	混合日期和时间值|
|TIMESTAMP|	4|'1970-01-01 00:00:01' UTC 到 '2038-01-19 03:14:07' UTC 结束时间是第 2147483647 秒，北京时间 2038-1-19 11:14:07，格林尼治时间 2038年1月19日 凌晨 03:14:07| YYYY-MM-DD hh:mm:ss	|混合日期和时间值，时间戳|

### 字符串类型
字符串类型指CHAR、VARCHAR、BINARY、VARBINARY、BLOB、TEXT、ENUM和SET

### 枚举与集合类型（Enumeration and Set Types）
ENUM: 枚举类型，用于存储单一值，可以选择一个预定义的集合。
SET: 集合类型，用于存储多个值，可以选择多个预定义的集合。

### 空间数据类型（Spatial Data Types）
GEOMETRY, POINT, LINESTRING, POLYGON, MULTIPOINT, MULTILINESTRING, MULTIPOLYGON, GEOMETRYCOLLECTION: 用于存储空间数据（地理信息、几何图形等）。

### 其他类型
bit存储指定几位bit的数据，例如：bit(8)存储8比特长度

## DCL、DQL、DML、DDL
- DDL(data definition language,数据定义语言)
> 定义关系模式、删除关系、修改关系模式以及创建数据库中的各种对象，比如表、聚簇、索引、视图、函数、存储过程和触发器等等。
数据定义语言是由SQL语言集中负责数据结构定义与数据库对象定义的语言，并且由CREATE、ALTER、DROP和TRUNCATE四个语法组成。

- DQL(,数据查询语言)
> 进行数据库中数据的查询

- DML(,数据操纵语言)
> 进行插入元组、删除元组、修改元组的操作。主要有insert、update、delete语法组成

- DCL 数据控制语言
> 用来授权或回收访问数据库的某种特权，并控制数据库操纵事务发生的时间及效果，能够对数据库进行监视。

### DDL
#### CREATE DATABASE 
```sql
CREATE {DATABASE | SCHEMA} [IF NOT EXISTS] db_name
    [create_option] ...

create_option: [DEFAULT] {
    CHARACTER SET [=] charset_name
  | COLLATE [=] collation_name
  | ENCRYPTION [=] {'Y' | 'N'}
}
charset_name: {
 utf8 | gbk | utf8mb4
}
```
#### CREATE TABLE

```sql
CREATE [TEMPORARY] TABLE [IF NOT EXISTS] tbl_name
    [(create_definition,...)]
    [table_options]
    [partition_options]
    [IGNORE | REPLACE]
    [[AS] query_expression]

column_definition: {
    data_type [NOT NULL | NULL] [DEFAULT {literal | (expr)} ]
      [VISIBLE | INVISIBLE]
      [AUTO_INCREMENT] [UNIQUE [KEY]] [[PRIMARY] KEY]
      [COMMENT 'string']
      [COLLATE collation_name]
      [COLUMN_FORMAT {FIXED | DYNAMIC | DEFAULT}]
      [ENGINE_ATTRIBUTE [=] 'string']
      [SECONDARY_ENGINE_ATTRIBUTE [=] 'string']
      [STORAGE {DISK | MEMORY}]
      [reference_definition]
      [check_constraint_definition]
  | data_type
      [COLLATE collation_name]
      [GENERATED ALWAYS] AS (expr)
      [VIRTUAL | STORED] [NOT NULL | NULL]
      [VISIBLE | INVISIBLE]
      [UNIQUE [KEY]] [[PRIMARY] KEY]
      [COMMENT 'string']
      [reference_definition]
      [check_constraint_definition]
}
```

#### CREATE TRIGGER
```sql
CREATE
    [DEFINER = user]
    TRIGGER [IF NOT EXISTS] trigger_name
    trigger_time trigger_event
    ON tbl_name FOR EACH ROW
    [trigger_order]
    trigger_body

trigger_time: { BEFORE | AFTER }

trigger_event: { INSERT | UPDATE | DELETE }

trigger_order: { FOLLOWS | PRECEDES } other_trigger_name
```
该语句创建一个新的触发器。触发器是一个与表关联的命名数据库对象，当表发生特定事件时，触发器就会激活。必须引用一个永久表。不能将触发器与TEMPORARY表或视图关联。

#### 显示表头
`show columns from <table_name>;`
`DESCRIBE <table_name>;`

### DCL

#### grant授予权限
GRANT语句使系统管理员能够授予权限和角色
`grant all on test.score to 'User01'@'localhost';`

```sql
GRANT
    priv_type [(column_list)]
      [, priv_type [(column_list)]] ...
    ON [object_type] priv_level
    TO user_or_role [, user_or_role] ...
    [WITH GRANT OPTION]
    [AS user
        [WITH ROLE
            DEFAULT
          | NONE
          | ALL
          | ALL EXCEPT role [, role ] ...
          | role [, role ] ...
        ]
    ]

GRANT PROXY ON user_or_role
    TO user_or_role [, user_or_role] ...
    [WITH GRANT OPTION]

GRANT role [, role] ...
    TO user_or_role [, user_or_role] ...
    [WITH ADMIN OPTION]

object_type: {
    TABLE
  | FUNCTION
  | PROCEDURE
}

priv_level: {
    *
  | *.*
  | db_name.*
  | db_name.tbl_name
  | tbl_name
  | db_name.routine_name
}

user_or_role: {
    user (see https://dev.mysql.com/doc/refman/8.0/en/account-names.html)
  | role (see https://dev.mysql.com/doc/refman/8.0/en/role-names.html)
}

```
### DML

#### insert语句的隐式转换
MySQL 在执行插入语句时，会进行一些隐式类型转换，以确保插入的数据类型与表中的列类型匹配。
默认的隐式转换有 字符串转整数、字符串转日期

**注意** 有些类型转换可能会导致数据丢失或意外的结果。可以使用 MySQL 提供的 `CAST()` 或 `CONVERT()` 函数来进行显式类型转换。

## mysql 示例

### 查看触发器
1. 选择数据库 `use <db_name>`, 通过`SHOW TRIGGERS;`查看
2. 使用 `SELECT * FROM information_schema.triggers;` 查看所有触发器。
 
### revoke移除权限
`revoke all on test.score to 'User01'@'localhost';`

#### 刷新系统权限表，即时生效
`flush privileges;`

### mysql锁

1. 行级锁 (`SELECT ... FOR UPDATE`)
2. 表级锁 (`LOCK TABLES <table_name> <read|write>`)
3. 元数据锁mdl(meta data lock)


`LOCK TABLES your_table WRITE`
`UNLOCK TABLES`

**注意** 对应表级锁而言，如果表存在触发器，会将相应的表均上锁。这时使用`rollback/commit`(需先开启事务)可以将所有上锁的表解除或者显示调用`unlock tables;`

**表锁与元数据锁的区别** 在MySQL5.5版本引入了MDL，当对一个表做增删改查操作的时候，加MDL读锁；当要对表做结构变更操作的时候，加MDL写锁。
> 读锁之间不互斥，因此可以有多个线程同时对一张表增删改查
> 读写锁之间、写锁之间是互斥的，用来保证变更表结构操作的安全性。因此，如果有两个线程要同时给一个表加字段，其中一个要等另一个执行完才能开始执行

#### 命令行锁操作
`show open tables;` 如果列`In_use` > 0,表示对应表被锁定
SELECT * FROM information_schema.INNODB_LOCKS; 查看当前正在锁

`show full processlist;` 查看mysql连接的进程.（对于wait lock的进程，在State列中会有一个Waiting for table metadata lock的信息）

`kill <id>;` 杀死指定id的mysql进程。


### mysql查看连接ip
- `show processlist;`
- `select SUBSTRING_INDEX(host,':',1) as ip , count(*) from information_schema.processlist group by ip;`

## mysql触发器

触发器是一种特殊的存储程序，它在执行特定的数据库操作（如 INSERT、UPDATE 或 DELETE）时自动执行。


## mysql问题集合

### not in无结果
mysql 的 not in 中，不能包含 null 值。否则，将会返回空结果集。

### 触发器在失败时，原操作未执行

> 问题示例:
```sql
CREATE TRIGGER `test_in` AFTER INSERT ON `t` FOR EACH ROW
BEGIN
	SELECT count(*) into @a from t2;
-- 	INSERT INTO `t2` VALUES(@a,'34');
	INSERT INTO `t2` VALUES(NULL,'34');
END;
```
> 可能原因:
- 事务管理：如果您在执行插入操作时使用了事务（例如，使用 `START TRANSACTION` 开始一个事务），并且在触发器执行后未提交事务（即没有执行 `COMMIT`），那么所有的操作都会被回滚，包括对表 `t` 的插入操作。

- 触发器中的错误：如果在触发器中执行的 SQL 语句出现错误（例如，插入 `t2` 时违反了某种约束），那么触发器的执行将失败，可能会导致整个事务被回滚，从而使得对表 `t` 的插入操作也不被保留。

- 触发器定义问题：确保触发器的定义是正确的，且没有其他触发器或约束影响到插入操作。

