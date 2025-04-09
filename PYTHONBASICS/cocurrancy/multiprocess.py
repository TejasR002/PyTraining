import multiprocessing.process
import time
import multiprocessing



def func1():
    i = 0
    while i < 10:
        time.sleep(0.3)
        print("this is func1 ",i)
        i+=1
def func2():
    i = 0
    while i < 10:
        time.sleep(0.2)
        print("This is func2 ",i)
        i+=2


t1 = multiprocessing.Process(target=func1)
t2 = multiprocessing.Process(target=func2)

t1.start()
t2.start()

t1.join()
t2.join()