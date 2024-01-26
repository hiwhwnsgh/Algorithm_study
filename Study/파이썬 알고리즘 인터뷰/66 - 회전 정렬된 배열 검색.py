from typing import List
def search(nums : List[int], target : int) -> int:
    # 예외처리
    if not nums:
        return -1
    
    # 최솟값을 찾아 피벗 설정
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left+(right-left)//2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    
    pivot = left
    print(f"pivot {pivot}")
    # 피벗 기준 이진 검색
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        mid_pivot = (mid + pivot) % len(nums)
        print(f"{left} {right} {mid_pivot}")
        if nums[mid_pivot] < target:
            left = mid + 1
        elif nums[mid_pivot] > target:
            right = mid - 1
        else:
            return mid_pivot
    return -1

nums = [4,5,6,1,7,0,2]
target = 1
print(search(nums,target))