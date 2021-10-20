# import jieba
# f=open("E:\\threekings.txt","r",encoding="utf-8")
# txt=f.read();#将文件读入到字符串变量txt
# words=jieba.lcut(txt)#分词处理 产生一个分词列表words
# counts={}
# for word in words:
#     if len(word)==1:
#         continue
#     else:
#         counts[word]=counts.get(word,0)+1
# items=list(counts.items())#将字典转换为列表，列表的元素是元组
# items.sort(key=lambda x:x[1],reverse=True)
# for i in range(15):
#     word,count=items[i]
#     print("{0}{1}".format(word,count))

import jieba
txt=open("E:\\threekings.txt","r",encoding="utf-8").read()
words=jieba.lcut(txt)
excludes=["将军","却说","今日","陛下","东吴","于是","魏兵","不敢","二人","不可","荆州","不能","如此","商议"]
counts={}
for word in words:
    if len(word)==1 or word in excludes:
        continue
    elif word in ["孟德","丞相","孟德曰","曹操"]:
        rword="曹操"
    elif word in ["孔明","孔明曰","诸葛亮"]:
        rword="诸葛亮"
    elif word in ["玄德","刘玄德","玄德曰","刘备"]:
        rword="刘备"
    elif word in ["云长","关羽长","关羽","关公"]:
        rword="关羽"
    elif word in ["张飞曰","张飞","张翼德","翼德"]:
        rword="张飞"
    elif word in ["赵云","赵子龙","子龙"]:
        rword="赵云"
    elif word in ["都督","周瑜"]:
        rword="周瑜"
    else:
        rword=word
    counts[rword]=counts.get(rword,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items[i]
    print("{0}{1}".format(word,count))