### ffmpeg命令
```
ffmpeg [全局选项] {[输入文件选项] -i 输入_url_地址} ...
 {[输出文件选项] 输出_url_地址} ...
```
如果你不想看 FFmpeg 标语和其它细节，而仅仅想看媒体文件信息，可以使用 -hide_banner选项
```
Hyper fast Audio and Video encoder
usage: ffmpeg [options] [[infile options] -i infile]... {[outfile options] outfile}...

Getting help:
    -h      -- print basic options
    -h long -- print more options
    -h full -- print all options (including all format and codec specific options, very long)
    -h type=name -- print all options for the named decoder/encoder/demuxer/muxer/filter/bsf/protocol
    See man ffmpeg for detailed description of the options.
```

**ffmpeg命令参考**

```mermaid
graph LR
S[ffmpeg]-->OP1[Print help / information / capabilities]
OP1-->OP1_zh["打印帮助/信息/功能"]
S-->OP2["Global options (affect whole program instead of just one file)"]
OP2-->OP2_zh["全局选项(影响整个程序，而不仅仅是一个文件)"]
S-->OP3[Per-file main options]
OP3-->OP3_zh["每个文件的主选项"]
S-->OP4[Video options]
OP4-->OP4_zh["视频选项"]
S-->OP5[Audio options]
OP5-->OP5_zh["音频选项"]
S-->OP6[Subtitle options]
OP6-->OP6_zh["字幕选项"]
```
```mermaid
graph LR
OP3[Per-file main options]-->description["-t 记录或转码音频/视频的“持续时间”秒"]
```

1. **Print help / information / capabilities**
|			选项				|			含义				|
|			---				|			---				|
|			-L				|			show license	|
|			-h topic		|			show help	|

2. **Per-file main options**
|			选项				|			含义				|
|			---				|			---				|
|			-t \<duration>				|			记录或转码音频/视频的“持续时间”秒	|
|			-to \<topic>		|			记录或转码停止时间	|
|			-fs \<limit_size>		|			设置以字节为单位的文件大小限制	|
|			-ss \<time_off>		|			设置开始时间偏移量	|

Print help / information / capabilities:
-L                  show license
-h topic            show help
-? topic            show help
-help topic         show help
--help topic        show help
-version            show version
-buildconf          show build configuration
-formats            show available formats
-muxers             show available muxers
-demuxers           show available demuxers
-devices            show available devices
-codecs             show available codecs
-decoders           show available decoders
-encoders           show available encoders
-bsfs               show available bit stream filters
-protocols          show available protocols
-filters            show available filters
-pix_fmts           show available pixel formats
-layouts            show standard channel layouts
-sample_fmts        show available audio sample formats
-dispositions       show available stream dispositions
-colors             show available color names
-sources device     list sources of the input device
-sinks device       list sinks of the output device
-hwaccels           show available HW acceleration methods
#### 查看输入文件格式
ffprobe -show_format < input file >

color 是一种幕布，可以作为一个视频源，在文章一开始给的例子中，就作为一个视频源使用，它可以通过 d 参数设定它的持续时间。
movie 导入视频源，可以视频视频或者图片作为视频源。
overlay 叠加视频，可以指定叠加视频的相对位置
concat 拼接视频，可以将视频进行拼接
fifo 队列，用于排列视频，与concat 一同使用