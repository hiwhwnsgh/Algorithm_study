
N = int(input())
array = []
for i in range(N):
    array.append(int(input()))
for i in range(1,N):
    key = i
    while key>0 and array[key-1]>array[key]:
        array[key-1],array[key] = array[key],array[key-1]
        key-=1

for i in range(N):
  print(array[i])
