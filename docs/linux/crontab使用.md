# crontab使用

+ -u 指定一个用户
+ -l 列出某个用户的任务计划
+ -r 删除某个用户的任务
+ -e 编辑某个用户的任务

## cron文件语法

可用`crontab -e`命令来编辑，编辑的是/var/spool/cron下对应用户的cron文件，也可以直接修改/etc/crontab文件。

具体格式如下：

| Minute | Hour | Day  | Month | Dayofweek | command |
| ------ | ---- | ---- | ----- | --------- | ------- |
| 0-59   | 0-23 | 1-31 | 1-12  | 0-6       | command |

每个字段代表的含义如下：
`Minute`    每个小时的第几分钟执行该任务
`Hour`      每天的第几个小时执行该任务
`Day`       每月的第几天执行该任务
`Month`     每年的第几个月执行该任务
`DayOfWeek` 每周的第几天执行该任务，0代表周日
`Command`   指定要执行的程序

特殊符号:

+ "\*" 代表取值范围内的数字
+ "/" 代表"每"
+ "-" 代表从某个数字到某个数字
+ "," 分开几个离散的数字

## 新增计划任务

`crontab -e` // 然后添加相应的任务，:wq存盘退出。

## 查看调度任务

`crontab -l` // 列出当前的所有调度任务
`crontab -l -u test` // 列出用户test的所有调度任务

## 示例

添加计划任务，一般一行对应一个任务

```text
# 每个小时的第30分钟，执行一次
30 * * * * /usr/bin/python3 /home/project/timed.py
# 每6个小时的第30分钟，执行一次
30 */6 * * * /usr/bin/python3 /home/project/timed.py
# 每周一到周五的凌晨0点、1点、2点，各执行一次
0 0,1,2 * * 1-5 /usr/bin/python3 /home/project/timed.py

# 将执行日志写到文件中
0 0 * * 1-5 /usr/bin/python3 /home/project/timed.py >> /home/project/timed.log
# 将错误日志也写入到此日志文件(2>&1)
0 0 * * 1-5 /usr/bin/python3 /home/project/timed.py >> /home/project/timed.log 2>&1
# 将日志文件名称以日期时间命名
# 2019-01-01.log
0 0 * * 1-5 /usr/bin/python3 /home/project/timed.py >> /home/project/$(date + "\%Y-\%m-\%d").log 2>&1
# 2019-WEEK_01.log
0 0 * * 1-5 /usr/bin/python3 /home/project/timed.py >> /home/project/$(date + "\%Y-WEEK_\%W").log 2>&1
# 2019-01-01_01.log
0 0 * * 1-5 /usr/bin/python3 /home/project/timed.py >> /home/project/$(date + "\%Y-\%m-\%d_\%H").log 2>&1
```

## 重启cron服务

```bash
service cron restart
```
