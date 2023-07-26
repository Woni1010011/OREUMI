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


# bfs 의 경우 queue를 이용하기 때문에 
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
# 정점 초기화
visited = [False] * (n+1)

# 방문순서 저장
vis_bfs = []

def bfs (start) :
    # 시작 정점을 기준으로 queue 생성
    queue = deque([start])
    # 시작 정점을 방문했음
    visited[start] = True
    while queue :
        # 방문한 정점 제거
        v = queue.popleft()
        vis_bfs.append(v)
        # 그래프 탐색
        for i in graph[v] :
            # 방문여부 확인
            if not visited[i] :
                # 정점과 연결된 정점을 queue에 추가
                queue.append(i)
                # 방문여부 확인
                visited[i] = True

bfs(v)
print(vis_bfs)