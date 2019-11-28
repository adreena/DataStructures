

def LevelOrderTraversal(root):

    q = [(root,0)]
    order = defaultdict(lambda:[])
    while len(q)>0:
        top, level = q.pop(0)
        defaultdict[level].append(top.val)
        if top.left is not None:
            q.append((top.left, level+1))
        if top.right is not None:
            q.append((top.right, level+1))
    return [order[i] for i in range(len(order))]
