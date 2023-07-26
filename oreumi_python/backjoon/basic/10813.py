import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = [x for x in range(1, n+1)]

a = []
for i in range(1, n+1) :
    a.append(i)

for _ in range(m) :
    i, j = map(lambda x: int(x) - 1, input().split())
    li[i], li[j] = li[j], li[i]

print(*li)