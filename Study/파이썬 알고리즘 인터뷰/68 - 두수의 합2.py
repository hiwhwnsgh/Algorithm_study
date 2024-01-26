# 투포인터
from typing import List
import bisect

def TwoTwoSum(numbers : List[int], target : int) -> List[int]:
    left,right = 0, len(numbers) - 1
    while not left == right:
        if numbers[left] + numbers[right] < target:
            left +=1
        elif numbers[left] + numbers[right] > target:
            right -= 1
        else:
            return left+1,right+1   #리턴 값

# 이진 검색
def binaryTwoSum(numbers : List[int], target :List) -> List[int]:
    for k,v in enumerate(numbers):
        left, right = k + 1, len(numbers) - 1
        
        expected = target - v
        print(expected)
        # 이진 검색으로 나머지 판별
        while left<=right:
            mid = left + (right - left) // 2
            print(left,right,mid)
            if numbers[mid] < expected:
                left = mid + 1
            elif numbers[mid] > expected:
                right = mid - 1
            else:
                return k + 1, mid + 1
# bisect 모듈 + 슬라이싱
def bisectSlicingTwoSum(numbers : List[int], target:int) -> List[int]:
    for k,v in enumerate(numbers):
        expected = target - v
        i = bisect.bisect_left(numbers[k+1:],expected)
        if i < len(numbers[k+1:]) and numbers[i+k+1] == expected:
            return k + 1, i + k + 2

# bisect 모듈 + 슬라이싱 최소화
def bisectSlicingMinTwoSum(numbers : List[int], target:int) -> List[int]:
    for k,v in enumerate(numbers):
        expected = target - v
        nums = numbers[k+1:]
        i = bisect.bisect_left(nums,expected)
        if i < len(nums) and (numbers[i+k+1] == expected):
            return k+1,i+k+2

# bisect 모듈 + 슬라이싱 제거
def bisectSlicingDelTwoSum(numbers : List[int], target:int) -> List[int]:
    for k,v in enumerate(numbers):
        expected = target - v
        i = bisect.bisect_left(numbers, expected, k + 1)
        if i < len(numbers) and numbers[i] == expected:
            return k+1, i+1

array = [2,7,11,15]
target = 9
result = binaryTwoSum(array,target)
print(result)