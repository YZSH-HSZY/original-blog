# 笔记说明
记录github网站的各种使用笔记

## GitHub Actions
(github action官方文档)[https://docs.github.com/zh/actions]

GitHub Actions 是一个持续集成和持续交付（CI/CD）平台，允许您自动化构建、测试和部署流程。可以创建工作流，对存储库中的每个拉取请求进行构建和测试，或者将合并的拉取请求部署到生产环境。

> GitHub Actions workflow是一个具体的工作流任务，在存储库中发生指定事件时触发（也可以手动触发）。workflow可以包含一个或多个作业，作业按顺序或并行运行。作业job包含一个或多个步骤，这些步骤要么运行您定义的脚本，要么运行一个动作，这是一个可以简化您流水线的可重用扩展。
> Action也指一个自动化应用，用于执行复杂但经常重复的任务

**注意** 每个作业job将在自己的虚拟机运行器内或容器内运行

### Action使用情景
包括但不限于DevOps、管理issue（自动打标签）、发布应用包、代码规范性检查和自动测试、其他的自动脚本等

### 创建workflow
在存储库的目录 `.github/workflows` 下，由 一个`YAML` 文件定义一个 `workflow`

**注意** workflow可以相互引用，参[工作流重用](https://docs.github.com/en/actions/using-workflows/reusing-workflows)

### workflow文件编写规则

workflow使用yaml文件编写，如以下选项

#### name
工作流的名称。 GitHub 在存储库的Action选项卡下显示工作流的名称。如果省略，会显示相对于存储库根目录的工作流文件路径。

#### run-name
从工作流生成的**工作流运行的名称**（注意区分name）， GitHub 在存储库的Action选项卡上的工作流运行列表中显示工作流运行名称。如果省略了 run-name 或仅为空格，则运行名称将设置为工作流运行的事件特定信息。 例如，对于由 push 或 pull_request 事件触发的工作流，将其设置为提交消息或拉取请求的标题。

**可包含表达式，可引用 github 和 inputs 上下文**
如: `run-name: Deploy to ${{ inputs.deploy_target }} by @${{ github.actor }}`

#### on
设置事件自动触发工作流运行

- 使用单个事件 `on: push`
- 使用多个事件 `on: [push, fork]`
- 对于存在使用活动类型

#### run

每个 run 关键字代表运行器环境中一个新的进程和 shell。 当您提供多行命令时，每行都在同一个 shell 中运行。 如
- 单行命令: `run: npm install`
- 多行命令, 如下:
```yml
run: |
  npm ci
  npm run build
```

### action可用事件Events


### 使用act本地调试Action

act 是一个本地运行GitHub Actions的工具

[act github 仓库](https://github.com/nektos/act)
[act 官方文档](https://github.com/nektos/act)

### Action自动令牌身份验证

GitHub 提供一个令牌，可用于代表 GitHub Actions 进行身份验证。每个工作流作业开始时，GitHub 会自动创建唯一的 `GITHUB_TOKEN` 机密以在工作流中使用。 可以使用 `GITHUB_TOKEN` 在工作流作业中进行身份验证。

[官方文档](https://docs.github.com/zh/actions/security-for-github-actions/security-guides/automatic-token-authentication#permissions-for-the-github_token)
**注意** GITHUB_TOKEN 在作业完成或最多 24 小时后过期。令牌在 github.token 上下文中也可用

## github page
[github page官方教程](https://docs.github.com/zh/pages/getting-started-with-github-pages/about-github-pages#types-of-github-pages-sites)

GitHub Pages 是一项静态站点托管服务，它直接从 GitHub 上的仓库获取 HTML、CSS 和 JavaScript 文件，可通过构建过程运行文件，然后发布网站。

[github page官方示例](https://github.com/collections/github-pages-examples)

### page站点分类

1. 组织，连接到github特定账户，最多一个。默认形如 `http(s)://<organization>.github.io`
2. 用户，连接到github特定账户，最多一个。默认形如 `http(s)://<username>.github.io`
3. 项目，项目站点连接到 GitHub 上托管的特定项目(即特定仓库)，无数量限制。形如 `http(s)://<username>.github.io/<repository>`

### pages创建

参[创建教程](https://docs.github.com/zh/pages/getting-started-with-github-pages/creating-a-github-pages-site)

- 你只需创建一个仓库(名为`<yzsh-hszy>.github.io`)即可创建一个用户站点
**注意** 如果用户或组织名称包含大写字母，必须写为小写字母
- 在站点仓库中, GitHub Pages 将查找 index.html、index.md 或 README.md 文件，作为站点的入口文件。
**注意** 入口文件的具体位置取决于github page的发布源

### pages设置

在仓库的settings选项中,左侧的代码和自动化(Code and automation)列表下,存在Page项.点击该项即可编辑GitHub Pages设置.
包含以下可配置内容:
1. 设置发布源(Action/default deploy from branch)
2. branch发布时,配置部署分支名和路径
3. 添加自定义域名

### 自动生成的pages-build-deployment活动
在你构建

## 示例
### github contributions计数规则
1. main分支
2. 邮箱地址（非私有）
- > 对于私有邮箱，github提供一个用于contributions计数、拉取、推送的邮箱地址，你可以在github settings email查看，形如`113163252+YZSH-HSZY@users.noreply.github.com`
(详细信息仓库)[https://docs.github.com/zh/account-and-profile/setting-up-and-managing-your-github-profile/managing-contribution-settings-on-your-profile/why-are-my-contributions-not-showing-up-on-my-profile#your-local-git-commit-email-isnt-connected-to-your-account]

- > 对于私有邮箱，在创建远程仓库时，默认的初始提交将使用`@users.noreply.github.com`邮箱记录，如
```
commit 0b7fb916ae76ad7f97beb79edb91a01993dfdc17
Author: YZSH-HSZY <113163252+YZSH-HSZY@users.noreply.github.com>
Date:   Fri Jun 14 23:04:19 2024 +0800

    Initial commitcommit 
```
- > 对于私有邮箱，暴露私有邮箱的推送会被拒绝，如
```
remote: error: GH007: Your push would publish a private email address.
remote: You can make your email public or disable this protection by visiting:
remote: http://github.com/settings/emails
To github.com:YZSH-HSZY/mblog.git
 ! [remote rejected] main -> main (push declined due to email privacy restrictions)
error: failed to push some refs to 'github.com:YZSH-HSZY/mblog.git'
```
**注意** 可以在github settings email中取消`Block command line pushes that expose my email`来允许命令行设置邮箱（可能暴露私有邮箱的方式）来提交，这时对main分支的提交将会被contributions统计。

3. 具有项目主页的非mian分支


### github同步其他代码仓库到本仓库

1. 借助 `github action` 完成，示例如下：
```yaml
name: sync_fork_from_gitee

on:
  schedule:
    - cron: '0 0 * * *'  # 每天同步一次，可以根据需要调整(参cron编写规则)
  workflow_dispatch:  # 允许手动触发工作流(在仓库主页的action选项中手动运行)

permissions:
  contents: write  # 允许在本仓库中写入内容,使用 GitHub Actions 提供的默认 `GITHUB_TOKEN`

jobs:
  sync:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout GitHub repository
        uses: actions/checkout@v2
        with:
          repository: YZSH-HSZY/original-blog
          token: ${{ secrets.GITHUB_TOKEN }}
          path: github-repo

      - name: Clone Gitee repository
        run: |
          git clone https://gitee.com/YZSH-HSZY/blog.git gitee-repo
          cp -r gitee-repo/* github-repo/  # 将 Gitee 的内容复制到 GitHub 仓库

      - name: Commit and Push Changes
        run: |
          cd github-repo
          git config user.name "YZSH-HSZY"
          git config user.email "yzsh_hszy@outlook.com"
          git add .
          git commit -m "Sync from Gitee" || echo "No changes to commit"
          git push origin main  # 根据你的主分支名称调整
```

2. 对于gitee和github仓库，可以借助仓库镜像可以实现不同平台之间仓库分支、标签和提交信息的自动同步

## 基于jekyll的个人博客搭建

Jekyll 是一个可以将纯文本转换为静态博客网站的工具，支持多种格式和渲染器。也是github官方推荐的个人博客搭建工具。

### jekyll目录

```
_config.yml/_config.toml  指定配置选项

```

## 基于pelican的个人博客搭建
pelican是一个python实现的静态网站生成器，对python的支持更加友好。

[参pelican笔记](../doc_maker/pelican.md)