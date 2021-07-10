# 设置命令行默认codepage

使用mycli等命令时可能出现中文乱码的情况，这基本是因为默认的代码页不是936（GBK）或者65001（UTF-8）

## 查看/修改codepage

```cmd
chcp # 查看codepage
chcp 65001 # 修改codepage
```

## 设置默认codepage

在`HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Command Processor`新建字符串值`AutoRun`，内容设为`@chcp 65001>nul`

## 备注

1. 如果通过此方法将`AutoRun`内容设为`@chcp 65001>nul && cd /d D:\`以设置默认启动路径为`D:\`，将会影响包括在地址栏敲`cmd`启动命令行的情况，所以不建议使用。

2. 美国/加拿大英语是`codepage 437`
