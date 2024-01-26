import sys
from typing import *

class ListNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Deque:
    def __init__(self,k: int):
        self.head,self.tail = ListNode(None),ListNode(None)
        self.k,self.len = k,0
        self.head.right,self.tail.left = self.tail,self.head
    def _add(self,node : ListNode, new:ListNode):
        n = node.right
        node.right = new
        new.left,new.right = node,n
        n.left = new
    def _del(self,node :ListNode):
        n = node.right.right
        data = node.right
        node.right = n
        n.left = node
        return data.val
    def insertFront(self,value : int) -> bool:
        if self.len == self.k:
            return False
        self.len +=1
        self._add(self.head , ListNode(value))
        return True
    def insertLast(self,value : int) -> bool:
        if self.len == self.k:
            return False
        self.len+=1
        self._add(self.tail.left,ListNode(value))
        return True
    def deleteFront(self) -> str:
        if self.len == 0:
            return -1
        self.len-=1
        data = self._del(self.head)
        return data
    def deleteLast(self) -> str:
        if self.len==0:
            return -1
        self.len-=1
        data = self._del(self.tail.left.left)
        return data
    def getFront(self) -> int:
        return self.head.right.val if self.len else -1
    def getRear(self) -> int:
        return self.tail.left.val if self.len else -1
    def isEmpty(self) -> bool:
        return self.len == 0
    def isFull(self)->bool:
        return self.len == self.k
    def isSize(self) -> int:
        return self.len
N = int(sys.stdin.readline())
deq = Deque(N)
for i in range(N):
    num = list(map(str,sys.stdin.readline().rstrip().split()))
    if num[0] == 'push_back':
        deq.insertLast(int(num[1]))
    elif num[0] == 'push_front':
        deq.insertFront(int(num[1]))
    elif num[0] == 'pop_front':
        print(deq.deleteFront())
    elif num[0] == 'pop_back':
        print(deq.deleteLast())
    elif num[0] == 'front':
        print(deq.getFront())
    elif num[0] == 'back':
        print(deq.getRear())
    elif num[0] == 'size':
        print(deq.isSize())
    elif num[0] == 'empty':
        if deq.isEmpty():
            print(1)
        else:
            print(0)