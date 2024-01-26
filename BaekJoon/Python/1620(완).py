import sys
input = sys.stdin.readline
n,m = map(int,input().split())
dic = {}
array = []
for i in range(n):
    string = input().rstrip()
    array.append(string)
    dic[string]=i+1
for i in range(m):
    string = input().rstrip()
    if string.isdigit():
        print(array[int(string)-1])
    else:
        print(dic.get(string))


