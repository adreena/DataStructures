'''
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
'''
from collections import Counter
import heapq
def topKfreqWords(words,k):
    counter = Counter(words)
    heap = []
    for word, count in counter:
        heapq.heappush(heap, (-count, word))
        if len(heap)>k:
            heapq.heappop(heap)
    output = []
    while len(heap)>0:
        output.append(heapq.heappop(heap)[0])
    return output
