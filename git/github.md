## 说明
记录github网站的各种使用笔记

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