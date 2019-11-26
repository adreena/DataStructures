'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
'''

def mergeIntervals(nums):
    nums.sort(key=lambda x: x[0])
    output = [nums[0]]
    for num in nums[1:]:
        if num[0]<= output[-1][1]:
            output[-1][1] = max(nums[1], output[-1][1])
        else:
            output.append(num)
    return output
