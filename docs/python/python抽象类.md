# python抽象类

```python
import abc

class Foo(abc.ABCMeta):

    @property
    @abc.abstractmethod
    def bar(self):
        pass
```

如果`@property`和`@abc.abstractmethod`位置放错，会报错`AttributeError: attribute '__isabstractmethod__' of 'property' object is not writable`

如上写法，可以要求继承自Foo类的子类，必须实现bar方法/拥有bar属性
