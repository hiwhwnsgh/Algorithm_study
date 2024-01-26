N= int(input())
array = list(map(int,input().split()))
count = 0
for i in range(N):
    if array[i]==1:
        continue
    elif array[i]<4:
        count+=1
        continue
    for j in range(2,array[i]):
        if array[i] % j==0:
            count -=1
            break
    count+=1
print(count)
    
