# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

#1- o(nlgn), O(1)
def TwoSum(nums,target):
    if len(nums)<2:
        return [-1, -1]

    nums.sort()
    i = 0
    j = len(nums)-1
    while i <= j:
        temp_sum = nums[i] + nums[j]
        if temp_sum < target:
            i+=1
        elif temp_sum>target:
            j-=1
        else:
            return [i,j]
    return [-1, -1]

# O(n), O(n)
from collections import defaultdict
def TwoSum(nums,target):

    rems = defaultdict(lambda:-1)
    for i, num in enumerate(nums):
        rems[target-num] = i

    for i, num in enumerate(nums):
        if rems[num]!=-1 and rems[target-num]!=i:
            return [i, rems[num]]
    return []
