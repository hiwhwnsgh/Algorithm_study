import math
T = int(input())
for i in range(T):
    a,b = map(int,input().split())
    s = pow(a,b,10)
    if s!=0:
        print(s)
    else:
        print(10)
    
        
