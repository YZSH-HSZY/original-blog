# docker


## docker 安装

1. 使用官方提供的测试安装脚本安装(不推荐)
```
curl -fsSL https://test.docker.com -o test-docker.sh
sudo sh test-docker.sh
```
2. Docker 在 https://get.docker.com/ 提供了一个方便的脚本，可以在开发环境中非交互式地安装 Docker。不推荐用于生产环境，但它对于创建符合您需求的配置脚本很有用。

[docker安装文档](https://docs.docker.com/engine/install/ubuntu/#install-using-the-convenience-script)

**注意** 从 `https://get.docker.com/` 下载的脚本，使用 `--dry-run` 查看脚本将要执行的内容

### 将用户添加到docker组中
`sudo usermod -aG docker ${USER}`

**注意** 需要注销后再登录，以重新评估组成员资格。或者使用 `newgrp docker` 变换当前组id，重新激活登录环境。

## 配置 docker hub 镜像源

我们获取 docker images 时默认从 `https://hub.docker.com` 拉取的。在国内该hub源访问速度异常慢，尤其是大一点的镜像经常出现timeout。

```
管理员权限编辑或创建/etc/docker/dameon.json，添加docker中国地区镜像
{
 "registry-mirrors": ["https://registry.docker-cn.com"]
}
```

其他镜像：网易 http://hub-mirror.c.163.com
阿里云 https://<...>.mirror.aliyuncs.com 需要自己去以下链接创建专属镜像仓库 `https://cr.console.aliyun.com/`

> 通过以下命令重启docker守护进程
```sh
sudo systemctl daemon-reload
sudo systemctl restart docker
```

### docker代理设置

#### docker pull代理
docker pull 的代理被 systemd 托管，需要设置 systemd 如 `sudo vim /etc/systemd/system/docker.service.d/http-proxy.conf`，编辑内容如下:
```yml
[Service]
Environment="HTTP_PROXY=http://127.0.0.1:8123"
Environment="HTTPS_PROXY=http://127.0.0.1:8123"
```
重启服务生效
```sh
sudo systemctl daemon-reload
sudo systemctl restart docker
```
可以通过 `sudo systemctl show --property=Environment docker` 看到设置的环境变量

[参docker proxy设置博客](https://www.cnblogs.com/Chary/p/18502958)

## docker 使用

使用 docker --help 查看帮助信息

```
ubuntu@VM-12-17-ubuntu:~$ docker --help
Usage:  docker [OPTIONS] COMMAND
```
### docker pull

#### docker 拉取指定架构的镜像
`docker pull [--platform {linux/amd64,linux/arm/v7,linux/arm64/v8,linux/ppc64le,linux/riscv64,linux/s390x}] NAME[:TAG]`

**注意** 运行不同架构的容器,需要安装 `qemu-user-static`, 此时 docker 会自动使用qemu模拟架构运行,未安装 docker run 时报错 `requested image's platform (linux/arm/v7) does not match the detected host platform (linux/amd64/v3)`

### docker tag

#### docker 查看hub中镜像可用标签

1. 在浏览器打开 hub.docker.com 上搜索镜像查找标签
2. 使用 curl 工具查看，示例如下

```
curl https://registry.hub.docker.com/v1/repositories/mysql/tags\
| tr -d '[\[\]" ]' | tr '}' '\n'\
| awk -F: -v image='mysql' '{if(NR!=NF && $3 != ""){printf("%s:%s\n",image,$3)}}'

或者借助python的json工具
curl https://registry.hub.docker.com/v1/repositories/rancher/rancher/tags | python -m json.tool | grep 2.4
```

#### image tag重命名
`docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]` 创建一个新tag,此时一个image id会有多个tag,可用删除不需要的tag

### docker image

#### 查看image 创建的commit消息
`docker histroy IMAGE` 查看镜像的历史记录和注释消息

### docker container

#### 创建container时指定container名
`docker container [--name string] IMAGE [COMMAND]`

#### 获取container中文件到本地
`docker cp CONTAINER:SOURCE DEST_PATH` 复制指定容器中源路径到本地目的路径

#### 进入运行中的docker容器
1. `docker attach test_contain` 附加到容器中
2. `docker exec -it test_contain /bin/bash` 在运行容器中执行命令，使用 `-it` 交互式使用bash

**注意** attach 多个实例会附加到同一个容器终端进程,退出则均会退出;而exec会在容器中开启多个bash会话

### 停止docker服务
如果你想要完全停止 docker 服务，你需要同时关闭 docker.service 和 docker.socket 文件： sudo systemctl stop docker.service sudo systemctl stop docker.socket 如果需要在系统启动时禁用 Docker 服务，可以使用以下命令： sudo systemctl disable docker 这个命令会禁用 Docker 服务，以防止它在系统启动时自动启动。

### docker已存在容器配置挂载点
你需要先停止docker，才能更改容器配置
1. 使用`docker info | grep 'Root'`查看容器存放目录
2. 使用`docker ps -a`查看容器的id
3. 修改config.v2.json和hostconfig.json文件
> 在config.v2.json中找到MountPoints,修改如下：
```
{
...
"MountPoints": {
    ......,
    "/opt/shardingsphere-proxy/logs": {
        "Source": "/atguigu/server/proxy-a/logs",
        "Destination": "/opt/shardingsphere-proxy/logs",
        "RW": true,
        "Name": "",
        "Driver": "",
        "Type": "bind",
        "Propagation": "rprivate",
        "Spec": {
            "Type": "bind",
            "Source": "/atguigu/server/proxy-a/logs",
            "Target": "/opt/shardingsphere-proxy/logs"
        },
        "SkipMountpointCreation": false
    }
    //注释，如果是将主机映射至容器中，源路径为主机路径
    <容器内部路径>:{
        "Source":<映射源路径>,
        "Destination": <映射目的路径>,
        "RW": true,
        "Name": "",
        "Driver": "",
        "Type": "bind",
        "Propagation": "rprivate",
        "Spec": {
            "Type": "bind",
            "Source": "/atguigu/server/proxy-a/logs",
            "Target": "/opt/shardingsphere-proxy/logs"
        },
        "SkipMountpointCreation": false
    }
},
...
}
```
### docker已存在容器配置端口映射

你需要先停止docker，才能更改容器配置
1. 使用`docker info | grep 'Root'`查看容器存放目录
2. 使用`docker ps -a`查看容器的id
3. 修改config.v2.json和hostconfig.json文件
4. hostconfig.json的PortBindings选项设置挂载端口绑定
```
hostconfig.json文件
...
"PortBindings": {
    "8000/tcp": [
        {"HostIp": "", "HostPort": "8000"},
     ]
},
...
```
5. config.v2.json的ExposedPorts选项设置容器暴露端口
```
config.v2.json文件
    ...
    "ExposedPorts": {
        "8000/tcp": {},
    },
    "Env":[...],
    "Cmd":[...]
    ...
```
### docker 的 ubuntu 容器内安装 python

这里以ubuntu:20.04镜像示例，先创建并进入容器
1. 升级使用 apt update 升级 apt 包管理器

2. 安装wget下载工具`apt install wget`

3. 在官网下载需要的 python 源码压缩包[python 官方网站](https://www.python.org/downloads/source/ "打开官网")
示例：https://www.python.org/ftp/python/3.8.13/Python-3.8.13.tgz

下载指定的python源代码`wget https://www.python.org/ftp/python/3.8.13/Python-3.8.13.tgz`

4. 解压`tar -zxvf Python-3.8.13.tgz`
5. 进入解压目录`cd Python-3.8.13`
6. 准备python依赖

```
apt-get -y install gcc automake autoconf libtool make 
apt-get -y install make*
apt-get -y install zlib*
apt-get -y install openssl libssl-dev libffi-dev libsqlite3-dev liblzma-dev libbz2-dev
apt-get install sudo
```
6. 运行`./configure`配置

7. 运行`make && make install`编译安装


#### docker 的 ubuntu 容器内安装 python 中bug合集
1. python交互终端退格和方向键失灵，总打出\[H等.
解决方案：`sudo pip3 install gnureadline`

### docker run 启动并运行新容器
```sh
# 使用docker help查看帮助，在常用命令中发现run是创建并运行新容器
Common Commands:
  run         Create and run a new container from an image

Options:
  -v,--volume [HOST-DIR:]CONTAINER-DIR[:OPTIONS]
```


### docker查看已启动容器的标准输出

`docker logs {container_name | container_id}`

## docker 文件挂载

docker 支持的文件挂载方式有以下几种:
- `volumes`: 由 Docker（/var/lib/docker/volumes/在 Linux 上）管理的主机文件系统的一部分中。非 Docker 进程不应修改文件系统的这一部分。卷是在 Docker 中持久化数据的最佳方式
- `bind mounts`: 可以存储在主机系统的任何位置。它们甚至可能是重要的系统文件或目录。Docker 主机或 Docker 容器上的非 Docker 进程可以随时修改它们。
- `tmpfs mounts`: 挂载仅存储在主机系统的内存中，永远不会写入主机系统的文件系统

### docker volume

- 创建卷 `docker volume create data_volume`
- 显示存在的卷 `docker volume ls`
- 显示一个或多个卷的详细信息 `docker volume inspect data_volume`
- 删除未使用的本地卷 `docker volume prune data_volume`
- 删除一个或多个卷 `docker volume rm data_volume`

## docker network

[docker网络官方文档](https://docs.docker.com/engine/network/)

### 添加ipv6支持

- 默认桥接网络bridge添加ipv6支持
> * 主机需要具有global ipv6地址(scope-link无法进行dhcp自动分配)
> * `/etc/docker/daemon.json` 添加配置`"ipv6": true`;分配子网`"fixed-cidr-v6": "2001:db8:1::/64"`
> * 重启docker守护进程 `sudo systemctl restart docker`

- 使用自定义ipv6网络
> * 创建一个ipv6的docker网络 `docker network create --ipv6 ip6net`/`docker network create --ipv6 --subnet 2001:db8::/64 ip6net`
> * 启动容器时指定此网络 `docker run --rm --network ip6net -p 80:80 traefik/whoami`
> * 已启动容器先断开源网络在连接新ipv6网络 `docker network disconnect <原网络名称> <容器名称或ID>`;`docker network connect <新网络名称> <容器名称或ID>`

> 参考文档:
[docker官方文档-开启ipv6支持](https://docs.docker.com/engine/daemon/ipv6/)
[知乎-docker ipv6支持博客](https://zhuanlan.zhihu.com/p/400379696)

### 使用linux已有的桥接网卡

宿主机必须存在桥接网卡, 之后才可通过 `--opt com.docker.network.bridge.name=<bridge_name>` 指定网卡名, 示例如下:
`docker network create --driver bridge --attachable --opt com.docker.network.bridge.name=<physical_network_interface_name> --subnet 192.100.1.0/24 --gateway 192.100.1.1 --ipv6 <network_name>`

## docker持久化

### 容器与镜像间转换
```
Commands:
  # 将容器文件系统导出为tar归档文件
  export      Export a container's filesystem as a tar archive
  
  # 从tar归档文件创建容器（需指定镜像），只是将tar文件系统覆盖掉默认文件系统
  import      Import the contents from a tarball to create a filesystem image

  # 基于容器创建一个新镜像
  commit      Create a new image from a container's changes

  # 保存镜像作为tar归档文件
  save        Save one or more images to a tar archive (streamed to STDOUT by default)

  # 从tar归档文件加载镜像
  load        Load an image from a tar archive or STDIN

```

## docker资源配置

#### docker 容器限制cpu和内存
`docker run -m 512m -cpus 2 --memory-reservation=256m <image_name>`
其中-m选项指定限制的内存，--memory-reservation指定在内存不足时更新限制内存，-cpus指定可使用的cpu数（可为小数）


## docker bulid

[多平台构建文档](https://docs.docker.com/build/building/multi-platform/)

## 示例

### docker for window

[window inside docker仓库](https://github.com/dockur/windows)

在ubuntu上启动window-docker容器
- 检查机器是否支持kvm进行加速 `kvm-ok` (apt install cpu-checker), 检查 `/dev/kvm` 是否存在
- 拉取window docker镜像 `docker pull dockurr/windows` 或者 从仓库手动构建 `docker build -t dockurr/windows .`
- 从 `docker-compose.yml` 创建容器 `docker compose up`, 默认会从Microsoft servers下载指定的window版本iso镜像; 或者从docker-cli创建 `docker run -it --rm -p 8006:8006 --device=/dev/kvm --device=/dev/net/tun --cap-add NET_ADMIN --stop-timeout 120 dockurr/windows`
```yml
services:
  windows:
    image: dockurr/windows
    container_name: windows
    environment:
      VERSION: "11"
    devices:
      - /dev/kvm
      - /dev/net/tun
    cap_add:
      - NET_ADMIN
    ports:
      - 8006:8006
      - 3389:3389/tcp
      - 3389:3389/udp
    restart: always
    stop_grace_period: 2m
```

> 支持的window版本如下:
|Value  |  	Version 	                | Size   |
|-------|-------------------------------|--------|
|11     |	Windows 11 Pro	            |5.4 GB  |
|11l    |	Windows 11 LTSC	            |4.2 GB  |
|11e    |	Windows 11 Enterprise	    |5.8 GB  |
|10     |	Windows 10 Pro	            |5.7 GB  |
|10l    |	Windows 10 LTSC	            |4.6 GB  |
|10e    |	Windows 10 Enterprise	    |5.2 GB  |
|8e     |	Windows 8.1 Enterprise	    |3.7 GB  |
|7e     |	Windows 7 Enterprise	    |3.0 GB  |
|ve     |	Windows Vista Enterprise	|3.0 GB  |
|xp     |	Windows XP Professional	    |0.6 GB  |
|2025   |	Windows Server 2025	        |5.0 GB  |
|2022   |	Windows Server 2022	        |4.7 GB  |
|2019   |	Windows Server 2019	        |5.3 GB  |
|2016   |	Windows Server 2016	        |6.5 GB  |
|2012   |	Windows Server 2012	        |4.3 GB  |
|2008   |	Windows Server 2008	        |3.0 GB  |
|2003   |	Windows Server 2003	        |0.6 GB  |

**注意** 如果报错`qemu-system-x86_64: failed to initialize kvm: Device or resource busy` 并且`kvm-ok` 检查无问题, 请确保一个应用在使用kvm, 此处是VirtualBox

## bug

### docker运行不同架构镜像需注意的bug

1. 检查binfmt_misc模块是否存在并且挂载 `lsmod | grep "binfmt_misc"` / `df /proc/sys/fs/binfmt_misc/`
    >使用 `mount binfmt_misc -t binfmt_misc /proc/sys/fs/binfmt_misc` 挂载
2. 查看 `qemu-user-static` 是否安装
3. docker拉取对应平台架构镜像
4. 根据架构挂载qemu卷 `docker run -it -d --name res -v /usr/bin/qemu-i386-static:/usr/bin/qemu-i386-static ubuntu:armv7_20.04`