

def isSymmetric(root1, roo2):
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    if root1.val == root2.val and \
       isSymmetric(root1.left, root2.right) and isSymmetric(root1.right, root2.left):
       return True
    return False

def main(root):
    return isSymmetric(root, root)
