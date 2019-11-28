

from collections import defaultdict

def DFS_cycle(node):
    if visited[node] == 1:
        return False
    if visited[node] == -1:
        return True
    visited[node] = -1
    for nxt in graph[node]:
        if not DFS(nxt):
            return False
    visited[node] = 1
    return True

def courseSchedule(courses, numCourses):
    graph = defaultdict(lambda:[])
    for a,b in courses:
        graph[a].append(b)

    visited = [0]*numCourses

    for i in range(numCourses):
         if not DFS_cycle(i):
             return False
    return True
