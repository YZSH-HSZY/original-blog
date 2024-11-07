# tasks任务
vscode支持用户提供tasks.json文件创建自定义的自动任务。
[官方文档](https://code.visualstudio.com/Docs/editor/tasks)

## 自定义任务

### 支持的属性
- `label`: 用户界面中使用的任务标签。
- `type`: 任务的类型。对于自定义任务，这可以是 shell 或 process 。如果指定了 shell ，命令被解释为一个 shell 命令（例如：bash、cmd 或 PowerShell）。如果指定了 process ，命令被解释为要执行的一个进程。
- `command`: 要执行的实际命令。
- `windows`: 任何与 Windows 特定的属性。当命令在 Windows 操作系统上执行时，将使用这些属性代替默认属性。
- `group`: 定义任务属于哪个组。在示例中，它属于 test 组。属于测试组的任务可以通过从命令调色板运行运行测试任务来执行。
- `presentation`: 定义了用户界面中任务输出的处理方式。在这个示例中，集成终端显示输出的 always 被揭示，并在每次任务运行时创建一个 new 终端。
- `options`: 覆盖默认设置， cwd （当前工作目录）， env （环境变量），或 shell （默认 shell）。选项可以在任务级别设置，也可以全局设置或按平台设置。在这里配置的环境变量只能在您的任务脚本或进程中引用，如果它们是参数、命令或其他任务属性的一部分，则不会被解析。
- `runOptions`: 定义任务何时以及如何运行。
- `hide`: 隐藏任务在运行任务快速选择中，这对于复合任务中不可独立运行的元素很有用。

## 示例

```json
{
  // See https://go.microsoft.com/fwlink/?LinkId=733558
  // for the documentation about the tasks.json format
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Run tests",  // 用户界面中使用的任务标签
      "type": "shell",  // 任务的类型。对于自定义任务，[shell | process]
      "command": "./scripts/test.sh",
      "windows": {
        "command": ".\\scripts\\test.cmd"
      },  // 命令在 Windows 操作系统上执行时，将使用这些属性代替默认属性。
      "group": "test",
      "presentation": {
        "reveal": "always",  // 保持显示，可选[never | always]
        "panel": "new"  // 控制是否在任务间共享面板
      }
    }
  ]
}
```
