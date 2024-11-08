# matplotlib
matplotlib是python最流行的2D绘图库，提供了高级函数接口和对象接口两种绘图方式，类似于MATLAB绘图工具。

[一个简易的入门教程](https://wizardforcel.gitbooks.io/matplotlib-intro-tut/content/matplotlib/16.html)

## 示例

### 实时显示图标数据

> 描述: 如绘制股票实时定价数据，或者显示传感器实时数据。(因此和一般的matplotlib绘图相比，其x/y数据shape会更改)。需要使用 **Matplotlib 的动画功能**

```python
import matplotlib.pyplot as plt
import matplotlib.animation as animation  # matplotlib的动画支持
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data = open('example.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(x)
            ys.append(y)
    ax1.clear()
    ax1.plot(xs, ys)

# 动画绑定到图表中（fig），运行animate的动画函数，设置 1000ms 的间隔
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()

```

### 不同类型的数据绘制

1. 动态实时数据的更新
要实现动态实时曲线的绘制，关键是要能够及时更新曲线的数据。在Matplotlib中，可以使用set_data()方法来更新图形数据，例如：
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
line, = ax.plot(x, y)

for i in range(10):
    y = np.sin(x + i/10 * np.pi) # 模拟更新数据
    line.set_data(x, y) # 更新数据
    plt.pause(0.1) # 暂停一段时间，让图形更新显示
```
通过循环模拟数据的不断更新，然后在每次更新后使用set_data()方法来重新设置曲线的x和y坐标值，就可以实现动态更新曲线的效果。其中，plt.pause()方法用于暂停一段时间，让图形有足够的时间刷新显示，其参数为暂停的时间长度（以秒为单位）。

1. 不同数据类型的绘制方式
在绘制实时数据时，有些数据是连续的，有些数据是离散的，有些数据是带有噪声的。针对不同的数据类型，我们可以使用不同的绘制方式来实现最佳的绘图效果。


2.1 连续数据的绘制
对于连续的数据，我们可以使用Matplotlib中的plot()方法来实现曲线的绘制。例如：
```PYTHON
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
line, = ax.plot(x, y)

for i in range(10):
    y = np.sin(x + i/10 * np.pi) # 模拟更新数据
    line.set_ydata(y) # 只更新y坐标值
    plt.pause(0.1)
```
在每次更新数据时，我们只需要更新y坐标值即可，因为x坐标值是不变的。这种绘制方式适用于温度、湿度、气压等连续的物理量。

2.2 离散数据的绘制
对于离散的数据，我们可以使用Matplotlib中的scatter()方法来实现散点的绘制。例如：
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 10)
y = np.random.rand(10)

fig, ax = plt.subplots()
scat = ax.scatter(x, y)

for i in range(10):
    y = np.random.rand(10) # 模拟更新数据
    scat.set_offsets(np.column_stack((x, y))) # 更新数据
    plt.pause(0.1)
```
在每次更新数据时，我们需要使用set_offsets()方法来更新散点的位置，其参数为一个二维数组，其中第一维为各点的x和y坐标值，第二维为各点的颜色值等其他属性（可选）。这种绘制方式适用于光电传感器、声音传感器等离散的传感器数据。

2.3 带噪声数据的绘制
对于带噪声的数据，我们可以利用Matplotlib中的fill_between()方法来实现绘制范围区间的效果。例如：
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.rand(100)*0.2 # 模拟带噪声数据

fig, ax = plt.subplots()
line, = ax.plot(x, y)

for i in range(10):
    y = np.sin(x + i/10 * np.pi) + np.random.rand(100) * 0.2 # 模拟更新数据
    line.set_ydata(y)
    ax.fill_between(x, y-0.2, y+0.2, alpha=0.2) # 标示范围区间
    plt.pause(0.1)
```
在每次更新数据时，我们需要使用fill_between()方法来标识出范围区间，在这个例子中我们使用了一个alpha参数来控制范围区间的透明度。这种绘制方式适用于带有噪声的传感器数据、网络传输数据等。

### matplotlib date数据转换
```python
from matplotlib import dates 
dates.DateConverter.convert(w,None,None)
# 设置副刻度格式
hoursLoc = mpl.dates.HourLocator(interval=6) 
# 为6小时为1副刻度
ax1.xaxis.set_minor_locator(hoursLoc)
ax1.xaxis.set_minor_formatter(dates.DateFormatter('%H'))
# 参数pad用于设置刻度线与标签间的距离
ax1.tick_params(pad=10)
```