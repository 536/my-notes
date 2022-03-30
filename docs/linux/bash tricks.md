# Bash tricks

## Internal

- `clear` ==> `ctrl + l`
- `cd` 回到用户目录下
- `cd -` 回到上一个目录

- `history` 查看历史命令

  设置`HISTTIMEFORMAT='%Y-%m-%d %T - '`，查看history的内容格式会变化
  
- `!!` 执行上一个的命令
    
    `sudo !!` 用sudo执行上一个命令
    
- `!{{number}}` 执行history中的第number个命令

- `ctrl + r` 支持模糊搜索的历史命令查询
- `tail -f -n 50 {{pathToFile}}` 查询文件的最新n行数据，实时刷新（偏向于日志文件的查看）
- `cmd1 || cmd2` cmd1执行失败才不执行cmd2
- `cmd1 && cmd2` cmd1执行失败便不执行cmd2
- `ctrl + z` 将程序放到后台（常用：vim界面下切换到命令行界面）（`fg`命令切回前台）
- `ls | column -t` 将输出按列打印
- `pushd`/`popd` pushd将目录放到堆栈中，popd的时候拿出
- `man`/`help` 获取命令的帮助信息
- `truncate -s 0 pathToFile` 将文件内容清空
- `>/dev/null 2>&1` 不打印任何内容，包括错误信息
- `ssh`远程执行命令
  
  1. 简短命令
  
  `ssh user@host "cd /home && ls >ls.txt"`
  
  2. 复杂命令
  
  ```bash
  touch remote.bash
  ```
  
  ```bash
  # >remote.bash
  #!/bin/bash
  ssh user@host >/dev/null 2>&1 << EOF
  cd /home
  touch abcdefg.txt
  exit
  EOF
  echo done!
  ```
  
  ```bash
  bash remote.bash
  ```
  
- `which` 查看命令的绝对路径
- `whereis` 查看命令/文件在`PATH`中的路径
- `w`
- `who`
- `whoami`
- `id`
- `last`

- `whatis`

- `wc`
- `watch` Execute a command repeatedly, and monitor the output in full-screen mode.

- `env` 查看当前环境变量
- `env {{cmd}}` 使用env中的命令执行（比如：`env python3`）

- `ps -ef|grep python3` 查看进程
- `kill -2/9 {{pid}}` 结束进程
- `killall {{processName}}` 结束进程
- `lsof -[itucp]`

- `free -m`
- `df -h`
- `vmstat`
- `top`

- `host {{site.com}}`
- `dig {{site.com}}`
- `nc`
- `telnet`
- `ssh`
- `ping`
- `ifconfig`
- `ip address`
- `tcpdump`
- `traceroute`

- `strings`
- `ldd`
- `locate`
- `tr`
- `shuf .ssh/id_rsa -n 2`

- `factor 2333333`
- `seq -s " " 5 3 20`

- `file`
- `stat`
- `tree`
- `find . -name "xxx"`
- `pwd`
- `cd`
- `pushd`/`popd`
- `mv`
- `cp`
- `rm`

- `su`/`su - {{userName}}`
- `chown`
- `chgrp`
- `chmod`

## External

- `tldr`
  
  "too long, didn't read"
  
  输出命令的常见用法示例，用于参考

- `duf`
  
  比`df -h`更加h的形式输出文件系统信息
  
## Advanced

- `xargs`
- `awk`

## Other

- `mount`/`umount` `nfs-server`/`nfs-common`
- 
