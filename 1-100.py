import requests
from bs4 import BeautifulSoup
page=0
count=1#定义count用于计数
while 1:
    url='https://movie.douban.com/top250?start=%s&filter='%(str(page*25))
    page=page+1#让page加1 用于下一页
    headers={
    'Cookie': 'bid="KkHt/HwdmFU"; ll="118184"; __yadk_uid=tSl5oJyxpA23qoCxD3YC53yANoBHYHfz; _vwo_uuid_v2=D44A39D1FE90BD73B0F4CDBB3B962DE40|42e5777a99d842410ac944520b5dc0cf; __gads=ID=5c68e3ec112b36ef:T=1596509028:S=ALNI_MYivpaKzGLLKWXhW-Lwx07Oj3H2-w; __utmz=30149280.1597490135.3.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1601186724%2C%22https%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3D%25E8%25B1%2586%25E7%2593%25A3%26rsv_spt%3D1%26rsv_iqid%3D0xbd41aafc000c167e%26issp%3D1%26f%3D8%26rsv_bp%3D1%26rsv_idx%3D2%26ie%3Dutf-8%26tn%3Dbaiduhome_pg%26rsv_enter%3D1%26rsv_dl%3Dtb%26rsv_sug3%3D9%26rsv_sug1%3D14%26rsv_sug7%3D101%26rsv_sug2%3D0%26rsv_btype%3Di%26inputT%3D5105%26rsv_sug4%3D5105%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.930129377.1596428139.1597490135.1601186725.4; __utmb=30149280.0.10.1601186725; __utmc=30149280; __utmc=223695111; __utma=223695111.814282256.1596428139.1601186725.1601186744.4; __utmb=223695111.0.10.1601186744; __utmz=223695111.1601186744.4.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_id.100001.4cf6=3d761a48b66dc337.1596428138.3.1601186850.1596509028.',
    'Host': 'movie.douban.com',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    html=requests.get(url,headers=headers)#获取第一页的网页远源码
    soup=BeautifulSoup(html.text,'lxml')#把源码解析成bs4对象 源代码，解析器
    titles=soup.find_all(attrs={'class':'hd'})#通过bs4对象的定位方法定位到class=hd的元素块们
    for title in titles:#循环访问这些元素块
        print(count,title.text.replace('\n','').replace(' ',' '))#取出单个块内的文字去除空格与换行
        count=count+1
        print('------------')









