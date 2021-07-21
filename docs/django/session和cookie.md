# session和cookie

想到哪写到哪

## session

### 有何作用

将无状态的http请求变成会话的形式，将符合要求的请求的数据持久化

比如鉴权、会话缓存

### 保存在哪里

保存在服务端

默认保存在django_session表中，有三个字段session_key/session_data/expire_date

## cookie

### 有何作用

作为session的一个key，配合服务端的session来实现相关功能

也可单独实现一些基础的功能，比如记住用户选择的夜间模式、界面语言等

### 保存在哪里

保存在客户端

每次客户端请求时在http headers中添加cookie，服务端解析cookie并获取session，从而判断会话是否有效。此场景下cookie可以视为session的钥匙
