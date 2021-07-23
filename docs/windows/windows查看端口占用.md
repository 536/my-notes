# windows查看端口占用

查看端口是否被占用及占用端口的程序是什么，以`3306`端口为例

```bat
netstat -aon|findstr :3306
```

> ```text
>   TCP    0.0.0.0:3306           0.0.0.0:0              LISTENING       4696
>   TCP    0.0.0.0:33060          0.0.0.0:0              LISTENING       4696
>   TCP    [::]:3306              [::]:0                 LISTENING       4696
>   TCP    [::]:33060             [::]:0                 LISTENING       4696
> ```

最后一列的`4696`即为进程的PID

```bat
tasklist |findstr 4696
```

> ```text
> mysqld.exe                    4696 Services                   0      4,268 K
> ```

由此可知，进程`mysqld.exe`正占用`3306`端口

关闭占用端口的进程

```bat
通过进程名称
TASKKILL /IM mysqld.exe
通过进程ID，同时关闭子进程
TASKKILL /PID 3306 /T
强制关闭
TASKKILL /F /IM mysqld.exe /T
```
