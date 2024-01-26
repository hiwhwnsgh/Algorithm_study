import sys

def binarySearch(nums, target):
    left,right = 0, len(nums)-1
    while left<=right:
        mid = (left+right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid -1
        else:
            return 1
    return 0

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    note = sorted(list(map(int,sys.stdin.readline().split())))
    M = int(sys.stdin.readline())
    note2 = list(map(int,sys.stdin.readline().split()))
    for index in range(M):
        print(binarySearch(note,note2[index]))