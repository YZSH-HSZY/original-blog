# linux kernel

## ko模块

**dev env**
- `apt install linux-headers-generic linux-tools-generic linux-tools-common`

**tool**
- `lsmod(8), insmod(8), modprobe(8), modinfo(8) depmod(8)`
> `lsmod`: 用于显示已安装的模块信息,在`/proc/modules`文件也有已加载的模块信息
> `modinfo`: 显示模块是否可用(包括未加载的模块)
> `modprobe`: 安装模块, 使用 `--show-depends <ko_name>` 显示模块安装依赖关系

**module path**
- 内核模块通常存储在 `/lib/modules/$(uname -r)`, 使用 `find /lib/modules/$(uname -r) -type f -name '*.ko*'` 查看所有模块
- `/boot/config-$(uname -r)`存放内核编译配置选项
> `m`: 表示模块已编译但未加载, 如`CONFIG_CAN_VCAN=m`
> `y`: 表示模块已内置到内核(无需加载), 如`CONFIG_CAN_VCAN=m`
> `# CONFIG_PREEMPT is not set`: 表示内核不支持该模块

### bug

#### modprobe: ERROR: Module vfb not found in directory /lib/modules/6.8.0-51-generic

- 将ko文件复制到 `/lib/modules/$(uname -r)` 目录下
- 尝试执行 `depmod` 命令
- 使用 `modprobe module_name` 不要带 `.ko` 后缀

#### modprobe: ERROR: could not insert 'vfb': Operation not permitted

- docker内，在 `docker run` 启动容器时加入 `--privileged=true` 选项获取宿主机的root权限