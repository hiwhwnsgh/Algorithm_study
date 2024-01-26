
import sys

class Stack():
    def __init__(self):
        self.top = -1
        self.array = ['0' for i in range(100)]
    def push(self,s):
        self.top +=1
        self.array[self.top]= s
    def pop(self):
        string = self.array[self.top]
        self.array[self.top] = '0'
        self.top -=1
        return string
    def get_array(self):
        return self.array
stack = Stack() 
while True:
    cnt = 0
    stack.__init__()
    tf = True
    string = sys.stdin.readline()
    if string[0] == '.' and string[1] == '\n':
        break
    while string[cnt] != '\n':
        if string[cnt] == '(' or string[cnt] == '[':
            stack.push(string[cnt])
        elif string[cnt] == ')':
            get_pop = stack.pop()
            if get_pop != '(':
                tf = False
        elif string[cnt] == ']':
            get_pop = stack.pop()
            if get_pop != '[':
                tf = False
        cnt+=1
    if '(' in stack.get_array() or '[' in stack.get_array():
        tf = False
    if tf:
        print("yes")
    else:
        print("no")