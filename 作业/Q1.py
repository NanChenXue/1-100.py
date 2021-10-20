import json
import requests
import csv
url="https://www.mmm920.com/products?coupon=0&keyword=ALL&points=0&redPacket=0"
headers={
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Authorization': 'null',
'Connection': 'keep-alive',
'Content-Length': '134',
'Content-Type': 'application/json',
'Host': 'w.mmm920.com',
'Origin': 'https://www.mmm920.com',
'Referer': 'https://www.mmm920.com/',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-site',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}
html=requests.post(url,headers=headers)
datas=json.loads(html.text)#把数据解析成json对象
for product in datas['products']:
    print(product['products']['name'])
    t = open('text.csv', 'a+', encoding='utf-8_sig', newline='')
    c = csv.writer(t)
    c.writerow(product['products']['name'])
