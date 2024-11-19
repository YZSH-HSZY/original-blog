# git

Git 是一个分布式版本控制系统，用于跟踪项目的更改历史和协作开发。它由 `Linus Torvalds` 于 2005 年创建，旨在提高代码管理的效率和可靠性。

## 基本术语

- **仓库 (Repository)**: 项目的存储区域，包含所有文件、历史记录和分支。
- **分支 (Branch)**: 开发线路，允许开发者在不影响主分支的情况下进行更改。
- **提交 (Commit)**: 对文件的快照，是对更改的记录。
- **远程 (Remote)**: 托管在服务器上的仓库，支持团队协作。
- **合并 (Merge)**: 将分支的更改合并到另一个分支中。

## 常用命令

- `git init`: 初始化一个新的 Git 仓库。
- `git clone <repository-url>`: 克隆远程仓库到本地。
- `git add <file>`: 添加文件到暂存区。
- `git commit -m "message"`: 提交暂存区的更改。
- `git push`: 将本地更改推送到远程仓库。
- `git pull`: 从远程仓库拉取并合并更改。
- `git branch`: 列出分支。
- `git checkout <branch>`: 切换到指定分支。
- `git merge <branch>`: 合并指定分支到当前分支。

## git安装包中内置工具
1. git 内置了一个msys2环境(这是一个适用于window上posix兼容层，基于cygwin)，包含一系列posix命令
2. gitk 一个图形化的存储库浏览器(git log 的gui封装)，用于浏览和可视化存储库的历史记录。
3. git_gui git的图形化界面

## git的gui工具
配置gui工具中文编码 `git config --global gui.encoding utf-8`
