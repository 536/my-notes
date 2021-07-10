# python多线程

## 多线程

```python
import threading


def thread_run():
    print(f'Thread {threading.current_thread().name}')


if __name__ == '__main__':
    thread_1 = threading.Thread(name='thread_1', target=thread_run)
    thread_2 = threading.Thread(name='thread_2', target=thread_run)
    thread_1.start()
    thread_2.start()
```

```python
import threading


class MyThread(threading.Thread):
    def __init__(self, name):
        super(MyThread, self).__init__(name=name)

    def run(self) -> None:
        print(f'Thread {threading.current_thread().name}')


if __name__ == '__main__':
    thread_1 = MyThread('thread_1')
    thread_2 = MyThread('thread_2')
    thread_1.start()
    thread_2.start()
```

## 线程同步

```python
import threading
import time

mylock = threading.RLock()
num = 0


class MyTread(threading.Thread):
    def __init__(self, name):
        super(MyTread, self).__init__()

        self.name = name

    def run(self) -> None:
        global num
        while True:
            mylock.acquire()
            print(f'Thread {self.name} locked. num={num}')
            if num >= 4:
                mylock.release()
                print(f'Thread {self.name} released. num={num}')
                break
            num += 1
            print(f'Thread {self.name} released. num={num}')
            mylock.release()
            time.sleep(1)


if __name__ == '__main__':
    thread_1 = MyTread('thread_1')
    thread_2 = MyTread('thread_2')
    thread_1.start()
    thread_2.start()
```

## 总结

在Python的CPython解释器中存在着GIL（Global Interpreter Lock，全局解释器锁），在执行代码时会产生互斥锁来限制线程对共享资源的访问，直到解释器遇到I/O操作或者操作次数达到一定数目时才会释放GIL。

由于GIL锁的存在，每次执行代码之用到了一个CPU，所以，对于CPU密集型（运算量大的）的代码，更适合使用多进程。但针对IO密集型的（文件读写/网络吞吐等），多线程比较适合。
