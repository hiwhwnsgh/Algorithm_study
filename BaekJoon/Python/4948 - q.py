import math
import sys
import math

while True:
    N = int(sys.stdin.readline())
    count = 0
    if N == 0:
        break
    if N == 1:
        print(1)
    else:
        for i in range(N,2*N):
            if N % i == 0:
                continue
            else:
                count +=1
    print(count)
