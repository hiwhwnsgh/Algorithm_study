import sys
import collections
from typing import List
def lowerBound(nums : List[int],target:int)->int:
    left,right = 0, len(nums)
    while left<right:
        mid = (left+right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return right
    
while True:
    N,M = map(int,sys.stdin.readline().split())
    if N == 0 and M == 0:
        break
    dic = collections.defaultdict(str)
    cnt = 0
    for _ in range(N):
        num = sys.stdin.readline()
        dic[num] = 1
    for _ in range(M):
        num = sys.stdin.readline()
        if dic[num]:
            cnt += 1
    
    
    # for n1 in nums1:
    #     index = lowerBound(nums2,n1)
    #     if len(nums2) > 0 and len(nums2) > index and n1 == nums2[index]:
    #         cnt += 1

    print(cnt)
