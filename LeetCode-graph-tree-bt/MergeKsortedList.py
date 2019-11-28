'''
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''
import heapq
class NodeWrap:
    def __init__(self, data):
        self.data = data
    def __lt__(self, other):
        return self.data.val < other.data.val

def mergeKSortedList(lists):
    heap = []
    for l in lists:
        if l is not None:
            heapq.heappush(heap, NodeWrap(l))
    head = Node(0)
    output= None
    head.next = output
    while len(heap)>0:
        top = heapq.heappop(heap)
        if top.data.next is not None:
            heapq.heappush(heap, NodeWraap(top.data.next))
        if output is None:
            output = Node(top.data.val)
        else:
            output.next = Node(top.data.val)
            output = output.next
    return head.next
