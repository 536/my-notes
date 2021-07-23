# bat在运行中进行百度搜索

将此脚本命令为`bd.bat`然后放在系统变量PATH指向的任意文件夹下

```bat
@echo off
set browser="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
set url=https://www.baidu.com/s?wd="%*"
start %browser% %url%
```

可在运行命令中使用`bd hello world`来直接百度`hello world`
