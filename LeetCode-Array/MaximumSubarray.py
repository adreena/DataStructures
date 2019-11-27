'''
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.
'''
def maxSubarray(nums):
    max_sum = float('-inf')
    current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(current_sum+num, num)
        max_sum = max(max_sum, current_sum)
    return max_sum
