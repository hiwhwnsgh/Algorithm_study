S = input()
l = [-1 for i in range(26)]
a = 97
for i in range(len(S)):
    for j in range(26):
        if S[i] == chr(a):
            if l[a-97] == -1:
                l[a-97]=i
        a+=1
    a=97
for i in range(26):
    print(l[i],end=' ')
