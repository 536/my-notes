# python多个装饰器执行的顺序

```python
def A(fn):
    print(2)

    def run():
        print(3)
        fn()
        print(9)

    return run


def B(fn):
    print(1)

    def run():
        print(4)
        fn()
        print(8)

    return run


def C(fn):
    print(0)

    def run():
        print(5)
        fn()
        print(7)

    return run


@A
@B
@C
def test():
    print(6)


if __name__ == '__main__':
    test()

```

output:

```text
0
1
2
3
4
5
6
7
8
9
```
