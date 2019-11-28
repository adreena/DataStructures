

def isSubtree(t1, t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    if t1.val ==t2.val and isSubtree(t1.left, t2.left) and isSubtree(t1.right, t2,right):
        return True
    return False

def traverse(t1, t2):
    if t1 is not None:
        return isSubtree(t1,t2) or traverse(t1.left, t2) or traverse(t1.right, t2)
    return False
