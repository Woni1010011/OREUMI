# https://www.acmicpc.net/problem/2563

import sys
input = sys.stdin.readline

T = int(input())
graph = [[0] * 100 for _ in range(100)]

for _ in range(T) :
    x, y = map(int, input().split())
    
    for i in range(x, x+10) :
        for j in range(y, y+10) :
            graph[i][j] = 1

result = 0

for line in graph :
    result += sum(line)

print(result)