# cling

cling 基于 LLVM 和 clang 的交互式 C++ 解释器(Read-evaluate-print loop)

> 参考文档:
> - [cling仓库](https://github.com/root-project/cling.git)

## USAGE

### 安装

- 从conda安装 `conda install conda-forge::cling`
- 使用docket环境 `docker pull compilerresearch/cling`

### 命令选项


### 内置命令

- `.help`: 查看信息帮助
- `.(I|include) [path]`: 显示所有include路径/添加路径到include中
- `.L <filename>`: 加载文件/库
- `.q`: 退出解释器
