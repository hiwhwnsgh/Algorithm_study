n,m = map(int,input().split())
word = set()
word2 = set()
for i in range(n):
    word.add(input())
for i in range(m):
    word2.add(input())
array = sorted(word & word2)
print(len(array))
for i in array:
    print(i)