
def MinimumWindowSubstr(s, t):
    t_count = [0]*26
    s_count = [0]*26
    for c in t:
        t_count[ord(c)-ord('a')]+=1

    start = 0
    count = 0
    min_len = float('inf')
    min_start = -1
    for i in range(len(s)):
        c = s[i]
        s_count[ord(c)-ord('a')]+=1
        if s_count[ord(c)-ord('a')] <= t_count[ord(c)-ord('a')]:
            count+=1
        if count == len(t):
            # minmize left
            while s_count[ord(s[start])-ord('a')] > t_count[ord(s[start])-ord('a')] or \
                  t_count[ord(s[start])-ord('a')] == 0:
                  start+=1
                  s_count[ord(s[start])-ord('a')] -=1
            if i - start +1 < min_len:
                min_len = i-start+1
                min_start = start
    if min_start >=0:
        return s[min_start:min_start+min_len]
