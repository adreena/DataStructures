
dp = [[0 for i in range(len(matrix[0])+1)] for j in range(len(matrix)+1)]
for i in range(1,len(matrix)):
    for j in range(1,len(matrix[0])):
        dp[i][j] = dp[i-1][j]+dp[i][j-1]+matrix[i-1][j-1] -dp[i-1][j-1]


def sumRegion(row1, col1, row2, col2 ):

    top = 0
    left = 0
    total = dp[row2+1][col2+1]

    if row1>0:
        top = dp[row1-1][col2+1]
    if col1>0:
        left = dp[row2+1[col1-1] - dp[row1][col1-1]
    return total-left-top
