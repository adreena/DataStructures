

def mergeBT(t1, t2):
    if t1 is None and t2 is None:
        return None
    if t1 is None:
        return t2
    if t2 is None:
        return t1

    new_node = Node(t1.val+t2.val)
    new_node.left = mergeBT(t1.left, t2.left)
    new_node.right = mergeBT(t1.right, t2.right)
    return new_node
