# canboat

CANBoat 提供 NMEA 2000 和 NMEA 0183 实用程序。它包含一个 NMEA 2000 PGN 解码器，可以读取和写入 N2K 消息。它并不意味着作为一个最终用户的工具，而是作为一个深入研究 NMEA 2000 网络的发现机制。

## cli tool

### analyzer

analyzer支持读取如下格式:
- Plain format: `timestamp, priority, pgn, source, destination, number of data bytes(max 8 bytes)`, 如
> `2025-04-25-17:09:21.338,4,130074,99,255,8,04,96,49,50,5c,00,08,01`
- Fast format: 超过8 bytes的字节会被压缩至一行, 如
> `2022-09-23T11:05:20.451Z,2,127489,236,255,26,00,28,00,ff,ff,bb,71,a2,03,00,00,e0,b0,05,00,ff,ff,ff,ff,ff,00,00,00,00,7e,ff`
- Airmar format: 由 `Airmar's WeatherCaster` 软件产生
- Chetco format: 由 `Chetco NMEA 2000 devices` 产生
- Garmin formats: 由 `Garmin plotters` 绘图仪导出的日志文件功能

## example

- `./rel/linux-x86_64/candump2analyzer ./samples/actisense-522.candump.log > temp_analyzer_format.txt` 将candump记录的log格式转为analyzer使用格式
- `./rel/linux-x86_64/analyzer < temp_analyzer_format.txt` 分析analyzer格式文件(ASCII格式),输出可读的ASCII格式/JSON格式(需`-json`选项)
- `./rel/linux-x86_64/analyzer -json -nv < temp_analyzer_format.txt | ./rel/linux-x86_64/n2kd`
- `./rel/linux-x86_64/actisense-serial -w -d out.txt` 从标准输入中读取analyzer格式文件并转化为actisense输出到out.txt中