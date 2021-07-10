# django CBV传递默认参数

```python
# urls.py
IndexView.as_view(param='test')
# views.py
print(self.param)
```
