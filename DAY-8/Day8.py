# import asyncio
# import time
 
# # ─── Without async (slow) ─────────────────────────────────────
# def check_server_sync(server):
#     time.sleep(1)   # Simulates a network call that takes 1 second
#     return f'{server}: OK'
 
# def check_all_sync(servers):
#     results = []
#     for server in servers:
#         results.append(check_server_sync(server))  # Waits for each one
#     return results
 
# # ─── With async (fast) ────────────────────────────────────────
# async def check_server_async(server):
#     await asyncio.sleep(1)   # Async sleep — releases control while waiting
#     return f'{server}: OK'
 
# async def check_all_async(servers):
#     # Create all tasks at once
#     tasks = [check_server_async(s) for s in servers]
#     # Run all tasks concurrently, wait for all to finish
#     results = await asyncio.gather(*tasks)
#     return results
 
# # Run the async function
# servers = ['web-01', 'web-02', 'web-03', 'db-01', 'cache-01']
# start=time.time()
# # results=check_all_sync(servers) sync run
# results = asyncio.run(check_all_async(servers))
# elapsed = time.time() - start
# print(f'Time: {elapsed:.1f}s') 
# # print(time.time())
# # for r in results:
# #     print(r)
# # print(f'Time: {elapsed:.1f}s')   # ~1.0s instead of ~5.0s!

# import asyncio
# import aiohttp
 
# async def check_endpoint(session, server):
#     '''Checks the health of one server endpoint'''
#     url = f'http://{server}/health'
#     try:
#         async with session.get(url, timeout=aiohttp.ClientTimeout(total=5)) as resp:
#             if resp.status == 200:
#                 data = await resp.json()
#                 return {'server': server, 'status': 'healthy', 'data': data}
#             else:
#                 return {'server': server, 'status': 'unhealthy', 'code': resp.status}
#     except asyncio.TimeoutError:
#         return {'server': server, 'status': 'timeout'}
#     except aiohttp.ClientConnectorError:
#         return {'server': server, 'status': 'unreachable'}
 
# async def health_check_fleet(servers):
#     '''Run health checks on all servers concurrently'''
#     async with aiohttp.ClientSession() as session:
#         tasks = [check_endpoint(session, s) for s in servers]
#         results = await asyncio.gather(*tasks)
    
#     healthy   = [r for r in results if r['status'] == 'healthy']
#     unhealthy = [r for r in results if r['status'] != 'healthy']
    
#     print(f'Health Check Complete: {len(healthy)}/{len(results)} healthy')
#     for r in unhealthy:
#         print(f'  ALERT: {r["server"]} — {r["status"]}')
#     return results
 
# servers = ['192.168.192.1', '10.0.0.2', '10.0.0.3', '10.0.0.4', '10.0.0.5']
# asyncio.run(health_check_fleet(servers))


import asyncio
hosts=["google.com","github.com","openai.com"]
async def ping(hosts):
    proc=await asyncio.create_subprocess_exec(
        "ping", "-n","1",hosts,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE

    )
    out,err=await proc.communicate()
    if proc.returncode == 0:
        print(f'{hosts} up')
    else:
        print(f'{hosts} down')

async def main():
    await asyncio.gather(*(ping(h) for h in hosts))

asyncio.run(main())

#---not use asyn---
# avoid if task is CPU-heavy 
        #-video encoding 
        #huge compression 
        # MLtraing
        # large parsing 


# post request:-

# import requests

# url='https://jsonplaceholder.typicode.com/posts'
# data={
# 'title':'test',
# 'body':'adding for checklist',
# 'userId':101
# }
# response=requests.post(url,data)
# #check if the request was successful(HTTP satatus code 201 fro created )
# if response.status_code==201:
#     print(f'success , new post created with {response.json()["id"]}')
# else:
#     print(f'ERROR {response.status_code}')


#put and delete 
# import requests
# #define the URL and Updated Data 
# url='https://jsonplaceholder.typicode.com/posts'
# data={
# 'id':92,
# 'title':'id minus libero illum nam ad officiis',
# 'body':'earum voluptatem facere provident blanditiis velit laboriosam\npariatur accusamus odio saepe\ncumque dolor qui a dicta ab doloribus consequatur omnis\ncorporis cupiditate eaque assumenda ad nesciunt',
# }
# #make  a PUT request to update the resource 

# response=requests.put(url,data)
# #check if the request was successful(HTTP satatus code 200 fro created )
# if response.status_code==200:
#     print(f'success ,  post updated {response.json()}')
# else:
#     print(f'ERROR {response.status_code}')

# #make a DELETE request to delete the resource 
# response=requests.delete(url)
# #check if the DELETE request was succesfull (200 for ok)
# if response.status_code==200:
#     print("success post deleted ")
# else:
#     print(f'ERROR {response.status_code}')

#weather report generation

# import requests
# api_key="d7f0a9c19c0a348daed92969e0565afe"
# city="Bangalore"
# # url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
# url=f'https://wttr.in/{city}?format=j1'
# response=requests.get(url)
# # print(response.status_code)
# print(response.json()["current_condition"][0]["temp_C"])

# import requests
# api_key="d7f0a9c19c0a348daed92969e0565afe"
# city="Chennai"
# url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

# response=requests.get(url)
# # print(response.status_code)
# data=response.json()
# print('City :',data['name'])
# print('Temparature :' ,data['main']['temp'],'C')
# print('weather :',data['weather'][0]['description'])
# print('Humidity',data["main"]["humidity"],"%")
# print("wind Speed",data['wind']['speed'],'m/s')
# print("timezone",data['timezone'])







