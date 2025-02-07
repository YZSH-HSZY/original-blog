# Dockerfile

[参官方dockerfile文档](https://docs.docker.com/reference/dockerfile/)

## 什么是 Dockerfile？
Dockerfile 是一个用来构建docker镜像的文本文件，文本内容包含了一条条构建镜像所需的指令和说明。

我们可以使用 Dockerfile 定制镜像，并借助docker hub来快速部署项目

Dockerfile分为四部分：基础镜像信息、维护者信息、镜像操作指令、容器启动执行指令。

## dockerfile指令
Dockerfile的指令是**忽略大小写**的，建议使用大写，**使用 # 作为注释**，每一行只支持一条指令，每条指令可以携带多个参数。

Dockerfile的指令根据作用可以分为两种，构建指令和设置指令。

1. 构建指令用于构建image，其指定的操作不会在运行image的容器上执行；
2. 设置指令用于设置image的属性，其指定的操作将在运行image的容器中执行。


|Dockerfile 指令	|   说明    |
|-------------------|-------------------|
|FROM	            |指定基础镜像，用于后续的指令构建。|
|MAINTAINER	        |指定Dockerfile的作者/维护者。（已弃用，推荐使用LABEL指令）|
|LABEL	            |添加镜像的元数据，使用键值对的形式。|
RUN	在构建过程中在镜像中执行命令。|
|CMD                |指定容器创建时的默认命令。（可以被覆盖）|
|ENTRYPOINT	        |设置容器创建时的主要命令。（不可被覆盖）|
|EXPOSE	            |声明容器运行时监听的特定网络端口。|
|ENV	            |在容器内部设置环境变量。|
|ADD	            |将文件、目录或远程URL复制到镜像中。|
|COPY	            |将文件或目录复制到镜像中。|
|VOLUME	           |为容器创建挂载点或声明卷。|
|WORKDIR	        |设置后续指令的工作目录。|
|USER	            |指定后续指令的用户上下文。|
|ARG	            |定义在构建过程中传递给构建器的变量，可使用 "docker build" 命令设置。|
|ONBUILD	        |当该镜像被用作另一个构建过程的基础时，添加触发器。|
|STOPSIGNAL	        |设置发送给容器以退出的系统调用信号。|
|HEALTHCHECK	    |定义周期性检查容器健康状态的命令。|
|SHELL	            |覆盖Docker中默认的shell，用于RUN、CMD和ENTRYPOINT指令。|

**注意**
- VOLUME指令指定的卷列表只会在容器中创建目录, `docker run` 时仍需指定 `-v host_data_path:contain_path`
- CMD指定的命令会作为参数传递给ENTRYPOINT(defaule /bin/sh)
> 如果dockerfile中为 `CMD echo hello` 则未指定 `docker run `args 执行 `/bin/sh -c 'echo hello'` 后自动退出

## dockerfile实列

1. 第一行必须指定 基础镜像信息, 如 `FROM ubuntu`
2. 维护者信息,如 `MAINTAINER docker_user docker_user@email.com`
3. 镜像操作指令, 示例如下:
> RUN：用于执行后面跟着的命令行命令。 有以下俩种格式：
- shell 格式：RUN <命令行命令>
- exec 格式：RUN ["可执行文件", "参数1", "参数2"]

> 例如：RUN ["./test.php", "dev", "offline"] 等价于 RUN ./test.php dev offline
RUN echo "deb http://archive.ubuntu.com/ubuntu/ raring main universe" >> /etc/apt/sources.list
RUN apt-get update && apt-get install -y nginx
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf
4. 容器启动执行指令 `CMD /usr/sbin/nginx`

> dockerfile指令说明
```
FROM		#基础镜像，一切从这里开始构建
MAINTAINER	#镜像是谁写的，姓名+邮箱
RUN			#镜像构建的时候需要运行的命令
ADD			#添加内容，步骤，tomcat镜像，这个tomcat的压缩包！
WORKDIR		#镜像的工作目录	
VOLUME		#挂载的目录
EXPOSE		#暴露端口配置
CMD			#指定这个容器启动的时候要运行的命令，只有最后一个会生效，可被替代
ENTRYPOINT	#指定这个容器启动的时候要运行的命令，可以追加命令
ONBUILD		#当构建一个被继承 Dockerfile 这个时候就会运行ONBUILD 的指令
COPY 		#类似ADD，将我们文件拷贝到镜像中
ENV			#构建的时候设置环境变量
```

**注意**：Dockerfile 的指令每执行一次都会在 docker 上新建一层。所以过多无意义的层，会造成镜像膨胀过大。你可以使用&&并行执行需要的shell命令

### dockerfile上下文

上下文路径是指 docker 在构建镜像，有时候想要使用到本机的文件（比如复制），docker build 命令得知这个路径后，会将路径下的所有内容打包。

> 解析：由于 docker 的运行模式是 C/S。我们本机是 C，docker 引擎是 S。实际的构建过程是在 docker 引擎下完成的，所以这个时候无法用到我们本机的文件。这就需要把我们本机的指定目录下的文件一起打包提供给 docker 引擎使用。如果未说明最后一个参数，那么默认上下文路径就是 Dockerfile 所在的位置。

**注意**：上下文路径下不要放无用的文件，因为会一起打包发送给 docker 引擎，如果文件过多会造成过程缓慢。

```sh
# 构建镜像，将当前目录做为构建上下文
docker build .

# Dockerfile 一般位于构建上下文的根目录下， 也可以通过-f指定该文件的位置
# 还可以通过-t参数指定构建成镜像的仓库、标签
docker build -f /path/to/Dockerfile -t nginx:v1 .
```

### 一个简易的dockerfile构建asr服务的示例

```dockerfile
FROM ubuntu:20.04
MAINTAINER qgq yzsh_hszy@outlook.com

ENV LANG en_US.utf8
# 挂载卷
VOLUME /home/asr-web

# 声明容器输出端口，使用-P随机映射主机端口时会自动挂载到容器声明端口
EXPOSE 3000/tcp

# 切换工作目录
WORKDIR /home/asr-web

RUN  sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list && \
     apt-get clean && \
     apt-get update && \
     apt-get install -y libmysqlclient-dev tzdata  \
                        python3 python3-dev python3-pip \
    && apt-get clean \
    && apt-get autoclean \
	&& ln -s /usr/bin/pip3 /usr/bin/pip && ln -s /usr/bin/python3 /usr/bin/python \
	
	&& pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple  \
	&& rm -rf /var/lib/apt/lists/* && rm /tmp/requirements.txt \
    && npm i

CMD ["npm run dev"]
```