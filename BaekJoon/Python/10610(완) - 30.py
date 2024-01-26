import sys

s = list(sys.stdin.readline())
s.pop()
s.sort(reverse=True)
s = "".join(s)
s = int(s)
if s % 30 == 0:
    print(s)
else:
    print(-1)