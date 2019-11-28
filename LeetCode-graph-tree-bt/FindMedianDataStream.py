import heapq

def findMedian(nums):
    maxheap = []
    minheap = []

    for num in nums:
        heapq.heappush(max_heap, -1*num)
        heapq.heappush(min_heap, heapq.heappop(max_heap)*-1)
        if len(min_heap)>len(max_heap):
            heapq.heappush(max_heap, heapq.heappop(min_heap)*-1)
    if len(min_heap) == len(max_heap):
        return (min_heap[0] + max_heap[0]*-1) /2
    else:
        return max_heap[0]*-1
