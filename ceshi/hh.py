from bs4 import BeautifulSoup
doc='''
<html>
<head>
<title>标题标签练习</title>
</head>
<body>
    <a href="www.baidu.com">农业农村部:设立涉农热线 有效助推春季农业生产</a>
    <a class="a1">工信部:做好疫情防控期间宽带网络助教助学工作</a>
    <a>国家卫健委发布新冠肺炎诊疗方案（试行第七版）</a>
    <a>易地扶贫搬迁后续扶持措施出台 保群众合法权益</a>
</body>
</html>
'''
soup=BeautifulSoup(doc,'html.parser')
#s=soup.prettify() #转换成字符串

#查找文档中class=“a1”的a标签
#tag=soup.find("a",attrs={"class":"a1"})

#获取元素的属性值tag["属性值"]
#tag=soup.find("a")
#print(tag["href"])

#获取元素的文本值tag.text
tags=soup.find_all("a")
for tag in tags:
 print(tag.text)
