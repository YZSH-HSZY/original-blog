##### Android Studio 运行模拟器

在下载的 Android SDK 目录下找到模拟器 emulator 目录。在 cmd 中运行命令 emulator.exe -list-avds 查看所有虚拟机信息

##### emulator.exe 的使用

```
Android Emulator usage: emulator [options] [-qemu args]
```

你可以使用 emulator.exe --help 查看命令帮助信息

```
     -help     print this help
     -help-<option>     print option-specific help

     -help-disk-images about disk images
     -help-debug-tags     debug tags for -debug <tags>
     -help-char-devices     character <device> specification
     -help-environment     environment variables
     -help-virtual-device     virtual device management
     -help-sdk-images     about disk images when using the SDK
     -help-build-images     about disk images when building Android
     -help-all     prints all help content
```

##### logcat输出格式说明
每个日志都有一个日期、时间戳、进程和线程 ID、标记、包名称、优先级以及与之关联的消息。不同的标签具有独特的颜色，有助于识别日志的类型。每个日志条目的优先级为 FATAL 、 ERROR 、 WARNING 、 INFO DEBUG 或 VERBOSE 。

For example, the following log message has a priority of DEBUG and a tag of ProfileInstaller:
例如，以下日志消息的优先级为 DEBUG ，标记为 ProfileInstaller ：
