import sys
H,W = map(int,sys.stdin.readline().split())
block = list(map(int,sys.stdin.readline().split()))
volume = 0
left, right = 0,W-1
left_max, right_max = block[left],block[right]

while left<right:
    left_max,right_max = max(block[left],left_max), max(block[right],right_max)
    # 더 높은 쪽을 향해 투 포인터 이동
    if left_max <=right_max:
        volume += left_max-block[left]
        left+=1
    else:
        volume += right_max - block[right]
        right -=1
print(volume)