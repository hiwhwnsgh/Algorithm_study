import sys

dic = {}
N,M = map(int,sys.stdin.readline().split())
powers = []
for _ in range(N):
    name, power = map(str,sys.stdin.readline().split())
    powers.append(int(power))
    dic[name] = int(power)

for i in range(M):
    num = int(sys.stdin.readline())

