import requests
import json
import csv
import time
timeStamp=time.time()#获取当前时间戳
while 1:
    timeArray=time.localtime(timeStamp)#把当前时间戳转换为字符日期20200927
    otherStyleTime=time.strftime("%Y%m%d",timeArray)
    print('现在采集日期为：',otherStyleTime)
    headers={
    'Accept':'*/*',
    'Accept-Encoding':'gzip,deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'Cookie':'Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1601194236;_lxsdk_cuid=174ce9d18dc25-0d866ac4f28946-3323765-1fa400-174ce9d18ddc8;_lxsdk=FFD573E0009811EB908019617B169A639F4CF6C176274B27832557D99DE65A9C;Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1601194238;__mta=143611146.1601194236831.1601194236831.1601194237906.2;__mta=143611146.1601194236831.1601194300248.1601194367003.6;_lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic;_lxsdk_s=174ce9d18dd-b0f-d3c-ee8%7C%7C21',
    'Host':'piaofang.maoyan.com',
    'Referer':'http://piaofang.maoyan.com/dashboard/movie?date=2020-09-01',
    'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/84.0.4147.105Safari/537.36',
    'X-FOR-WITH':'VM0S7spZmi3r0K1xWgprtKgk/zPczq89iLNLriGOr/YMi/h4h2uiGeitd3isFm29DdSrYLwNyISQrCgokSVVYNpARtuGpIisqS0hBWpqQi9bU92W7/q4GK+XERysFue1MSWw0sXRkDLsoijdnMkRdKJyXKS9vG6rL6PeKNKX8su2ziWaDGXkJWPZ6YjxeKWWkSdCJxhZt5MiVWM+46WiUA==',
    }
    url='http://piaofang.maoyan.com/dashboard-ajax/movie?showDate='+otherStyleTime#拼接url达到获取第一天数据的结果
    timeStamp=timeStamp-86400#把时间戳减去一天的秒数这样就能下一次 转换时间戳时获取到上一天的时间
    html=requests.get(url=url,headers=headers)
    datas=json.loads(html.text)#把数据解析成json对象
    #取出中间需要的电影数据列表  print(datas['movieList']['list'])
    for data in datas['movieList']['list']:
        print(otherStyleTime,data['movieInfo']['movieName'],data['movieInfo']['releaseInfo'],data['sumBoxDesc'])
        t=open('text.csv','a+',encoding='utf-8_sig',newline='')
        c=csv.writer(t)
        c.writerow([data['movieInfo']['movieName'],data['movieInfo']['releaseInfo'],data['sumBoxDesc']])
        #在列表中找出我们要的数据进行保存
        if otherStyleTime=='20200901':
            break