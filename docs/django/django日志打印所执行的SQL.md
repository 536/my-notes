# django打印所执行的SQL

## 直接使用queryset对象

```python
docs = Doc.objects.all()
print(str(docs.query))
```

## 直接获取数据库连接

```python
from django.db import connection

print(connection.queries)
```

## 配置settings中的LOGGING

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
        },
    },
    'handlers': {
        'sql': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, "sql_info.log"),
            'formatter': 'simple'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['sql', 'console'],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
}
```
