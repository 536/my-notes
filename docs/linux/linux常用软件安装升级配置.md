# linux常用软件安装升级配置

## 安装git

有许多种安装方式，主要分为两种，一种是通过编译源代码来安装；另一种是使用为特定平台预编译好的安装包。

### 从源代码安装

```bash
# 安装依赖
yum install curl-devel expat-devel gettext-devel openssl-devel zlib-devel
apt-get install libcurl4-gnutls-dev libexpat1-dev gettext libz-dev libssl-dev

# 下载源码
# https://mirrors.edge.kernel.org/pub/software/scm/git/
wget https://mirrors.edge.kernel.org/pub/software/scm/git/git-2.9.5.tar.gz

# 解压
tar -zxf git-2.9.5.tar.gz

# 编译并安装
cd git-2.9.5
make prefix=/usr/local all
sudo make prefix=/usr/local install
```

### 从预编译好的二进制包安装

```bash
yum install git-core
# 或者
apt-get install git
```

### 参考

<https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>

## 安装redis

### 从源代码安装

```bash
# 安装依赖
yum install gcc

# 下载源码
mkdir /usr/local/redis
cd /usr/local/redis
# http://download.redis.io/releases/
wget http://download.redis.io/releases/redis-5.0.5.tar.gz

# 解压
tar -zxf redis-5.0.5.tar.gz

# 编译并安装
cd redis-5.0.5
make MALLOC=libc
cd src && make install
```

### 启动

```bash
cd /usr/local/redis/src
# 直接启动redis
./redis-server

# 以后台进程方式启动redis
# 1. 将daemonize no修改为daemonize yes
vim /usr/local/redis/redis-5.0.5/redis.conf
# 2. 指定redis.conf文件启动
./redis-server /usr/local/redis/redis-5.0.5/redis.conf

# 3. 关闭redis进程
ps -aux | grep redis
kill -9 #reids-server的PID#

# 4. 设置redis开机自启动
mkdir /etc/redis
# 将/usr/local/redis/redis-5.0.5/redis.conf文件复制一份到/etc/redis目录下，并命名为6379.conf
cp /usr/local/redis/redis-5.0.5/redis.conf /etc/redis/6379.conf
# 将redis的启动脚本复制一份放到/etc/init.d目录下
cp /usr/local/redis/redis-5.0.5/utils/redis_init_script /etc/init.d/redisd
cd /etc/init.d
# 设置开机自启
chkconfig redisd on

# 如果以上命令执行失败
vim /etc/init.d/redisd
# 在第一行加入如下两行注释，保存退出

# chkconfig:   2345 90 10
# description:  Redis is a persistent key-value database

# 注释的意思是，redis服务必须在运行级2，3，4，5下被启动或关闭，启动的优先级是90，关闭的优先级是10。
# 重新执行开机自启的命令
chkconfig redisd on

# 5. 这时候已经可以使用服务的方式开启/关闭redis了
service redisd start
service redisd stop
```

### 问题

> $ service redis start
>
> /var/redis/run/redis_6379.pid exists, process is already running or crashed

```bash
# 可用安装文件启动
redis-server /etc/redis/6379.conf

# 或者软重启让系统自动恢复
shutdown -r now

# 或者直接删除此文件
rm -rf /var/redis/run/redis_6379.pid
```

### 参考

<https://www.cnblogs.com/zuidongfeng/p/8032505.html>

## Python3

```bash
# 安装Python3.6.8
yum  -y  install  bzip2-devel expat-devel gdbm-devel readline-devel sqlite-devel  libffi-devel  tk-devel gcc gcc-c++ openssl  openssl-devel

# wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tar.xz
wget https://mirrors.huaweicloud.com/python/3.6.8/Python-3.6.8.tar.xz

tar xf Python-3.6.8.tar.xz

cd Python-3.6.8/
mkdir /usr/local/python3
./configure --prefix=/usr/local/python3
make -j8
make -j8 install

ln -s /usr/local/python3/bin/python3.6 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3

python3 -V
```

## nginx

