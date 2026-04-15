#addition of two numbers  single line comment 
''' multiple line comments  
svfdfdf
dsf
fd
f
df
f
'''
# Data types  
# when ever decalring variables , the variable name must strat with alphabet or '_', maximum length 30 
# a=10 #integet
# b=3.15 # float
# c="Servers" #string represents a text or sequence of characters that can be written inside a single or double quotes 
# d='weebserver' #String 
# f=True #boolean type and case sensitive they must start with Capital letter  , can be either True oor False , its is ued to handle logic and decision making 
# g=False     # boolean
# h=None  #Nonetype ,, means "no value , "nothing ", unknown ", its is uded to show absence of any data 
# i=""    #string  blank , string value with no characters inside , it is not same as None!
# j="  "# strig - empty spaces ,string value with one or more spaces , and it is not same as NOne!
# type() function which is used to  find out what type of dat type  it shoud wotk with print(type()) function only 
# print(type(a)) #every variable consider as object type only 
# print (type(b))
# print (type(c))
# print (type(f))
# print (type(h))

# port_number=8080 #int
# cpu_usage=73.56 #float
# server_name='web-server-01' #string 
# is_healthy=True #bool
# servers=["web1","web2","db1","cache1"]# list
# server_ifo={
#     "name":"web-server-01",
#     "ip":"10.0.0.1",
#     "port":80,
#     "active":True
# } # dictionary 

# print("ip address " ,server_ifo["ip"]) # print ip address 
# print("port number ",server_ifo["port"]) # print ip address 
# print("server_info",server_ifo)

# print("server list",servers)

# print("server list is:\n",servers[2])

# print("server ",server_name,"running on port ",port_number)
# # output formating type  by using format string 
# print(f"server {server_name} running on port number {port_number}")

# a+=20 # a=a+20
# a-=20 # a=a-20 (10-20)
# print (a)

#monitoring CPU usage and raising the alers

cpu_usage=30# simulated current CPU usage 

if cpu_usage>=90:
    print("CRITICAL:CPU usage is dangerously high")
    print("ACTION: triggering auto scale ")
elif cpu_usage>=75:
    print("WARNING: CPU usage is elevated ")
    print("ACTION:  Sending alert to slack ...")
elif cpu_usage>=50:
    print("INFO : CPU usage is moderate.")
else:
    print("OK: CPU usage is normal ")
