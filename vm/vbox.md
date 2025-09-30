# vbox

[简易教程](https://cn.linux-console.net/?p=20740)

vboxmanage startvm ubuntu20 [-type {headless, gui, vrdp}]

vboxmanage list runningvms

vboxmanage controlvm ubuntu20 poweroff

挂起 vboxmanage controlvm ubuntu20 pause

vboxmanage list runningvms -l

恢复 vboxmanage controlvm ubuntu20 resume

vboxmanage createvm --name FedoraLinuxVM --ostype Fedora_64 --register

查看可用虚拟机类型 vboxmanage list ostypes


例如，我们可以将名称从FedoraLinuxVM更改为Fedora35，如下所示。

vboxmanage modifyvm FedoraLinuxVM --name Fedora35
如下所示为 VM 分配内存、CPU 和图形控制器。

vboxmanage modifyvm Fedora35 --memory 4096 --cpus 2 --vram 20 --graphicscontroller vmsvga --rtcuseutc on

## example

### vbox机器取消磁盘文件动态扩容

> 使用ui图像界面
1. 关闭使用该磁盘的虚拟机
2. 在 VirtualBox 管理器中选择"管理" > "虚拟介质管理器"
3. 选择您的动态磁盘，点击"复制"按钮
4. 在复制对话框中，选择"固定分配"作为新磁盘类型
5. 指定新磁盘文件的名称和位置
6. 完成后，将虚拟机配置更改为使用新磁盘

### 启动虚拟机失败, 提示: VirtualBox can't operate in VMX root mode. Please disable the KVM kernel extension

需要禁用kvm内核模块并重新加载vboxdrv模块

```sh
rmmod kvm_intel
rmmod kvm
modprobe vboxdrv
```
