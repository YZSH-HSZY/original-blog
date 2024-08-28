## python for window

这是一个使用python进行window编程的学习文档，需要安装pywin32的python包。

[window api 官网](https://learn.microsoft.com/zh-cn/windows/win32/api/winuser/nf-winuser-setwindowpos "MSDN中文文档")

### 使用python安装pywin32时，导入报错解决

直接使用`pip install pywin32`安装即可，如果在import时，报`找不到指定的模块。`错误，可以在python安装目录下执行
`python.exe Scripts/pywin32_postinstall.py -install`

### pywin32、win32api、win32gui、win32com、win32con

pywin32、win32api、win32gui、win32com、win32con 名称非常类似，特别容易混淆

1. **pywin32**

pywin32 主要的作用是供 Python开发者快速调用 Windows API的一个模块库。该模块的另一个作用是是通过Python进行COM编程。

落地场景：
如果你想在Windows操作系统用Python实现自动化工作，pywin32模块经常用到。

2. win32gui 在安装 pywin32 之后就可以使用，这个模块定义了 Windows 下关于图形操作的API，FindWindow和 FindWindowEx 函数都可以使用。
该模块可以单独安装。

3. win32con  同上述模块基本一致，也是与 pywin32 配合使用的模块，这个模块内定义了Windows API内的宏。

4. win32api 也是安装 pywin32 之后就会配备的模块，Win32 API 即为Microsoft 32位平台的应用程序编程接口，接口可以在下述参考，除Python外，其它语言也可以对接。

>使用该模块会经常用到一个手册：http://www.yfvb.com/help/win32sdk/webhelplefth.htm

5. win32com  Python 操作 COM 组件的库（COM是Component Object Model （组件对象模型）的缩写）

其实到这里你会发现 pywin32 是底座，其它的都属于搭配模块。

```
win32api：提供了常用的用户API；
win32gui：提供了有关用户界面图形操作的API；
win32con：提供了消息常量的操作API；
win32file：提供了文件操作的API；
win32com：提供COM组件操作API。
```
## 相关API介绍

### win32gui模块

|API名|描述|
|----------|---------------------------------------|
|`EnumWindows`|获取所有窗口|
|`SetForegroundWindow`|将创建指定窗口的线程引入前台并激活窗口。 键盘输入将定向到窗口。当使用另一个窗口时，无法将窗口强制到前台。（成功调用即获取相应`SetForegroundWindow`权限）|
|`SetWindowPos`|设置窗口顺序（无法激活非活动窗口），拥有该窗口的进程必须具有 `SetForegroundWindow` 权限。|
|`ShowWindow`|将窗口显示到前台|

win32con.HWND_TOPMOST,将窗口置顶，即使未获取焦点仍置顶并保持，使用win32con.HWND_NOTOPMOST取消
win32con.HWND_TOP，将窗口置于 Z 顺序的顶部
win32con.SWP_NOMOVE，保留当前位置 (忽略 X 和 Y 参数，第3和第4位置参数) 
win32con.SWP_NOSIZE，保留当前大小 (忽略 cx 和 cy 参数，第5和第6位置参数) 
win32con.SWP_SHOWWINDOW，显示“接收端口跟踪选项” 窗口。
win32con.SWP_NOACTIVATE，不激活窗口。 如果未设置此标志，则会激活窗口

### python置顶window窗口
参考代码如下：
```
import win32gui, win32con
import sys
windows_list = []
# 获取所有窗口
win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), windows_list)

for window in windows_list:
    # 获取窗口类和标题
    classname = win32gui.GetClassName(window)
    title = win32gui.GetWindowText(window)
#     print(f'classname:{classname} title:{title}')
    if title.__eq__('任务管理器'):
#         print(f'classname:{classname} title:{title}')
        # 判断窗口是否可见
        bVisible = win32gui.IsWindowVisible(window)
        if bVisible == 0:
            raise SystemExit("{title}窗口不可见")
        # 将最小化的可见窗口展示到前台
        win32gui.ShowWindow(window, win32con.SW_SHOWNORMAL)
        # SetForegroundWindow将创建指定窗口的线程引入前台并激活窗口。 键盘输入将定向到窗口。当使用另一个窗口时，无法将窗口强制到前台。
#         win32gui.SetForegroundWindow (window)
        '''
            **注意：SetWindowPos无法激活非活动窗口，设置窗口顺序，拥有该窗口的进程必须具有 SetForegroundWindow 权限。**
            
            win32con.HWND_TOPMOST,将窗口置顶，即使未获取焦点仍置顶并保持，使用win32con.HWND_NOTOPMOST取消
            win32con.HWND_TOP，将窗口置于 Z 顺序的顶部
            win32con.SWP_NOMOVE，保留当前位置 (忽略 X 和 Y 参数，第3和第4位置参数) 
            win32con.SWP_NOSIZE，保留当前大小 (忽略 cx 和 cy 参数，第5和第6位置参数) 
            win32con.SWP_SHOWWINDOW，显示“接收端口跟踪选项” 窗口。
            win32con.SWP_NOACTIVATE，不激活窗口。 如果未设置此标志，则会激活窗口
        '''
        b = win32gui.SetWindowPos(window, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE |
                                  win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW | (win32con.SWP_NOACTIVATE if bVisible != 0 else 0))
        win32gui.SetWindowPos(window, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE |
                                  win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW | (win32con.SWP_NOACTIVATE if bVisible != 0 else 0))
        win32gui.SetWindowPos(window, win32con.HWND_TOP, 0, 0, 0, 0, win32con.SWP_NOMOVE |
                                  win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW | (win32con.SWP_NOACTIVATE if bVisible != 0 else 0))
        print (b)
```

### python调用window系统COM组件转换docx到pdf
```
>>> import win32com.client
>>> word = win32com.client.Dispatch("Word.Application")
>>> win32com.__file__
'C:\\Users\\YZSH_\\anaconda3\\envs\\mf\\lib\\site-packages\\win32com\\__init__.py'
>>> doc = word.Documents.Open(r'C:\Users\YZSH_\Desktop\program\blog\paper\output_split\0.docx')
>>> doc.SaveAs(r'C:\Users\YZSH_\Desktop\program\blog\paper\output_split\00.pdf', FileFormat=17)
>>> doc.Close(0)
```

## win桌面软件窗口结构查看

1. Inspect.exe 是一种基于 Windows 的工具，它可以选择任何 UI 元素并查看其辅助功能数据。 可以查看 Microsoft UI 自动化属性和控件模式以及 Microsoft Active Accessibility (MSAA) 属性。 “检查”还可以测试 UI 自动化树中自动化元素的导航结构以及 Microsoft Active Accessibility 层次结构中的可访问对象。

2. spy++.exe Microsoft Spy++是一个非常好的查看Windows操作系统的窗口、消息、进程、线程信息的工具，简单易用，功能强大。
（1）我经常用来查询一个不知道从哪里弹出来的广告窗口是哪个进程搞的鬼……然后干掉
（2）枚举所有窗口，查看父子关系，搜索某个窗口是否存在
（3）查询一个窗口（包括隐藏窗口）的属性，包括标题、类名、位置、进程线程
（4）通过分析其他软件的窗口消息，辅助研究其内部实现原理
（5）分析某窗口的消息参数，给其发送冒充消息，以实现特殊的功能

**注意** 以上软件均需要通过 `vs build tool` 安装vs开发工具

### pywinauto 操作窗口控件
```python
from pywinauto import Application
import time

app = Application('uia').start("notepad.exe")
win = app.window(title_re="无标题 - 记事本")
# 获取当前窗口下控件
print(win.print_ctrl_ids())
```