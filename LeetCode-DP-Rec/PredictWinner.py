

def predictWinner(coins):
    dp = [[(0,0) for i in range(len(coins))] for i in range(len(coins))]
    for i in range(len(coins)):
        dp[i][i] = (coins[i],0)

    k=0
    for i in range(len(coins)):
        k+=1
        for j in range(0, len(coins)-k):
            pick_first = coins[j] + dp[j+1][j+k][1]
            pick_last = coins[j+k] + dp[j][j+k-1][1]
            if pick_first>pick_last:
                dp[j][j+k] = (pick_first, dp[j+1][j+k][0])
            else:
                dp[j][j+k] = (pick_last, dp[j][j+k-1][0])
    if dp[0][-1][0]> dp[0][-1][1]:
        return True
    return False
