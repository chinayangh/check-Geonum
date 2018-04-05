# -*- coding: utf-8 -*-
#import openpyxl
#import urllib3
#import json
import os
#import time
#import http.client
import requests
import linecache
import re


#f = open("input.txt","r",1000,"utf-8")
for i in range(8545, 8555):
    count = linecache.getline('book2.txt', i)
    hao = count.rstrip("\n")
    #print(hao)
# for line in f:
#     #print(line)
#     hao=line.rstrip("\n")

    url = 'http://m.ip138.com/mobile.asp?mobile=' + hao
    #url = 'https://cx.shouji.360.cn/phonearea.php?number=' + hao
    # r = requests.get('https://cx.shouji.360.cn/phonearea.php?number=12345678900')
    s = requests.Session()
    # with requests.Session() as s:
    #     s.get(url)
    #r = s.get(url)
    #msg=s.get(url).json()
    #page=[]
    msg = s.get(url).text
    #print(msg)
    # m_tr = re.findall(r'<td>卡号归属地.*?<\/tr>', msg, re.I|re.S|re.M)
    # words=str(m_tr)
    # m_td = re.findall(r'<span>(.*?)</span>', words, re.S|re.M)
    m_td = re.findall(r'<span>(.*?)</span>', msg, re.S | re.M)
    #print(m_tr)
    #print(m_td)
    txt = open("data-test.txt", "a")
    if len(m_td[1]) == 2:
        print(i, ":", hao, ":", m_td[1])
        print(i, ":", hao, ":", m_td[1], file=txt)
        continue
    print(i, ":", hao, ":", str(m_td[1])[3:5])
    print(i, ":", hao, ":", str(m_td[1])[3:5], file=txt)
    txt.close()
    # for line in m_tr:
    #     print(line)
        #words_box = []
        # #if re.search('[<td>]{1}[卡]{1}[号]{1}[归]{1}[属]{1}[地]{1}', line):
        #     words_box.extend(line.strip().split())

    # if len(msg["data"]["city"]) == 0:
    #     msg["data"]["city"] = msg["data"]["province"]
    # value_list = list(msg["data"].values())
    # # #print(value_list)
    # txt = open("data-test.txt", "a")
    # # #print( hao[:-1], ":", value_list[1],)
    # print(i, ":", hao, ":", value_list[1], )
    # print(i, ":", hao, ":", value_list[1], file=txt)
    # # print(hao, ":", value_list[1], file=txt)
    # txt.close()
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
#             # r = http.request('GET','https://cx.shouji.360.cn/phonearea.php?number=12345678900').data
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
