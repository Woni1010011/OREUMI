# 입력값
"""
n : 정점의 개수 / m : 간선의 개수, v : 시작할 정점의 번호
4 5 1
1 2
1 3
1 4
2 4
3 4
"""

import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())

# 그래프 만들기
graph = [[] for _ in range(n+1)]
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
vis_bfs = []

def bfs (start) :
    queue = deque([start])
    visited[start] = True
    while queue :
        v = queue.popleft()
        vis_bfs.append(v)
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True

bfs(v)
print(vis_bfs)