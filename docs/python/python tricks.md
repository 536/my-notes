# python tricks

* 将12345转换为[1, 2, 3, 4, 5]

```python
list(str(12345))
```

* 将[1, 2, 3, 4, 5]转换为12345

```python
from functools import reduce

reduce(lambda x, y: x * 10 + y, [1 , 2, 3, 4, 5])
```
