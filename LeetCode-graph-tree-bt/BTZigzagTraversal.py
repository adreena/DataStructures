
from collections import defaultdict

def zigzagBT(root):
    level_order = defaultdict(lambda:[])
    q = [(root, 0)]
    while len(q)>0:
        top, level = q.pop(0)
        level_order[level].append(top.val)
        if top.left:
            q.append((top.left, level+1))
        if top.right:
            q.append((top.right, level+1))
    levels = [level_order[i] for i in range(len(level_order))]
    for i in range(len(levels)):
        if i % 2 != 0:
            l.reverse()
    return levels
