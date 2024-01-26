from TreeNode import TreeNode
import sys
class Solution:
    prev = -sys.maxsize
    result = sys.maxsize

    # 재귀 구조 중위 순회 비교 결과
    def minDiffInBST(self,root : TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)
        
        self.result = min(self.result,root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.result
    # 반복 구조 중위 순회 비교 결과
    def minDiffStackBST(self,root:TreeNode) -> int:
        prev = -sys.maxsize
        result = sys.maxsize
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            print(node.val)
            
            result = min(result,node.val - prev)
            prev = node.val
            node = node.right
        return result

    
root = TreeNode(8)
root.left = TreeNode(4)
root.left.left = TreeNode(2)
root.left.left.left = TreeNode(1)
root.left.left.right = TreeNode(3)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(5)
root.left.right.right = TreeNode(7)
root.right = TreeNode(12)
solution = Solution()
#print(solution.minDiffInBST(root))
print(solution.minDiffStackBST(root))