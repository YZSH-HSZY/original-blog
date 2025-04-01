# openssl
OpenSSL 是一个强大的商业级、功能齐全的开源工具包，适用于 TLS（以前称为 SSL）、DTLS 和 QUIC（目前仅限客户端）协议。

[openssl-github仓库](https://github.com/openssl/openssl)

## build

> openssl依赖:
- make
- Perl 5 with core modules
- The Perl module Text::Template
- an ANSI C compiler
- POSIX C library (at least POSIX.1-2008), or compatible types and functionality.
- a development environment in the form of development libraries and C header files
- a supported operating system

> Ubuntu上安装prel模块Text::Template
```sh
$ apt-cache search Text::Template
libtext-template-perl - perl module to process text templates
$ sudo apt-get install libtext-template-perl
```

> compile
```sh
./Configure --prefix=/opt/openssl-1.1.1d/ --debug linux-x86_64
make -j8; make install
```
## openssl术语

### OpenSSL EVP (Envelope) 框架
EVP (Envelope) 是 OpenSSL 提供的高级加密接口，它抽象了各种加密算法、哈希算法和密钥派生函数的底层实现，为开发者提供统一的 API 接口。

> 核心特点
> - 算法抽象: 统一不同加密算法的调用方式
> - 多算法支持: 对称加密、非对称加密、哈希、HMAC、KDF 等
> - 硬件加速: 自动利用可用的硬件加速功能
> - 线程安全: 适合多线程环境使用

### Cipher(加密算法)
指具体的加密算法和模式, 如AES-128-CBC, ChaCha20-Poly1305

> 加密算法命名规格: 算法名称、密钥长度和操作模式

### Key(密钥)
加密/解密所需的数据, 长度取决于算法(AES-128->16字节，AES-256->32字节)

### IV(初始化向量，Initialization Vector)
确保相同明文加密结果不同的随机值, 长度通常与块大小相同(AES为16字节)

> 关键点:
> - 不需要保密，但不可重复使用(GCM模式)
> - CBC模式需要不可预测性

### Plaintext(明文)
待加密的原始数据

> 长度在块加密模式中可能需要填充

### AAD(附加认证数据，Additional Authenticated Data)
需要认证但不加密的数据(仅GCM等认证加密模式使用),保护关联数据(如报文头)的完整性

> 特点:
> - 不加密但参与完整性校验
> - 接收方必须提供相同的AAD才能验证成功

### Tag(认证标签)
加密生成的完整性校验值(GCM等模式特有), 通常16字节(128位)

> 作用:
> - 验证密文和AAD是否被篡改
> - 解密时必须校验Tag

### Ciphertext(密文)
加密后的输出数据, $Ciphertext = Encrypt(Key, IV, Plaintext)$

> 特点:
> - 与明文长度相同(CTR/GCM模式)或有填充(CBC模式)
> - 若无正确Key/IV无法解密
