

def isGraphBipartite(graph):
    colors = defaultdict(lambda:-1)

    for i in range(len(graph)):
        if colors[i] == -1:
            colors[i] = 0
            q = [i]
            while len(q)>0:
                top = q.pop(0)
                for nxt in graph[top]:
                    if colors[nxt] == color[top]:
                        return False
                    colors[nxt] = colors[top]^1
                    q.append(nxt)
    return True
