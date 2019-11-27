'''
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
'''

def wordBreak(s, wordDict):
    wordDict = set(wordDict)
    q = s[0]
    visited=[False]*len(s)
    visited[0] = True
    while len(q)>0:
        idx = q.pop(0)
        if idx == len(s):
            return True
        for j in range(idx,len(s)):
            if s[idx:j+1] in wordDict and not visited[j+1]:
                q.append(j+1)
                visited[j+1] = True
    return False
