# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# O(n), O(1)
def findMedian(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
        start =0
        end = len(nums1)
        while start<=end:
            partX = (start+end)//2
            partY= (len(nums1)+len(nums2)+1)//2 - partX

            if partX == 0:
                maxLeftX= float('-inf')
            else:
                maxLeftX = nums1[partX-1]
            if partY == 0:
                maxLeftY= float('-inf')
            else:
                maxLeftY = nums2[partY-1]

            if partX == len(A):
                minRightX= float('inf')
            else:
                minRightX = nums1[partX]
            if partY == len(B):
                minRightY= float('inf')
            else:
                minRightY = nums2[partY-1]

            if maxLeftX<=minRightY and maxLeftY<=minRightX:
                if (len(nums1)+len(nums2)) %2 ==0:
                    return (max(maxLeftX, maxLeftY)+min(minRightX, minRightY))/2
                return max(maxLeftX, maxLeftY)
            elif maxLeftX>minRightY:
                end = partX-1
            else:
                start = partX+1
