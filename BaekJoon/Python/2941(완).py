a = ["c=","c-","dz=","d-","lj","nj","s=","z="]
S = input()
count = 0
for i in range(len(a)):
    if S.count(a[i])>0:
        count+=S.count(a[i])
        S = S.replace(a[i]," ")
for i in range(len(S)):
    if S[i] != " ":
        count+=1
print(count)
