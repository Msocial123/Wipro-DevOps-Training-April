#loops
#for loop

# print the numbers from 1 to 10
# print(f"number :1")
# print(f"number :2")
# print(f"number :3")
# predefined function range() its is going to provide the numbers for given sequence 
# for number in range(1,11):
#     print(number)

# loop through servers to deploy code:
# servers =["server1","server2","server3"]
# for server in servers:
#     print(f"Deploying the code to {server}")

#while loop
# count=1
# while count<=5:
#     print(count)
#     count +=1

# while False:
#     print("runs forever")
# stop when the number / range mets at 5 Break
# for number in range(1,11):
#      if number == 5:
#        # print(number)
#         break
#      print(number)
# continue:
# for number in range(5):
#     if number == 2:
#         continue
#     print(number)
#pass
# for number in range(5):
#     if number == 2:
#         pass
#     print(number)

# nested loops
# for i in range(3):
#     for j in range(2):
#         print(i,j)

#loop with else block:

# for i in range(3):
#     print(i)
# else:
#     print("loop is finished")

# loop through list

# servers=["webserrver","db1","nginix"] #list
# for server in servers:
#     print(server)

# servers=["webserver","db1","nginix"] #list

# for i,server in enumerate(servers):
#     print(i,server)


# data={"name":"Murali","mobile":123456789}
# for key,value in data.items(): #it is built in method  of the dictionary datat type used to retrive a dynamic "view " op all key-value pairs in the dictionary 
#     print(key,value)

# 1. check multiple server status 
#2.read the logs line by line 
# with open("log.txt") as file
#     for line in file:
#         print(line)
# 3.retry mechanism (while loop)
# retry =0
# while retry < 3:
#     print("trying to  connect....")
# retry += 1
# 4. Automating file processing 

# files=["a.tx","logs.txt","data.csv"]

# for file in files:
#     print(f'processing {file}')

# Functions:
# print("start")
# def greet():
#     print()   
# greet()
# print ("end")
# print("wake up ")
# print("start machine")
# print("make a coffee")
# print("add more milk")
# print("enjoy it")
# print("working for a while")
# print("wake up ")
# print("start machine")
# print("make a coffee")
# print("add more milk")
# print("enjoy it")

# def make_coffe():
#     print("start machine")
#     print("make a coffee")
#     print("add more milk")
#     print("enjoy it")

# print("wake up")
# make_coffe()
# print("working for a wile " )
# make_coffe()
#built in function (just calling)
# print(len("python"))
# #functions from libraries (IMport tehn call)
# import math
# number=4
# print(math.sqrt(number))

#function defination
# def multiply_two(X):
#     print(X*2)
# #function call

# for i in range(1,11):
#     multiply_two(i)

# functions with return 
# def multiplication(a,b):
#      return a * b

# # print(multiplication(5,2))
# result=multiplication(5,2)
# print(result)

# default arguments:
# def multiplication(a=5,b=2):
#      return a * b
# print(multiplication())

#lambda functions:anonymous function 
# 
# lambda
# logic or expressions --> quick and custome logic  -
# def tax(price):
#     return price*1.2
# tax= lambda price:price*1.2
# print(tax)

# output(result)= lambda  X(input): expression (function,methods,loops,check condition )

# multiple =lambda X:X*2
# print(multiple(2))

# add = lambda x,y:x + y
# print(add(1,2))

# check = lambda i: i in  "python"
# print(check('p'))

# numbers= [1,2,3,4] #list 
# result=map( lambda X: X * X,numbers)
# print (list(result))

# a=10
# b=20
# sum=a+b
# print(sum)
# a=input("enter a Value")
# b=input("enter b value ")
# print(type(a))
# print(type(b))
# sum=a+b
# print(type(sum))

# a=int(input("enter a Value"))
# b=float(input("enter b value "))
# print(type(a))
# print(type(b))
# sum=a+b
# print(sum)


#recursive function example factorial 
# 0!=1
# 1!=1*1=1
# 4! =4*3*2*1=24
# 10 =10*9*8*7*6*5*4*3*2*1
# def factorial(n):
#     if n ==0 or n == 1:
#         return 1
#      #recursive step  n!= n * (n-1)
#     print(n)
#     return n * factorial(n -1)
# number=4
# result=factorial(number)
# print(f"the factorial of {number} is : {result}")

#automated Deployment script ... simulating CI/CD pipelines 

# def pull_code():
#     print("pulling the latest code from the GIt")

# def build():
#     print("BUilding the application")

# def deploy():
#     print("Deployong the application")

# def pipeline():
#     pull_code()
#     build()
#     deploy()
# pipeline()

#import math complete module
# from math import sqrt,pi... specified function
# from math import * --- import everything , --- not at all recomended 
# import datetime as dt  -- importing module specifying alias names 

import caluculator  # userdefined module 

print(caluculator.addition(10,20))
