'''
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.
Example 1:

Input: "babad"
Output: "bab"
'''

def longestPalindromic(s):
    dp = [[False]*(len(s)+1)]*(len(s)+1)
    for i in range(len(s)+1):
        dp[i][i]=True

    k=0
    max_len = 0
    start = 0
    for i in range(1, len(s)+1):
        k+=1
        for j in range(0, len(s)-k+1):
            if s[j] == s[j+k]:
                dp[j][j+k] = dp[j-1][j+k-1]
                if k == 2 or k==3:
                    dp[j][j+k] = True
                if max_len <k+1:
                    max_len = k+1
                    start = j
    return s[start:start+max_len]
