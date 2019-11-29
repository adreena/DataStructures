
from collections import defaultdict
min_key = float('inf')
max_key = float('-inf')
levels = defaultdict(lambda:[])

def BTVertical(root):
    q = [(root, 0)]
    while len(q)>0:
        top, d = q.pop(0)
        levels[d].append(root.val)
        min_key = min(d, min_key)
        max_key = max(d, max_key)
        if top.left:
            q.append(top.left, d-1)
        if top.right:
            q.append(top.right, d+1)
            
    return [levels[i] for i in range(len(levels))]
