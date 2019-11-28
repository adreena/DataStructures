'''
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
'''

max_sum = float('-inf')
def maxSumPath(root):
    if root is None:
        return None
    cur_sum = root.val
    left_val = None
    right_val = None
    if root.left is not None:
        left_val = maxSum(root.left)
        cur_sum = max(cur_sum, left_val, left_val+cur_sum)
    if root.right is not None:
        right_val = maxSum(root.right)
        cur_sum = max(cur_sum, right_val, right_val+cur_sum)

    max_sum = max(max_sum, cur_sum)
    if right_val and left_val:
        return max( root.val + max(left_val, right_val), root.val)
    elif right_val:
        return max( root.val +  right_val, root.val)
    else:
        return root.val
