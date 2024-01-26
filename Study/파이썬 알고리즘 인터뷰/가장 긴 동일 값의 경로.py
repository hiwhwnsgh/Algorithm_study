# p. 393
# 가장 긴 동일 값의 경로
from TreeNode import TreeNode
class Solution:
    result : int = 0
    def longestUnivaluePath(self,root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if node is None:
                return 0
            

            # 존재하지 않는 노드까지 DFS 재귀 탐색
            left = dfs(node.left)
            right = dfs(node.right)
            # 현재 노드가 자식 노드와 동일한 경우 거리 1 증가
            if node.left and node.left.val == node.val:
                left +=1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right +=1
            else:
                right = 0
            print(left,'',right)
            # 왼쪽과 오른쪽 자식 노드 간 거리의 합 최댓값이 결과
            self.result = max(self.result,left+right)
            return max(left,right)
        dfs(root)
        return self.result
root = TreeNode('A')
root.right = TreeNode('A')
root.left = TreeNode('B')
root.left.left = TreeNode('C')
root.left.right = TreeNode('C')
root.right.right = TreeNode('A')
solution = Solution()
print(solution.longestUnivaluePath(root))