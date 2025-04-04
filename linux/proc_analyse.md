# 介绍
此文件存放进行程序分析的零散笔记

## strace
strace 用于跟踪系统调用和信号

- `strace -fe write -p 1026` 追踪指定pid进程的write系统调用
- `strace -f -e open,execve wget http://www.baidu.com` 执行指定程序并跟踪 `open/execve` 系统调用

## process net socket analyse
查看所有为socket的fd `ll /proc/<pid>/fd | grep "sock"`
查看指定进程使用的udp socket fd `ss -u -a -6  -p | grep <pid>` 

## socket

`ncat -l 8888`
`nc localhost 8888`