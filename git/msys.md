# msys

## USAGE
- 安装指定包 `pacman -S <pkg_name>` 
- 卸载指定包 `pacman -R <pkg_name>` 
- 查询所有安装包 `pacman -Q` 
- 查询指定安装包是否安装 `pacman -Qs <pkg_name>` 

### bug

#### 安装时报exists in filesystem

> 问题描述:
```sh
mingw-w64-x86_64-gnutls: /mingw64/share/doc/gnutls/pkcs11-vision.png exists in filesystem
Errors occurred, no packages were upgraded.
```
> 解决方案: 添加`--overwrite="*"` 选项覆写已存在文件

## pkgs
`msys/openbsd-netcat` 等同 `ubuntu/ncat`(提供nc命令)

## example

### git的msys搭建pacman包管理器

[msys2软件仓库](https://repo.msys2.org/msys/x86_64/)

1. 从msys2软件仓库下载如下包 `pacman-<version>-<arch>.pkg.tar.zst`;`pacman-mirrors.pkg.tar.zst`;`msys2-keyring-1.pkg.tar.zst` 
2. 将上述软件包解压至 git 的安装目录
3. 在git-bash配置软件源 `sed -i "s#https\?://mirror.msys2.org/#https://mirrors.tuna.tsinghua.edu.cn/msys2/#g" /etc/pacman.d/mirrorlist*`
4. 更新认证仓库key及db文件
```sh
pacman-key --init       # 确保正确初始化密钥及其签名
pacman-key --populate msys2     # 重新加载/usr/share/pacman/keyrings/中给定的keyring的默认密钥
pacman -Sy          # 刷新软件包数据库
pacman -S --dbonly pacman # 仅更新软件包pacman数据库
```