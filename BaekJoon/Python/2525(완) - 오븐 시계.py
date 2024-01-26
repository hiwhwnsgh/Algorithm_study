import sys
A, B = map(int,sys.stdin.readline().split())
C = int(sys.stdin.readline())
B += C
A += B // 60
B = B % 60
while A>23:
    A -= 24
print(f'{A} {B}')