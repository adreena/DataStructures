'''
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining
'''
def max_water(nums):
    lefts = [0]*len(nums)
    rights = [0]*len(nums)
    max_water = 0

    lefts[0] = nums[0]
    rights[-1]= nums[-1]

    for i in range(1,len(nums)):
        lefts[i] = max(lefts[i-1], nums[i])

    for i in range(len(nums)-2, -1, -1):
        rights[i] = max(rights[i+1], nums[i])

    for i in range(nums):
        max_water += min(rights[i], lefts[i])-nums[i]

    return max_water
