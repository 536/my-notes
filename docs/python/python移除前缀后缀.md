# python移除前缀后缀

切勿使用`lstrip`方法，此方法会以单个字符为标准，找到便移除，并不以整个prefix为标准。


```python
def removeprefix(s, prefix):
    if sys.version=>3.9:
        return s.removeprefix(prefix)
    return s[len(prefix):] if s.startswith(prefix) else s
```

https://stackabuse.com/python-remove-the-prefix-and-suffix-from-a-string/
