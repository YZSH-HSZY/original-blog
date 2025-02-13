# linux下窗口应用


## x-server

### 相关命令
- `xvfb` (apt install xvfb) 用于X版本11的虚拟framebuffer X服务器
- `xvfb-run` (apt install xvfb) 在虚拟x服务器环境中运行指定的x客户端或命令
- `xrandr` (apt install x11-xserver-utils) 原始命令行接口到RandR扩展,显示screens及对应分辨率
- `xdpyinfo` (apt install x11-utils) 显示x程序的信息工具, 显示DISPLAY详细信息
- `x11vnc` (apt install x11vnc) 允许远程访问图形界面会话的 VNC 服务端
    > `x11vnc -storepasswd` 设置访问密码, 默认存储在 `~/.vnc/passwd`
    > `x11vnc -display :99 -rfbport 5900 -forever -shared -rfbauth ~/.vnc/passwd`

## temp
https://www.cnblogs.com/chaichengxun/p/15409996.html