'''
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
'''

def regMatch(s,p):
    dp = [[False]*(len(p)+1)]*(len(s)+1)
    dp[0][0] = True
    for i in range(1, len(p)+1):
        if p[i-1] == '*':
            dp[0][i] = dp[0][i-2]
    for i in range(1, len(s)+1):
        for j in range(1, len(p)+1):
            if p[j-1] == s[i-1] or p[j-1]== '.':
                dp[i][j] = dp[i-1][j-1]
            else:
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        dp[i][j] |= dp[i-1][j]
    return dp[-1][-1]
