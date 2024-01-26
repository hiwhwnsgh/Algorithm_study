import sys
import collections
dic = collections.defaultdict()
N,M = map(int,sys.stdin.readline().split())
for _ in range(N):
    site, password = map(str,sys.stdin.readline().split())
    dic[site] = password
for _ in range(M):
    site = sys.stdin.readline().rstrip()
    print(dic[site])