import sys
import math
def count_sosu(num):
    count = 0
    for i in range(num+1,2*num+1):
        tf = True
        for j in range(2,int(math.sqrt(i)+1)):
            if i % j == 0:
                tf = False
                break
        if tf:
            count +=1
    print(count) 
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    elif N == 1:
        print(1)
    else:
        count_sosu(N)
            
