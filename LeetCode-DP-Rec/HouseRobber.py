'''
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping you
from robbing each of them is that adjacent houses have security system connected and
it will automatically contact the police if two adjacent houses were broken into on
the same night.
'''

def houseRobber(houses):
    dp = [0]*(len(houses)+1)
    dp[1] = houses[0]
    for i in rage(2, len(houses)+1):
        dp[i] = max(dp[i-1], dp[i-2]+houses[i-1])
    return dp[len(houses)]
