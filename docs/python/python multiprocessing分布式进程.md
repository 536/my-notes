# python multiprocessing分布式进程

* 管理节点

```python
from multiprocessing.managers import BaseManager
from multiprocessing import Queue

queue = Queue()
BaseManager.register('queue', callable=lambda: queue)
manager = BaseManager(address=(ip, port), authkey='test'.encode('utf-8'))
manager.get_server().serve_forever()
# manager.start()
# queue.put(sth)
# manager.shutdown()
```

* 生产者

```python
from multiprocessing.managers import BaseManager

BaseManager.register('queue')
manager = BaseManager(address=(ip, port), authkey='test'.encode('utf-8'))
manager.connect()
queue = manager.queue()

queue.put(sth)
```

* 消费者

```python
from multiprocessing.managers import BaseManager

BaseManager.register('queue')
manager = BaseManager(address=(ip, port), authkey='test'.encode('utf-8'))
manager.connect()
queue = manager.queue()

while not queue.empty():
    sth = queue.get()
```
