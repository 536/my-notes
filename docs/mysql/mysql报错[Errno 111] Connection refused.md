# mysql报错[Errno 111] Connection refused

1. 客户端连接异常

    ```bash
    $ mycli -uroot -hlocalhost
    (2003, "Can't connect to MySQL server on 'localhost' ([Errno 111] Connection refused)")
    ```

2. 查看mysql运行日志

    ```text
    2021-04-29T01:04:54.736544Z 0 [Note] mysqld (mysqld 5.7.33) starting as process 1 ...
    2021-04-29T01:04:54.757484Z 0 [Note] InnoDB: PUNCH HOLE support available
    2021-04-29T01:04:54.757546Z 0 [Note] InnoDB: Mutexes and rw_locks use GCC atomic builtins
    2021-04-29T01:04:54.757550Z 0 [Note] InnoDB: Uses event mutexes
    2021-04-29T01:04:54.757553Z 0 [Note] InnoDB: GCC builtin __atomic_thread_fence() is used for memory barrier
    2021-04-29T01:04:54.757555Z 0 [Note] InnoDB: Compressed tables use zlib 1.2.11
    2021-04-29T01:04:54.757558Z 0 [Note] InnoDB: Using Linux native AIO
    2021-04-29T01:04:54.758993Z 0 [Note] InnoDB: Number of pools: 1
    2021-04-29T01:04:54.759131Z 0 [Note] InnoDB: Using CPU crc32 instructions
    2021-04-29T01:04:54.766179Z 0 [Note] InnoDB: Initializing buffer pool, total size = 128M, instances = 1, chunk size = 128M
    2021-04-29T01:04:54.766216Z 0 [ERROR] InnoDB: mmap(137428992 bytes) failed; errno 12
    2021-04-29T01:04:54.766222Z 0 [ERROR] InnoDB: Cannot allocate memory for the buffer pool
    2021-04-29T01:04:54.766226Z 0 [ERROR] InnoDB: Plugin initialization aborted with error Generic error
    2021-04-29T01:04:54.766231Z 0 [ERROR] Plugin 'InnoDB' init function returned error.2021-04-29T01:04:54.766235Z 0 [ERROR] Plugin 'InnoDB' registration as a STORAGE ENGINE failed.
    2021-04-29T01:04:54.766239Z 0 [ERROR] Failed to initialize builtin plugins.
    2021-04-29T01:04:54.766241Z 0 [ERROR] Aborting

    2021-04-29T01:04:54.766247Z 0 [Note] Binlog end
    2021-04-29T01:04:54.766316Z 0 [Note] Shutting down plugin 'CSV'
    2021-04-29T01:04:54.767574Z 0 [Note] mysqld: Shutdown complete
    ```

    可以看到`Cannot allocate memory for the buffer pool`，报内存加载失败

3. 查看当前内存和swap大小

   ```bash
   $ free -m
                 total        used        free      shared  buff/cache   available
   Mem:            990         265          61           0         664         578
   Swap:             0           0           0
   ```

   可以看到内存的剩余空间仅为90M，而mysql运行日志中所需内存大小为128M，并且swap空间也为0，所以mysql启动失败

4. 创建/增加swap空间

   ```bash
   $ cd /
   $ mkdir swap
   $ cd swap/
   $ dd if=/dev/zero of=swapfile bs=1M count=2048
   2048+0 records in
   2048+0 records out
   2147483648 bytes (2.1 GB, 2.0 GiB) copied, 15.8203 s, 136 MB/s
   $ ll
   total 2097152
   -rw-r--r-- 1 root root 2147483648 Apr 29 10:14 swapfile
   $ mkswap swapfile
   mkswap: swapfile: insecure permissions 0644, 0600 suggested.
   Setting up swapspace version 1, size = 2 GiB (2147479552 bytes)
   no label, UUID=cf4611b7-1d78-4def-8d4b-8530baab2f96
   $ chmod 0600 swapfile
   $ free -m
                 total        used        free      shared  buff/cache   available
   Mem:            990         265          61           0         664         578
   Swap:             0           0           0

   $ swapon swapfile
   $ free -m
                 total        used        free      shared  buff/cache   available
   Mem:            990         267          66           0         656         577
   Swap:          2047           0        2047

   ```

5. 查看mysql状态

    ```bash
    $ docker ps -a
    CONTAINER ID   IMAGE       COMMAND                  CREATED       STATUS          PORTS                               NAMES
    4e93544a4126   mysql:5.7   "docker-entrypoint.s…"   2 weeks ago   Up 26 seconds   0.0.0.0:3306->3306/tcp, 33060/tcp   mysql
    ```
