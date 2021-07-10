# ffmpeg从视频文件推RTSP流

主要架构是

1. 启动RTSP服务器
2. `ffmpeg`执行推流命令
3. 使用`ffplay`等RTSP客户端播放流

## 启动RTSP服务器

有很多选择，比如[rtsp-simple-server](https://github.com/aler9/rtsp-simple-server)、[EasyDarwin](https://github.com/EasyDarwin/EasyDarwin)，基本都是双击启动即可

## ffmpeg执行推流命令

`ffmpeg -re -stream_loop -1 -i HuaHuo.mp4 -vcodec copy -acodec copy -s 1366x768 -f rtsp rtsp://127.0.0.1:8554/stream/ch1`

## 播放RTSP流

`ffplay rtsp://127.0.0.1:8554/stream/ch1`

## 其他通过视频文件转RTSP流的方法

[happytimesoft rtsp-server](http://www.happytimesoft.com/products/rtsp-server/index.html)

[live555MediaServer](http://www.livesw.com/mediaServer)

## 备注

1. `rtsp-simple-server`
   + 开源MIT
2. `EasyDarwin`
   + 开源但是仓库中未提供license
   + 有可视化界面，功能比较多
3. `happytimesoft rtsp-server`
   + 源码收费
4. `live555MediaServer`
   + 开源LGPL
