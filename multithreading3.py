# import threading
# # import time
# import os

# def file_read_write(file1,file2):

#     print(os.getcwd())
#     os.chdir("D:\\contents")
#     print(os.getcwd())

#     my_data=""
#     with open ("employees.txt","r")as f1:
#         my_data=f1.read()
#         print(my_data)
#         f1.close

#     os.chdir("D:NOMAN PYTHON \\MULTITHREADING")
#     with open ("new_employees.txt","w")as f2:
#         f2.write(my_data)
#         f2.close()

# t1=threading.Thread(target=file_read_write,args=("employees.txt","new_employees.txt"))
# t1.start()
# t1.join()

#=======================================================================================



import threading
import os

def file_read_write(file1, file2):
    source_path = os.path.join(r"D:\contents", file1)
    destination_path = os.path.join(r"D:\NOMAN PYTHON\MULTITHREADING", file2)
    

    with open(source_path, "r") as f1:
        my_data = f1.read()

    print(my_data)

    with open(destination_path, "w") as f2:
        f2.write(my_data)

t1 = threading.Thread(
    target=file_read_write,args=("employees.txt", "new_employees.txt"))

t1.start()
t1.join()
