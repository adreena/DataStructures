'''
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green.
The cost of painting each house with a certain color is different.
You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix.
For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on...
Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
'''

def paintCost(costs):
    dp = [[0 0 0]*len(costs)]
    dp[0] = costs[0]

    for house_row in len(costs):
        for i in range(3):
            dp[house_row][i] = min(dp[house_row-1][:i]+dp[house_row-1][i+1:]) + costs[house_row][i]
    return min(dp[-1])
