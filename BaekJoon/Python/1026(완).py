
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
total = 0
for i in range(n):
    total += min(a)*max(b)
    a.remove(min(a))
    b.remove(max(b))
print(total)