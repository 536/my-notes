# windows下Apache+mod_wsgi部署

## 环境信息

+ Python 3.6.8

+ Django 2.2.3

+ mod_wsgi 4.6.8+ap24vc14

+ Apache 2.4.41

+ Windows 10

Apache下载地址：<https://www.apachelounge.com/download/>

mod_wsgi下载地址：<https://www.lfd.uci.edu/~gohlke/pythonlibs/#mod_wsgi>

## 安装步骤

1.安装mod_wsgi并获取Python环境信息

```batch
mod_wsgi-express module-config
> LoadFile "c:/python36/python36.dll"
> LoadModule wsgi_module "c:/python36/lib/site-packages/mod_wsgi/server/mod_wsgi.cp36-win_amd64.pyd"
> WSGIPythonHome "c:/python36"
```

2.解压下载好的`httpd-2.4.41-win64-VS16.zip`到D盘根目录，目录结构参考如下

```batch
tree D:\Apache24
```

> ```text
> D:\APACHE24
> ├───bin
> │   └───iconv
> ├───cgi-bin
> ├───conf
> │   ├───extra
> │   └───original
> │       └───extra
> ├───error
> │   └───include
> ├───htdocs
> ├───icons
> │   └───small
> ├───include
> ├───lib
> ├───logs
> ├───manual
> └───modules
> ```

3.修改conf/httpd.conf

3.1修改Apache目录

找到`Define SRVROOT "c:/Apache24"`，修改为`Define SRVROOT "d:/Apache24"`

3.2修改监听端口号

找到`Listen 80`，修改为`Listen 8080`

3.3修改服务地址

找到`#ServerName www.example.com:80`，下方添加一行`ServerName 127.0.0.1:8080`

3.4在文件末尾添加python执行环境信息（步骤一中的三行）

3.5在文件末尾添加项目信息

```xml
# 指定项目的wsgi.py配置文件路径,这个py文件是在你的Django项目中
WSGIScriptAlias / "D:\PYTHON\blog\blog\wsgi.py"

# 指定项目目录,即你的Django项目路径
WSGIPythonPath  "D:\PYTHON\blog"

<Directory "D:\PYTHON\blog\blog">
<Files wsgi.py>
    Require all granted
</Files>
</Directory>

# 项目静态文件地址, Django项目中静态文件的路径
Alias /static "D:\PYTHON\blog\static"
<Directory "D:\PYTHON\blog\static">
    AllowOverride None
    Options None
    Require all granted
</Directory>

# 项目media地址, 上传图片等文件夹的路径
Alias /media "D:\PYTHON\blog\media"
<Directory "D:\PYTHON\blog\media">
    AllowOverride None
    Options None
    Require all granted
</Directory>
```

4.安装并启动服务

4.1安装服务

```batch
cd /d d:\Apache24\bin
httpd.exe -k install -n "django_blog"
```

当出现service is successfully installed.字样时表示服务安装成功，可以在系统的服务列表中找到名为“django_blog”的服务。

此步出错的日志在`Apache24\logs\install.log`中[参考**报错处理**]。

4.2启动服务

```batch
httpd.exe -k start -n "django_blog"
```

此步正常不会返回消息，成功与否需要在访问后检查日志。

5.浏览器访问127.0.0.1:8080

此步出错的日志在`Apache24\logs\error.log`中[参考**报错处理**]。

## 报错处理

+ (OS 10048)通常每个套接字地址(协议/网络地址/端口)只允许使用一次。

  端口被占用了，换一个。

+ `ModuleNotFoundError: No module named 'encodings'`

  使用虚拟环境venv时的mod_wsgi配置中会缺少python.dll的信息，所以不能用venv的环境。

+ `ModuleNotFoundError: No module named 'django'`

  某些情况下，Python环境为用户所有，需要将项目中使用到的所有包用管理员权限重新安装，便可解决此问题。

+ 不能上传文件

  检查配置无误后，将项目中上传文件部分的路径修改为绝对路径，防止路径出错。

## 参考

<https://blog.csdn.net/Mr_blueD/article/details/79759483>
