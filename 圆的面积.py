try:
    a=input("请输入一个带符号的数字：")
    if a[-2] in ['cm','CM']:
        s=eval(a[0:-2])*0.1
        print("对应的分米是{:.2f}s".format(s))
    elif a[-1] in ['m','M']:
        c=eval(a[0:-1])*0.01
        print("对应的米是{:.2f}c".format(c))
    else:
        print("您输入的数字有误！")
except:
    print("您输入的数据有误")
