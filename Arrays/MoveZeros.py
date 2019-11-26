
'''
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
'''
def moveZeros(nums):
    write_idx = -1
    i = 0
    while i <len(nums):
        if nums[i] != 0:
            nums[write_idx] = nums[i]
            if i != write_idx:
                nums[i] = 0
            write_idx+=1
        i+=1
