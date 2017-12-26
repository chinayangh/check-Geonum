# -*- coding: utf-8 -*-
#import openpyxl
#import urllib3
#import json
import os
#import time
#import http.client
import requests
import linecache


#f = open("input.txt","r",1000,"utf-8")
for i in range(1,10):
    count = linecache.getline('input.txt',i)
    hao = count.rstrip("\n")
# for line in f:
#     #print(line)
#     hao=line.rstrip("\n")
    
    url = 'https://cx.shouji.360.cn/phonearea.php?number=' + hao
    # r = requests.get('https://cx.shouji.360.cn/phonearea.php?number=13838384380')
    # url = 'https://cx.shouji.360.cn/phonearea.php?number=' + hao
    r = requests.get(url)
    msg=r.json()
    #print(msg)
    if len(msg["data"]["city"]) == 0:
        msg["data"]["city"] = msg["data"]["province"]
    value_list = list(msg["data"].values())
    #print(value_list)
    txt = open("data.txt", "a")
    #print( hao[:-1], ":", value_list[1],)
    print(i,":",hao, ":", value_list[1], )
    #print(hao, ":", hao, ":", value_list[1], file=txt)
    print(hao, ":", value_list[1], file=txt)
    txt.close()
# urllib3.disable_warnings()
# headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36"}
# http = urllib3.PoolManager(timeout=10000.0)
# while 1:
#     lines = f.readlines()
#     if not lines:
#         break
# for line in f:
#             print(line)
#             hao=str(line)
#             time.sleep(5)
#             url = 'https://cx.shouji.360.cn/phonearea.php?number=' + hao
#             print(url)
#             # r = http.request('GET','https://cx.shouji.360.cn/phonearea.php?number=13396590555').data
#             urllib3.disable_warnings()
#             r = http.request('GET', url,headers=headers).data
#             time.sleep(5)
#             #print(r)
#             msg = json.loads(r.decode('utf-8'))
#             print(msg)
#             if len(msg["data"]["city"]) == 0:
#                 msg["data"]["city"] = msg["data"]["province"]
#             value_list = list(msg["data"].values())
#             time.sleep(5)
#             txt = open("data.txt", "a")
#             print(line, ":", hao, ":", value_list[0], value_list[1])
#             print(line, ":", hao, ":", value_list[0], value_list[1], file=txt)
#             txt.close()

os.system("pause")
