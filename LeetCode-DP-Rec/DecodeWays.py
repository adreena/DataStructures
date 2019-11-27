'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
'Z' -> 26
'''

def decode(amount):
    dp = [0]*(len(amount)+1)
    dp[0] = 1
    dp[1] = 1
    if amount[0] == '0':
        dp[0] = 0

    for i in range(2,len(amount)+1):
        one_digit = int(amount[i-1])
        two_digit = int(amount[i-2:i])
        if one_digit>0:
            dp[i] = dp[i-1]
        if two_digit>=10 and two_digit<=26:
            dp[i] += dp[i-2]
