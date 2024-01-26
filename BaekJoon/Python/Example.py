import heapq

def findKthLargest(nums,k):
    heapq.heapify(nums)

    for _ in range(len(nums)-k):
        result = heapq.heappop(nums)
        print(result)
    return heapq.heappop(nums)

print("hi: "+ str(findKthLargest([3,2,3,1,2,4,5,5,6],4)))