# p. 390
# 43번 이진 트리의 직경
from TreeNode import TreeNode
class Solution:
    longest : int =0
    
    def diameterOfBinaryTree(self,root:TreeNode) -> int:
        def dfs(node : TreeNode) ->int:
            if not node:
                return -1
            # 왼쪽, 오른쪽의 각 리프 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)
            # 가장 긴 경로
            self.longest = max(self.longest,left+right+2)
            # 상태값
            return max(left,right)+1
        s = dfs(root)
        print(s)
        return self.longest
root = TreeNode(1)
root.left = TreeNode(2)
root.right= TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
solution = Solution()
result =solution.diameterOfBinaryTree(root)
print(result)