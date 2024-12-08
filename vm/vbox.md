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