import sys
class stack:
    def __init__(self):
        self.array = ['0' for i in range(50)]
        self.top = -1
    def push(self,ps):
        self.top +=1
        self.array[self.top]= ps
   
    def pop(self):
        if self.top >= 0:
            num = self.top
            self.array[num] = '0'
            self.top -=1
            return self.array[num]
        else:
            return "False"
    def sum(self):
        return sum(self.array)
    def get_array(self):
        return self.array
N = int(sys.stdin.readline())
st = stack()
for i in range(N):
    cnt = 0
    tf = True
    st.__init__
    PS = sys.stdin.readline()
    while PS[cnt] !='\n':
        if PS[cnt] == '(':
            st.push('(')
        else:
            if st.pop() == "False":
                tf = False
        cnt+=1
    if '(' in st.get_array():
        tf = False
    if tf:
        print("YES")
    else:
        print("NO")
