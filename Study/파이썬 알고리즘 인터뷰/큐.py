import collections
# 큐를 이용한 스택 구현
class MyStack:
    def __init(self):
        self.q = collections.deque()
    
    def push(self,x):
        self.q.append(x)
        #요소 삽입 후 맨 앞에 두는 상태로 재정렬
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())
    
    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]
    
    def empty(self):
        return len(self.q) == 0

# 스택을 이용한 큐 구현
class MyQueue:
    def __init(self):
        self.input = []
        self.output = []
    def push(self,x):
        self.input.append(x)
    def pop(self):
        self.peek()
        return self.output.pop()
    def peek(self):
        #output이 없으면 모두 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
    def empty(self):
        return self.input == [] and self.output==[]