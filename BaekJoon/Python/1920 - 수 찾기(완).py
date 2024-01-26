import sys
from typing import List
def search(nums : List[int], target:int) -> int:
    def binary_search(left,right):
        if left<=right:
            mid = (left+right) // 2
            if nums[mid] < target:
                return binary_search(mid+1,right)
            elif nums[mid] > target:
                return binary_search(left,mid-1)
            else:
                return 1
        else:
            return 0
    return binary_search(0,len(nums)-1)
            

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int,sys.stdin.readline().split()))

A.sort()
for i in range(M):
    search(A,B[i])

