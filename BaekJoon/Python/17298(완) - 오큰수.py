import sys
from typing import List
def OhBignumber(nums: List[int]) -> List[int]:
    result = [-1 for i in range(len(nums))]
    if not nums:
        return 0
    stack = []
    for i,j in enumerate(nums):
        while stack and j>nums[stack[-1]]:
            top = stack.pop()
            result[top] = j
        print(stack)
        stack.append(i)
    return result
A = int(sys.stdin.readline())
N = list(map(int,sys.stdin.readline().split()))
print(*OhBignumber(N))