'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
'''

lca = None

def findLCA_helper(root,p, q):
    if root is None:
        return False
    else:
        found = False
        if root.val == p.val or root.val == q.val:
            found = True
        inLeft = findLCA_helper(root.left)
        inRight = findLCA_helper(root.right)

        if found + inLeft+ inRight >=2:
            lca = root
        return found | inLeft | inRight

def findLCA(root, p, q):
    findLCA_helper(root, p, q)
    return lca
