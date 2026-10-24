import threading
import time

# passing arguments to a function by using threads
        

sq=[]
cb=[]

def squares(s,e,a,name,version):
    for i in range(s,e):
        print(a,time.strftime(  "%H:%M:%S--" ),":",i*i)
        print(name,version,sep="\t")
        sq.append(i*i)
        time.sleep(1)


def cubes(s,e,b,name,version,year):
    for i in range(s,e):
        print(b,time.strftime(  "%H:%M:%S--" ),":",i*i*i)
        print(name,version,sep="\t")
        time.sleep(2)
        cb.append(i*i*i)



t1=threading.Thread(target=squares,args=(1,5,"squares"),kwargs={"name":"thread1","version":1.01})
t2=threading.Thread(target=cubes,args=(10,15,"cubes"),kwargs={"name":"thread1","version":2.01,"year":2026})
        
t1.start()
t2.start()

t1.join()
t2.join()

print(sq)
print(cb)
        
        



