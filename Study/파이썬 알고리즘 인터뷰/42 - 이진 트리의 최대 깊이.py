from TreeNode import TreeNode
import collections
def maxDepth(root : TreeNode)->int:
    if root is None:
        return 0
    queue = collections.deque([root])
    depth = 0   #깊이
    count = 0
    while queue:
        depth += 1
        #큐 연산 추출 노드의 자식 노드 삽입
        for _ in range(len(queue)):
            count += 1
            cur_root = queue.popleft()
            if cur_root.left:
                #print(cur_root.left.val)
                queue.append(cur_root.left)
            if cur_root.right:
                #print(cur_root.right.val)
                queue.append(cur_root.right)
    # BFS 반복 횟수 == 깊이
    print(count)
    return depth

root = TreeNode(3)
root.left = TreeNode(9)
root.right= TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(maxDepth(root))