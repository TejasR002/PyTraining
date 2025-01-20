import time
import threading

def func1():
    i = 0
    while i < 10:
        time.sleep(0.3)
        print(i)
        i+=1
def func2():
    i = 0
    while i < 10:
        time.sleep(0.2)
        print(i)
        i+=2


t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)

t1.start()
t2.start()

t1.join()
t2.join()