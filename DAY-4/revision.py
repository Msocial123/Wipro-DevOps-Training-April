# salary=float(input("enter your salary :"))
# print("salary:",salary/12)

# Ctc,deductions=map(float,input("enter ctc ,deduction").split())
# print("Net salary:",Ctc-deductions)
# import os
# path=r"\www\var\version\.env"
# dire,file=os.path.split(path)
# print(f"directories{dire} \n files :{file}")

#separator
# print("a","b","c",sep="-")
# print("www","var","version",sep="/")
#end 
#slary pay slip
# import sys
# name= input("EMployee Name:")
# basic =float(input("Basic Pay:"))
# allowance = float(input("Allowances: "))
# deduction  = float(input("Deductions:"))

# gross = basic + allowance
# net = gross - deduction

# print("\n----------- salary slip -------")
# print(f"Employee Name :{name}")
# print(f"Basic Pay: {basic}")
# print(f"Allowances:{allowance}")
# print(f"gross salary:{gross}")
# print(f"Deduction:{deduction}")
# print(f"Net salary:{net}")

# import sys
# name= sys.argv[1]
# basic =sys.argv[2]
# allowance = sys.argv[3]
# deduction  = sys.argv[4]

# gross = float(basic) + float(allowance)
# net = gross - float(deduction)

# print("\n----------- salary slip -------")
# print(f"Employee Name :{name}")
# print(f"Basic Pay: {basic}")
# print(f"Allowances:{allowance}")
# print(f"gross salary:{gross}")
# print(f"Deduction:{deduction}")
# print(f"Net salary:{net}")
import sys 
# print(sys.version)
# username=input("entrer the user name ")

# if username =="":
#     print("no user name entered .. exiting ")
#     sys.exit()
# print("welcome ",username)
# to get where python got installed 
# for p in sys.path:
#     print(p)
# sys.path.append(path) # you can add path dynamically 
#suppose you have a custom module billin in different folder :

# a=10
# b=20
# name="murali"
# sys.path.append(r"D:\Myworkspace\DAY3")
# import caluculator
# import os
# print(dir(caluculator)) 
# print("sum :",caluculator.addition(a,b))
# print(sys.getsizeof(b))
# print(sys.getsizeof(name))

# data=[10,20,30]
# servername="webser1"
# # print(f"Data{sys.getsizeof(data)}, bytes")
# # print(f"server name{sys.getsizeof(servername)}, bytes")

# if sys.getsizeof(servername) >50:
#     print("Large server name ")
# else:
#     print("server size expected ")
import os
# print(dir(os)) # to know about module 
# print(os.getcwd())
# print(os.listdir())
# print(os.mkdir("folder name "))

# var=os.walk(os.getcwd())
# print(var)
# for  value in var:
#     print(value)
# var=os.walk(os.getcwd())
# for cur_dir,list_dir,list_files in var:
#     print(cur_dir)
#     print(list_dir)
#     print(list_files)
# os.rmdir("DAY3")
# os.rmdir("DAY3")
# files="D:\Myworkspace\DAY8\day1.py"
# os.remove(files) # to delete the files
# import shutil
# path="D:\Myworkspace\DAY8"
# shutil.rmtree(path)
# print(os.name)
# print(os.path.isdir("D:\Myworkspace\DAY7")) 
# from dotenv import load_dotenv
# load_dotenv() # load .env file 
# dbserv=os.getenv("DB_SERVER_USER")
# dbhost=os.getenv("DB_SERVER_HOST")
# dbpassword=os.getenv("DB_SERVER_PASSWORD")
# print(f"user : {dbserv} hostname:{dbhost} password : {dbpassword}")

# f=open("day1.py",'r')
# # print(f.read(30))
# print(f.readlines(50))
# f.close()
# with open("day1.py") as f:
#     for line in f:
#         print(line,end='')

# with open("results.txt",'a') as f:
#     a=20
#     b=40
#     sum=a+b
#     f.write(f"{str(sum)} \n")

import sys
name= input("EMployee Name:")
basic =float(input("Basic Pay:"))
allowance = float(input("Allowances: "))
deduction  = float(input("Deductions:"))

gross = basic + allowance
net = gross - deduction
with open("payslip.tx",'w') as f:
    f.write("\n----------- salary slip -------\n")
    f.write(f"Employee Name |:{name}\n")
    f.write(f"Basic Pay |: {str(basic)}\n")
    f.write(f"Allowances |:{str(allowance)}\n")
    f.write(f"gross salary |:{str(gross)}\n")
    f.write(f"Deduction: |{str(deduction)}\n")
    f.write(f"Net salary: |{str(net)}\n")
