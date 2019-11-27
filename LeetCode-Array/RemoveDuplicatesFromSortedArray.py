'''
Given a sorted array nums, remove the duplicates in-place such that
each element appear only once and return the new length.
'''

def removeDuplicates(nums):
    write_idx = 0
    i = 1
    while i < len(nums):
        if nums[i] != nums[i-1]:
            write_idx+=1
            nums[write_idx] = nums[i]
        i+=1
    nums = nums[:write_idx+1]
    return len(nums)
