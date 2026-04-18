
# import sys
# text = sys.stdin.read()
# print(text.upper())

# import sys
# sys.stdout.write("Deployment started\n")
# import sys
# sys.stderr.write("Kubernetes connection failed\n") # used to seperate error message as log file 
import sys

# tests_passed = False
# file='a.txt'
# if not tests_passed:
#     sys.stderr.write("Tests failed\n")
#     sys.exit(1)

# import sys

# print("Starting deployment")
# sys.stderr.write("Database connection warning\n")
# sys.stderr.write("server is not running \n")
# print("Deployment complete")
# print("servers are running ")

import subprocess
import sys
# subprocess.run("echo Hello Student",shell=True)
# subprocess.run("echo Hello Student", shell=True)
# subprocess.run(["ping", "google.com"])
# result = subprocess.run(
#     ["ipconfig"],
#     capture_output=True,
#     text=True
# )
# print(result.stdout)
# print(type(result))
# import subprocess

# result = subprocess.run(
#     ["ipconfig"],
#     capture_output=True,
#     text=True
# )

# with open("output.log", "w", encoding="utf-8") as f:
#     f.write(result.stdout)

# print("Saved successfully.")
# subprocess.run(
#     ["ping", "google.com"],
#     timeout=5
# )
# process = subprocess.Popen(
#     ["ping", "google.com"],
#     stdout=subprocess.PIPE,
#     text=True
# )

# for line in process.stdout:
#     print(line.strip())

# subprocess.run("pip","install","requests")
# subprocess.Popen("calc.exe")
# subprocess.Popen("notepad.exe")
# print("caluculator opened")
# import revision
# print(revision.gross)

# output=subprocess.check_output(["python", "--version"],text=True)
# print(output)
# output=subprocess.check_output(["ping", "google.com"],text=True)
# print(output)
# output=subprocess.check_output(["wmic","logicaldisk","get","size"],text=True)
# print(output)

# process=subprocess.Popen(
#     ["git","--version"],
#     stdout=subprocess.PIPE,
#     stderr=subprocess.PIPE,
#     text=True
# )
# out,err=process.communicate()
# print(out,err)
# subprocess.run(["python",".\day1.py"])

# import logging

# logging.warning("Low diskspace")
# import logging
# logging.basicConfig(filename='namecheck.log',level=logging.DEBUG)
# logging.disable()
# def namecheck(name):
#     if len(name)< 2:
#         logging.debug("checking for name length")
#         return 'invalid name'
#     elif name.isspace():
#         logging.debug('checking if the name has spaces.....')
#         return 'invalid name'
#     elif name.isalpha():
#         logging.debug('checking if the name is alphabet...........')
#         return 'invalid name'
#     elif name.replace(' ','').isalpha():
#         logging.debug('checking for full name .....')
#         return 'invalid name'
#     else:
#         logging.debug("failed all the cases ")
#         return 'invalid name '
# logging.debug(namecheck('1'))

# import logging
# logging.basicConfig(filename='log_level.log')
# logging.debug('this is a debug message')
# logging.info('this is a INFO message')
# logging.warning('this is WARNING message')
# logging.error('thi is ERROR message')
# logging.critical('this is CRITICALL message')

# by default warning is having heighest priority , from that warning remaining all is going to print 

# import logging
# logging.basicConfig(filename='log_level.log',filemode='w',level=logging.ERROR) # by default file mode is append 
# logging.debug('this is a debug message')
# logging.info('this is a INFO message')
# logging.warning('this is WARNING message')
# logging.error('thi is ERROR message')
# logging.critical('this is CRITICALL message')

import logging
logging.basicConfig(filename='log_level.log',level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s') # by default file mode is append 
logging.debug('this is a debug message')
logging.info('this is a INFO message')
logging.warning('this is WARNING message')
logging.error('thi is ERROR message')
logging.critical('this is CRITICALL message')
