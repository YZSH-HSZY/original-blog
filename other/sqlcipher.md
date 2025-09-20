# sqlcipher

一个开源的sqlite加密控制库

> 参考文档:
- [sqlcipher官方仓库](https://github.com/sqlcipher/sqlcipher)
- [sqlcipher社区](https://discuss.zetetic.net/c/sqlcipher/5?page=3)
- [ActiveTcl下载](https://platform.activestate.com/ActiveState/ActiveTcl-8.6)
- [sqlite官方git镜像](https://github.com/sqlite/sqlite)

## compile

以4.1.0版本为例

**MSVC Compile**
> - 准备 `openssl 1.1.x` 库, `ActiveTcl`包(`sqlcipher`使用`tcl`生成部分源码和测试)
> - 拉取 `sqlcipher` 源码并切换到4.1.0
> - 修改 `Makefile.msc` 添加`TCC`/`RCC`/`LTLINKOPTS`的额外选项, 如下所示
```
TCC = $(TCC) -DSQLITE_HAS_CODEC -DSQLITE_TEMP_STORE=2 -IC:\opt\openssl-1.1.1d-x64\include
RCC = $(RCC) -DSQLITE_HAS_CODEC -DSQLITE_TEMP_STORE=2 -IC:\opt\openssl-1.1.1d-x64\include
LTLINKOPTS = $(LTLINKOPTS) /LIBPATH:C:\opt\openssl-1.1.1d-x64\lib libcrypto.lib
```
> `nmake -f Makefile.msc`

**注意** 
- 不同sqlcipher版本支持的openssl-api不一致, 可根据changelog查看对应支持
- `4.1.0` 版本只需要开启 `SQLITE_HAS_CODEC` 宏即可


## 使用

sqlcipher 生成的exe有 `sqlcipher.exe`/`sqlite3.exe` 两种, 根据版本的不同有所变化

> 简易示例:
- 使用 `sqlite3 :memory: "PRAGMA cipher_version;"` 查看sqlcipher版本
- `sqlite3 :memory: "SELECT sqlite_version();"` 查看对应的sqlite版本
- `sqlite3 :memory: "PRAGMA compile_options;"` 查看编译选项

**注意** 加解密的`key`(密码)/`cipher_compatibility`(加密版本)/`kdf_iter`(密钥迭代次数)/`cipher`(加密方法) 都必须一致, 才能正确解密