import sys
N = int(sys.stdin.readline())
for i in range(N):
    word = sys.stdin.readline().rstrip()
    tf = False
    for j in range(len(word)):
        prev = j
        for z in range(j+1,len(word)):
            if word[prev] == word[z] and z-prev == 1:
                prev = z
            elif word[prev] == word[z] and z-prev > 1:
                N-=1
                tf = True
                break
        if tf:
            break
print(N)
