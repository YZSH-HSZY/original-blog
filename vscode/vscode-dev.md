# vscode开发容器

vscode使用 `.devcontainer/devcontainer.json` 以及 可选的 Dockfile或docker-compose.yml文件创建开发容器

[vscode Dev Containers官方文档](https://code.visualstudio.com/docs/devcontainers/tutorial)

## devcontainer.json 文件格式

```json
//devcontainer.json
{
  "name": "Node.js",

  // Or use a Dockerfile or Docker Compose file. More info: https://containers.dev/guide/dockerfile
  "image": "mcr.microsoft.com/devcontainers/javascript-node:0-18",  // (Docker Hub、GitHub Container Registry、Azure Container Registry)中的镜像名

  //"dockerfile": "",  // 使用dockerfile文件替代镜像(相对路径)

  // Features to add to the dev container. More info: https://containers.dev/features.
  // "features": {},

  // 配置工具特定的属性，比如 VS Code 的 settings 和 extensions 
  "customizations": {
    "vscode": {
      "settings": {},
      "extensions": ["streetsidesoftware.code-spell-checker"]
    }
  },

  // "settings": "" // 添加默认的settings.json值到容器的settings文件

  // "extensions": []  //指定应在创建容器时安装的扩展 ID 数组

  // "forwardPorts": [3000],  // 将容器内的端口列表映射到本地

  // 设置特定转发端口的默认属性
  "portsAttributes": {
    "3000": {
      "label": "Hello Remote World",
      "onAutoForward": "notify"
    }
  },

  "postCreateCommand": "yarn install"  // 在容器创建后运行的命令字符串或命令参数列表

  // "remoteUser": "root"  // 在容器中（包括子进程）以用户身份运行 VS Code。默认为 containerUser 
}
```

## 创建开发容器

### vscode通过 `devcontainer.json` 创建开发容器

1. 将需要放入dev contain中的项目单独用vscode打开
2. 在根目录下创建 `.devcontainer.json` 或者 `.devcontainer/devcontainer.json` 文件
3. 配置 devcontainer.json 的内容
4. vscode 运行命令 `remote-containers.reopenInContainer`
5. 等待构建完成

## bug

### x86机器上通过 qemu-user-static 运行arm容器时,vscode 开发容器连接报库`libatomic.so.1`错误
> 进入arm容器，手动安装`apt install libatomic1`