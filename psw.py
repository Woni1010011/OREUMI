# <-- 1439 번 : 뒤집기

import re


S = "0001100"

# 0그룹과 1그룹으로 나눈다.
# 나눈 그룹의 많은 수를 기준으로 정한다.
# 기준이 된 수 => 최소횟수


# 런타임 에러
# import sys
# S = sys.stdin.readlines()

# S_zero = S.split('1')
# S_one = S.split('0')

# count_zero = 0
# count_one = 0

# for i in S_zero :
#     if '0' in i :
#         count_zero+=1

# for i in S_one :
#     if '1' in i :
#         count_one += 1

# print(min(count_zero, count_one))

# 바뀐 횟수와 뒤집은 횟수에서 규칙발견

# S = input()
# count = 0

# for i in range(1, len(S)) :
#     if S[i] != S[i-1] :
#         count+=1

# print((count+1)//2)

# # =============================

# # 값을 누적해나간다.
# # 
















