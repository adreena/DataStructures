

def dfs(bi, bj, wi, word, board):
    if wi == len(word):
        return True
    if bi<0 or bi>=len(board) or \
       bj<0 or bj>=len(board[0]) or \
       wi >len(word) or \
       word[wi]!=board[bi][bj]:
       return False
    temp = board[bi][bj]
    board[bi][bj]=' '
    found = dfs(bi+1, bj, wi+1, word, board) or \
            dfs(bi-1, bj, wi+1, word, board) or \
            dfs(bi, bj+1, wi+1, word, board) or \
            dfs(bi, bj-1, wi+1, word, board)
    board[bi][bj] = temp
    return found
    
def findWord(board, word):

    for i in range(board):
        for j in range(board[0]):
            if board[i][j] == word[0]:
                if dfs(i,j,0,word,board):
                    return True
    return False
