# node debug
此部分介绍node调试笔记

## vscode + nodejs debug
> 使用 vscode 自带的nodejs调试器调试js文件, 流程如下:
1. 创建 `launch.json` 文件, nodejs调试器vscode自带, 无需插件下载
2. 编写配置文件, 一个configurations示例如下:
```json
{
    "type": "node",
    "request": "launch",
    "name": "debug_ct_server",
    "skipFiles": [
        // "<node_internals>/**"
    ],
    "program": "/CT/OneNetCT/server/index.js",
    "cwd": "/CT/OneNetCT/server",
    "console": "integratedTerminal"
}
```

## node inspect(cli debug)

使用node提供的检查器进行命令行调试

### 调试命令

#### 断点

- `setBreakpoint('<file-path>', <line-number>)`/`sb('index.js', 10)` 在指定文件和行号设置断点
- `breakpoints` 查看已设置断点
- 在js文件中添加代码 `debugger;` 设置动态执行断点

#### 堆栈

- `backtrace` 查看当前堆栈

#### example

- 查看当前作用域的变量
> 在调试器暂停时, `exec console.log('Current variables:', Object.keys(this));`

- 检查局部变量
> `exec console.log('arguments:', arguments);  // 查看函数参数`
> `exec console.log('opts:', typeof opts);     // 检查 opts 是否存在`