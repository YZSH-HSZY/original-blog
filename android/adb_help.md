## adb命令

```
你可以使用adb help来获取帮助信息
D:\QtScrcpy-win-x86-v2.1.2>adb help
Android Debug Bridge version 1.0.41
Version 33.0.2-8557947
Installed as D:\QtScrcpy-win-x86-v2.1.2\adb.exe
//命令有如下选项
global options:
	...
general commands:
	...
networking:
	...
file transfer:
	...
shell:
	...
app installation (see also `adb shell cmd package help`):
	...
debugging:
	...
security:
	...
scripting:
	...
internal debugging:		--内部调试
	...
usb:
	...
```

**adb命令参考**

|		选项			|		参数			|
|		---			|		---			|
|		usb			|		|

### settings命令
```
Settings 提供命令如下:
  help
      输出帮助信息
  get [--user <USER_ID> | current] NAMESPACE KEY
	  检索KEY的当前值
  put [--user <USER_ID> | current] NAMESPACE KEY VALUE [TAG] [default]
      设置KEY的值
      TAG to associate with the setting.TAG与设置关联。
      {default} 设置默认值, 不区分大小写,仅适用与 global/secure 命名空间
  delete [--user <USER_ID> | current] NAMESPACE KEY
      Delete the entry for KEY.
  reset [--user <USER_ID> | current] NAMESPACE {PACKAGE_NAME | RESET_MODE}
      Reset the global/secure table for a package with mode.
      RESET_MODE 为 {untrusted_defaults, untrusted_clear, trusted_defaults}之一, 不区分大小写
  list [--user <USER_ID> | current] NAMESPACE
      Print all defined keys.
**NAMESPACE** 只能为 {system, secure, global}之一, 不区分大小写
```
### adb设置代理

`adb shell settings put global http_proxy <ip:port>`

取消代理设置，恢复默认`adb shell settings put global http_proxy :0`

## adb 示例

### 模拟鼠标滚动
- `adb shell input roll <dx> <dy>`
- `adb shell input swipe <start_x> <start_y> <end_x> <end_y> <duration_time>`.