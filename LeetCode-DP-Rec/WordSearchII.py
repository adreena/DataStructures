'''
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:

Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
'''
all_matches = []
def searchTrieDFS(i, j, trie, board):
    current_node = trie[board[i][j]]
    is_match = current_node.pop('$', False)
    if is_match:
        all_matches.append(is_match)
    temp =board[i][j]
    board[i][j] = '#'
    for nr, nc in [(i+1,j), (i-1,j), (i, j+1), (i, j-1)]:
        if nr >=0 and nr < len(board) and nc>=0 and nc<len(board[0]):
            searchTrieDFS(nr, nc, current_node, board)
    board[i][j] = temp
    if not current_node:
        trie.pop(current_node)
def wordSearch2(words, board):
    trie = {}
    for word in words:
        node = trie
        for w in word:
            node.setdefault(w:{})
        node['$'] = word

    for i in range(len(board)):
        for j in range(len(board[0])):
            if borad[i][j] in trie:
                SearchTrie(i, j, trie, board)
