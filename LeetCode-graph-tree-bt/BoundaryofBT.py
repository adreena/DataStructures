

def isLeaf(node):
    if node is not None and node.left is None and node.right is None:
        return True
    return False
def boundaryOfBT(root):
    temp = root.left
    left_boudnary = [root.val]
    while temp is not None:
        if not isLeaf(temp)
            left_boudnary.append(temp.val)
        if temp.left:
            temp = temp.left
        else:
            temp = temp.right
    temp = root
    q = [temp]
    while len(q)>0:
        top = q.pop(0)
        if isLeaf(top):
            left_boudnary.append(top.val)
        if top.left is not None:
            q.append(temp.left)
        elif top.right is not None:
            q.append(temp.right)

    if root.right is not None:
        stack = []
        temp = root.right
        while temp is not None:
            if not isLeaf(temp):
                stack.append(temp.val)
            if temp.right:
                temp = temp.right
            else:
                temp = temp.left
    while len(stack)>0:
        left_boudnary.append(stack.pop())
    return left_boudnary
