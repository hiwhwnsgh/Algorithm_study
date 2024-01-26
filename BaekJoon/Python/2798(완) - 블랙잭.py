import sys

N,M = map(int,sys.stdin.readline().split())
array = list(map(int,sys.stdin.readline().split()))
result = 0
array.sort()
for i in range(N-1):
    left,right = i+1,N -1
    while left<right:
        sums = array[i] + array[left] + array[right]
        if sums <= M:
            result = max(result,sums)
            left+=1
        elif sums > M:
            right -=1
print(result)
