import sys
def Priority(str):
    if str =='(' or str == ')':
        return 0
    elif str == '+' or str == '-':
        return 1
    elif str == '*' or str == '/':
        return 2
Equation = sys.stdin.readline()
i = 0
top = -1
stack = list(range(len(Equation)))
postfix = []
while True:
    if Equation[i] >= 'A' and Equation[i] <='Z':
        print(Equation[i],end='')
    elif Equation[i] == '(':
        top +=1
        stack[top] = Equation[i]
    elif Equation[i] == ')':
        while True:
            if stack[top] =='(':
                top -=1
                break
            else:
                print(stack[top],end='')
                top -=1
    elif Equation[i] == '+' or Equation[i] == '-' or Equation[i] == '*' or Equation[i] == '/': 
        while top != -1:
            if Priority(stack[top]) >= Priority(Equation[i]):
                print(stack[top],end='')
                top -=1
            else:
                break
        top += 1
        stack[top] = Equation[i]
    elif Equation[i] == '\n':
        while top != -1:
            print(stack[top],end='')
            top -=1
        break
    i+=1