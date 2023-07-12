# <--- 문제 : 11727 번 : 2*n 타일링2
# 작성자 : 박성원
# 작성일 2023-07-12

# 다이나믹 프로그래밍

import sys

# 입력값
n = int(sys.stdin.readline())

# 초기값 설정
dp = [0] * (n+1)
dp[1] = 1
dp[2] = 3

# 1부터 대입하여 발견한 규칙을 코드화
for i in range(3, n+1) :
    dp[i] = dp[i-1] + dp[i-2]*2

# 문제의 조건
print(dp[n] % 10007)
