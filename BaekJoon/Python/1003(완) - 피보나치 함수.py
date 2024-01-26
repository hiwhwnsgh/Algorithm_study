import sys
T = int(sys.stdin.readline())


for _ in range(T):
    n = int(sys.stdin.readline())
    result = [0]
    x,y= 0,1
    for i in range(0,n-1):
        x,y = y, x+y
        result.append(x)
    if n==0:
        print("1 0")
    elif n==1:
        print("0 1")
    else:
        print(f"{result[n-1]} {result[n-1] + result[n-2]}")