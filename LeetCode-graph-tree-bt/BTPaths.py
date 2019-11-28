'''
Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]
'''

paths = []
def BTPaths(root, output):
    if root is None:
        return
    if root.left is None and root.right is None:
        if output != '':
            output+='->'+str(root.val)
        else:
            output = str(root.val)
    else:
        if output != '':
            output+='->'+str(root.val)
        else:
            output = str(root.val)
        BTPaths(root.left, output)
        BTPaths(root.right, output)
