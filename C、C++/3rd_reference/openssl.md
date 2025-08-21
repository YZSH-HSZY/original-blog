# openssl
OpenSSL 是一个强大的商业级、功能齐全的开源工具包，适用于 TLS（以前称为 SSL）、DTLS 和 QUIC（目前仅限客户端）协议。

[openssl-github仓库](https://github.com/openssl/openssl)
[IANA-加密套件值定义](https://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml)

## build

### build in unix-like
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
$ apt-file search Text::Template
libtext-template-perl - perl module to process text templates
$ sudo apt-get install libtext-template-perl
```

> compile
```sh
./Configure --prefix=/opt/openssl-1.1.1d/ --debug linux-x86_64
make -j8; make install
```

### build in window

> 参考资源:
- [nasm下载](https://www.nasm.us/pub/nasm/releasebuilds/)
- [window-perl下载](http://www.activestate.com/activeperl/)

> depend:
- `nasm` / `perl`

> 安装命令:
- `perl Configure {VC-WIN32,VC-WIN64A} --prefix=C:\opt`; `nmake`

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

**注意** Tag 是自动计算的，但需开发者手动提取。必须调用 `EVP_EncryptFinal_ex`（即使 outlen=0）才能生成有效 Tag。解密时需用相同的 Tag 验证，否则数据会被视为无效。

### Ciphertext(密文)
加密后的输出数据, $Ciphertext = Encrypt(Key, IV, Plaintext)$

> 特点:
> - 与明文长度相同(CTR/GCM模式)或有填充(CBC模式)
> - 若无正确Key/IV无法解密

## 证书certificate

openssl内部操作证书的编码转换一般以 `d2i_*`(将DER编码对象转为内部结构)/`i2d_*`(将内部结构转为DER编码对象) 开头

### 相关命令示例

- `openssl x509 -in tmp_ser_pri_key.crt.crt -noout -text` 查看PEM格式证书的详细信息
- `openssl ciphers -v "AES256-GCM-SHA384:ADH-AES256-GCM-SHA384@SECLEVEL=0"` 检查实际生效的加密算法
- `openssl ciphers -V` 显示十六进制的官方密码套件值
- `openssl cms -cmsout -in example.cmsc -inform DER -print` 打印证书内部字段

### 概念

#### CMS 文件 和 PEM 文件

> CMS 文件(.cms/.p7s/.p7m)
> - 二进制格式(DER编码): 默认情况下，CMS 文件采用 `DER(Distinguished Encoding Rules)` 编码，是 `ASN.1` 标准的二进制格式，不可直接阅读。
> - 例如：`.p7s`(签名文件)、`.p7m`(加密文件)、`.cms` 等扩展名。

> 文本格式(PEM)
> - CMS 文件也可以转换为 PEM 格式(`Base64` 编码的 DER 数据)，以 `-----BEGIN PKCS7-----` 开头，方便在文本环境中传输
> - CMS 通常用于数字签名、加密、证书封装(如 `PKCS#7/CMS` 格式的签名文件)

CMS/PEM文件转换命令
- DER(CMS)→ PEM: `openssl cms -in file.cms -inform DER -out file.pem -outform PEM`
- PEM → DER(CMS): `openssl cms -in file.pem -inform PEM -out file.der -outform DER`

### Example

#### c-api验证证书

```c
int verify_cms_signature(const char *cms_file, int der_format, 
                        const char *cert_file, const char *out_file) {
    BIO *in = NULL, *out = NULL, *certbio = NULL;
    CMS_ContentInfo *cms = NULL;
    X509 *cert = NULL;
    STACK_OF(X509) *certs = NULL;
    int ret = 0;
    
    /* 初始化 OpenSSL */
    OpenSSL_add_all_algorithms();
    
    /* 读取输入文件 */
    in = BIO_new_file(cms_file, "rb");
    if (!in) goto end;
    
    /* 读取 CMS 数据 */
    if (der_format) {
        cms = d2i_CMS_bio(in, NULL);
    } else {
        cms = PEM_read_bio_CMS(in, NULL, NULL, NULL);
    }
    if (!cms) goto end;
    
    /* 读取验证证书 */
    if (cert_file) {
        certbio = BIO_new_file(cert_file, "r");
        cert = PEM_read_bio_X509(certbio, NULL, NULL, NULL);
        if (!cert) goto end;
        certs = sk_X509_new_null();
        sk_X509_push(certs, cert);
    }
    
    /* 准备输出 */
    out = BIO_new_file(out_file, "wb");
    if (!out) goto end;
    
    /* 执行验证 */
    if (CMS_verify(cms, certs, NULL, NULL, out, CMS_NOINTERN|CMS_NOVERIFY) == 1) {
        printf("CMS Verification successful\n");
        ret = 1;
    } else {
        printf("CMS Verification failed\n");
        ERR_print_errors_fp(stderr);
    }
    
end:
    /* 清理资源 */
    if (cms) CMS_ContentInfo_free(cms);
    if (in) BIO_free(in);
    if (out) BIO_free(out);
    if (certbio) BIO_free(certbio);
    if (certs) sk_X509_free(certs);
    
    return ret;
}
```

## dtls

### DTLS 1.2 握手顺序(以 PSK 模式为例)

1. ClientHello →
（客户端发起握手，携带随机数、加密套件列表等）
2. HelloVerifyRequest ←
（服务端返回 Cookie，防御 DoS 攻击）
3. ClientHello →
（客户端重新发送，这次携带 Cookie）
4. ServerHello, ServerHelloDone ←
（服务端确认加密套件和参数）
5. ClientKeyExchange, ChangeCipherSpec, Finished →
（客户端发送密钥材料，启用加密，并验证握手完整性）
6. ChangeCipherSpec, Finished ←
（服务端启用加密并验证）
7. Application Data
（双方开始加密通信）

**注意** HelloVerifyRequest 是用于防御 DoS 攻击 的机制，但必须显式启用, 在服务端使用`SSL_CTX_set_options(ctx, SSL_OP_COOKIE_EXCHANGE);`

**注意** pre-psk在整个dtls会话连接过程中均不可见, 具体值由双方在连接前进行约定, 在dtls-session连接过程中, (dtls1.3中客户端必须发送 psk_identities, 服务器必须返回 selected_identity, 1.2可简化实现)

### Example

- `SSL_is_init_finished(_ssl)`判断握手完成

## C-API

### BIO

- `BIO_new_mem_buf`: 创建一个 只读 的内存 BIO, 引用已有的内存缓冲区
- `BIO_s_mem()`: 返回一个内存BIO函数
- `BIO_new(BIO_s_mem())`: 创建一个 可读写 的动态内存 BIO, 调用 `BIO_free()` 时释放
- `BIO_set_data`: 实现自定义 BIO 类型时，存储状态信息(设置 BIO 的私有指针,由用户自身管理,区分BIO_write)
- `BIO_write`: 向 BIO 的缓冲区写入数据, 供之后的加解密处理获取

> 内存BIO是使用内存进行I/O操作的BIO, 写入内存BIO的数据存储在`BUF_MEM`结构中, 该结构可以**适当地扩展**以容纳存储的数据

- `BIO_s_secmem()`: 使用安全堆存储数据

> 只读BIO不能重新读取(即每次读取任意数据,这些数据类似从内存中删除),只能访问之后的数据
> 只读 BIO 的设计目的是 高效解析已有数据(如证书、密钥等)，OpenSSL 不会主动修改用户提供的缓冲区
## bug

### openssl在解密时如果存在iv需要在选择算法之后,设置key/iv之前
```c

// Select cipher
EVP_DecryptInit_ex(ctx_de, EVP_aes_256_gcm(), nullptr, nullptr, nullptr);
// EVP_DecryptInit_ex(ctx_de, EVP_aes_256_gcm(), nullptr, key, iv);

// Set IV length, omit for 96 bits
EVP_CIPHER_CTX_ctrl(ctx_de, EVP_CTRL_AEAD_SET_IVLEN, sizeof(iv), nullptr);

// Specify key and IV
EVP_DecryptInit_ex(ctx_de, nullptr, nullptr, key, iv);
```

### openssl解密时tag验证失败

> 加密时存储tag
```c

```
> 解密时验证tag步骤
```c
// Set expected tag value
EVP_CIPHER_CTX_ctrl(ctx, EVP_CTRL_AEAD_SET_TAG, 16, (void*)tag);

// Finalise: note get no output for GCM
int rv = EVP_DecryptFinal_ex(ctx, outbuf, &outlen);
// Print out return value. If this is not successful authentication failed and plaintext is not trustworthy.
fprintf(stdout, "Tag Verify %s\n", rv > 0 ? "Successful!" : "Failed!");
ERR_print_errors_fp(stderr);

EVP_CIPHER_CTX_free(ctx);
```

**注意** AEAD模式中, TAG验证失败是正常流程的一部分, 不属于 OpenSSL 错误, 因此不会将这种失败记录到错误队列中, 使用 `ERR_print_errors` 获取消息为空.