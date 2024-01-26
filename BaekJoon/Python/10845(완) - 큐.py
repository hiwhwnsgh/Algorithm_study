import sys
N = int(sys.stdin.readline())
num = []
front = 0
back = 0
for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        num.append(int(command[1]))
        back +=1
    elif command[0] == "pop":
        if back == front:
            print(-1)
        else:
            print(num[front])
            front+=1
    elif command[0] == "front":
        if back == front:
            print(-1)
        else:
            print(num[front])
    elif command[0] == "back":
        if back == front:
            print(-1)
        else:
            print(num[back-1])
    elif command[0] == "empty":
        if front == back:
            print(1)
        else:
            print(0)
    elif command[0] == "size":
        print(back-front)