pi=0
for k in range(0,100):
    pi+=1/16**k*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))
print("{0:20.15f}".format(pi))


# import random
# import math
# import time
#
# datas=1000*1000
# start=time.perf_counter()
# n=0
# for i in range(datas):
#     x,y=random.random(),random.random()
#     d=math.sqrt(x**2+y**2)
#     if d<=1:
#         n+=1
# end=time.perf_counter()
# print("{0:20.10f}".format(4*n/datas))
# print("共用时{0}秒".format(end-start))