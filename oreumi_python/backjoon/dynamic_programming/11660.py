# https://www.acmicpc.net/problem/11660

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
print(array)

for _ in range(m) :
    x1, x2, y1, y2 = map(int, input().split())
    for i in range(x1+1, x2) :
        for j in range(y1+1, y2) :
            print(array[i][j])
            pass
