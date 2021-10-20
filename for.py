# s="Hello World"
# i=eval(input("请输入一个整数："))
# if i==0:
#     print(s)
# elif i<0:
#     for c in s:
#         print(c)#默认换行
# else :
#     for n in range(0,len(s),2):
#         print(s[n:n+2])
# d= {'a': 1, 'b':2, 'b': '3'}
# a={'a': 1, 'b':2}
# c=d^a
# print(c)
# a=['a','b','c']
# c=['d','e']
# b=a.append(c)
# print(a)
# k=10000
# s=0
# while  k>1:
#
#        print(k)
#
#        k=k/2
#        s+=1;
# print(s)
try:
    weight = eval(input("请输入体重kg:"))
    height = eval(input("请输入身高cm:")) / 100
except:
    print("您输入的数据有误！")
else:
    s = weight / (height * height)
    if s < 18.5:
        print(s)
        a, b = "偏瘦","偏瘦";
    elif s <= 24:
        print(s)
        a, b = "正常", "偏胖";
    elif s <= 25:
        a, b = "偏胖";
    elif s <= 28:
        a, b = "偏胖", "肥胖";
    elif s <= 30:
        a, b = "偏胖","肥胖";
    else:
        a,b="肥胖","肥胖";
print(a,b);
