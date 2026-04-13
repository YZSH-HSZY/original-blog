# 介绍
此文件介绍使用vscode+ai组合搭建的自动完成环境

## cline + openrouter

cline(vscode插件) 用于在vscode上自动运行某些任务，配置权限允许后，也可以在终端中自动执行命令并获取结果，配合 openrouter(一个智能模型API聚合平台) 可以更换多个模型选择最好的去执行任务。


### 一个免费自动任务配置

1. 注册 `openroute`
2. 在 `openroute` 官网上，选择 `Personal --> API Keys --> Create` 创建一个cline使用的接口，在 `Credit limit (optional)` 里设置花费上限为 0$
3. 复制 `API-KEY` (注意此key之后不可见)
4. 在vscode上安装 cline 插件
5.  cline 面版中配置 openroute 使用，`Settings --> API Provider(Select OpenRoute) --> API KEY(Parse Key) --> Model(Select free model)`
