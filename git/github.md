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
### action可用事件Events


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