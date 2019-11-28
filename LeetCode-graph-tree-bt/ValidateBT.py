

prev_node = None
def isValidBT(root):
    if root is None:
        return True

    if not isValidBT(root.left):
        return False
    if prev_node is not None:
        if prev_node >= root.val:
            return False
    prev_node = root.val
    return isValidBT(root.right)
