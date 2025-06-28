# git

Git 是一个分布式版本控制系统，用于跟踪项目的更改历史和协作开发。它由 `Linus Torvalds` 于 2005 年创建，旨在提高代码管理的效率和可靠性。

## 基本术语

- **仓库 (Repository)**: 项目的存储区域，包含所有文件、历史记录和分支。
- **分支 (Branch)**: 开发线路，允许开发者在不影响主分支的情况下进行更改。
- **提交 (Commit)**: 对文件的快照，是对更改的记录。
- **远程 (Remote)**: 托管在服务器上的仓库，支持团队协作。
- **合并 (Merge)**: 将分支的更改合并到另一个分支中。

### **HEAD,index,working tree**

- HEAD 指针指向我们所在的分支，可在.git/HEAD文件中查看，git会以 `HEAD指针 --> 分支指针 --> 最新commit` 管理当前变更的forward路径
- index 为git数据库和工作区之间的暂存区，内部存放 `git add` 添加的变更索引
- working tree 工作树是git对编辑目录的专称，在工作树下查看和编辑的文件的实际内容

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
- `git commit --amend`: 修改最近一次的提交(如消息,提交文件等)

## git安装包中内置工具
1. git 内置了一个msys2环境(这是一个适用于window上posix兼容层，基于cygwin)，包含一系列posix命令
2. gitk 一个图形化的存储库浏览器(git log 的gui封装)，用于浏览和可视化存储库的历史记录。
3. git_gui git的图形化界面

## git的gui工具
配置gui工具中文编码 `git config --global gui.encoding utf-8`

## git hooks

git 提供一系列hooks用于用户自定义代码同步的系列操作。默认存放在 `$GIT_DIR/hooks/*` 或者 git配置设置的路径 `git config --get core.hooksPath`/*

**注意** .git目录默认不参与代码同步

[githooks文档](https://git-scm.com/docs/githooks)

## git commit

### 通用的提交规范

> commit message format：`<type_name>[scope]: describe message`
```sh
feat: 添加新模块, 新功能等增量式改动
improvement: 在已有功能上的改进
fix: bug修复
test: 针对某一功能或者模块的测试
style: 代码风格的变动，不影响代码原有功能
doc: 文档修改，如注释
chore: 构建过程或辅助工具的变动
refactor: 已有功能代码重构，不影响代码原有功能
perf: 原有模块，功能的性能优化
build: 构建系统
ci: 对CI配置文件修改
chore: 修改构建流程、或者增加依赖库、工具
revert: 回滚版本
```

## git clone

### clone支持的协议

git支持的传输协议包含以下几种:
- https: `git clone `
- ssh: `git clone`
- file: `git clone`
- git: 此协议一般用于只读,在互联网上分享