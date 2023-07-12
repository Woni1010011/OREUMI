# import sys

# n = int(sys.stdin.readline())

# li = list(map(int, sys.stdin.readline().split()))


# dp = [0] * (n+1)

# dp[1] = li[0] + li[1] if li[0] + li[1] > 0 else 0

# for i in range(2, n) :
#     if li[i] + dp[i-1] < 0 :
#         dp[i] = 0
#     else :
#         dp[i] = dp[i-1] + li[i]


# result = max(dp) if max(dp) > max(li) and max(dp) != 0 else max(li)
# print(result)
    
## ===================== 런타임에러

import sys 

n = int(sys.stdin.readline())

li = list(map(int, sys.stdin.readline().split()))

dp = [0] * (n)
dp[0] = li[0]

for i in range(1, n) :
    dp[i] = max(li[i], li[i] + dp[i-1])

print(max(dp))