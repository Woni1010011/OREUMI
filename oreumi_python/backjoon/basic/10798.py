# https://www.acmicpc.net/problem/10798

import sys
input = sys.stdin.readline

li = [list(input().rstrip()) for _ in range(5)]
max_li = 0

for i in li :
    max_li = max(max_li, len(i))

ans = ''

for i in range(max_li) :
    for j in range(5) :
        try :
            ans += li[j][i]
        except :
            pass

print(ans)
