### TUI文本用户界面
在os的引导界面中常常使用，不够如果你只想要在控制台简单的实现一个文本交互界面，可以使用print输出和cls清屏来模拟。
如果想像一个通用脚本，例下载或构建脚本那样，既能够以文本动画的形式展示也可以在保留历史命令输出的情况下，不断刷新界面，那么你需要了解一下VT控制台的功能，或者接触一下curses相关的库。

#### VT控制台
只用print的话，可以使用VT-100的控制指令来移动cursor。除了移动cursor，还可以干各种其他事情。在谷歌或bing国际版里搜索“ANSI Escape Codes”，“Virtual Terminal Sequences”，“VT100 escape codes”来学习使用方式，维基百科的说的比较详细。另外，在Windows里，需要执行一下os.system('')以开启VT-100模式。其实还有更科学但是更复杂的方式，可以搜索“Windows console enable vt100”之类。

比较复杂的方式，*nix里可以用ncurses，Windows里可以用Win32 Console API。

```
import time
import os

if __name__ == '__main__':
    os.system('')  # start VT-100 in windows console

    print('start:')

    for i in range(5):
        time.sleep(0.2)
        print('line {}'.format(i))

    print('\033[5A', end='')  # cursor up 5 lines
    print('\r', end='')  # cursor back to start
    print('\033[0J', end='')  # erase from cursor to end

    for i in range(5):
        time.sleep(0.2)
        print('new {}'.format(i))

    print('end')

```

VT100是一个终端类型定义,VT100控制码是用来在终端扩展显示的代码。比如果终端上任意坐标用不同的颜色显示字符。
所有的控制符是\033或\e打头（即 ESC 的 ASCII 码）用输出字符语句来输出。可以在命令行用 echo 命令，或者在 C 程序中用 printf 来输出 VT100 的控制字符。
```
\033[0m		// 关闭所有属性
\033[1m		// 设置为高亮
\033[4m		// 下划线
\033[5m		// 闪烁
\033[7m		// 反显
\033[8m		// 消隐
\033[nA		// 光标上移 n 行
\033[nB		// 光标下移 n 行
\033[nC		// 光标右移 n 行
\033[nD		// 光标左移 n 行
\033[y;xH	// 设置光标位置
\033[2J		// 清屏
\033[K		// 清除从光标到行尾的内容
\033[s		// 保存光标位置
\033[u		// 恢复光标位置
\033[?25l	// 隐藏光标
\033[?25h	// 显示光标

\033[30m – \033[37m 为设置前景色

30: 黑色
31: 红色
32: 绿色
33: 黄色
34: 蓝色
35: 紫色
36: 青色
37: 白色

\033[40m – \033[47m 为设置背景色

40: 黑色
41: 红色
42: 绿色
43: 黄色
44: 蓝色
45: 紫色
46: 青色
47: 白色
```

#### curses库

Curses 是一个能提供基于文本终端窗口功能的动态库，（跟随python默认安装）它可以: 
使用整个屏幕创建和管理一个窗口使用 8 种不同的彩色为程序提供鼠标支持使用键盘上的功能键 
Curses 可以在任何遵循 ANSI/POSIX 标准的 Unix/Linux 系统上运行。Windows 上也可以运行，不过需要额外安装 windows-curses 库： `pip install windows-curses `

[python官方的curses文档](https://docs.python.org/zh-cn/3.11/library/curses.html)

```
import curses 
myscreen = curses.initscr() 
myscreen.border(0)
myscreen.addstr(12, 25, "Python curses in action!")
myscreen.refresh()
myscreen.getch() 
curses.endwin() 
```
需要注意 addstr 前两个参数是字符坐标，不是像素坐标getch 会阻塞程序，直到等待键盘输入curses.endwin() 作用是退出窗口如果需要持续监听用户的交互，需要写个循环，并对 getch() 获得的输入进行判断 

Curses 非常轻巧，特别适合处理一下简单交互，代替复杂参数输入的程序，既优雅，有简单，而且 Curses 也是其他文字终端 UI 的基础。 
#### npyscreen库
Npyscreen也是一个用了编写文本终端的 Python 组件库，是**基于 Curses 构建的应用框架**。比起 Curses，Npyscreen 更接近 UI 式编程，通过组件的组合完成 UI 展示和交互，而且 Npyscreen 可以自适应屏幕变化。提供强大的功能，满足快速开发程序的要求，无论是简单的单页程序还是复杂的多页应用。

Npyscreen 提供了多个控件，比如 表单（Form）、单行文本输入框（TitleText）、日期控件（TitleDateCombo）、多行文本输入框（MultiLineEdit）、单选列表（TitleSelectOne）、进度条（TitleSlider）等多种控件。

引入 Npyscreen 模块，如果没有可以通过 pip 安装：`pip install npyscreen`


#### Urwid 库
如果说 Curses 和 Npysreen 是轻量级的文本终端 UI 框架，那么 Urwid 绝对称得上是重量级选手。 

Urwid 包含了众多开发文本 UI 的特性，例如： 
应用窗口自适应文本自动对齐轻松设置文本块强大的选择框控件可以和各种基于事件驱动的框架集成，比如和 Twisted, Glib, Tornado 等等提供诸如编辑框、按钮、多(单)选框 等多种预制控件显示模式支持原生、Curses模式、LCD 显示屏 以及 网络显示器支持 UTF-8 以及 CJK 字符集（可以显示中文）支持多种颜色 

Urwid 完全是按照面向对象的思想打造的框架： 
  
注意：Urwid 只能在 Linux 操作系统中运行，Windows 上会因为缺失必要组件无法运行 
  
 


NetEase-MusicBox  是基于 Curses 开发，如果运行起来，能被它的强悍所震撼，有空可以玩玩，比心！ 

Curses: https://docs.python.org/3/howto/curses.html 

俄罗斯方块游戏: https://github.com/cSquaerd/CursaTetra 

npyscreen: https://npyscreen.readthedocs.io/ 

vim: https://www.vim.org/ 

Urwid: https://urwid.org/index.html 

Twisted: https://www.twistedmatrix.com/trac/ 

Glib: https://docs.gtk.org/glib/ 

Tornado: https://www.tornadoweb.org/en/stable/ 

命令行网易云音乐 : https://github.com/darknessomi/musicbox 

