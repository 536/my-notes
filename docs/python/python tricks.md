# python tricks

- 将12345转换为[1, 2, 3, 4, 5]

```python
list(str(12345))
```

- 将[1, 2, 3, 4, 5]转换为12345

```python
from functools import reduce

reduce(lambda x, y: x * 10 + y, [1 , 2, 3, 4, 5])
```

- 将列表中的数据按出现次数排序

```python
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 6, 3]
sorted(set(l), key=l.count, reverse=True)
```

- 打印列表中的数据出现次数最多的n个数据

```python
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 6, 3]
# way 1
sorted(set(l), key=l.count, reverse=True)[:n]

# way 2
from collections import Counter
Counter(l).most_common(n)
```
