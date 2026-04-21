
# try:
#     num=10/52
# except:
#     print("error occured , devide by zero is not possible")
# print("end of program")

# try:
#     number=int(input("enter the mobile number"))
#     print(number)
# except ValueError:
#     print("invalid number")

# try:
#     x=int(input("enter numbe:"))
#     div=10/x
#     print("the result is ",div)
# except ValueError:
#     print(" enter only the integer values ")
# except ZeroDivisionError:
#     print("cannot devide by zero.....")


# try:
#     x=int(input("enter numbe:"))
#     div=10/x
#     print("the result is ",div)
# except Exception as e:
#     print(e)
# full syntax for exceptions:
# try:
#     code()
# except error1:
#     code:
# except error2:
#     code:
# else:
#     code
# finally:
#     code

# else block it can execute when only there is no exceptions;;;

# try:
#     x=int(input("enter numbe:"))
#     div=10/x
   
# except Exception as e:
#     print(e)
# else:
#      print("the result is ",div)
# finally:
#     print("closing the program ")


# try:
#     x=int(input("enter numbe:"))
#     div=10/y
   
# except Exception as e:
#     print(e)
# else:
#      print("the result is ",div)
# finally:
#     print("closing the program ")


# age= -1
# try:
# if age<0:
# raise ValueErrorError("age cannot be negative")

# class ServerDownError(Exception):
#     pass
# raise ServerDownError("production server is down")

# nested try-except:

# try:
#     try:
#         x=10/0
#     except:
#         print("inner error")
#     x=10/0
# except:
#     pass

# try:
#     age=int(input("enter the age"))
#     if age >18:
#         print("eligible for voting ")
# except Exception as e:
#     print(e)
# else:
#      print("not eligible for voting ")
# finally:
#     print("closing the program ")

# you have to restart the ngnix web server automatically:

# import subprocess
# try:
#     print("restarting Nginx services.......")

#     subprocess.run(
#         ["services.msc","restart","nginx"], #systemctl for linux os
#         check=True
#     )
#     print("ngnix aerver restarted succesfully")
# except FileNotFoundError:
#     print("systemctl command not found ")
# except PermissionError:
#     print("permission denied run with sudo")
# except subprocess.CalledProcessError:
#     print("Nginx service restart failed")
# except Exception as e:
#     print("unexpected Error",e)
# finally:
#     print("execution completed ")

# info = 0
# error = 0
# warning = 0
# try:
#     with open("log_level.log", "r") as file:
#         for line in file:
#             if "INFO" in line:
#                 info += 1
#             elif "ERROR" in line:
#              error += 1
#             elif "WARNING" in line:
#                 warning += 1


#         print("INFO:", info)
#         print("ERROR:", error)
#         print("WARNING:", warning)

# except FileNotFoundError:
#     print("PLEASE PROVIDE VALID FILE ")

# class Employee:
#     company="solution"
#     print("company",type(company))
#     def __init__(self):
#         pass
# emp=Employee()
# emp1=Employee()
# print("identification emp",id(emp))
# print("identification emp1",id(emp1))
# print(emp)
# print(emp1)
# print("type of object",type(emp))

# class Student:
#     def __init__(self):
        
#         self.name="murlai"
#         self.rollno=101
#         self.mark=90
#     def details(self):
#         print("hello i am ",self.name)
#         print("my roll number ",self.rollno)
#         print("marks  are ",self.mark)

# s=Student()
# s.details()
# print(s.name)
# print(s.rollno)
#constructor 
# class Student:
#     def __init__(self):
#         print("constructor execution ....")
#         self.name="murlai"
#         self.rollno=101
#         self.mark=90
#     def details(self):
#         print("hello i am ",self.name)
#         print("my roll number ",self.rollno)
#         print("marks  are ",self.mark)

# s=Student()
# s2=Student()
# s3=Student()
# print(id(s))
# print(id(s2))

# class Student:
#     def __init__(self,name,roll,marks):
#         self.name=name
#         self.roll=roll
#         self.marks=marks
#     def display_students(self):
#         print("name",self.name)
#         print("roll number",self.roll)
#         print("marks ",self.marks)

# s1=Student('murlai',1001,99)
# s1.display_students()

# class Test:
#     def __init__(self):
#         print("address of object refered by self:,",id(self))

# t=Test()
# print("Address of object referenced b T",id(t))


# class Student:
#     def __init__(self,name,roll,marks):
#         self.name=name
#         self.roll=roll
#         self.marks=marks
#     def display_students(self):
#         name="heloo"
#         print("name",self.name)
#         print("roll number",self.roll)
#         print("marks ",self.marks)
        
# s1=Student('murali',1001,99)
# s2=Student('mohan',1002,98)
# s1.display_students()
# s2.display_students()

# 

#encapsulation:-
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.__salry=salary #private 
#     def show_salary(self):
#         print("salary :",self.__salry)
#     def increase_salary(self,amount):
#         self.__salry+=amount
#         print("salary updated ")

# e1=Employee("ravi ",500000)
# e1.show_salary()
# e1.increase_salary(5000)
# e1.show_salary()

#polymorphism
# class UPI:
#     def pay(self):
#         print("paid using UPI")
# class Card:
#     def pay(self):
#         print("paid using CARD")
# class Netbanking:
#     def pay(self):
#         print("paid using Netbanking")

# method=[UPI(),Card(),Netbanking()]
# for m in method:
#     m.pay()
class AWS:
    def __init__(self):
        pass
    def deploy(self):
        print("deployed to AWS")
class Azure:
    def deploy(self):
        print("deployed to Azure")
class GCP:
    def deploy(self):
        print("deployed to GCP")
ob=AWS()
ob.deploy()
# provider=[AWS(),Azure(),GCP()]
# AWS.deploy()
# # aws.deploy()
# # a=Azure()
# # a.deploy()
# gcp=GCP()
# # gcp.deploy()