# vim/vi
vim是vi的扩展版，一款文本编辑器

## vim模式

### 一般模式（命令模式）

### 编辑模式
### 底线命令模式

## vim配置
vim的配置文件有 `/etc/vim/vimrc`/`~/.vimrc`

### 常用vim配置

- 设置tap为4个空格 `set tabstop=4`(设置缩进宽度)
- 使用空格代替缩进 `set expandtab`
- 自动缩进 `set autoindent`
- 显示行号 `set number`
- 显示列 `set ruler`
- 显示相对行号(基于当前行) `set relativenumber`
- 取消显示行号 `set nonumber`
- 高亮当前行 `set cursorline`

## vim常用文本编辑命令
- `u` 撤销
- `ctrl+r` 重做（恢复）
- `d` 删除一个字符（后接删除方向）
- `dd` 删除本行
- `D` 删除至行尾
- `a` 在当前后一个字符编辑
- `i` 在当前字符编辑
- `v` 进入选择文本模式
- `V` 选中当前行并进入选择文本模式
- `w` 保存
- `w {another_file}` 另存为

## vim实用技巧

### vim宏录制

vim可以通过宏录制的方式进行大量重复操作, 如

- py中在行首添加注释
> 在一般模式下按 `q` + 任意寄存器如 `w` 进入录制模式, 操作 `j` --> `^` --> `i` --> `# ` --> `ESC` --> `q`结束录制.
> 之后通过 `num@w` 进行指定num次数的回放

### vim列编辑模式

- `Ctrl`+`v`/`Ctrl`+`q`,前者在linux下,后者在window下,进入列编辑模式
- 选择需要处理的行
- 按 `I` 在光标前插入, `A` 在光标后插入

### vim分屏
在底线命令模式下 `:sp {file_name}`/`:vsp {file_name}` 进入水平或垂直编辑

# test
## vim插件
