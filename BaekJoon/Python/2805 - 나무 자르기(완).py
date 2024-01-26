import sys

N,M = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))
left,right = 0,sum(nums)

def binary_search(arr, start, end):
    while start <= end:
        mid = (start+end) // 2
        total = 0
        
        for x in arr:
            if x > mid:
                total+= x- mid
            
        if total < M:
            end = mid-1
        else:
            start = mid +1
        print(start," ", end)
    return end

print(binary_search(nums,0,max(nums)))