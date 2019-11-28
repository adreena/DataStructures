

def isBalanced(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    left = isBalanced(root.left)
    right = isBalanced(root.right)
    if abs(left -right)>1:
        return False
    if left is False or right is False:
        return False
    return max(left, right)+1
