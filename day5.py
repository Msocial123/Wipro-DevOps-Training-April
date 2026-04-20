# import argparse
# parser=argparse.ArgumentParser(description="basic example")
# parser.add_argument("name",help="Enter your name ")
# parser.add_argument("mobile_number",type=int, help="enter your mobile number ")
# args=parser.parse_args()
# print("name",args.name)
# print("mobile",args.mobile_number)

# # file analizer
# import argparse
# parser=argparse.ArgumentParser(description="File analizer")
# parser.add_argument("filename",help="please put file name to analyze ")
# #optional flags 
# parser.add_argument("--lines",action="store_true",help="show line count") #short ---first character ,, long means full argument 
# parser.add_argument("--words",action="store_true",help="show words count")
# parser.add_argument("--chars",action="store_true",help="show character count")
# parser.add_argument("--cam",action="store_true",help="show character count")
# parser.add_argument("--all",action="store_true",help="shows full report")

# args=parser.parse_args()

# with open(args.filename,"r") as file:
#     data=file.read()
#     total_line=data.count("\n")+1
#     total_words=len(data.split())
#     total_chars=len(data)
# if args.all:
#     print(f"\n complete analysis report")
#     print("-" * 40)
#     print("Lines:",total_line)
#     print("Words",total_words)
#     print("Characters:",total_chars)
# else:
#     if args.lines:
#          print("Lines:",total_line)
#     if args.words:
#         print("Words",total_words)
#     if args.chars:
#         print("Characters:",total_chars)
#     if args.cam:
#         print("camera")
#     if not(args.lines or args.words or args.chars):
#         parser.print_help()
        



# from datetime import datetime
# Now=datetime.now()
# print(Now)

#if u want print only the date :-
from datetime import date ,datetime,timedelta
# today=date.today() to print current date only
# print(today)

# now=datetime.now()
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)
# print(now.strftime("%y-%m-%d"))#sting format time 
# print(now.strftime("%y/%m/%d"))
# print(now.strftime("%H:%M:%S"))
# print(now.strftime("%B:%A"))
#time differece
# start=datetime(2026,4,20,15,50,30)
# end =datetime(2026,4,20,18,30,30)
# dif=end-start
# print(dif)

# timedelta --> is a class eith in datetimemodules ,that represents a duration or the difference between 2 points in time
# now = datetime.now()
# after_5_days= now + timedelta(days=5)
# print(after_5_days)

# import time

# print("starting ")
# print("the name is ............")
# time.sleep(15) # hold the execution time in seconds 
# print("Murali  Mohan ")

# import time
# timenow=time.time()
# # convert time stamp:

# print(datetime.fromtimestamp(timenow))
# print(datetime.utcnow())

#weekday check 0--> monday and 1--> sunday 
# # today=date.today()
# daycheck=datetime(2026,4,26,15,50,30)
# print(daycheck.weekday())

# import calendar
# for month in range(1,13):
#     print(calendar.month(2026,month))

# backup file naming:-
from datetime import datetime,timedelta
# filename= "backup_" + datetime.now().strftime("%y%m%d_%H%M%S") + ".tx"
# print(filename)
#log analyzer
# log_date=date(2026,4,10)
# today_date=date.today()
# if today_date - log_date > timedelta(days=7):
#     print("archive logs ")
# else:
#     print("keep logs")



# AUTO DELETE OLD LOGS:

import os
from datetime import datetime,timedelta

log_dir =r"C:\Users\babud\Desktop\wipro"
retention_days=7
now=datetime.now()
cuttoff=now - timedelta(days=retention_days)
for filename in os.listdir(log_dir):
    filepath=os.path.join(log_dir,filename)

    filepath=os.path.join(log_dir,filename)
    if os.path.isfile(filepath):
        modified_time=datetime.fromtimestamp(os.path.getatime(filepath))

        if modified_time > cuttoff:
            print("delete :",filepath)
            os.remove(filepath)
        else:
            print("keeep:",filepath)


    