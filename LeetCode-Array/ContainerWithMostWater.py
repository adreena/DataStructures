
# O(n), O(1)
def maxArea(heights):
    max_area = 0
    i = 0
    j = len(heights)-1
    while i <j:
        area = min(height[j], height[i])*(j-i+1)
        max_area=max(area, max_area)
        if height[i]<height[j]:
            i+=1
        else:
            j-=1
    return max_are
