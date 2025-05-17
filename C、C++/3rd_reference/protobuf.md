# protobuf

Protocol Buffers(协议缓冲区)是 Google 推出的数据交换格式, 语言中立、平台中立、可扩展的结构化数据序列化机制

protobuf 将消息 .proto 文件编译成语言相关的源文件(支持 C++/Python/Go等), 使用时需要proto编译器

> [protobuf官方仓库]( https://github.com/google/protobuf)


## USAGE

### 安装

1. 下载预编译二进制
```sh
PB_REL="https://github.com/protocolbuffers/protobuf/releases"
curl -LO $PB_REL/download/v< param protoc-version >/protoc-< param protoc-version >-linux-x86_64.zip
```
2. 使用apt安装 `apt install -y protobuf-compiler`
3. window上使用winget安装 `winget install protobuf`