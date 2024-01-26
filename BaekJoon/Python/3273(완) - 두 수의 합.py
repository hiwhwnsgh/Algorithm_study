import sys
n = int(sys.stdin.readline())
sequence = list(map(int,sys.stdin.readline().split()))
target = int(sys.stdin.readline())
left = 0
right = len(sequence)-1
count = 0
sequence.sort()
while not left == right:
    if sequence[left]+sequence[right] < target:
        left +=1
    elif sequence[left]+sequence[right] > target:
        right -=1
    else:
        right-=1
        count+=1
print(count)