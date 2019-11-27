'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
'''
inorder_idx = {}

def helper(postorder, left, right):
    if left >right:
        return None
    val = postorder.pop()
    idx = inorder_idx[val]
    root = TreeNode(val)
    root.left = helper(postorder, left, idx-1)
    root.right = helper(postorder, idx+1, right)
    return root
def buildTree(inorder, postorder):
    inorder_idx = {val:i for i , val in enumerate(inorder)}
    return helper(postorder, 0, len(inorder)-1)
