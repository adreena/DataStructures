'''
Input:  [1,2,3,4]
Output: [24,12,8,6]
'''

def productOfArray(nums):
    rights = [1]*len(nums)
    for i in range(len(nums)-2,-1,-1):
        rights[i]=right[i+1]*nums[i+1]
    temp =1
    for i in range(len(nums)):
        rights[i]*=temp
        temp*=nums[i]
    return nums
