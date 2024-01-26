import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N,M = map(int,sys.stdin.readline().split())
    A = list(map(int,sys.stdin.readline().split()))
    B = list(map(int,sys.stdin.readline().split()))
    B.sort()
    total = 0
    for value in A:
        left,right = 0,len(B)
        while left<right:
            mid = (left+right) // 2
            if B[mid]<value:
                left = mid +1
            else:
                right = mid
        total += right
    print(total)
        