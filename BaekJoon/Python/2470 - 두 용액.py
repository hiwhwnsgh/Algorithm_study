import sys
from typing import List
def twoSolution(nums : List[int]) -> List[int]:
    left = 0
    right = len(array)-1
    nums.sort()
    result = []
    while not left == right:
        if nums[left]+nums[right] > 0:
            right -=1
        elif nums[left] + nums[right] <0:
            left +=1
        else:
            result.append(nums[left])
            result.append(nums[right])
            return result
    result.append(nums[left])
    result.append(nums[right])
    return result
N = int(sys.stdin.readline())
array = list(map(int,sys.stdin.readline().split()))
result = twoSolution(array)
print(result)


