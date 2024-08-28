# open-project
这里存放一些开源项目的复现笔记

## AliceBot

AliceBot 是一个简单的 Python 异步多后端机器人框架，支持多种协议适配，可以轻松地编写易于学习和使用的插件来拓展其功能。AliceBot 使用了非常灵活且易于使用的插件编写方式，用户只需要编写两个方法即可实现一个功能强大的插件。它的适配协议并不与任何一种库或网络协议绑定，目前官方维护了 OneBot、QQ、钉钉等协议适配。

### 技术栈

- Web Application
- WebSocket

### 相关介绍

1. https://github.com/AliceBotProject/alicebot
2. https://github.com/AliceBotProject/alicebot-example

### 项目产出要求

1. 调研学习 Telegram Bot API 和现有的 Telegram 机器人支持库
2. 设计并编写 Telegram 适配器
3. 代码符合规范，能够通过 CI 测试

### 项目prepare

#### Telegram介绍

Telegram 是一款专注于速度和安全性的**消息传递应用程序**。快速、简单且免费和开源。

提供了面向开发者的api接口手册
- Telegram API 手册： https://core.telegram.org/api
- MTproto 协议手册：https://core.telegram.org/mtproto

> Telegram提供两种 API,Bot API 允许您轻松创建使用 Telegram 消息作为界面的程序。 Telegram API and TDLib 允许您构建自己的自定义 Telegram 客户端。

这里只介绍Bot API:
> 此 API 允许您将机器人连接到我们的系统。Telegram Bots 是不需要额外电话号码即可设置的特殊帐户。这些帐户充当服务器上某处运行的代码的接口。
> 要使用它，您无需了解我们的 MTProto 加密协议的工作原理——我们的中间服务器将为您处理所有加密和与 Telegram API 的通信。您可以通过简单的 HTTPS 接口与此服务器通信，该接口提供 Telegram API 的简化版本。
> 机器人开发人员还可以利用我们的支付 API 接受来自世界各地 Telegram 用户的付款。

Bot是完全在 Telegram 应用程序中运行的小型应用程序。用户通过灵活的界面与机器人交互，这些界面可以支持任何类型的任务或服务。

#### 第一个例子Hello World

Telegram Bot API 通过JSON进行响应。通过 HTTPS 请求查询 API 并等待响应。您可以发出多种类型的请求，以及可以使用和接收的许多不同对象作为响应。
1. 获取bot token
 - @BotFather 然后在对话中键入/newbot
 - 设置bot名字和用户名
![试用bot api](img/image.png)
2. 注册
![测试bot获取msg](img/getMessage.png)



#### Telegram Bot程序编写

[telegram官方bot文档教程](https://core.telegram.org/bots/tutorial)
[telegram官方bot代码示例](https://gitlab.com/Athamaxy/telegram-bot-tutorial/-/tree/main)

Telegram Bot API 通过JSON进行响应。

##### Telegram Bot python示例代码

- IDE
    PyCharm
    Visual Studio Code
- Dependencies
    在终端中键入此命令，然后按 enter 。
    `pip install python-telegram-bot==13.12`
- Export Your Project
    将源文件从项目文件夹复制到文件夹 TBotRemote 
- Run Your Bot
    在终端中键入此命令，然后按 enter 。
    `cd TBotRemote`
    `python TutorialBot.py`
