'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

outputs = []
def generateParen_helper(num_left, num_right, output):
    if num_left == num_right and num_left == 0:
        outputs.append(output)
        return
    else:
        if num_left >0:
            generateParen_helper(num_left-1, num_right, output+'(')
        if num_left<num_right:
            generateParen_helper(num_left, num_right-1, output+')')

def generateParen(n):
    generateParen_helper(n, n, '')
    return outputs
