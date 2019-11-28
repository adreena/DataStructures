
'''
Input: [3,2,1,5,6,4] and k = 2
Output: 5
'''
import heapq
def kthLargestElement(nums,K):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap)>K:
            heapq.heapop(heap)
    return heap[-k]
