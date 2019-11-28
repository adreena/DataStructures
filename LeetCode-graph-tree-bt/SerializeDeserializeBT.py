
serialized = []
def serialize(root):
    if root is None:
        serialized.append(None)
        return

    serialized.append(root.val)
    if left is not None:
        left = serialize(root.left)
        serialized.append(left.val)
    if right is not None:
        right = serialized(root.right)
        serialized.append(right.val)

def deserialize(serialized):
    if len(serialized)>0:
        if serialzed[0] is None:
            serialzed.pop(0)
            return
        top = serialized.pop()
        root = Node(top)
        root.left = deserialize(serialized)
        root.right = deserialize(serialized)
        return root
    else:
        return
