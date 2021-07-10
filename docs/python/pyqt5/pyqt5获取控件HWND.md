# pyqt5获取控件HWND

使用一个SDK的时候需要传入控件的HWND，找了好久没有相关的属性，最后发现是这个

```python
hwnd = int(self.winId())
```
