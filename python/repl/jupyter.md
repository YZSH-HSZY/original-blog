# jupyter
Jupyter 是一个大型的综合项目，包含Jupyter Notebook , JupyterLab，Jupyter Console等

> jupyter notebook
jupyter notebook是一个笔记本编写应用程序，支持多种语言的笔记(由内核决定，默认为ipython内核，支持python)，

> jupyter lab是什么
jupyter notebook的增强版，在同一浏览器标签界面使用内置头标签打开多个窗口和文件导航窗口等（修复jupyter notebook打汉字拼音不可见bug）

[jupyter官方文档](https://docs.jupyter.org/en/latest/)

[jupyter notebook使用教程](https://jupyter-notebook.readthedocs.io/en/latest/notebook.html#notebook-user-interface)

## jupyter系列相关配置

### jupyter中文设置
在环境变量中添加LANG项，值为zh_CN.UTF8

### jupyter notebook工作目录设置
使用`jupyter notebook --generate-config`查看配置文件路径

### jupyter快捷方式打开默认bug
去除%USERPROFILE%和%HOMEPATH%参数

### vscode的jupyter交互魔法%+命令时输出乱码

使用 `!chcp 65001` 更改内置shell编码

**注意** !和%的区别, %是交互支持的魔法命令(包括一些常用的shell命令).而!在shell情况下执行(支持所有shell命令)

#### jupyter lab汉化
[pypi的jupyterlab汉语包](https://pypi.org/project/jupyterlab-language-pack-zh-CN/)

## jupyter notebook魔法命令

支持的魔法命令有两种, `line magic(%<cmd>)` / `cell magic(%%<cmd>)`

> 示例:
- 将当前单元格写入文件 `%%writefile [-a] example.py`
- 运行脚本文件 `%run example.py`
- 加载文件到当前单元格 `%load example.py`
- 查看当前目录 `%pwd`
- 变更当前目录 `%cd <dir_path>`
- 查看当前变量 `%whos`
- 清除变量 `%reset`
- 计算执行时间 `%%time`

[ipython内建魔法命令](https://ipython.readthedocs.io/en/stable/interactive/magics.html)

## jupyter notebook快捷键

> jupyter有三种类型的cell
1. code cell，命令模式下按 `Y` 进入
2. markdown cell，命令模式下按 `M` 进入
3. raw cell

> jupyter有两种模式
1. 编辑模式， 按 `Enter` 进入。此模式用于编辑cell。
2. 命令模式， 按 `Esc` 进入。此模式支持操作cell自身

### 命令模式下快捷键
- `Y` 变换cell为Code类型
- `M` 变换cell为Markdown类型
- `A` 在上方添加cell
- `B` 在下方添加cell
- `D + D` 删除当前cell
- `Z` 回退上一步操作
- `L` 显示行号

**注意** 如果无效，请检查大写锁定 `CapsLock` 有无打开

## 使用示例
### jupyter命令启动
直接在anaconda prompt使用`jupyter notebook`命令打开jupyter

### jupyter查看python函数帮助信息
1. 使用shift+tab
2. 在函数名后接？号

### jupyter恢复误删单元格或者历史代码

1. 进入命令模式（左侧为蓝色，右上无🖊标记），按z撤销
2. 使用%history查看历史代码

###  ipynb转makedown格式

1. 需 `nbconvert pandas`包
2. 执行命令`jupyter nbconvert --to {FORMAT} <ipynb_file>`
> FORMAT包含以下几种格式:
> asciidoc, custom, html, latex, markdown, notebook, pdf, python, rst, script, slides, webpdf

