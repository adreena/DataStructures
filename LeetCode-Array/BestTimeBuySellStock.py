

def max_profit(nums):
    max_p = 0
    min_buy = nums[0]
    for num in nums[1:]:
        max_p = max(num-min_buy, max_p)
        min_buy = min(min_buy, num)
    return max_p
