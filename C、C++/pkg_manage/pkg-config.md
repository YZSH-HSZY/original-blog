# pkg-config

编译标志提供工具(获取库的编译和链接选项)

## Example

- `pkg-config opencv --libs --cflags`: linux下使用pkg-config查看包是否存在

#### 使用pkg-config管理C/C++编译选项

使用pkg-config获取库/模块的所有编译相关的信息

- 可以设置`PKG_CONFIG_PATH`环境变量指定pkg-config额外搜索pc文件路径
- 可以使用`pkg-config --variable pc_path pkg-config`查看pkg-config built-in search path(默认搜索路径)。
> `pkg-config --print-variables pkg-config`查看指定包中定义的变量，其中pkg-config中变量pc_path为pkg-config的默认搜索路径，在编译安装时确认。
**注意** 你可以通过环境变量 `PKG_CONFIG_LIBDIR` 来覆盖默认搜索pc文件路径。
- example:
> `pkg-config --cflags --libs opencv`,--cflags选项列出opencv头文件路径，--libs选项列出库文件以及附加链接库路径