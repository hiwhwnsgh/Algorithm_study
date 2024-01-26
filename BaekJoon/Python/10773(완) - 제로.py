import sys
class stack:
    def __init__(self,num):
        self.array = [0 for i in range(num)]
        self.top = -1
    def push(self,num):
        self.top +=1
        self.array[self.top]= num
    def pop(self):
        self.array[self.top] = 0
        self.top -=1
    def sum(self):
        return sum(self.array)
N= int(sys.stdin.readline())
st = stack(N)
for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        st.pop()
    else:
        st.push(num)
print(st.sum())
