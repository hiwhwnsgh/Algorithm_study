from typing import List

def singleNumber(nums : List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result

num = [2,2,1]
result = singleNumber(num)
print(result)