import sys
N = int(sys.stdin.readline())
count = 0
while(N>0):
    if N % 5 == 0:
        count += N/5
        break
    N -= 3
    if N == 1 or N == 2:
        count = -1
        break
    count +=1
    
print(int(count))
