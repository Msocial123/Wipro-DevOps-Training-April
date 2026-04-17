import os
# print(dir(os)) to know about module 

# os.chdir("D:\\Myworkspace\\testing")
# # os.mkdir("testing")
# print(os.getcwd())
# print(os.listdir('.'))
# var=os.walk(os.getcwd())
# print(var)
# for  value in var:
#     print(value)
# var=os.walk(os.getcwd())
# for cur_dir,list_dir,list_files in var:
#     print(cur_dir)
#     print(list_dir)
#     print(list_files)
# functions and methods --> function directly,, methods call by object ---os.methodname()
# print(os.name) # windows-nt    mac/linux ---posix
# print(os.getcwd())
# os.chdir("D:\Admin-Retail-Application")
# print(os.getcwd())
# os.chdir("D:\Myworkspace")
# print(os.listdir('.'))
# print(os.listdir("D:\Admin-Retail-Application"))
# os.mkdir("reports")
# print(os.listdir('.'))
# for i in range(4,11):
#     os.mkdir(f"DAY{i}")

# os.chdir("D:\Admin-Retail-Application")
# # print(os.getcwd())
# os.makedirs("2026/April/Reports") #create nested folder 
# os.rmdir("Day10") #--> remove empty folder 
# os.rmdir("Day9")
# os.removedirs("2026/April/Reports") #to remove nested directories 
# os.rename("oldfilename.extention","new filename.extention")
# os.rename("wipro_tra.txt","wipro_trainings.txt")
# os.remove("filename.extention")
# os.remove("wipro_trainings.txt")
# print(os.path.exists("day21.py"))  #check if the file is exists or not , it returns true if file is exists  else false
# print(os.listdir())

# files=["java","python","ds"]
# for file in files:
#     os.mkdir(file)
# auto cleanup the script 
# for file in os.listdir():
#     if file.endswith(".tmp"):
#         os.remove(file)

# print(os.path.exists("D:\Myworkspace\day21.py"))

# path=os.path.join("Users","Admin","Docs") #create safely join paths
# print(path)

# print(os.path.isfile("day1.py")) # check file is available or not

#print(os.path.isdir("D:\Myworkspace\DAY8")) # CHECK THE DIRECTORY IS AVAILABLE OR NOT IN THE PATH
#pip install python-dotenv
# os.getenv()
from dotenv import load_dotenv
load_dotenv() # load .env file 
# dbserv=os.getenv("DB_SERVER_USER")
# dbhost=os.getenv("DB_SERVER_HOST")
# dbpassword=os.getenv("DB_SERVER_PASSWORD")
# print(f"user : {dbserv} hostname:{dbhost} passwordv : {dbpassword}")
#os.environ --> set environmet varianle named ENV with value for the current python process

# os.environ["ENV"] = "production"
# print(os.getenv("ENV"))
# var=os.walk(os.getcwd()) # used to get the information of each and every folders and files as nested format
# print(var)
# for  value in var:
#     print(value)
# var=os.walk(os.getcwd())
# for cur_dir,list_dir,list_files in var:
#     print(cur_dir)
#     print(list_dir)
#     print(list_files)

from  sys import argv ,exit
# print(type(sys.argv))
# print(sys.argv[1])
# print(sys.argv[2])
# print(f"the number of cmd line arguments {len(argv)}")
# print(f"list of cmd arguments {argv}")
# print(f"the cmd arguments one by one :")
# for arg in argv:
#     print(arg)

# print sum of all cmd line arguments:

# args=argv[1:]
# sum=0
# for x in args:
#     sum=sum + int(x)
# print(sum)


# f1=open('file1.txt')
# f2=open('file2.txt')
# f3=open('outputfile.txt','w')

# for x in f1:
#     f3.write(x)
# for x in f2:
#     f3.write(x)
# args=argv[1:]
# print(f"Name: {args}")
# print(argv[1] + argv[2])
# print(int(argv[1]) + int(argv[2]))

# print(argv[60])
# print(argv)
#deployment script
# env=argv[1]
# if env=="prod":
#     print("deployong to the production")
# elif env == "dev":
#     print("deploying  to development")

# sys.exit() --- terminates program immediately 
# print("processing....")
# print("loading...")
# # print(exit(1)) 1= fail , 0= success 
# print("deployed sucessfully ")
# exit()
# CI pipelines:
# disk = 95
# if disk>90:
#     print("disk full")
#     exit(1)
# print("disk is healthy ")
# print(os.getcwd())
# \n give new line
# \t tab
# r= rath path 
# f=open(r'C:\Users\babud\Desktop\wipro-april\questionpaper.txt','r')
# print(f.read())
# f.close()

# using context manager  to open file 

# with open(r'C:\Users\babud\Desktop\wipro-april\questionpaper.txt','r') as f:
#     for line in f:
#         print(line,end='')

# with open(r'C:\Users\babud\Desktop\wipro-april\questionpaper.txt','r') as f:
#     print(f.read()) read() can  read the file data at once , if 1Gb of file uhave u need memory space gb

# with open(r'C:\Users\babud\Desktop\wipro-april\questionpaper.txt','r') as f:
#     # print(f.read(20)) # print top 20 characters 
#     print(f.readlines()) # print each line consists of one list


# write operation
# with open('TEST.txt','w') as f:
#     f.write(" hello ,")
# with open('TEST.txt','a') as f:
#     f.write(" \n i am murali mohan M")
# with open(r'C:\Users\babud\Desktop\wipro-april\questionpaper.txt','r') as readfile:    
#     for line in readfile:
#         if line.startswith("Answer") is True:
#             with open('Answers.txt','a') as appendfile:
#                 appendfile.write(line)

# import math
# import random
# import sys 

# sys.path.append(r'D:\Myworkspace\DAY3') # its going to append this path to the execution 

# import caluculator

# print(caluculator.addition(6,10))  
# print(math.sqrt(10))
# print(math.pow(2, 3))
# print(math.ceil(4.9))
# print(sys.executable) # print the location where python enumerator is avialbel 
# data=[1,2]
# print(sys.getsizeof(data)) #bytes

# for v in range(1,6):
#     os.makedirs(f"/Backup/backup_{v}")
# path ="D:\Backup"
# folder=sorted(os.listdir(path))
# print(type(folder))
# print(folder)
# while len(folder) >3:
#     old=folder.pop(0) #pop method used to remove top element from the list 
#     os.rmdir(os.path.join(path,old)) #create full path = D:\Backup\backup_1
#     print(old,"deleted")


