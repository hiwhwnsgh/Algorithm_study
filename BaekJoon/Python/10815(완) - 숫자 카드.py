import sys
input = sys.stdin.readline
N = int(input())
array = list(map(int,input().split()))
M = int(input())
array2 = list(map(int,input().split()))
set1 = set(array)
set2 = set(array2)
intersction_reuslt = set1 & set2
result = [0 for i in range(M)]
for i in range(M):
    if array2[i] in intersction_reuslt:
        result[i] = 1
print(*result)