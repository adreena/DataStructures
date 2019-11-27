'''
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
'''
def minCoinChange(coins, amount):
    dp = [amount+1]*(amount+1)
    dp[0] = 0

    for i in range(len(dp)):
        for coin in coins:
            if coin <= i:
                if i == coin:
                    dp[i] = 1
                else:
                    dp[i] = min(dp[i], dp[coin]+dp[i-coin])
    if dp[-1] == amount+1:
        return -1
    return dp[-1]
