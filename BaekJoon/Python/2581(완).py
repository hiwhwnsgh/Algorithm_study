import math
M = int(input())
N = int(input())
array=[]
for i in range(M,N+1):
    tf=True
    if i==1:
        continue
    elif i<4:
        array.append(i)
        continue
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            tf = False
            break
    if tf:
        array.append(i)
total = 0
mini = 999999999999
if len(array)==0:
    print(-1)
else:
    for i in array:
        total+=i
        if i<mini:
            mini=i
    print(total)
    print(mini)
