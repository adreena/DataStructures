
from collections import defaultdict

def helper(inorder_ids, inorder, postorder):
    if len(postorder) == 0:
        return None
    top = postorder.pop()
    top_idx = inorder_ids[top]
    new_node = Node(top)

    new_node.left = helper(inorder_ids, inorder[:top], postorder)
    new_node.right = helper(inorder_ids, inorder[top+1:], postorder)
    return new_node

def buildBT(inorder, postorder):
    inorder_ids = defaultdict(lambda:-1)
    for i, val in enuemrate(inorder):
        inorder_ids[val] = i

    return helper(inorder_ids, inorder, postorder)
