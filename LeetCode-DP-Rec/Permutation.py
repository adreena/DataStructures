'''
Given a collection of distinct integers, return all possible permutations.
'''

def permutes(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]
    temp = []
    for i in range(len(nums)):
        keep = nums[i]
        rest = nums[:i]+nums[i+1:]
        for r in rest:
            temp.append([keep]+r)
    return temp
