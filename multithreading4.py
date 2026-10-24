import threading
import os
import time

os.chdir("D:\\source")
with open ("file1.txt","r")as fr:
    with open ("file2.txt","w")as fw:
        fw.write(time.strftime("%H:%M:%S"))
        fw.write(fr.readline())
        
    fw.close()
    fr.close()