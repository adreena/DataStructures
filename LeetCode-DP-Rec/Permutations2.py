'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''

nums.sort()
def permutations(nums):
    if len(nums) == 0:
        return []
    if len(nums)==1:
        return [nums]
    temp = []
    for i in range(len(nums)):
        if i >0 and nums[i] == nums[i-1]:
            continue
        keep = nums[i]
        rest = nums[:i] + nums[i+1:]
        for r in permutations(rest):
            temp.append([keep]+r)
    return temp
