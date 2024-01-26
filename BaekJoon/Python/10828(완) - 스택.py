import sys
N = int(sys.stdin.readline())
toss = -1
num = list(range(N))
for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        toss+=1
        num[toss] = int(command[1])
    elif command[0] == "pop":
        if toss == -1:
            print(toss)
        else:
            print(num[toss])
            toss-=1
    elif command[0] == "size":
        print(toss+1)
    elif command[0] == "empty":
        if toss == -1:
            print(1)
        else:
            print(0)
    elif command[0] == "top":
        if toss == -1:
            print(-1)
        else:
            print(num[toss])