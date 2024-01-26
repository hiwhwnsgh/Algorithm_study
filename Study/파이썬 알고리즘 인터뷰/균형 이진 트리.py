# p. 413
# 균형 이진 트리
from TreeNode import TreeNode
def isBalanced(root : TreeNode) -> bool:
    def check(root):
        if not root:
            return 0
        
        left = check(root.left)
        right = check(root.right)
        # 높이 차이가 나는 경우 -1, 이외에는 높이에 따라 1 증가
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left,right) + 1
    return check(root) != -1
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(4)
print(isBalanced(root))
root2 = TreeNode(3)
root2.left = TreeNode(9)
root2.right = TreeNode(20)
root2.right.left = TreeNode(15)
root2.right.right = TreeNode(7)
print(isBalanced(root2))