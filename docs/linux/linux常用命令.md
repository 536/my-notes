# linux常用命令

`uname -a` 查看系统版本

`lsb_release -a` 查看系统版本

`cat /etc/os-release` 查看系统版本

`cat /etc/redhat-release` 查看系统版本

`cat /etc/centos-release` 查看系统版本

`rpm -q centos-release` 查看系统版本

`lsblk` 查看分区和磁盘

`df -h` 查看空间使用情况

`fdisk -l` 分区工具查看分区信息

`cfdisk /dev/sda` 查看分区

`blkid` 查看硬盘label（别名）

`du -sh ./*` 统计当前目录各文件夹大小

`free -h` 查看内存大小

`cat /proc/cpuinfo| grep "cpu cores"| uniq` 查看cpu核心数
