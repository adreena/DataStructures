'''
Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
'''

# O(nlogK) , O(k)
import heapq
def kClosestPoints(nums, k):
    order = []
    for x,y in nums:
        heapq.heappush(order, (-1*(x**2+y**2), [x,y]))
        if len(order)>k:
            heapq.heappop(order)
    output = []
    while len(order)>0:
        output.append(heapq.heapop(order)[1])
    return output
