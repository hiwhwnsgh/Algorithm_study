import sys
import collections

N = int(sys.stdin.readline())
arr = sys.stdin.readline().split()
M = int(sys.stdin.readline())
arr2 = sys.stdin.readline().split()
result = collections.Counter(arr)
print(' '.join(f'{result[x]}' if x in result else '0' for x in arr2))