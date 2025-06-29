# git

## git 帮助信息
短选项-h会在命令行中输出帮助信息，长选项--help会在浏览器查看本地html帮助文档

## worktree介绍
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

## git-mintty-msys相关命令及示例

### git的msys搭建pacman包管理器

[参msys使用git-bash](./msys.md#git的msys搭建pacman包管理器)

### git在局域网中同步
git-bash 内置了 `sshd` 工具，可以开启sshd服务让其他可访问的主机将本地仓库当做远程，以进行代码同步

#### 在 git-bash 下开启sshd服务

1. sshd开启需要posix环境，git-bash内置了msys2环境，请在其下运行命令
2. 配置sshd认证的密钥
- 进入ssh配置目录 `cd /etc/ssh/`
- 查看sshd_config文件发现主机密钥有三类
```sh
#HostKey /etc/ssh/ssh_host_rsa_key
#HostKey /etc/ssh/ssh_host_ecdsa_key
#HostKey /etc/ssh/ssh_host_ed25519_key
```
- 使用ssh-keygen生成一个rsa密钥，`ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key`
- 通过sshd命令的全路径开启服务 `/usr/bin/sshd`

**注意** 更新sshd_config文件后，通过 ps -ef 查找sshd，kill杀死，在重新运行sshd更新
**注意** 主机密钥用于防止中间人攻击,和参与通信AES加密的密钥交换; 之后登录需用户密钥用以验证用户身份

### 本地仓库同步步骤

1. 确保本机sshd服务开启
2. 使用 `git remote add origin ssh://<username>@<ip_address>/d/PaddleOCR/.git` 添加远程仓库用于测试
3. `git push origin master`，输入密码后，出现`Everything up-to-date`说明sshd远程仓库配置成功
4. 在其他局域网主机中使用 `git clone ssh://<username>@<ip_address>/d/PaddleOCR/.git` 拉取
5. 在其他局域网主机push变更，需要你的本地仓库(即其他主机的远程origin仓库)的HEAD分离提交分支(master)，你可以切换到`remotes/origin/master`或其他分支

**注意** 也可使用`file://`文件协议

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

## git config

命令格式：`usage: git config [<options>]`

**注意** options有四种类型，为 `{Config file location, Action, Type, Other}`

> Config file location指定读取git的config文件位置;
1. --system读取 git安装目录下etc/gitconfig 文件(针对所有用户生效)
2. --global读取 `%USERPROFILE%/.gitconfig` 文件(针对当前用户生效)
3. --local读取 仓库.git/config 文件(在仓库工作目录时,默认使用)
4. `-f <file>` 指定读取配置文件路径

### config常用的配置项

[参官方文档自定义配置](https://git-scm.com/book/zh/v2/%E8%87%AA%E5%AE%9A%E4%B9%89-Git-%E9%85%8D%E7%BD%AE-Git)

1. 配置git编辑器项 `core.editor`, 如 `git config --global core.editor [code|vi|nano]`
2. 配置git提交消息模板 `commit.template`, 如 `git config --global commit.template ~/.gitmessage.txt`
```txt
Subject line (try to keep under 50 characters)

Multi-line description of commit,
feel free to be detailed.

[Ticket: X]
```
3. 配置git拉取的证书验证 `http.sslverify`, 如 `git config --local http.sslverify [true|false]`

**注意** 提交消息可通过多个-m来支持多行提交或者直接使用 `git commit` 打开文本编辑器编辑消息
[参bolg](https://www.ruanyifeng.com/blog/2016/01/commit_message_change_log.html)
可借助 npm包 `Commitizen` 编写提交规范


### git config取消设置项
使用 `--unset` 取消config设置

### 查看所有配置项及其对应config文件位置
`git config -l --show-origin`

### 设置gpg-key文件位置
`git config --global user.signingKey <ssh_file_full_path>`

**注意** 需要同时将配置 `gpg.format` 设置为 "ssh" ,此时`user.signingKey`可以包含私有 ssh 密钥的路径，也可以包含使用 ssh-agent 时的公钥的路径。或者，它可以包含直接包含 以`key::`为前缀的公钥（例如："key::ssh-rsa XXXXXX identifier）。

### ssh key与gpg key区别
在我们使用gitee或github时，账户setting中存在add ssh keys和gpg keys选项，这两个key的作用场景不同，其中ssh主要用于远程登陆，而gpg主要用于安全传输。

**注意** 在你进行拉起仓库等需要权限的操作时，会进行身份验证，这时会使用ssh验证用户身份。如果你配置了gpg密匙，那么在数据传输时会使用其进行加密。

### git设置代理
1. 配置全局代理
`git config --global https.proxy https://127.0.0.1:7890`
2. 为指定站点配置代理
`git config --global https.https://github.com.proxy https://127.0.0.1:7890`
3. 设置ssh代理, 需要在ssh的配置文件中使用
    - 根据git使用的ssh执行文件,配置ssh_config文件
    - 如果是window内置ssh,则为 `%userprofile%/.ssh/config` 文件
    - 如果是git内置ssh,则为 `%git_home%/etc/ssh/ssh_config` 文件

> 示例如下：
```sh
# linux/mac下
# 第一种 SOCKS5 协议
Host github.com
    User git
    ProxyCommand nc -X 5 -x 127.0.0.1:7891 %h %p
    
# 第二种
Host github.com
    User git
    ProxyCommand nc -x 127.0.0.1:7891 %h %p

# window下
# HTTP代理
Host github.com
    User git
    ProxyCommand connect -H 127.0.0.1:7890 %h %p
    
# SOCKS5代理
Host github.com
    User git
    ProxyCommand connect -S 127.0.0.1:7891 %h %p
```

## git log命令

`git log [path...]` 接收path参数时将显示于此路径相关的提交

```sh
OPTIONS:
    --pretty[=<format>], --format=<format>
    --reverse
        倒叙形式展示提交日志

PRETTY FORMATS:
    - oneline: <hash> <title-line>
    - short: 
        commit <hash>
        Author: <author>
        <title-line>
    - medium: 
        commit <hash>
        Author: <author>
        Date:   <author-date>
        <title-line>
        <full-commit-message>
    - full
    - fuller
    - reference
    - email
    - mboxrd
    - raw
    - format:<format-string>
        %H(commit hash)/%h(abbreviated commit hash)/%T(tree hash)/%an(author name)/%ae(author email)/%ad(author date)/%as(author date, short format (YYYY-MM-DD))/%cn(commit name)/%cs(committer date, YYYY-MM-DD)/%s(subject)

```
> 示例:
    * 单行显示 `short_commit_id,commit_name,commit_date,description`: `git log --format="%h,%cn,%cs,%s"`
    * 倒叙显示日系 `git log --oneline --reverse `

### git log 使用示例

- 查看指定文件相关的commit记录 `git log --follow filename`
    > 选项`--follow`: 继续列出除重命名之外的文件历史记录(仅适用于单个文件)
- 显示指定文件每次提交的diff(区别) `git log -p filename`
- 查看某次提交中的某个文件变化 `git show comit_id filename`
- 查看某次提交 `git show commit_id`
- 以图形化界面的方式显示修改列表 `gitk --follow filename`


## git撤销/恢复内容(包括commit/HEAD/worktree)

### 撤销commit

#### git reset
`git reset` 用于将当前HEAD重置为指定状态，HEAD之后的commit节点会丢弃
**注意** reset只用于本地仓库、缓存和工作区，对于远程仓库需使用`--force`强制更改

#### git revert
`git revert <old_commit_id>` 会生成一个新的 commit，将指定的 old commit 修改内容从当前分支上覆盖掉
**注意** 原始修改old_commit对于log节点会保留，因此重新推送的话，该部分会进行比较

### 对于`git commit --amend`附加的提交进行恢复
1. 使用`git reflog`查看回滚记录
2. `git reset --mixed <commit-id>` 恢复HEAD及index, 之后重新添加文件并提交

### 单文件worktree恢复

- 将未提交暂存区的文件恢复 `git restore --source <commit_id> -- <recoverfile>`
- 将未提交暂存区的文件恢复 `git checkout -- <recoverfile>`

## git 多分支合并

#### git merge
<!-- TODO -->

#### git rebase
`git rebase <upstream-branch-name> <to-branch-name>` 用于在另一个分支上重新提交

> git rebase时其工作流程
1. 切换到to-branch分支；
2. 将to-branch中比upstream-branch多的commit先撤销掉，并将这些commit放在一块临时存储区（.git/rebase）；
3. 将upstream-branch中比to-branch多的commit应用到to-branch上，此刻to-branch和upstream-branch的代码状态一致；
4. 将存放的临时存储区的commit重新应用到to-branch上；

### git冲突示例

#### 解决pull冲突
pull冲突一般是由于团队合作中，有人更改了远程文件（同时你本地也修改了同一个文件的同一行）
1. 你可以保存到本地仓库中（`git add <change_file>; git commit`），然后拉取远程文件（git pull），并在git版本管理帮助下合并文件
2. 你也可以使用 `git stash`将本地修改暂存（让git版本管理忽视你所更改的文件），并之后处理
3. 也可以使用`git checkout -b <new_branch_name> <old_branch_name>`根据旧分支创建一个新分支，用于避免合并出错。
> 在新分支中将本地变化commit提交到本地仓库，之后切换到旧分支并合并远程分支。如果没报错的话，你就可以使用`git merge <temp_new_branch> <old_branch>`来将临时新分支（存储之前本地更改）合并到旧分支（最新的远程分支拉取到本地的分支）中


## git清理

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


## git branch

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
**注意** 未被git管理的文件在切换分支时不会更改，（如在差异记录里新添加到.gitignore的文件）

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

## git tag

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

#### tag查看创建时间信息

1. `git show <tag_name>`
2. `git log --tags --simplify-by-decoration --pretty="format:%d %ci" --no-walk`

#### tag和branch重名

当tag和branch重名时，对于git的一些操作会造成歧义，这时git仅会报warn仍执行默认指向，**请避免这种情况发生**
> 对于已经存在的重名，引用时提供`refs/tags/<tag_name>` / `refs/heads/<branch_name>` 区分

#### 远程tag
- 推送指定分支到远程 `git push <remote_name> {tag_name}`
- 推送所有本地分支到远程 `git push <remote_name> --tags`
- 查看远程tags `git ls-remote --tags <remote_name>`
- 删除本地tag之后，移除远程tag `git push origin :refs/tags/<tag_name>`

### git update-index
`git update-index` 用于将工作树中的文件内容注册到索引

```
Options:
    --[no-]skip-worktree 当指定时, 路径记录的对象名称不会更新。该选项设置和取消设置路径的"skip-worktree"位。此时git不会监听该文件
    --[no-]assume-unchanged 此标志位被设置时, 用户承诺不会更改, 此时ggit也不会跟踪此文件。

```
**注意** `skip-worktree`/`assume-unchanged` 的区别在于前者 `pull` 时，如果远程文件发生与你的取消监听文件有冲突，git 会以远程文件为最新覆盖掉旧的，这样原先的取消监听文件将会失效。后者 在 `pull` 时，git 会尽力维护你的取消监听文件，确保它们不会被给覆盖掉，并提示冲突了。

**注意** 通过如下指令查看设置`skip-worktree`/`assume-unchanged`标志位的文件
```sh
- window
git ls-files -v | findstr /B h 			列出 assume-unchanged
git ls-files -v | findstr /B S  		列出 skip-worktree
linux环境
git ls-files -v|grep "^h"
git ls-files -v|grep "^S"
```

## git reflog

查看分支的操作记录, 包括HEAD被重置的情况

> reflog的历史操作存储在本地,不会参与远程同步

## submodule/subtree管理子仓库

> 区别:
1. 空间占用
   - subtree 属于拷贝子仓库, 而 submodule 属于引用子仓库
   - subtree 在初始化 add 时, 会将子仓库 copy 到父仓库中, 并产生至少一次 merge 记录
   - submodule 在初始化 add 时, 会在父仓库新建一个 .gitmodules 文件, 用于保存子仓库的 commit hash 引用
2. clone
    - subtree: subtree add 至父仓库之后, 后续的 clone 操作与单一仓库操作相同
    - submodule: 后续 clone 时 submodule 还需要 init/update 操作
3. commit
    - subtree: 父仓库直接提交父子仓库目录里的变动。若修改了子仓库的文件，则需要执行 subtree push
    - submodule: 父子仓库的变动需要单独分别提交。且注意先提交子仓库再提交父仓库

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

2. 子模块移除 `git submodule deinit <submodule_name>`
3. 更新子模块url `git submodule set-url <submodule_name> <new_url>` 

**注意** git submodule移除后，需同时通过 `git rm --cache <submodule_path>` 更新git缓存, 避免git submodule查看信息问题

#### git subtree

> 示例:
- `git subtree add --prefix=3rdparty/openssl https://github.com/openssl/openssl.git master`

##### 将subtree添加的多个commit合并为一个commit
1. `git reset --soft <except-save-commitid>`将HEAD指向想要保留的最近commit,之后`git commit` 提交最近几次的修改


## git 示例

### git合并本地仓库

1. 创建一个最后保留的仓库(`git init` 或 `git clone`)
2. 通过 `git remote add loacl_wh <局部路径>` 添加一个其他分支
3. 使用 `git pull local_wh master` 拉取另一个本地仓库的master分支内容
4. 使用 `git checkout -b <分支名>` 切换或创建一个保留的最终分支
5. 使用 `git merge local_wh/master` 合并另一个本地仓库的master分支到当前分支

### git合并不同分支指定文件
1. 对于简易添加或覆盖的场景,可以直接使用 `git checkout <target_branch> -- <file>...` 合并指定分支的指定文件
2. 对于合并文件在两分支中均有差异的现象,可以使用 `git checkout -p <target_branch> -- <file>...` 来交互式选择合并块
3. 也可以借助临时分支，完成两分支的合并后，在通过第一步的覆盖合并完成

### git查看指定分支的文件
`git show {commit_id/tag_name/branch_name}:<file_path>`

### fork时同步上游仓库的问题
fork一个官方仓库到自己的用户目录下进行学习或开发时，经常需要同步官方仓库上的其他更改，可通过以下方式解决:
- 以cpython为例:
```sh
git remote add upstream https://github.com/python/cpython  # 添加一个上游仓库
git config --local branch.main.remote upstream  # git配置. 设置默认的拉取和推送的远程分支名;形如branch.<branch_name>.remote
git remote set-url --push upstream git@github.com:<your-username>/cpython.git  # 更改上游upstream的默认推送为自己的仓库
```

### git clone拉取非标准ssh port端口
`git clone ssh://smartwork@192.168.8.14:2222/home/smartwork/work/icon_data`

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

**注意** 在浅层克隆后(即depth 1), 拉取远程仓库其他分支或tag,使用 `git config remote.origin.fetch "+refs/heads/*:refs/remotes/origin/*"` 移除浅层限制

### git查看仓库大小

`git count-objects -vH`
只统计添加到仓库的文件的大小，不包含.gitignore忽略的文件