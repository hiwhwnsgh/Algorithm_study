import heapq
from LinkeList import *
def mergeKList(lists : List[ListNode]) -> ListNode:
    root = result = ListNode(None)
    heap = []

    # 각 연결 리스트의 루트를 힙에 저장
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap,(lists[i].val, i, lists[i]))
    
    # 힙 추출 이후 다음 노드는 다시 저장
    while heap:
        node = heapq.heappop(heap)
        idx = node[1]
        result.next = node[2]

        result = result.next
        if result.next:
            heapq.heappush(heap, (result.next.val, idx, result.next))
        
    return root.next

head = Solution()
array = head.toReversedLinkedList([[1,4,5],[1,3],[2,4,6]])
while array:
    print(array.val)
    array = array.next
result = mergeKList(array)
while result:
    print(result.val)
    result = result.next
