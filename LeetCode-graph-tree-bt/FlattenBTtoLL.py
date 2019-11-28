'''
    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
'''


def flattenBT(root):
    if root is None:
        return None

    left = flattenBT(root.left)
    right = flattenBT(root.right)
    if left is not None:
        root.right = left
        root.left = None
        while root.right:
            root = root.right
        root.right = temp
    return root
