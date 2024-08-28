### tkinter
tkinter是python内置的gui模块（是一个"Tk 接口"，针对 Tcl/Tk GUI 工具包的标准 Python 接口），你可以使用tkinter来创建一个跨平台的gui应用程序。

[python官方文档-tkinter部分](https://www.tkdocs.com/shipman/)
[tkinter官方教程](https://tkdocs.com/tutorial/firstexample.html)

Tkinter 并不只是做了简单的封装，而是增加了相当多的代码逻辑，让使用体验更具 Python 风格（pythonic） 。

在命令行执行 python -m tkinter，应会弹出一个简单的 Tk 界面窗口， 表明 tkinter 包已安装完成，还会显示当前安装的 Tcl/Tk 版本，以便阅读对应版本的 Tcl/Tk 文档。

#### Tcl、Tk、Ttk关系

1. Tcl 是一种动态解释型编程语言，正如 Python 一样。尽管它可作为一种通用的编程语言单独使用，但最常见的用法还是**作为脚本引擎或 Tk 工具包的接口嵌入到 C 程序中**。Tcl 库有一个 C 接口，用于创建和管理一个或多个 Tcl 解释器实例，并在这些实例中运行 Tcl 命令和脚本，添加用 Tcl 或 C 语言实现的自定义命令。每个解释器都拥有一个事件队列，某些部件可向解释器发送事件交由其处理。与 Python 不同，Tcl 的执行模型是围绕协同多任务而设计的，Tkinter 协调了两者的差别（详见 Threading model ）。

2. Tk是一个用C实现的Tcl包，它添加了自定义命令来创建和操作GUI小部件。每个Tk对象都嵌入了自己的Tcl解释器实例，其中装入了Tk。Tk的小部件非常可定制，但代价是外观过时。Tk使用Tcl的事件队列来生成和处理GUI事件。

3. Ttk带有主题的 Tk（Ttk）是较新加入的 Tk 部件，相比很多经典的 Tk 部件，在各平台提供的界面更加美观。自 Tk 8.5 版本开始，Ttk 作为 Tk 的成员进行发布。Python 则捆绑在一个单独的模块中， tkinter.ttk。

#### 第一个例子
```
'''
从tkinter中导入所有组件，ttk是一个现代化的tk组件
'''
from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass
        
# root构造一个最高层级的 Tk 部件，这通常是一个应用程序的主窗口，并为这个部件初始化 Tcl 解释器。 每个实例都有其各自所关联的 Tcl 解释器。
root = Tk()
root.title("Feet to Meters")

# 接下来，我们创建一个框架容器（frame widget），它将保存用户界面的内容。
mainframe = ttk.Frame(root, padding="3 3 12 12")
# 创建框架后，将其直接放置在我们的主应用程序窗口中。将小部件放置在网格中的父小部件中
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# minsize (列/行的最小大小),weight (有多少额外的空间传播到这一列) and pad (另有多少空间).
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))
另外租多少空间
meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
```


但通常，您只想做一些简单的事情来封装数据，而不是将所有内容放入全局变量空间中。你可以重写以将主代码封装到类中。

```
from tkinter import *
from tkinter import ttk

class FeetToMeters:

    def __init__(self, root):

        root.title("Feet to Meters")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
       
        self.feet = StringVar()
        feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet)
        feet_entry.grid(column=2, row=1, sticky=(W, E))
        self.meters = StringVar()

        ttk.Label(mainframe, textvariable=self.meters).grid(column=2, row=2, sticky=(W, E))
        ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(column=3, row=3, sticky=W)

        ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        feet_entry.focus()
        root.bind("<Return>", self.calculate)
        
    def calculate(self, *args):
        try:
            value = float(self.feet.get())
            self.meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
        except ValueError:
            pass

root = Tk()
FeetToMeters(root)
root.mainloop()
```