T = int(input())
for i in range(T):
    a,b = input().split()
    for j in range(len(b)):
        print(b[j]*int(a),end='')
    print()
