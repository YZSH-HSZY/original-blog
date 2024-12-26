### conda
conda是一个多语言的环境管理工具，对不同的项目可以配置不同环境，避免冲突。

[北京外国语大学开源镜像](https://mirrors.bfsu.edu.cn/anaconda/archive/)


[北京外国语大学开源镜像](https://mirrors.bfsu.edu.cn/anaconda/archive/)

[conda包搜索](https://anaconda.org/conda-forge)

#### miniconda安装

[hash及下载文件名](https://docs.anaconda.com/miniconda/miniconda-hashes/)
[wget下载安装命令](https://docs.anaconda.com/miniconda/#miniconda-latest-installer-links)

#### conda的channel
- `conda-forge` 是一个社区项目和 GitHub 组织，包含 conda 软件的存储库，提供了各种软件的 conda 包。构建的分发版上传到 `anaconda.org/conda-forge`，并可以通过 conda 进行安装。

#### conda使用

##### conda环境操作
1. 创建环境
`conda create -n <env_name> python=<python_version>`

2. 切换环境
```
window: activate <env_name>
linux: source activate <env_name>
```

3. 复制环境
`conda create -n <new_env_name> --clone <old_env_name>`

4. 导入和导出环境
```
conda env export > <env_name.yaml>  # 导出环境
conda env create -f <env_name.yaml>  # 导入环境
```
5. conda环境打包并离线安装
  > pip或conda安装`conda-pack`，使用`conda-pack -n <env_name>`打包环境

##### conda安装包

1. 离线安装conda包 `conda install --use-local <.conda_file>`
2. 从指定channel中安装conda包 `conda install `


**注意** conda安装时查找索引solving environment很慢，可以预先安装 `conda install mamba -n base -c conda-forge` 实现并行运算

##### conda配置虚拟环境中的环境变量

- 查看环境中所有变量 `conda env config vars list [-n <env_name>]`
- 设置环境变量 `conda env config vars set <var_name>=<value> [-n <env_name>]`;注意：需要重新激活环境使更改生效。
- 删除环境变量 `conda env config vars unset <var_name> [-n <env_name>]`

**注意** 设置的环境变量可以在 `miniconda\envs\qgis\conda-meta\state` 文件中查看


##### conda安装损坏的包
`conda install -f pip`

##### conda终端自动激活
```sh
conda config --set auto_activate_base true       ## 启动终端自动激活
conda config --show     ## 显示编译后的所有配置值
conda info --envs       ## 查看环境激活状态
```

##### conda历史记录
1. 查看环境安装历史记录
`conda list --revision`
2. conda回滚操作
`conda install --revision N`，N这里是指更改历史的序号


#### conda镜像配置

##### 镜像源

**conda镜像的源配置维护较少，可能会有许多报错，你可以使用pip来安装，仅用conda管理python版本**
添加清华镜像
```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --append channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/fastai/
conda config --append channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
conda config --append channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/
 

conda config --set show_channel_urls yes
```

##### conda直接修改.condarc
1. Windows 用户无法直接创建名为 .condarc 的文件，可先执行 `conda config --set show_channel_urls yes` 生成该文件之后再修改。
```
# 在使用conda install <packages_name>报错时，如果显示搜索包失败，可以更换镜像站
PackagesNotFoundError: The following packages are not available from current channels:
```
TUNA 还提供了 Anaconda 仓库与第三方源（conda-forge、msys2、pytorch等，查看完整列表）的镜像，各系统都可以通过修改用户目录下的 .condarc 文件:

channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
ssl_verify: true

2. 注意如果需要pytorch, 还需要添加pytorch的镜像：

conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
3. 如果需要换回conda的默认源，直接删除channels即可，命令如下：

conda config --remove-key channels

##### .condarc示例

```yaml
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
```

#### conda配置node
需要配置conda的镜像源，最好是私建的镜像源。
`conda install -c conda-forge nodejs`这会在默认base环境中添加node包。
你也可以使用`conda create -yn <env_name> nodejs`来创建一个node新环境。

#### conda bug合集

##### 使用conda时，pip install可能会与环境冲突，推荐使用conda install安装包
canda虚拟环境中pyinstaller打包报错，与pathlib包冲突。请使用conda install命令安装pyinstaller包


### spyder
一款仿matlab的python编辑器
**中文设置**
在tools/preferences/application中选择简体中文
