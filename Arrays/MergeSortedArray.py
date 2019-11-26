'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
'''

def mergArrays(nums1, nums2, m, n):
    i = m-1
    j = n-1
    write_idx = len(nums1)-1
    while i >=0 and j >=0:
        if nums1[i]>nums2[j]:
            nums1[write_idx] = nums1[i]
            i-=1
        elif nums1[i]< nums2[j]:
            nums1[write_idx] = nums2[j]
            j-=1
        else:
            nums1[write_idx] = nums1[i]
            write_idx-=1
            nums1[write_idx] = nums2[j]
            j-=1
            i-=1
        write_idx-1
    while j  >=0:
        nums1[write_idx] = nums[j]
        j-=1
        write_idx-=1
    return nums1
