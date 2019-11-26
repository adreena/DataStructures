'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

def next_permute(nums):
    # find the last increasing pair
    i = 1
    idx = -1
    while i < len(nums):
        if nums[i]>nums[i-1]:
            idx = i
    if idx == -1:
        return nums.sort()
    prev_idx = idx-1
    next_max = None
    next_idx = None
    j = idx
    while j <len(nums):
        if nums[j]>nums[prev_idx]:
            if next_max is None or nums[j]<next_max:
                next_max = nums[j]
                next_idx = j
    nums[prev_idx], nums[next_idx] = nums[next_idx], nums[prev_idx]
    nums[idx:] = sorted(nums[idx:])
