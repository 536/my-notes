# python ctypes定义变长度的结构体field

```cpp
typedef struct
{
    uint length;
    char data_list[1]
}
```

一般情况下通过ctypes定义的structure如下

```python
class StructX(ctypes.Structure):
    __field__ = [
        ('length', ctypes.c_uint32),
        ('data_list', ctypes.c_char * 1),
    ]
```

```python
# 实例化
struct_x = StructX()
```

但如果此结构体定义的data_list部分长度不定，则可使用以下方法

```python
def StructX(length: int):
    class Wrapper(ctypes.Structure):
        __field__ = [
            ('length', ctypes.c_uint32),
            ('data_list', ctypes.c_char * length),
        ]
    return Wrapper
```

```python
# 实例化
struct_x = StructX(100)() # 注意末尾括号
```
