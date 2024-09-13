### git 帮助信息
短选项-h会在命令行中输出帮助信息，长选项--help会在浏览器查看本地html帮助文档

### worktree介绍
(git-worktree官方文档)[https://git-scm.com/docs/git-worktree]

git在 2015 年就开始支持的功能worktree,是一个管理附加到同一存储库的多个工作树的工具。一个 git 存储库可以支持多个工作树(及分支)，允许您一次签出多个分支。使用 git worktree add 新的分支与存储库相关联，以及将该分支与同一存储库中的其他分支区分开来的元数据。分支与此元数据一起称为"worktree"。

这个"worktree"被称为"链接工作树"，而不是由 `git-init` 或 `git-clone` 产生的"主工作树"。一个存储库有一个主工作树（如果它不是空存储库）和零个或多个链接的工作树。完成链接工作树的工作后，可以使用 git worktree remove 移除它。

> 支持命令如下:
```
git worktree add [-f] [--detach] [--checkout] [--lock [--reason <string>]]
		   [--orphan] [(-b | -B) <new-branch>] <path> [<commit-ish>]
git worktree list [-v | --porcelain [-z]]
git worktree lock [--reason <string>] <worktree>
git worktree move <worktree> <new-path>
git worktree prune [-n] [-v] [--expire <expire>]
git worktree remove [-f] <worktree>
git worktree repair [<path>…​]
git worktree unlock <worktree>
```
**注意** git工作需要名称为 .git 的文件或目录，如果你使用worktree，你需要在工作目录下创建.git文件，并在其中指定git的缓存目录，如 `gitdir: ./.bare`

#### worktree创建
使用选项 --bare，如：`git clone --bare <remote-rep-url>`，这样只会拉取git的HEAD目录，你可以任取一个别名并创建.git文件在gitdir选项中指向它。

#### git worktree add
`git worktree add <path>` 会自动创建分支（名称是 `<path>` 的组件），如果打算工作在一个新的分支(即在多个分支间相互切换)，这会很方便。例如，

> `git worktree add ../hotfix` 创建新分支hotfix,并在路径../hotfix中签出它。若要改为处理新工作树中的现有分支，请使用 `git worktree add <path> <branch>` 

> 如果您只是计划在不干扰现有开发的情况下进行一些实验性更改或进行测试 `git worktree add -d <path>` 可以创建一个与任何分支无关的一次性工作树,其提交信息HEAD 与当前分支分离。

### git配置ssh key

#### 更改ssh key文件位置
1. 使用core.sshCommand配置选项，当git运行任何需要SSH隧道的命令时，此配置将覆盖默认的SSH命令。如`git config core.sshCommand "ssh -i ~/.ssh/id_rsa_work"`
2. 使用ssh配置文件config，默认在` %USERPROFILE%\.ssh\config`下
> 其中可以指定domain的ssh key文件位置，如
```
Host github.com
    HostName github.com
    IdentityFile "D:\Git\usr\ssh"
```

### git push 时每次都要输入用户名和密码的解决办法
如果我们git clone的下载代码的时候是连接的http形式，而不是git@git (ssh)的形式，当我们操作git pull/push到远程的时候，总是提示我们输入账号和密码才能操作成功，频繁的输入账号和密码会很麻烦。
`git config --global credential.helper store`

### git clone仓库过大时解决方案
1. 方法一
直接延长克隆时间,让它超时时间很长，慢慢下载。
`git config --global http.postBuffer 524288000(这个是超时时间)`
2. 方法二
先克隆最近提交的版本，然后拉取所有版本
`git clone --depth=1 http://xxx.git  #拉取最近1次提交的版本`
`git fetch --unshallow # 拉取完整当前分支`
`git remote set-branches origin '*' # 追踪所有远程分支`
`git fetch -v # 拉取所有远程分支`

### git config命令

命令格式：`usage: git config [<options>]`

**注意** options有四种类型，为 `{Config file location, Action, Type, Other}`

> Config file location指定读取git的config文件位置;
1. --system读取 git安装目录下etc/gitconfig 文件(针对所有用户生效)
2. --global读取 `%USERPROFILE%/.gitconfig` 文件(针对当前用户生效)
3. --local读取 仓库.git/config 文件(在仓库工作目录时,默认使用)
4. `-f <file>` 指定读取配置文件路径

#### git config取消设置项
使用 `--unset` 取消config设置

#### 查看所有配置项及其对应config文件位置
`git config -l --show-origin`

#### 设置gpg-key文件位置
`git config --global user.signingKey <ssh_file_full_path>`

**注意** 需要同时将配置 `gpg.format` 设置为 "ssh" ,此时`user.signingKey`可以包含私有 ssh 密钥的路径，也可以包含使用 ssh-agent 时的公钥的路径。或者，它可以包含直接包含 以`key::`为前缀的公钥（例如："key::ssh-rsa XXXXXX identifier）。

#### ssh key与gpg key区别
在我们使用gitee或github时，账户setting中存在add ssh keys和gpg keys选项，这两个key的作用场景不同，其中ssh主要用于远程登陆，而gpg主要用于安全传输。

**注意** 在你进行拉起仓库等需要权限的操作时，会进行身份验证，这时会使用ssh验证用户身份。如果你配置了gpg密匙，那么在数据传输时会使用其进行加密。

### git设置代理
1. 配置全局代理
`git config --global https.proxy https://127.0.0.1:7890`
2. 为指定站点配置代理
`git config --global https.https://github.com.proxy https://127.0.0.1:7890`

### git log命令

#### 查看指定文件相关的commit记录
`git log filename`
#### 显示指定文件每次提交的diff(区别)
`git log -p filename`
#### 查看某次提交中的某个文件变化
`git show comit_id filename`
#### 查看某次提交
`git show commit_id`
#### 以图形化界面的方式显示修改列表
`gitk --follow filename`

### git撤销提交

#### git reset
`git reset` 用于将当前HEAD重置为指定状态，HEAD之后的commit节点会丢弃
**注意** reset只用于本地仓库、缓存和工作区，对于远程仓库需使用`--force`强制更改

#### git revert
`git revert <old_commit_id>` 会生成一个新的 commit，将指定的 old commit 修改内容从当前分支上覆盖掉
**注意** 原始修改old_commit对于log节点会保留，因此重新推送的话，该部分会进行比较

### git 合并多分支

#### git merge
<!-- TODO -->

#### git rebase
`git rebase <upstream-branch-name> <to-branch-name>` 用于在另一个分支上重新提交

1. 切换到to-branch分支；
2. 将to-branch中比upstream-branch多的commit先撤销掉，并将这些commit放在一块临时存储区（.git/rebase）；
3. 将upstream-branch中比to-branch多的commit应用到to-branch上，此刻to-branch和upstream-branch的代码状态一致；
4. 将存放的临时存储区的commit重新应用到to-branch上；


### git查看仓库大小

`git count-objects -vH`
只统计添加到仓库的文件的大小，不包含.gitignore忽略的文件

### git清理操作

#### 查看git的远程缓存中所用空间最大的文件（.git/objects/pack目录下）

首先找出git中前N大的文件：以前五为例
```
git rev-list --objects --all | grep "$(git verify-pack -v .git/objects/pack/*.idx | sort -k 3 -n | tail -5 | awk '{print$1}')"
```
命令说明：
```​
> git verify-pack -v .git/objects/pack/pack-*.idx | sort -k 3 -g | tail -5​

2c5ba495f5cfbd9393b5559e8e2f50fa40390078 blob   9883322 8959560 9509049
13b39b44dc8f90b657dcf20d5b42f850ef4da5ed blob   12577437 12418079 46399648

sort -k指定按第3列排序，-g以普通数字比较，-n以字符串数字比较
tail -5列出最后5行
```
第一行的字母其实相当于文件的id,用以下命令可以找出id 对应的文件名：
`​git rev-list --objects --all | grep 13b39b44dc8f90b657dcf20d5b42f850ef4da5ed`
**对于已经加入版本管理中的文件，无法通过.gitignore取消，直接删除也会有远程备份**

**注意** 直接复制命令到git bash时，可能存在不可见的未知字符导致命令错误，你可以将该行命令的前后几个字符手动输入

#### 查看.git中存储的缓存文件
```
git rev-list --objects --all
```
#### 删除.git中存储的缓存文件
```
 git filter-branch --index-filter 'git rm --cached --ignore-unmatch  <需要删除的文件（包括路径和文件名）>'

```
#### 递归删除本地和远程中的文件目录
```
git rm -r SpeechServer/**/__pycache__
```
#### 清楚远程缓存
```
Administrator@PC172 MINGW64 /d/tt2/speech (master)

$ git rm -r --cached SpeechServer/VideoTransition/migrations/__pycache__
rm 'SpeechServer/VideoTransition/migrations/__pycache__/__init__.cpython-38.pyc'
```
#### git强制提交
```
Administrator@PC172 MINGW64 /d/tt/speech (master)
$ git push --force --all
```

#### 取消add添加的文件
使用`git status`查看
使用`git reset .`取消add添加的文件（该命令用于复位git的HEAD文件）

`git rm file_path` 删除暂存区和分支上的文件，同时工作区也不需要
`git rm --cached file_path` 删除暂存区或分支上的文件, 但工作区需要使用, 只是不希望被版本控制（适用于已经被git add,但是又想撤销的情况）
`git reset HEAD` 回退暂存区里的文件

#### 撤退commit操作
`git reset --hard <commit_id>`该操作会回退到指定的commit_id时的状态（该分支的工作区、暂存区、本地仓库都会更改，请谨慎使用）


### 分支操作

#### git查看分支

```
git branch  #查看本地分支
git branch -r #查看远程分支
git branch -a #查看所有分支（包括本地和远程）
```

**注意** 如果分支为空,那么通过 `branch` 查看分支不会显示。

#### git查看分支创建者
`git log --oneline remotes/origin/ttt2 | cut -d " " -f 1 | tail -1 | xargs git log`

#### 创建分支

1. `git branch <新分支名branch name>`根据当前分支创建新分支，仍在旧分支
2. `git checkout -b <new_branch_name> <old_branch_name>`根据指定旧分支创建新分支，并切换到新分支
3. 只创建空分支，使用git checkout -b命令创建的分支是有父节点的，这意味着新的分支包含了历史提交，所以我们需要使用`git checkout --orphan`命令，创建孤立分支(即无历史提交的空分支)
**注意** 空分支只是不包含commit信息，分支对应本地仓库是干净的，但仍会将当前分支的提交添加到暂存区，可以使用`git rm --cached .`删除暂存区上的文件

#### 切换分支
```
git checkout <切换分支名 branch name>
```
#### 推送新分支
```
git push origin <推送分支名 branch name>	# 非主分支需要指定地址（即推送地址别名origin）
```

#### 更新本地指定分支
你需要先切换到本地指定分支，然后使用`git pull origin <origin_branch_name>` 将远程分支合并到当前分支

#### 拉取指定分支
```
1. 重新clone仓库并指定分支
git clone -b <branch_name> <remote_url> (会自动建立跟踪关系)
2. 拉取远程所有分支
git fetch (注意：这条命令需要你已经clone了远程主分支，即默认分支)
3. 创建新分支，并更新 (如果使用git branch <branch_name>创建分支，你需要注意一下git追踪关系)
git checkout -b <local_branch_name> <remote_url>/<remote_branch_name>
git pull <远程仓库别名（默认origin）> <指定分支名>
```

### git tag
tag标签是一个特殊类型的分支，用于标记特定版本的项目快照。它们是不可变的，表示在特定时刻的项目状态。每个标签都有一个标识符，通常是一个版本号，如v1.0

既然tag是一个不可变的分支，那么你可以像操作分支一样操作tag，如
- 查看标签信息 `git show <tag_name>`
- 切换到标签对应的版本 `git checkout <tag_name>`
- 将tag推送到远程服务器 `git push origin <tag_name>` 

**注意** 使用 `git tag -h` 查看帮助信息

#### tag创建
1. 通过当前分支创建 `git tag <new_tag> [commit-hash,默认指向当前Head] [-m "message"]`
**注意** 标签名不要和branch分支重名
2. 通过指定分支的commit ID来创建标签`git tag my-tag <commit_id>`

### git冲突示例

#### 解决pull冲突
pull冲突一般是由于团队合作中，有人更改了远程文件（同时你本地也修改了同一个文件的同一行）
1. 你可以保存到本地仓库中（`git add <change_file>; git commit`），然后拉取远程文件（git pull），并在git版本管理帮助下合并文件
2. 你也可以使用 `git stash`将本地修改暂存（让git版本管理忽视你所更改的文件），并之后处理
3. 也可以使用`git checkout -b <new_branch_name> <old_branch_name>`根据旧分支创建一个新分支，用于避免合并出错。
> 在新分支中将本地变化commit提交到本地仓库，之后切换到旧分支并合并远程分支。如果没报错的话，你就可以使用`git merge <temp_new_branch> <old_branch>`来将临时新分支（存储之前本地更改）合并到旧分支（最新的远程分支拉取到本地的分支）中


### 子模块

#### git子模块submodule
子模块允许你将一个 Git 仓库作为另一个 Git 仓库的子目录。 它能让你将另一个仓库克隆到自己的项目中，同时还保持提交的独立。(与直接新建目录，并将新目录添加到.gitignore相比，可以分别远程管理子模块内容)

**子模块相关操作**
```
git submodule [--quiet] [--cached]
git submodule [--quiet] add [<options>] [--] <repository> [<path>]
git submodule [--quiet] status [--cached] [--recursive] [--] [<path>…]
git submodule [--quiet] init [--] [<path>…]
git submodule [--quiet] deinit [-f|--force] (--all|[--] <path>…)
git submodule [--quiet] update [<options>] [--] [<path>…]
git submodule [--quiet] set-branch [<options>] [--] <path>
git submodule [--quiet] set-url [--] <path> <newurl>
git submodule [--quiet] summary [<options>] [--] [<path>…]
git submodule [--quiet] foreach [--recursive] <command>
git submodule [--quiet] sync [--recursive] [--] [<path>…]
git submodule [--quiet] absorbgitdirs [--] [<path>…]

不带参数，显示现有子模块的状态。有几个子命令可用于对子模块执行操作。
```
1. 子模块添加
`git submodule add <submodule_url> <dir_name>`

> 如果你是旧版 Git 的话，你会发现 子模块目录中是空的，你还需要在执行一步「更新子模块」，才可以把远程仓库项目中的内容下载下来。`git submodule update --init --recursive`

**添加子模块后，会在当前目录下创建子模块目录并且在仓库主目录下会新建 .gitmodules 文件**

## git 示例

### git合并本地仓库

1. 创建一个最后保留的仓库(`git init` 或 `git clone`)
2. 通过 `git remote add loacl_wh <局部路径>` 添加一个其他分支
3. 使用 `git pull local_wh master` 拉取另一个本地仓库的master分支内容
4. 使用 `git checkout -b <分支名>` 切换或创建一个保留的最终分支
5. 使用 `git merge local_wh/master` 合并另一个本地仓库的master分支到当前分支