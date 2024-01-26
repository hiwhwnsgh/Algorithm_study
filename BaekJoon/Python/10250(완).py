import math
T = int(input())
array = []
for i in range(T):
    h,w,n = map(int,input().split())
    num = n%h
    Zero = 1
    if num==0:
        num+=1
    if n%h==0 and n%h<=h:
        num+=h-1
    num2 = math.ceil(n/h)
    if len(str(num2))>1:
        Zero = 0
    print("{}{}{}".format(num,"0"*Zero,num2))