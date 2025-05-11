# man
Linux 提供了丰富的帮助手册，通过 man 命令可以查看 Linux 中的命令帮助、配置文件帮助和编程帮助等信息。

[man使用文档](https://gnu-linux.readthedocs.io/zh/latest/Chapter01/00_man.html)

## man手册页分类
|章节           |	说明                                          |
|---------------|------------------------------------------------|
|1              |	标准用户命令（包含大量的命令手册）              |
|2              |	系统调用（在程序中使用，用来请求内核执行指令）   |
|3              |	库调用                                        |
|4              |	特殊文件（包含物理设备和设备的驱动信息）         |
|5              |	文件格式（包含配置文件）                        |
|6              |	游戏                                          |
|7              |	杂项（各种混杂信息）                            |
|8              |	管理命令（系统管理员使用的特殊命令）             |

**注意** 在查看帮助手册时，在第一行的左上角和右上角都会显示命令所在的章节，如：MAN(1)

## USAGE

`man [OPTION...] [章节] query`

## CONFIG

man的配置文件在 `/etc/manpath.config`, 有的系统是 `man_db.conf`

### 配置项 `MANDATORY_MANPATH`
`MANDATORY_MANPATH` 用于强制包含的手册路径, 确保关键手册可用(可使用 `manpath` 查看搜索man手册路径)
> example: `MANDATORY_MANPATH	/home/smartwork/3rdparty/openssl/output/openssl-1.1.1d/share/man`

### 配置项 `MANPATH_MAP`
`MANPATH_MAP` 用于自定义可执行程序的man帮助手册搜索路径, 即`man <execable-file>` 的搜索路径
> example: `MANPATH_MAP	/usr/local/bin		/usr/local/share/man`

### 配置项 `MANDB_MAP`
`MANDB_MAP` 用于优化 man 索引管理, 即配置man手册的数据库索引缓存路径
> example: `MANDB_MAP	/usr/local/man		/var/cache/man/oldlocal`


## INSTALL

### 从源码仅安装man手册

1. 需要asciidoctor用于生成man pages, `sudo apt-get install asciidoctor`
2. 下载源码仓库, 以nanomsg为例`git clone https://github.com/nanomsg/nanomsg.git`
3. 构建man手册 `make man`
4. 手动安装man手册 `sudo cp *.3 /usr/local/share/man/man3/  # 复制到系统 man 目录`
5. 或者更改`/etc/manpath.config` 的manpath配置文件, 添加条目, 如 `MANDATORY_MANPATH			/home/smartwork/work/3rdparty/nanomsg/output/nanomsg/share/man`
6. 更新man手册数据库 `sudo mandb  # 更新 man 数据库`

### EXAMPLE

#### 全字匹配搜索

`/\<word\>` 全字匹配使用`<>`包裹需要匹配的单词, 注意边界符号需转义