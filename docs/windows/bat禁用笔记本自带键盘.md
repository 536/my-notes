# bat禁用笔记本自带键盘

需要以`管理员权限`执行命令

```bat
# 禁用 - 重启生效
sc config i8042prt start= disabled
# 启用
sc config i8042prt start= demand
```

win10下如何关闭笔记本自带键盘？ - 汤吉的回答 - 知乎 <https://www.zhihu.com/question/36434420/answer/453941619>
