import sys
K,N = map(int,sys.stdin.readline().split())
arr = []
for _ in range(K):
    arr.append(int(sys.stdin.readline()))
left,right = 1,max(arr)
while left<=right:
    mid = (left+right) // 2
    lines = 0
    print(f"{left} {right} {mid}")
    for i in arr:
        lines += i//mid
    print(f"lines : {lines}")
    if lines>=N:
        left = mid + 1
    else:
        right = mid -1
print(right)

