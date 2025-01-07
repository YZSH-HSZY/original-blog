# docker


#### docker 安装

1. 使用官方提供的测试安装脚本安装(不推荐)
```
curl -fsSL https://test.docker.com -o test-docker.sh
sudo sh test-docker.sh
```
2. Docker 在 https://get.docker.com/ 提供了一个方便的脚本，可以在开发环境中非交互式地安装 Docker。不推荐用于生产环境，但它对于创建符合您需求的配置脚本很有用。

**注意** 从 `https://get.docker.com/` 下载的脚本，使用 `--dry-run` 查看脚本将要执行的内容

#### 将用户添加到docker组中
`sudo usermod -aG docker ${USER}`

#### 配置 docker hub 镜像源

我们获取 docker images 时默认从https://hub.docker.com拉取的。在国内该hub源访问速度异常慢，尤其是大一点的镜像经常出现timeout。

```
管理员权限编辑或创建/etc/docker/dameon.json，添加docker中国地区镜像
{
 "registry-mirrors": ["https://registry.docker-cn.com"]
}
```

其他镜像：网易 http://hub-mirror.c.163.com
阿里云 https://<...>.mirror.aliyuncs.com 需要自己去以下链接创建专属镜像仓库
https://cr.console.aliyun.com/

#### docker 使用

使用 docker --help 查看帮助信息

```
ubuntu@VM-12-17-ubuntu:~$ docker --help
Usage:  docker [OPTIONS] COMMAND
```

#### docker 查看镜像标签

1. 在浏览器打开 hub.docker.com 上搜索镜像查找标签
2. 使用 curl 工具查看，示例如下

```
curl https://registry.hub.docker.com/v1/repositories/mysql/tags\
| tr -d '[\[\]" ]' | tr '}' '\n'\
| awk -F: -v image='mysql' '{if(NR!=NF && $3 != ""){printf("%s:%s\n",image,$3)}}'

或者借助python的json工具
curl https://registry.hub.docker.com/v1/repositories/rancher/rancher/tags | python -m json.tool | grep 2.4

```

#### 停止docker服务
如果你想要完全停止 docker 服务，你需要同时关闭 docker.service 和 docker.socket 文件： sudo systemctl stop docker.service sudo systemctl stop docker.socket 如果需要在系统启动时禁用 Docker 服务，可以使用以下命令： sudo systemctl disable docker 这个命令会禁用 Docker 服务，以防止它在系统启动时自动启动。

#### docker已存在容器配置挂载点
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
#### docker已存在容器配置端口映射

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
#### docker 的 ubuntu 容器内安装 python

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

#### docker 启动并运行新容器
```
使用docker help查看帮助，在常用命令中发现run是创建并运行新容器
Common Commands:
  run         Create and run a new container from an image

```
#### docker查看已启动容器的标准输出

`docker logs {container_name | container_id}`

#### docker容器与镜像间转换
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

#### docker 容器限制cpu和内存
`docker run -m 512m -cpus 2 --memory-reservation=256m <image_name>`
其中-m选项指定限制的内存，--memory-reservation指定在内存不足时更新限制内存，-cpus指定可使用的cpu数（可为小数）