```bash
# 安装nginx
sudo yum -y install nginx

sudo systemctl enable nginx # 设置开机启动
sudo service nginx start # 启动nginx服务
sudo service nginx stop # 停止nginx服务
sudo service nginx restart # 重启nginx服务
sudo service nginx reload # 重新加载配置，一般是在修改过nginx配置文件时使用。
```

## mysql

```bash
# 安装mysql（ 5.6.4）
# 1.安装
wget http://dev.mysql.com/get/mysql-community-release-el7-5.noarch.rpm
rpm -ivh mysql-community-release-el7-5.noarch.rpm
yum install mysql-community-server

# 2.重启服务
service mysqld restart

# 查看是否开机自启
chkconfig --list | grep mysqld
chkconfig mysqld on

# 3.设置bind-ip

vim /etc/my.cnf
# 在[mysqld]:下面加一行
# bind-address = 0.0.0.0

# 4.登录mysql
mysql -u root
```

```sql
-- 5.设置外部ip可以访问
-- mysql中输入命令：
-- 后面用navicat连接远程服务器mysql的用户名和密码
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '123456' WITH GRANT OPTION;

FLUSH PRIVILEGES；

-- 6.设置mysql密码
-- 进入mysql：
set password = password('123456'); -- 密码123456
flush privileges;
```

### 修改密码

```bash
$ mysqladmin -u root password -p
Enter password: ****************
New password: ********
Confirm new password: ********
Warning: Since password will be sent to server in plain text, use ssl connection to ensure password safety.
```

```bash
$ mysql -uroot -hlocalhost -p
Enter password: ********
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 31
Server version: 8.0.16 MySQL Community Server - GPL

Copyright (c) 2000, 2019, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```

## sqlite3

```bash
# 下载源码
wget https://www.sqlite.org/2019/sqlite-autoconf-3290000.tar.gz
# 编译
tar zxvf sqlite-autoconf-3290000.tar.gz
cd sqlite-autoconf-3290000/
./configure --prefix=/usr/local
make && make install

# 替换系统低版本 sqlite3
mv /usr/bin/sqlite3  /usr/bin/sqlite3_old
ln -s /usr/local/bin/sqlite3   /usr/bin/sqlite3
echo "/usr/local/lib" > /etc/ld.so.conf.d/sqlite3.conf
ldconfig # https://www.cnblogs.com/schips/p/10183111.html
sqlite3 -version
```

## docker

参考：<https://www.cnblogs.com/yufeng218/p/8370670.html>

1、Docker 要求 CentOS 系统的内核版本高于 3.10 ，查看本页面的前提条件来验证你的CentOS 版本是否支持 Docker 。

通过 uname -r 命令查看你当前的内核版本

```bash
uname -r
```

2、使用 root 权限登录 Centos。确保 yum 包更新到最新。

```bash
sudo yum update
```

3、卸载旧版本(如果安装过旧版本的话)

```bash
sudo yum remove docker  docker-common docker-selinux docker-engine
```

4、安装需要的软件包， yum-util 提供yum-config-manager功能，另外两个是devicemapper驱动依赖的

```bash
sudo yum install -y yum-utils device-mapper-persistent-data lvm2
```

5、设置yum源

```bash
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
```

6、可以查看所有仓库中所有docker版本，并选择特定版本安装

```bash
yum list docker-ce --showduplicates | sort -r
```

7、安装docker

```bash
sudo yum install docker-ce  #由于repo中默认只开启stable仓库，故这里安装的是最新稳定版17.12.0
sudo yum install <FQPN>  # 例如：sudo yum install docker-ce-17.12.0.ce
```

8、启动并加入开机启动

```bash
sudo systemctl start docker
sudo systemctl enable docker
```

9、验证安装是否成功(有client和service两部分表示docker安装启动都成功了)

```bash
docker version
```

### docker-compose

+ pip install docker-compose

——报错setuptools需要>=3.5的版本，所以需要安装python3

+ github的release页面提供的方法：

