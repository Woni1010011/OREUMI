
# # N = int(input())
# N = 6
# dp = [0] * (N+1)
# dp[1] = 0

# for i in range(2, N+1) :
#     dp[i] = dp[i-1] + 1

#     if i % 3 == 0 and dp[i] > dp[i//3] + 1 :
#         dp[i] = dp[i//3] + 1
#     elif i % 2 == 0 and dp[i] > dp[i//2] + 1 :
#         dp[i] = dp[i//2] + 1

# print(dp[N])

# ans = []
# ans.append(N)
# ans.append(N-1)
# temp = N-1
# while temp != 0 :
#     if temp % 3 == 0 :
#         temp = temp//3
#     elif temp % 2 == 0 :
#         temp = temp//2 
#     else :
#         temp -= 1
#     ans.append(temp)
    

# for i in ans[:len(ans)-1] :
#     print(i, end=' ')



"""
백준 12852번 : 1로 만들기 2
작성자 : 정효주
작성일 : 2023-07-15 
"""

n = int(input())

dp = [0] * (n+1)  # 각 수에 대한 연산횟수
visited = [0] *(n+1)  # 이전 방문수

# 연산
for i in range(2, n+1):
    dp[i] = dp[i-1]+1
    visited[i] = i - 1

    if i % 3 == 0 and dp[i//3] +1 < dp[i]:
        dp[i] = dp[i//3] + 1
        visited[i] = i//3

    if i % 2 == 0 and dp[i//2] +1 < dp[i]:
        dp[i] = dp[i//2] + 1
        visited[i] = i//2

cnt = []  # 최솟값일때 연산에 포함되는 수
current = n
while visited[current] != 0:
    cnt.append(current)
    current = visited[current]
cnt.append(1)  # '1이 아닐때까지'이므로 마지막에 1을 더해줌

print(dp[n])
print(*cnt)