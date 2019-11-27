'''
Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.
'''

def longestValidParent(s):
    stack = [-1]
    max_len = 0
    while i < len(s):
        if s[i] == ')':
            stack.pop()
            if len(stack)==0:
                stack.append(i)
            else:
                max_len = max(max_len, i-stack[-1])
        else:
            stack.append(i)
        i+=1

    return max_len
