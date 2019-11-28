


def countComplete(root):
    if root is None:
        return 0
    if root.left and root.right:
        return 1
    return countComplete(root.left)+ countComplete(root.right)
