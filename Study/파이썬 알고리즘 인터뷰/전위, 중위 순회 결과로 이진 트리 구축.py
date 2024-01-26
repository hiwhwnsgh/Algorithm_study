# p. 444
# 전위, 중위 순회 결과로 이진 트리 구축
from TreeNode import TreeNode
from typing import List
def buildTree(preorder : List[int], inorder : List[int])->TreeNode:
    if inorder:
        # 전위 순회 결과는 중위 순회 분할 인덱스
        index = inorder.index(preorder.pop(0))
        # 중위 순회 결과 분할 정복
        node = TreeNode(inorder[index])
        node.left = buildTree(preorder,inorder[0:index])
        node.right = buildTree(preorder, inorder[index + 1:])

        return node
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
result = buildTree(preorder,inorder)
print(result.val)