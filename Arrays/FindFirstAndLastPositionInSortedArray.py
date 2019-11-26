# Given an array of integers nums sorted in ascending
# order, find the starting and ending position of a given
# target value.
min_idx = -1
max_idx = -1
def helper(start, end, nums, target):
    if start <= end:
        mid = (start+end)//2
        if nums[mid] < target:
            helper(mid, end, nums, target)
        elif nums[mid]> target:
            helper(star, mid, nums, target)
        else:
            if min_idx == -1:
                min_idx=mid
            min_idx = min(mid, min_idx)
            max_idx = max(mid, max_idx)
            helper(star, mid, nums, target)
            helper(mid, end, nums, target)

def searchRange(nums, target):
    helper(0, len(nums), nums, target)
    return [min_idx, max_idx]
