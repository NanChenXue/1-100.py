import requests
import csv
import json
import time
timeStamp=time.time()
while 1:
    timeArray=time.localtime(timeStamp)
    otherStyleTime=time.strftime("%Y%m%d",timeArray)
    print('现在采集日期为：',otherStyleTime)
    headers={
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': '_lxsdk_cuid=174cee32999c8-0508e64ce7d005-333376b-e1000-174cee3299ac8; _lxsdk=174cee32999c8-0508e64ce7d005-333376b-e1000-174cee3299ac8; _lxsdk_s=174cf3de975-a53-794-cbc%7C%7C4',
    'Host': 'piaofang.maoyan.com',
    'Referer': 'http://piaofang.maoyan.com/dashboard/movie?date=2020-09-02',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'X-FOR-WITH': 'O1XHiCFALwCbAwwIaVEfn7YbeTesIX1W53TkwTm4crN9Z9uj4ecNRzxHFI3IWn/r2mU9q80Tj+3wU7QtrB+TLZHuuCTJrlG7Xe/FfNHZAaEDpYvfUX0WsWZESR/nRVr3+8wYRfFGfwK0mPC97NpJBv+SGPCPOvD/t95NRk30ImKmSIfr/m7lOn29EE61o52fSpvQ/N70SQenIgqNMNBhzw==',
    }
    url='http://piaofang.maoyan.com/dashboard-ajax/movie?showDate='+otherStyleTime
    timeStamp=timeStamp-86400
    html=requests.get(url=url,headers=headers)
    datas=json.loads(html.text)
    #print(datas['movieList']['list'])
    for data in datas['movieList']['list']:
        print(otherStyleTime, data['movieInfo']['movieName'], data['movieInfo']['releaseInfo'], data['sumBoxDesc'],data['boxSplitUnit']['num'],
              data['boxRate'],data['showCount'],data['showCountRate'],data['avgShowView'],data['avgSeatView'])
        t = open('text.csv', 'a+', encoding='utf-8_sig', newline='')
        c = csv.writer(t)
        c.writerow([data['movieInfo']['movieName'], data['movieInfo']['releaseInfo'], data['sumBoxDesc'],
                    data['boxSplitUnit']['num'],data['boxRate'],data['showCount'],data['showCountRate'],data['avgShowView'],data['avgSeatView']])
    if otherStyleTime=='20200902':
        break