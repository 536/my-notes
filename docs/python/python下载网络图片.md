# python下载网络图片

个人比较推荐`requests`的方法

+ `requests`

```python
from contextlib import closing

import requests


def download(url, file_path):
    response = requests.get(url, stream=True)
    with closing(response):
        with open(file_path, 'wb') as f:
            for chunck in response.iter_content(1024):
                f.write(chunck)


download('https://w.wallhaven.cc/full/8o/wallhaven-8ogod1.jpg', 'wallpaper.jpg')
```

+ `urllib.request.urlretrieve`

```python
from urllib.request import urlretrieve

urlretrieve('https://w.wallhaven.cc/full/8o/wallhaven-8ogod1.jpg', 'wallpaper.jpg')
```
