import sys

N = int(sys.stdin.readline())
array = [1 for i in range(N)]
kg = []
cm = []
for i in range(N):
    kg_,cm_ = map(int,sys.stdin.readline().split())
    kg.append(kg_)
    cm.append(cm_)
count = 0
for i in range(N):
    for j in range(N):
        if kg[i]<kg[j] and cm[i]<cm[j]:
            array[i] +=1
print(*array)