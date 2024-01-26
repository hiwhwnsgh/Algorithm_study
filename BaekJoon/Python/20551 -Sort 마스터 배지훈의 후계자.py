import sys
from typing import List

def binary_search(nums : List[int], target) -> int:
    left,right = 0,len(nums)
    while left<right:
        mid = (left+right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return right

N,M = map(int,sys.stdin.readline().split())
A = []
D = []
for _ in range(N):
    A.append(int(sys.stdin.readline()))
for _ in range(M):
    D.append(int(sys.stdin.readline()))
A.sort()
for i in D:
    index = binary_search(A,i)
    if index>=0 and index <len(A) and A[index] == i:
        print(index)
    else:
        print(-1)