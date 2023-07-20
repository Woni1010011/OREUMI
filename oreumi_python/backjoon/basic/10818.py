# 10818번 : 최소, 최대

n = int(input())

li = list(map(int, input().split()))

ans = []
ans.append(min(li))
ans.append(max(li))

print(*ans)