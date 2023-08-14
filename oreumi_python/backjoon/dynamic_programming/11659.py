# https://www.acmicpc.net/problem/11659

# # 시간초과
# import sys
# input = sys.stdin.readline

# n, m  = map(int, input().split())
# li = list(map(int, input().split()))

# for _ in range(m) :
#     i, j = map(int, input().split())
#     ans = sum(li[i-1:j])
#     print(ans)

# dp로 풀기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))

dp = [0]
temp = 0

for i in li :
    temp += i
    dp.append(temp)
    
for _ in range(m) :
    i, j = map(int, input().split())
    ans = dp[j] - dp[i-1]
    print(ans)
