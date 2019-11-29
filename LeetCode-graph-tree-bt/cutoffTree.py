

def DFS(start, end):
    visited = defaultdict(lambda:False)
    stack = [start]
    while len(stack)>0:
        ci, cj = stack.pop()
        if end == [ci, cj]:
            return True
        visited[(ci,cj)] = True
        for ni, nj in [(ci+1,cj), (ci, cj+1), (ci-1, cj), (ci, cj-1)]:
            if ni >=0 and ni< len(ground) and \
               nj >=0 and nj < len(ground[0]) and \
               not visited[(ni,nj)]:
               stack.append((ni, nj))
    return False
def cutOffTrees(ground):
    trees = sorted([(v,row,col) for i, row in enumerate(ground)
                    for v, j in enumerate(row) if v>1]
    start = [0,0]
    count = 0
    for v, i, j in trees:
        nxt =[i,j]
        if not DFS(start, nxt):
            return False
        count+=1
        start = nxt
    return count
