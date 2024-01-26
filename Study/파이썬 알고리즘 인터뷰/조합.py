from typing import List
def combine(n : int, k: int) -> List[List[int]]:
    results = []

    def dfs(elements , start : int , k:int):
        if k == 0:
            results.append(elements[:])
            return
        
        # 자신 이전의 모든 값을 고정하여 재귀호출
        for i in range(start, n+1):
            elements.append(i)
            dfs(elements,i+1,k-1)
            elements.pop()
    dfs([],1,k)
    return results
print(combine(4,3))

# 내가 만든 조합 함수!
def combine2(nums : List[int], K : int):
    result = []
    array = []
    def dfs(elements : List[int],start : int,n : int):
        if n == 0:
            result.append(array[:])
            return
        for e in range(start,len(nums)):
            array.append(nums[e])
            dfs(elements[start:],e+1,n-1)
            array.pop()
    dfs(nums,0,K)
        
    return result
print(combine2([1,2,3,4],3))