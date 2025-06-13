# protobuf

Protocol Buffers(协议缓冲区)是 Google 推出的数据交换格式, 语言中立、平台中立、可扩展的结构化数据序列化机制

protobuf 将消息 .proto 文件编译成语言相关的源文件(支持 C++/Python/Go等), 使用时需要proto编译器

> [protobuf官方仓库]( https://github.com/google/protobuf)
> [proto中文文档](https://protobuf.com.cn/programming-guides/proto3)


## USAGE

### 安装

1. 下载预编译二进制
```sh
PB_REL="https://github.com/protocolbuffers/protobuf/releases"
curl -LO $PB_REL/download/v< param protoc-version >/protoc-< param protoc-version >-linux-x86_64.zip
```
2. 使用apt安装 `apt install -y protobuf-compiler`
3. window上使用winget安装 `winget install protobuf`

### 选项

## DEBUG
- `ShortDebugString`

## proto文件格式

- 版本描述(文件的第一个非空/非注释行): `edition = "2023";`|`syntax = "proto3";`|`syntax = "proto2";`
    > 自2023起, 使用edition替换syntax描述protobuf的版本行为(未指定默认为proto2)
- 可选包声明
- .proto文件引用
- message格式定义

## 示例

### 使用`google.protobuf.Any`兼容自定义消息格式
```cpp
// proto msg define
message MsgTransmit {
  sfixed32 transmit_head = 1;
  int32 class_id = 2;
  google.protobuf.Any msg_data = 3;
  sfixed32 transmit_tail = 4;
}
// judge Any msg type
MsgTransmit revc_data;
revc_data.ParseFromArray(dd, sizeof(dd));
revc_data.msg_data().Is<ControlMsg>();
ControlMsg data;
revc_data.msg_data().UnpackTo(&data);
```

### json/proto互转

```cpp
// json to proto
google::protobuf::util::JsonParseOptions options;
options.ignore_unknown_fields = true;  // 显示声明忽略json未知字段
google::message::... msg;
std::string str2 = "",
google::protobuf::util::JsonStringToMessage(str, &msg, options);

// proto to json
google::protobuf::util::JsonPrintOptions options;
options.add_whitespace = true;
options.always_print_primitive_fields = true;
options.preserve_proto_field_names = true;
google::message::... transmit_data;
std::string json;
google::protobuf::util::MessageToJsonString(transmit_data, &json, options);
```