import sys
import math
# 트리 생성
class Node:
    def __init__(self,data,l=None,r=None):
        self.data = data
        self.left = l
        self.right = r

# 이진트리 전위 순회
def preorder(Node):
    if Node !=None:
        print(Node.data,end=' ')
        preorder(Node.left)
        preorder(Node.right)

# 이진트리 중위 순회
def inorder(Node):
    if Node != None:
        inorder(Node.left)
        print(Node.data,end=' ')
        inorder(Node.right)

#이진트리 후위 순회
def postorder(Node):
    if Node != None:
        postorder(Node.left)
        postorder(Node.right)
        print(Node.data,end=' ')

# 노드의 전체 갯수 구하기
def count_node(Node):
    if Node == None:
        return 0
    print(Node.data,end=' ')
    return 1+count_node(Node.left) + count_node(Node.right)

# 단말 노드 갯수 구하기
def count_leaf(Node):
    if Node == None:
        return 0
    if Node.left == None and Node.right == None:
        return 1
    else:
        return count_leaf(Node.left) + count_leaf(Node.right)

# 트리 높이 구하기
def getHeight(Node):
    if Node == None:
        return 0
    hLeft = getHeight(Node.left)
    hRight = getHeight(Node.right)
    return 1+ max(hLeft,hRight)
d = Node('D')
e = Node('E')
b = Node('B',d,e)
f = Node('F')
c = Node('C',f)
root = Node('A',b,c)
preorder(root)
print()
inorder(root)
print()
postorder(root)
print()
print(count_node(root))
print(count_leaf(f))
print(getHeight(root))