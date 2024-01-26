from typing import List
import collections

# 브루트 포스로 계산
def  brotMaxSlidingWindow(nums: List[int],k:int)->List[int]:
    r = []
    for i in range(len(nums)-k+1):
        r.append(max(nums[i:i+k]))
    return r


# 큐를 이용한 최적화
def queueMaxSlidingWindow(nums: List[int], k:int)->List[int]:
    results =[]
    window = collections.deque()
    current_max = float('-inf')
    for i,v in enumerate(nums):
        window.append(v)
        if i < k -1:
            continue
        print(window)
        # 새로 추가된 값이 기존 최댓값보다 큰 경우 교체
        if current_max == float('-inf'):
            current_max = max(window)
        elif v > current_max:
            current_max = v
        results.append(current_max)

        #최댓값이 윈도우에서 빠지면 초기화
        if current_max == window.popleft():
            current_max = float('-inf')
        print(current_max)
    return results

nums = [1,3,-1,-3,5,3,6,7]
k = 3
result = queueMaxSlidingWindow(nums,k)
print(result)