import sys
N = int(sys.stdin.readline())
for i in range(N):
    a,b = map(str,sys.stdin.readline().split())
    tf = True
    for j in a:
        if j not in b:
            tf = False
    if tf:
        print(f"{a} & {b} are anagrams.")
    else:
        print(f"{a} & {b} are NOT anagrams.")
