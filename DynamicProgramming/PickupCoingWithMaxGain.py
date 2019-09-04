coins = [5, 10, 5, 15, 20, 10] #5,20,10      10,15,5
def pickupCoinsMaxGain(coins):
    dp = [[(0,0) for i in range(len(coins))] for j in range(len(coins))]
    
    for i in range(len(coins)):
        dp[i][i] = (coins[i],0)
    
    for l in range(2, len(coins)+1):
        for i in range(0, len(coins)-l+1):
            j = l+i-1
            pick_a = coins[i] + dp[i+1][j][1]
            pick_b = coins[j] + dp[i][j-1][1]
            if pick_a > pick_b:
                dp[i][j] = (pick_a, dp[i+1][j][0])
            else:
                dp[i][j] = (pick_b, dp[i][j-1][0])
    for row in dp:
        print(row)
pickupCoinsMaxGain(coins)
