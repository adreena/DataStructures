

max_dim = 0

def DiamBT(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    left = 0
    right = 0
    if root.left:
        left = DiamBT(root.left)
    if root.right:
        right = DiamBT(root.right)
    max_dim = max(max_dim, left+right)
    return max(left, right)+1
