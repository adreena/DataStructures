'''
Input: [1,2,3]
Output: [1,2,4]
'''

def plusOne(nums):
    carry = 0
    for i in range(len(nums)-1, -1,-1):
        nums[i]+=1+carry
        if nums[i]>9:
            carry = nums[i] %10
            nums[i] /= 10
        if carry == 0:
            break
    if carry>0:
        return [carry]+nums
    else:
        return nums
