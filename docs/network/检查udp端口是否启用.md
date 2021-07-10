# 检查udp端口是否启用

+ windows

使用到的工具`nmap`（wireshark安装时附带）

```batch
nmap 172.24.1.1 -sU -p 5080
```

+ linux

```bash
netcat（nc） -vzu 172.24.1.1 5080
```
