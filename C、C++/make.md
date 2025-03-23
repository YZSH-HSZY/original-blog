# make

make 程序会自动确定大型程序的哪些部分需要重新编译，并发出命令来重新编译它们。make通过makefile文件确定程序中文件之间的关系。

**注意** 使用make必须准备makefile文件

[gnu make 手册](https://www.gnu.org/software/make/manual/make.html)

## Kconfig

Kconfig 是 Linux 内核和 U-Boot 等开源项目中广泛使用的配置管理系统。它通过定义配置选项的层次结构和依赖关系，帮助开发者管理和生成配置文件(如 `.config`)。Kconfig 系统的主要特点是灵活、可扩展，并且支持交互式配置界面。

Kconfig 系统通过 Kconfig 文件和 defconfig 文件来定义和存储配置。

Kconfig 提供了多种交互式配置界面，方便开发者选择和修改配置选项，包括 `menuconfig`/`xconfig`/`nconfig`/`gconfig`

Kconfig 配置之后自动生成 `.config`(存储最终的配置项, 形如: `key=value`) 和 `autoconf.h`(包含配置选项的宏定义) 文件，用于编译和代码生成

### Kconfig文件

Kconfig 文件是一个文本文件，定义了配置选项的属性和关系。以下是一个简单的 Kconfig 文件示例

```
menu "Example Configuration"

config EXAMPLE_FEATURE
    bool "Enable Example Feature"
    default y
    help
      This is an example feature. Say Y to enable it.

config EXAMPLE_PARAMETER
    int "Example Parameter"
    default 100
    depends on EXAMPLE_FEATURE
    help
      This is an example parameter. Set its value here.

endmenu
```

> 字段说明
> - menu: 定义一个菜单
> - config: 定义一个配置选项
> - bool: 布尔类型选项（y/n）
> - int: 整数类型选项
> - default: 定义默认值
> - depends on: 定义依赖关系
> - help: 提供帮助信息

### 示例
- `make oldconfig` 使用提供的.config作为基础更新当前配置
  
## make 选项
```sh
Options:
  -f file, --file=file, --makefile=FILE
    使用文件作为makefile
```
## make debug

> make用与调试的命令行选项:

```sh
Options:
  --just-print, -n
    打印将要执行的命令，但不执行它们(除非在某些情况下)

  --print-database, -p
    打印读取makefile产生的数据库(规则和变量值);然后按往常或其他指定的方式执行。要打印数据库而不尝试重制任何文件，请使用 make -p -f/dev/null
  
  --warn-undefined-variables
    当引用未定义的变量时发出警告

  --debug[=FLAGES]
    打印调试信息。省略FLAGS时行为与指定-d时相同
    FLAGS允许值: 
      a(all,所有调试输出,等同-d)
      b(basic,基本调试输出)
      v(verbose,详细的基本调试)
      i(implicit rules,显示隐式规则)
      j(jobs,显示命令调用的详细信息)
      m(remaking,在重制makefile时进行调试)
      n(disable,禁用之前的所有调试标志)
```

## 常用示例

### make命令行覆盖makefile中变量

> 使用`-e`选项 `make -e KERNELDIR=/usr/lib/modules/5.4.0-205-generic/build`

### 保存 Kconfig的 .config 文件以便下次使用

`make savedefconfig ` 保存当前配置为./defconfig(最小配置), 之后可以复制到 `arch/{target_arch}/configs/{name}_defconfig` 来在之后使用