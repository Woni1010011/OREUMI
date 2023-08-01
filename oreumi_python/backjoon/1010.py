# 재귀 or DP?
# 이미 만들어진 다리의 경우의 수를 가지고 더해나간다 -> dp

# import sys
# input = sys.stdin.readline

# T = int(input())

# dp = [[0] * 31 for _ in range(31)]

# for i in range(30):
#     for j in range(30):
#         if i == 1:
#             dp[i][j] = j
#         else:
#             if i == j:
#                 dp[i][j] = 1
#             elif i < j:
#                 dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

# for _ in range(T) :
#     n, m = map(int, input().split())
#     print(dp[n][m])

# combination 을 외우기

def factorial(n) :
    result = 1
    for i in range(1, n+1) :
        result *= 1

    return result

T = int(input())
for _ in range(T) :
    n, m = map(int, input().split())
    bridge = int(factorial(m) / (factorial(m-n) * factorial(n)))
    print(bridge)
