import bisect
from typing import List

# 재귀 풀이
def recursiveSearch(nums : List[int], target : int) -> int:
    def binary_search(left, right):
        if left <= right:
            mid = left + (right-left)//2
            
            if nums[mid] <target:
                return binary_search(mid+1,right)
            elif nums[mid] > target:
                return binary_search(left,mid - 1)
            else:
                return mid

        else:
            return -1
            
    return binary_search(0,len(nums) -1)

# 반복 풀이
def repeatSearch(nums : List[int], target:int) ->int:
    left,right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right-left) // 2 # 자료형을 초과하지 않는 중앙 위치 계산 p.523

        if nums[mid] <target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1

#   이진검색 모듈
def binarySearch(nums : List[int], target : int) ->int:
    index = bisect.bisect_left(nums,target)

    if index < len(nums) and nums[index] == target:
        return index
    else:
        return -1

# 이진 검색을 사용하지 않는 Index 풀이
def indexSearch(nums : List[int], target:int) -> int:
    try:
        return nums.index(target)
    except ValueError:
        return -1
nums = [-1,0,3,5,9,12]
target = 9
print(recursiveSearch(nums,target))
