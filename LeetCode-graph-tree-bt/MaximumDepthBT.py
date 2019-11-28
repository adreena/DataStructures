

def maxDepth(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    left = maxDepth(root.left)
    right = maxDepth(root.right)

    return max(left, right)+1
