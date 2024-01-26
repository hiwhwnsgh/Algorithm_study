import sys
N,K = map(int,sys.stdin.readline().split())
array = []
for i in range(N):
    array.append(int(sys.stdin.readline()))
count = 0
for i in range(len(array)-1,-1,-1):
    if K - array[i] >= 0:
        count += K//array[i]
        K %= array[i]
print(count)