```bash
curl -L https://github.com/docker/compose/releases/download/1.25.4-rc2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose`
```

——下载速度过慢。

+ 在github页面下载对应版本的docker-compose二进制文件，然后复制到/usr/bin/docker-compose并修改权限

```bash
# 下载docker-compose-Linux-x86_64
wget https://github.com/docker/compose/releases/download/1.25.4-rc2/docker-compose-Linux-x86_64
# 复制到/usr/bin/docker-compose
cp ./docker-compose-Linux-x86_64 /usr/bin/docker-compose
# 添加执行权限
chmod +x /usr/bin/docker-compose

sudo docker-compose --version
```

## 环境变量

### 临时

```bash
# 执行以下命令，多个路径分开执行即可
export PATH="$PATH:/usr/local/python3/bin"
export PATH="$PATH:/usr/local/anything"
```

### 当前用户永久

```bash
# 编辑"~/.bash_profile"
vim ~/.bash_profile

# 添加以下内容，多个路径分行记录即可
export PATH="$PATH:/usr/local/python3/bin"
export PATH="$PATH:/usr/local/anything"

# 用"source"命令刷新环境变量
source ~/.bash_profile
```

### 所有用户永久

```bash
# 编辑"/etc/profile"
vim /etc/profile

# 添加以下内容，多个路径分行记录即可
export PATH="$PATH:/usr/local/python3/bin"
export PATH="$PATH:/usr/local/anything"

# 用"source"命令刷新环境变量
source /etc/profile
```

## 设置服务与开机启动

### uwsgi

<https://www.cnblogs.com/hanhy/articles/7278336.html>

CentOS 7的服务systemctl脚本存放在：/usr/lib/systemd/，有系统（system）和用户（user）之分，像需要开机不登陆就能运行的程序，还是存在系统服务里吧，即：/usr/lib/systemd/system目录下，并且每一个服务以 .service 结尾。

1. `/etc/init.d/uwsgid`

    ```bash
    #!/bin/bash
    if [ ! -n "$1" ]; then #$1：指该脚本后跟的第一个参数，-n：判断$1是否为非空，！：取相反
        echo "Usages: sh uwsgid.sh [start|stop|restart]"
        exit 0
    fi

    if [ $1 = start ]; then #如果第一个参数等于start，执行下面命令
        psid=$(ps aux | grep "uwsgi" | grep -v "grep" | wc -l)
        #上面执行了启动之后，判断启动是否正常，grep -v过滤掉“grep”，使用wc -l查看输出几行
        if [[ $psid -gt 4 ]]; then
            echo "uwsgi is running!"
            exit 0
        else
            /usr/bin/uwsgi --ini /usr/local/nginx/html/BRMS/BRMS_uwsgi.ini
            echo "Start uwsgi service [OK]"
        fi

    elif [ $1 = stop ]; then
        killall -INT uwsgi
        echo "Stop uwsgi service [OK]"
    elif [ $1 = restart ]; then
        killall -INT uwsgi
        /usr/bin/uwsgi --ini /usr/local/nginx/html/BRMS/BRMS_uwsgi.ini
        echo "Restart uwsgi service [OK]"
    else
        echo "Usages: sh uwsgid.sh [start|stop|restart]"
    fi
    ```

2. `/usr/lib/systemd/system/uwsgid.service`

    ```conf
    [Unit]
    Description=uwsgid
    After=network.target

    [Service]
    Type=forking
    ExecStart=/etc/init.d/uwsgid start
    ExecReload=/etc/init.d/uwsgid restart
    ExecStop=/etc/init.d/uwsgid stop
    PrivateTmp=true

    [Install]
    WantedBy=multi-user.target
    ```

3. 添加执行权限

    ```bash
    chmod +x /etc/init.d/uwsgid
    chmod +x /usr/lib/systemd/system/uwsgid.service
    ```

4. 服务设置

    ```bash
    # 开机自启
    systemctl enable uwsgid.service
    # 启动
    systemctl start uwsgid.service
    # 停止
    systemctl stop uwsgid.service
    # 重新启动
    systemctl restart uwsgid.service
    ```
