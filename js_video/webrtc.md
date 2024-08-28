### webrtc 学习笔记

webrtc 全名(Web Real-Time Communication)web 实时交流，支持网页进行实时的语言或视频通话。其中包含视频音频采集，编解码，数据传输，音视频展示等功能，我们可以通过技术快速地构建出一个音视频通讯应用。 虽然其名为 WebRTC，但是实际上它不光支持 Web 之间的音视频通讯，还支持 Android 以及 IOS 端，此外由于该项目是开源的，我们也可以通过编译 C++代码，从而达到全平台的互通。

**注意事项**

1. 因为浏览器的安全限制，使用`navigator.mediaDevices.getDisplayMedia`或其他方法获取设备屏幕流时，需要在 localhost、file、https 这三种安全环境下进行。
2. 在接触新的浏览器 api 使用时，可以参考 mdn 文档进行快速学习。[MDN--openWeb 开放 web 标准文档](https://developer.mozilla.org/zh-CN/ "打开链接")

#### webrtc 步骤

- 如何获取设备的媒体信息？
> 1.Media API的概念，MediaStream：用来表示一个媒体数据流。 MediaStreamTrack：在浏览器中表示一个媒体源。
> 2.在浏览器对象navigator中获取所有媒体信息mediaDevices，通过getDisplayMedia获取屏幕流、getUserMedia获取设备相机流。

- 如何进行录屏并保持录屏文件？
> 1.Edge 支持使用 MediaRecorder 来进行录制媒体流 mediaStream。`mediaRecorder = new MediaRecorder(video.srcObject,{mimeType:'video/webm;codecs=vp9'});` 其中第一个参数为 mediaStream，可以指定元数据类型 mimeType(例如"video/webm" 或者 "video/mp4") 。 
> 2.我们可以使用 Blob 和 URL.createObjectURL 来进行文件的保存。
