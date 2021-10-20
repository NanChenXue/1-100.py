def getNumbers():
    lt=[]
    x=input("请用户输入一列数(回车结束)：")
    while x!="":
        lt.append(eval(x))
        x=input("请用户输入一列数(回车结束)：")
    return lt

def sum(lt):
    s=0.0
    for x in lt:
        s+=x
    return s

def avg(lt):
    return sum(lt)/len(lt)

def dev(lt):
    s=0.0
    avg1=avg(lt)
    for x in lt:
     s+=(x-avg1)**2
    return s/len(lt)


def mean(lt):
    lt.sort()
    size=len(lt)
    if size%2==1:
        return lt[size//2]
    else:
        return (lt[size//2-1]+lt[size//2])/2

def main():
    numbers=getNumbers()
    s=sum(numbers)
    avg1=avg(numbers)
    dev1=dev(numbers)
    mean1=mean(numbers)
    print("这列数的个数是{4:d}和{0:.2f}平均值{1:.2f}方差{2:.2f}中位数{3:.2f}".format(s,avg1,dev1,mean1,len(numbers)))

main()
