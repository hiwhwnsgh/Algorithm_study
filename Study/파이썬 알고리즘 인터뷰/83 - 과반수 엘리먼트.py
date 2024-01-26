from typing import List
import collections
global count
count = 1
# 브루트 포스로 과반수 비교
def brutMajorityElement(nums : List[int])->int:
    for num in nums:
        if nums.count(num) > len(nums) // 2:
            return num

# 다이나믹 프로그래밍
def dynamicMajorityElement(nums : List[int])->int:
    counts = collections.defaultdict(int)
    for num in nums:
        if counts[nums] == 0:
            counts[num] = nums.count(num)
        if counts[nums] > len(nums) // 2:
            return num

#분할정복
def divMajorityElement(nums: List[int])->int:
    global count
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]
    
    half = len(nums) // 2
    a = divMajorityElement(nums[:half])
    b = divMajorityElement(nums[half:])
    count += 1
    return [b,a][nums.count(a) > half]
array = [2,2,1,1,1,3,2,2,2,2,2,4,5]
print(divMajorityElement(array))

#파이썬다운 방식
def pyMajorityElement(nums:List[int]) -> int:
    return sorted(nums)[len(nums)//2]