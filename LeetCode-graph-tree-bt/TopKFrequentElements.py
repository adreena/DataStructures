'''
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
'''
from collections import Counter
def topKFreqs(nums,k):
    counts = Counter(nums)
    return [key for key, val in counts.most_common(k)]
