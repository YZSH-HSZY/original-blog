# orm

## SQLAlchemy

### uri格式

标准格式为: `driver://user:pass@host/database`
示例：
1. `sqlite:///test.db`
2. `mysql+pymysql://root:passwd@ip_address/db_name`

**注意** sqlite相对路径和绝对路径均需三个 '/'，如 `sqlite:///D:\\dir_name\\data_record.db`

### 从数据库已有表自动生成python model

1. 通过 `sqlacodegen` 包生成，`sqlacodegen mysql+pymysql://user_name:passwd@server_ip/db_name --outfile=models.py [--tables tb_name]`

### sqlalchemy示例

#### sqlalchemy逆序排序

1. `session.query(Project).order_by(Project.id.desc()).all()`
2. `session.query(Project).order_by(desc(Project.project_name)).all()`

## bug

### SQLAlchemy执行时报Cannot evaluate Function错误

> 问题描述:
```
sqlalchemy.exc.InvalidRequestError: Could not evaluate current criteria in Python: "Cannot evaluate Function". Specify 'fetch' or False for the synchronize_session execution option.
```
> 解决方案:
> 网上的方案多为添加关键字参数 `synchronize_session='fetch'`，但我使用时无效，通过调试py文件，根据trace栈发现最终在使用的session的execute方法时，存在`execution_options=util.EMPTY_DICT`参数，execute会根据该字典执行py评估，默认执行选项synchronize_session为evaluate，因此可更改为以下:
```python
session.execute(
    update(ProductInfoTable)
    .where(and_(ProductInfoTable.product_code==product_code),or_(
            func.length(ProductInfoTable.production_date)==5, 
            func.isnull(ProductInfoTable.production_serial_number),
            func.isnull(ProductInfoTable.production_datetime)
    ))
    .values(
        **ProductCodeParseRule(product_code).parse(),
        production_datetime = production_datetime
    ),
    execution_options={
        'synchronize_session': 'fetch'
    }
)
```

### SQLAlchemy add数据时 Table can't callable

> 问题描述，通过session.add添加数据时
```python
db_session.add(
    t_capture_udp(
        capture_time=the_capture_time,
        src=packet['IP'].src,
        dst=packet['IP'].dst,
        data=packet['UDP'].payload.load,
        pgn_no=udp_parse_result.pgn_no if udp_contain_pgn_sign else 0
    )
)
>>> TypeError: 'Table' object is not callable
```
> 解决方案：
> 对于使用Table定义的数据库表在插入时，通过`Table.insert().values({clo_name=value},...)` 生成sql语句，之后通过 `session.execute` 执行