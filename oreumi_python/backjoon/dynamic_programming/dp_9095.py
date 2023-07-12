# <-- 9095번 : 1,2,3 더하기
# 다이나믹 프로그래밍
# 반복되는 패턴 / 초기값 셋팅 / 범위에 맞게 연산되는지 확인


# 입력값
n = int(input())
li = [int(input()) for _ in range(n)]

# 초기값 셋팅
dp = [0] * (max(li)+1)
dp[1], dp[2], dp[3] = 1,2,4

# 다이나믹 프로그래밍 bottom-up 방식
for i in range(4, len(dp)) :
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in li :
    print(dp[i])