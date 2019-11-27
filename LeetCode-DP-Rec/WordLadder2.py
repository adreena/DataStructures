'''
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
'''
from collections import defaultdict
def wordLadder(wordList, beginWord, endWord):
    wordDict = defaultdict(lambda:set())
    for word in wordList:
        for i in range(len(word)):
            key = word[:i]+'*'+word[i+1:]
            wordDict[key].add(word)

    # BFS find shortest paths
    visited = defaultdict(lambda:-1)
    parents = defaultdict(lambda:set())
    q = [beginWord]
    visited[beginWord] = 0
    while len(q)>0:
        current = q.pop(0)
        if current == endWord:
            break
        for i in range(len(current)):
            key = word[:i]+'*'+word[i+1:]
            for nxt in wordDict[key]:
                if nxt != current:
                    if visited[nxt] == -1:
                        visited[nxt] = visited[current]+1
                        q.append(nxt)
                    parents[nxt].add(current)


    # DFS : backtrack from endWord to begin and create paths
    paths = set()
    min_len = float('inf')
    for parent in parents[endWord]:
        stack = [parent]
        path = []
        while len(stack)>0:
            top = stack.pop()
            if top == beginWord:
                if len(path) >0 and len(path) == visited[endWord]:
                    paths.add(tuple(path))
            for prev in parents[parent]:
                if visited[prev]<visited[parent]:
                    stack.append(prev, [prev]+path)

    return paths
