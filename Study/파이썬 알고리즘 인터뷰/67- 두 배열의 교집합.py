from typing import List, Set
import bisect
# 브루트 포스로 계산
def forseIntersection(nums1 : List[int], nums2 : List[int]) -> List[int]:
    result : Set = set()
    for n1 in nums1:
        for n2 in nums2:
            if n1 == n2:
                result.add(n1)
    return result

# 이진 검색으로 일치 여부 판별
def binaryIntersection(nums1 : List[int], nums2 : List[int]) -> List[int]:
    result : Set = set()
    nums2.sort()
    for n1 in nums1:
        # 이진 검색으로 일치 여부 판별
        i2 = bisect.bisect_left(nums2, n1)
        print(i2)
        if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
            result.add(n1)
            print(result)
    return result

def twoIntersection(nums1 : List[int], nums2 : List[int]) -> List[int]:
    result : Set = set()
    # 양쪽 모두 정렬
    nums1.sort()
    nums2.sort()
    i = j = 0
    # 투 포인터 우측으로 이동하며 일치 여부 판별
    while i < len(nums1) and j < len(nums2):
        if nums1[i] > nums2[j]:
            j+=1
        elif nums1[i] < nums2[j]:
            i +=1
        else:
            result.add(nums1[i])
            i+=1
            j+=1
    return result

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
result = binaryIntersection(nums1,nums2)
print(result)