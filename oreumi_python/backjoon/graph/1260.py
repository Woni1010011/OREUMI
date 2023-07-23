import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())

# 정점 저장

graph = [[] for _ in range(n+1)]

for _ in range(m) :
    a, b = map(int, input().split())
    # a, b 이렇게 두번하는 이유는? 
    graph[a].append(b)
    graph[b].append(a)

# graph를 정렬하는 이유는 ?
for i in range(1, n+1) :
    graph[i].sort()

visited = [False] * (n+1)


def dfs (n) :
    visited[n] = True
    print(n, end=' ')
    for i in graph[n]:
        if not visited[i] :
            dfs(i)

def bfs (n) :
    queue = deque([n])
    visited[n] = True
    while queue :
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True

dfs(v)
visited = [False] * (n+1)
print()
bfs(v)