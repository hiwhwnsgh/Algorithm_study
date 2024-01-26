# p. 456
import heapq
from typing import List

# heapq 모듈 이용
def findKthLargest(nums: List[int], k : int) -> int:
    heap = list()
    for n in nums:
        heapq.heappush(heap,-n)
    print(heap)

    for _ in range(1,k):
        heapq.heappop(heap)
    
    return -heapq.heappop(heap)

# heapq 모듈의 heapify 이용
def findKthLargest2(nums:List[int], k: int) -> int:
    heapq.heapify(nums)
    print(nums)
    for _ in range(len(nums)-k):
        heapq.heappop(nums)
    print(nums)
    return heapq.heappop(nums)

# heapq 모듈의 nlargest 이용
def findKthLargest3(nums:List[int], k : int) -> int:
    return heapq.nlargest(k,nums)[-1]


# 정렬을 이용한 풀이
def findKthLargest4(nums : List[int], k : int) -> int:
    return sorted(nums,reverse=True)[k - 1]

print(findKthLargest([3,2,3,1,2,4,5,5,6,6],4))