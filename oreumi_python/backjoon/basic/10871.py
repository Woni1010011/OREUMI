# 10871번 : X보다 작은 수

n, x = map(int, input().split())
li = list(map(int, input().split()))

ans = []

for i in li :
    if i < x :
        ans.append(i)

print(*ans)