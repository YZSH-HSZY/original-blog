# tkinter
tkinter是python内置的gui模块（是一个"Tk 接口"，针对 Tcl/Tk GUI 工具包的标准 Python 接口），你可以使用tkinter来创建一个跨平台的gui应用程序。

[python官方文档-tkinter部分](https://www.tkdocs.com/shipman/)
[tkinter官方教程](https://tkdocs.com/tutorial/firstexample.html)

Tkinter 并不只是做了简单的封装，而是增加了相当多的代码逻辑，让使用体验更具 Python 风格（pythonic） 。

在命令行执行 python -m tkinter，应会弹出一个简单的 Tk 界面窗口， 表明 tkinter 包已安装完成，还会显示当前安装的 Tcl/Tk 版本，以便阅读对应版本的 Tcl/Tk 文档。

## Tcl、Tk、Ttk关系

1. Tcl 是一种动态解释型编程语言，正如 Python 一样。尽管它可作为一种通用的编程语言单独使用，但最常见的用法还是**作为脚本引擎或 Tk 工具包的接口嵌入到 C 程序中**。Tcl 库有一个 C 接口，用于创建和管理一个或多个 Tcl 解释器实例，并在这些实例中运行 Tcl 命令和脚本，添加用 Tcl 或 C 语言实现的自定义命令。每个解释器都拥有一个事件队列，某些部件可向解释器发送事件交由其处理。与 Python 不同，Tcl 的执行模型是围绕协同多任务而设计的，Tkinter 协调了两者的差别（详见 Threading model ）。

2. Tk是一个用C实现的Tcl包，它添加了自定义命令来创建和操作GUI小部件。每个Tk对象都嵌入了自己的Tcl解释器实例，其中装入了Tk。Tk的小部件非常可定制，但代价是外观过时。Tk使用Tcl的事件队列来生成和处理GUI事件。

3. Ttk带有主题的 Tk（Ttk）是较新加入的 Tk 部件，相比很多经典的 Tk 部件，在各平台提供的界面更加美观。自 Tk 8.5 版本开始，Ttk 作为 Tk 的成员进行发布。Python 则捆绑在一个单独的模块中， tkinter.ttk。

## tkinter控件

### Text多行文本

#### 获取Text文本内容
`get(self, index1, index2=None)` 
- `index1`以'line_no.col_no'形式指定第i行第j列，
- `index2` 一般为'end',表最后一个字符

**注意** 对于超出范围的行或列，以最后一个位置替代

### Entry单行文本

### Scrollbar滚动条

> 使用: `Scrollbar(master, [options])`
|可用option          |描述|
|--------------------|---------------------------------|
|activebackground    |鼠标悬停在滑块和箭头上方时他们的颜色|
|bg                  |当鼠标不在滑块和箭头上方时,滑块和箭头的颜色|
|bd                  |围绕槽的整个周长的3-d边框的宽度,以及箭头和滑块上3-D效果的宽度,默认值为槽周围没有边框,箭头和滑块周围有2像素边框|
|command             |每当移动滚动条时要调用的过程|
|cursor              |鼠标悬停在滚动条上时显示的光标|
|elementborderwidth  |箭头和滑块周围的边框的宽度,默认值为elementborderwidth=-1,这意味着使用borderwidth选项的值highlightbackground 滚动条没有焦点的颜色突出显示|
|highlightcolor      |当滚动条具有焦点时,焦点颜色会突出显示|
|highlightthickness  |焦点高亮显示的粗细,默认值为1,设置为0可抑制点高光的显示|
|jump                |此选项控制用户拖动滑块时发生的情况.通常(jump=0),滑块的每一小拖动都会导致调用命令回调,如果将此选项设置为1,则在用户释放鼠标按钮之前不会调用回调|
|orient              |对于水平滚动条，设置orient = HORIZONTAL，对于垂直滚动条，设置orient = VERTICAL|
|repeatdelay         |此选项控制在滑块开始向该方向重复移动之前，按钮 1 必须在槽中按住多长时间。默认值为重复延迟 = 300，单位为毫秒|
|repeatinterval      |重复间隔|
|takefocus           |通常，您可以通过滚动条小部件将焦点按 Tab 键。如果您不希望出现此行为，请设置 takefocus=0|
|troughcolor         |槽的颜色|
|width               |滚动条的宽度（如果水平，则其 y 尺寸，如果垂直，则其 x 尺寸）。默认值为 16|

## bug集合

### 使用 `widget['state']` 判断控件状态时有时生效有时失效
> 问题描述：tk控件实现了getitem方法，因此我们使用抽取时会返回封装的属性值，但是 `widget['state']` 在初次返回时是一个string对象，如果直接和python字面量字符串比较，会有转换的影响。
> 解决方案：通过 `str()` 进行先一步的转换

### combobox控件通过 `configure` 更改其state,更新文本内容不生效
> 问题描述：在 `normal` 和 `disabled` 之间，对combobox的文本值进行更改时，有时会出现内容更新不生效情况
> 解决方案：在combobox为`disabled`时，delete本身不起作用，频繁更改state时，会出现控件属性延迟更新的现象。root.update本身是更新ui显示，对属性延迟更新不生效。这时可在局部自己管理一个dict，用于保存属性变化和之间的更新值。并在之后更新。

### combobox的ComboboxSelected事件在代码更新current选择不生效

`ComboboxSelected` 为用户事件，只在ui触发时。想在代码里触发，可以手动调用绑定函数。



## 第一个例子
```python
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
feet_entry.grid(column=2, row=1, sticky=(W, E))  # 另外使用多少空间

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

```python
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

## 常见使用示例

### 弹窗和滚动框

#### 使用canv实现Checkbutton滚动

```python
# 弹窗创建
root.attributes('-disabled', 1)
top = Toplevel(root)
ff0 = Frame(top)
ff0.pack(fill='x')
scr = Scrollbar(ff0)
scr.pack(side=RIGHT, fill='y')
canv = Canvas(ff0)
canv.pack(side=LEFT)

ff1 = Frame(canv)
canv.create_window((0,0), window=ff1, anchor='nw')

def top_delete_func(*args):
    """ 销毁弹窗时，启用主窗口 """
    root.attributes('-disabled', 0)
    if isinstance(top, Toplevel): top.destroy()
    
top.protocol('WM_DELETE_WINDOW', top_delete_func)

d = datetime.now()
d_td = dt.timedelta(hours=d.hour, minutes=d.minute, seconds=d.second)
with sessionmaker(self.ENGINE)() as session:
    query_res: List[str] = session.query(PartGenerateInfoTable.part_code).where(
        cast(datetime.now(), Date) == cast(PartGenerateInfoTable.insert_time, Date),
        PartGenerateInfoTable.part_code.not_in(session.query(PartInfoTable.part_code))
    ).all()
all_check_var = []

for i in range(len(query_res)):
    b1 = BooleanVar()
    c1 = Checkbutton(ff1, text=str(query_res[i].part_code), variable=b1)
    all_check_var.append((b1, c1))
    c1.pack()

# 更新canv
canv.update()
# yscrollcommand=scr.set 让画布和滚动条绑定
# scrollregion=canv.bbox('all') 设置滚动区域，滚动区域是一个元组（x1,y1,x2,y2）
    # bbox 返回控件的区域，参数all表示返回画布上所有控件的区域
# command=canv.yview 设置滚动条滚动时触发的动作：滚动画布
canv.config(yscrollcommand=scr.set, scrollregion=canv.bbox('all'))
scr.config(command=canv.yview)

# 绑定canv鼠标滚动事件
def on_mousewheel(event):
    canv.yview_scroll(-1*(int(event.delta/120)), "units")

canv.bind("<MouseWheel>", on_mousewheel)

def print_no_use():
    # 打开一个新的工作簿
    workbook = openpyxl.Workbook()
    # 创建一个新的工作表
    worksheet = workbook.active
    data_is_not_null = False
    for check_b, p_s_n_ in all_check_var:
        if not check_b.get(): continue
        data_is_not_null = True
        check_b: BooleanVar
        p_s_n_: Checkbutton
        worksheet.append([p_s_n_.cget('text')])
    if not data_is_not_null:
        messagebox.showinfo("Success", "无未使用数据")
        top_delete_func()
        return

    workbook.save(join(exec_file_path, "Excel/未使用部件编号_" + \
        str(datetime.now())[:10] + "_" + str(datetime.now())[11:13] + \
            "_" + str(datetime.now())[14:16] + ".xlsx"))
    messagebox.showinfo("Success", "已打印")
    top_delete_func()

ff2 = Frame(top)
ff2.pack(fill='x')
btn_1 = Button(ff2, text='打印', command=print_no_use)
btn_1.pack()
```

**注意** `create_window`函数把控件放到画布，可以实现把控件视为画布的一部分，如果用`pack`函数来布局控件，它只能放在画布上，但不是画布的一部分，这时滚动条只能滚动画布，无法滚动其他子控件。