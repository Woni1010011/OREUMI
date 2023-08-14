# https://www.acmicpc.net/problem/2738

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = [list(map(int, input().rstrip().split())) for _ in range(n)]
li2 = [list(map(int, input().rstrip().split())) for _ in range(n)]

for i in range(n) :
    for j in range(m) :
        print(li[i][j] + li2[i][j], end=' ')
    print()