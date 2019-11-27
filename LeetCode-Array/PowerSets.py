


def powerSet(nums):
    if len(nums)==0:
        return []
    if len(nums) == 1:
        return [nums, []]

    first = nums[0]
    without_first = powerSet(nums[1:])
    with_first = []
    for w in without_first:
        with_first.append([first]+w)
    return with_first + without_first
