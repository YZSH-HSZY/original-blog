# micropython

## 编译安装
从[micropython官方中获取代码仓库](https://github.com/micropython/micropython/tree/v1.23.0)
[micropython官方build教程](https://github.com/micropython/micropython/wiki/Build-Troubleshooting)

1. 编译microp1ython交叉编译工具
```sh
cd mpy-cross
make
```
2. `make BOARD=... submodules`初始化子模块,BORARD指定固件运行的开发板类型
> 对于