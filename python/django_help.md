## django使用

### django安装
`pip install django`

### 项目创建

**注意** 在安装django后，会自动添加一部分可执行文件到python的scripts目录下，可参考django源码查看添加的脚本

这里使用django-admin创建项目 `django-admin startproject example` 会在当前目录下创建目录 `example`，内包含项目文件

#### 项目创建生成文件介绍
example: 项目的容器（一个纯 Python 包）
manage.py: 一个实用的命令行工具，可让你以各种方式与该 Django 项目进行交互。
example/__init__.py: 一个空文件，告诉 Python 该目录是一个 Python 包。
example/asgi.py: 一个 ASGI 兼容的 Web 服务器的入口，以便运行你的项目。
example/settings.py: 该 Django 项目的设置/配置。
example/urls.py: 该 Django 项目的 URL 声明; 一份由 Django 驱动的网站"目录"。
example/wsgi.py: 一个 WSGI 兼容的 Web 服务器的入口，以便运行你的项目。

**注意** WSGI(Web Server Gateway Interface, web服务网关接口)、ASGI(Async Server Gateway Interface, 异步服务网关接口)

#### url，path，re_path
* url是Django 1.x中的写法
* 在Django2.1中，开始舍弃Django1.x中的url写法，描写url配置的有两个函数path和re_path。
* re_path相对于path可以在路径中使用正则。

examle如下：
path('path/', consumer.ws_message),
需要使用路径全匹配，包括'/'
而re_path只需'path'

## web协议

Web协议出现顺序： CGI -> FCGI -> WSGI-> uwsgi
CGI： 最早的协议
FCGI： 比CGI快
WSGI(Web Server Gateway Interface) ： Python专用的协议
uwsgi： 比FCGI和WSGI都快，是uWSGI项目自有的协议，主要特征是采用二进制来存储数据，之前的协议都是使用字符串，所以在存储空间和解析速度上，都优于字符串型协议.

各模块作用：

nginx：是对外的服务器，外部浏览器通过url访问nginx，nginx主要处理静态请求
uWSGI：是对内的服务器，主要用来处理动态请求
uwsgi：是一种web协议，接收到请求之后将包进行处理，处理成wsgi可以接受的格式，并发给wsgi
wsgi：是python专用的web协议，根据请求调用应用程序（django）的某个文件，某个文件的某个函数
django：是真正干活的，查询数据等资源，把处理的结果再次返回给WSGI， WSGI 将返回值进行打包，打包成uwsgi能够接收的格式
uwsgi接收wsgi发送的请求，并转发给nginx,nginx最终将返回值返回给浏览器

### uWSGI与uwsgi区别
uWSGI：是对内的服务器，主要用来处理动态请求
uwsgi：是一种web协议，接收到请求之后将包进行处理，处理成wsgi可以接受的格式，并发给wsgi