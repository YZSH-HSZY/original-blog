# docker for window desktop

**注意**
> 4.30.0版本中, wsl2的docker-desktop-data已被移除(迁移至`\\wsl.localhost\docker-desktop\mnt\docker-desktop-disk`)


## 相关路径

- `%USERPROFILE%\AppData\Local\Docker\wsl`: dockers的容器存储位置

## exmaple

- `docker version` 查看个组件版本(client/engine/desktop)
- `docker info --format '{{.OSType}}'` 查看docker当前使用的容器类型

### switch to window container

在右下任务栏的docker图标中右键-->选择`switch to window container`