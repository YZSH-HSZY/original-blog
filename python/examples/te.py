import win32gui
import win32con


windows_list = []
win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), windows_list)
for window in windows_list:
    classname = win32gui.GetClassName(window)
    title = win32gui.GetWindowText(window)
#     print(f'classname:{classname} title:{title}')
    if title.__eq__('任务管理器'):
        print(f'classname:{classname} title:{title}')
        b = win32gui.SetWindowPos(window, win32con.HWND_TOP, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        print (b)