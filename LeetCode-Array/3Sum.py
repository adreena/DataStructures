'''
Given an array nums of n integers, are there elements a, b, c in nums such that
a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
'''
# O(nlgn)+O(n2), O(n)
def twoSum(nums, target):
    i = 0
    j = len(nums)
    output = set()
    while i < j:
        temp_sum = nums[i] + nums[j]
        if target === temp_sum:
            output.add((i,j))
            i+=1
            j-=1
        elif temp_sum< target:
            i+=1
        else:
            j-=1
    return output

def threeSum(nums):
    nums.sort()
    output = set()
    for i, num in enumerate(nums):
        twos = twoSum(nums[i+1:], -num)
        if len(twos) >0:
            for a, b in twos:
                output.add((i,a,b))
    return output
