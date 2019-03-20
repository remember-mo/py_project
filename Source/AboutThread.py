# coding: utf-8

from pythonLib import threading as threading

threadLocal = threading.local()
a = 1

def show():
    print(threading.current_thread().getName(), threadLocal.num)


def target():
    threadLocal.num = 0
    for i in range(89):
        threadLocal.num += 1
    show()

threads = []
for i in range(8):
    # thread = threading.Thread(target=target())
    threads.append(threading.Thread(target=target))
    threads[i].start()
