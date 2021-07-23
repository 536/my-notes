# python类装饰器

```python
class Add:

    def __init__(self, fn):
        print("初始化")
        self.num = 10
        self.fn = fn

    def __call__(self, *args, **kwargs):
        print("类装饰器开始工作")
        return self.fn(self.num)


@Add
def test1(n):
    return 1 + n


@Add
def test2(n):
    return 2 + n


if __name__ == '__main__':
    print(test1())
    print(test2())
```

output:

```text
初始化
初始化
类装饰器开始工作
11
类装饰器开始工作
12
```
