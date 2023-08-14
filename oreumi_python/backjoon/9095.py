# https://www.acmicpc.net/problem/9095

import sys
input = sys.stdin.readline

T = int(input())
li = [int(input()) for _ in range(T)]

dp = [0] * (max(li) + 1)

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, max(li)+1) :
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for i in li :
    print(dp[i])

def dfs (n) :
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, n+1) :
        dp[i] = dp[i-2] + dp[i-1] + dp[i-3]

    return dp[n]

for _ in range(T) :
    number = int(input())
    print(dfs(number))

