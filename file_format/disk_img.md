# 磁盘镜像文件

磁盘镜像文件能够完整地存储一个磁盘的内容和结构, 不仅适用于 CD 或 DVD, 还可以用于各种存储设备, 包括磁带驱动器/硬盘/固态硬盘/U 盘, 甚至软盘都可以转化成磁盘镜像文件. 可用于备份/操作系统分发/虚拟化和存档等

常见的磁盘镜像文件有 ISO、BIN/CUE 和 IMG 等

IMG(Hierarchal File Format, 分级文件格式)是一种文件压缩格式(archive format), `.IMG`这个文件格式可视为`.ISO`格式的一种超集合 用于:
- 创建软盘的镜像文件(disk image)
- 压缩整个软盘(通常指软盘，Floppy Disk或Diskette)或整片光盘的内容   


## 各种磁盘镜像文件格式比较

|特征               |ISO 格式	                    |BIN/CUE 格式	       |IMG 格式      |
|------------------|-------------------------------|----------------------|-------------|
|扇区大小	        |2048 字节	                    |4096 字节	           |512 字节      |
|原生操作系统支持	 |是(Windows、Linux 和 macOS)	 |是	                |是            |
|限制	            |不支持复制保护	                 |无	                |不支持复制保护 |
|最佳用途	        |备份无复制保护的光盘		      |                      |             |
|分发程序和操作系统	 |备份或复制带有复制保护的光盘	    |备份或刻录光盘	        |             |