## example

### 米尔 MYD-YT113-I 开发板SDK编译

[MYD-YT113 SDK V1.1.0下载地址](https://down.myir-tech.com/MYD-YT113/)

> 以t113_i为例
> - `./build.sh config`; 选项:`0.linux --> 2.longan --> 0.linux-5.4 --> 1.t113_i --> 1.myir-image-yt113i-full --> 1.nor --> 0.gnueabi`
> - `export set FORCE_UNSAFE_CONFIGURE=1` 解决root用户编译的安全错误
> - 修改 ` ./out/t113/ myir-image-yt113s3-emmc-full /longan/buildroot/build/host-libglib2-2.56.3/gio/gdbusauth.c` 在 `debug_print ("SERVER: WaitingForBegin, read '%s'", line);` 语句上添加判断条件 `if (line != NULL)`
> - 修改 `./out/t113/ myir-image-yt113s3-emmc-full /longan/buildroot/build/host-libglib2-2.56.3/gio/gdbusmessage.c` 在 `tupled_signature_str = g_strdup_printf ("(%s)", signature_str);` 语句上添加判断条件 `if (signature_str != NULL)`
> - 在 `out/t113_i/evb1_auto/longan/buildroot/build/libgpg-error-1.33/src` 下将所有 `namespace` 替换为 `pkg_namespace`, 命令: `grep -rl "namespace" out/t113_i/evb1_auto/longan/buildroot/build/libgpg-error-1.33/src/ | xargs sed -i 's/namespace/pkg_namespace/g'`