# 介绍

linux下使用rm误删除文件的恢复笔记

> 参考文档
- [linux恢复工具介绍](https://cn.linux-console.net/?p=5851)

## 相关工具

- lsof(`apt install lsof`)
- testdist/photorec(`apt install testdisk`)
- extundelete(`apt install extundelete`)

## example

1. 对应删除之后,操作删除的进程未结束并且对应句柄未释放的情况,可以使用`lsof`
> - `lsof | grep "delete" | grep <rm_file>`
2. 对于刚删除不久的文件或目录, 可以尝试使用`extundelete`回复
> - `sudo extundelete /dev/nvme0n1p2 --restore-directory /home/user/plppp`(扫描设备`/dev/nvme0n1p2`, 将`/home/user/plppp`目录回复至当前`RECOVERED_FILES/`目录下)
3. 以上几种均无法回复,可以尝试使用全盘扫描等工具进行文件, 如`photorec`
> - `sudo photorec /d output /dev/nvme0n1p2`(扫描设备`/dev/nvme0n1p2`, 在进行一些选项设置后, 将扫描的数据存储到`output.{idx}`目录下, 每个目录最大500个)

## 相关命令使用

### photorec

```sh
Usage: photorec [/log] [/debug] [/d recup_dir] [file.dd|file.e01|device]
       photorec /version

/log          : create a photorec.log file
/debug        : add debug information
```

**注意** photorec的恢复目录和设备不能是同一个文件系统,否则可能会发生错误