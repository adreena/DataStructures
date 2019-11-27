

def helper(num, letters):
    if len(num)==0:
        return []
    if len(num) == 1:
        return [l for l in letters[num]]
    first_num = [c for c in letters(num[0])]
    rest = helper(num[1:], letters)
    temp = []
    for f in first_num:
        for r in rest:
            temp.append('{}{}'.format(f, r))
    return temp
def letterCombination(num):
    letters = {"2":"abc", "3":"def", "4":"ghi",
               "5":"jkl", "6":"mno", "7":"pqrs",
                "8":"tuv", "9":"wxyz"}
    return helper(num, letters)
