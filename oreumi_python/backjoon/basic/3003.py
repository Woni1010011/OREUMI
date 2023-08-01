chess = [1, 1, 2, 2, 2, 8]
li = list(map(int, input().split()))
ans = [0, 0, 0, 0, 0, 0]

for i in range(6) :
    ans[i] = chess[i] - li[i]

print(*ans)