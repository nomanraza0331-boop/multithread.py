import threading
import time

def display():
    l1=[6,4,8,5,3,1,9,5,4,6]
    for i in l1:
        print(i)
        time.sleep(1)


def sum():
    l1=[6,8,4,6,5,4,8,9,5,5]
    s=0
    for i in l1:
        s+=1
        print(s)
        time.sleep(1)

def string():
    str="multitreading"
    l1=[]
    for i in str:
        l1.append(i)
        print(l1)
        time.sleep(1)


t1=threading.Thread(target=display)
t2=threading.Thread(target=sum)
t3=threading.Thread(target=string)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()




