'''
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
''''
from collections import defaultdict
rightview = defaultdict(lambda:None)

def rightSideIter(root, d):
    if root is None:
        return 0
    rightview[d] = root
    rightSideIter(root.left, d+1)
    rightSideIter(root.right, d+1)

def findRightView(root):
    rightSideIter(root)
    out_put = []
    for i in range(len(rightview)):
        output.append(rightview[i])
    return output
