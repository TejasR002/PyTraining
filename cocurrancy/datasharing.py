import time
import multiprocessing
 
result = []

def addone(x):
    global result
    x+=1
    result.append(x)
    print("one added",(result))

num = 5
result = multiprocessing.Array("i",1)
p1 = multiprocessing.Process(target=addone,args=(num,))  

p1.start()
p1.join()

