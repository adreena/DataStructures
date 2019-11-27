'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
'''
# O(logn)
def search(nums, target):
    start = 0
    end = len(nums)-1

    while start<end:
        mid = (start+end)//2
        if nums[mid] == target:
            return mid
        else:
            if nums[start]<=nums[mid]:
                if target>=nums[start] and target<=nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
            else:
                if target>=nums[mid] and target <=nums[end]:
                    start = mid+1
                else:
                    end = mid-1
