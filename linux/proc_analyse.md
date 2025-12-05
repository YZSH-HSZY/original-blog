# 介绍
此文件存放进行程序分析的零散笔记

## strace
strace 用于跟踪系统调用和信号

> Options:
```sh

```

> Example:
- `strace -fe write -p 1026` 追踪指定pid进程的write系统调用
- `strace -f -e open,execve wget http://www.baidu.com` 执行指定程序并跟踪 `open/execve` 系统调用
- `strace -e openat,mmap nvidia-smi 2>&1 | grep -i nvidia` 查看动态加载的nvidia库

## process net socket analyse

- 查看所有为socket的fd `ll /proc/<pid>/fd | grep "sock"`
- 查看指定进程使用的udp socket fd `ss -u -a -6  -p | grep <pid>` 
- 使用strace追踪socket的创建 `strace -fe socket <program-file>`

## socket调试

### nc命令

[参nc笔记](../net/debug/nc_ncat.md)

`ncat -l 8888`
`nc localhost 8888`

## 内存分析

- 使用strace追踪内存分配系统调用
> 主要内存相关系统调用解释：
> * `brk/sbrk` - 调整程序的数据段大小（传统的内存分配方式）
> * `mmap/munmap` - 内存映射/取消映射（现代内存分配主要方式）
> * `mprotect` - 更改内存区域的保护属性
> * `shmat/shmdt` - 共享内存的附加/分离

**注意** `brk` 分配的内存只能由`brk`收缩或者进程结束时系统回收;`munmap` 只释放通过 `mmap` 分配的内存
**注意** 即使程序内部调用了 free(), glibc 的内存管理器也可能选择保留这些内存(通过 brk 分配的堆空间)