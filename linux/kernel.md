# linux kernel

## ko模块

**dev env**
- `apt install linux-headers-generic linux-tools-generic linux-tools-common`

### bug

#### modprobe: ERROR: Module vfb not found in directory /lib/modules/6.8.0-51-generic

- 将ko文件复制到 `/lib/modules/$(uname -r)` 目录下
- 尝试执行 `depmod` 命令
- 使用 `modprobe module_name` 不要带 `.ko` 后缀

#### modprobe: ERROR: could not insert 'vfb': Operation not permitted

- docker内，在 `docker run` 启动容器时加入 `--privileged=true` 选项获取宿主机的root权限