import sys

n = int(sys.stdin.readline())

li = [int(sys.stdin.readline()) for i in range(n)]

dp = [0] * (max(li) + 1)

dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(4, max(li)+1) :
    dp[i] = dp[i-2] + dp[i-3]

for i in li:
    print(dp[i])