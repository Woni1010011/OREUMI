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
input = sys.stdin.readline

n, m, v = map(int, input().split())
# 그래프 만들기
graph = [[] for _ in range(n+1)]
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# 방문여부 확인필요
visited = [False] * (n+1)


def dfs (start) :
    visited[start] = True
    vis_dfs.append(start)
    for i in graph[start] :
        if not visited[i] :
            dfs(i)
    
vis_dfs = []
dfs(v)
print(vis_dfs)

