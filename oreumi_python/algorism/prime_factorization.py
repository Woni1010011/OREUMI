# 소인수 분해
# 주어진 수를 소수의 곱으로 분해하는 과정
# 즉, 어떤 수를 소수들의 곱으로 나타내는 것

# 원리
# 주어진 수에 나머지가 0이 나올때까지 2로 나눈다 (짝수제거)
# 조건에 따라 홀수의 소인수 유무 확인 (홀수제거)
# p * p <= n을 하는 이유 :
# 반복문에서 p를 나눠 인수유무를 결정해야하는데 n이 p^2보다 작으면 나눌수 없기 때문에 p*p <= n 조건으로 소인수의 유무를 확인
# p += 2를 하는 이유 : 홀수인 소인수를 찾기 위함.

import sys

number = int(sys.stdin.readline())

factors = []

# 짝수를 걸러내는 과정
while number % 2 == 0 :
    factors.append(2)
    number //=2

# 홀수를 걸러내는 과정
p = 3
while p * p <= number :
    if number % p == 0:
        factors.append(p)
        number //= p
    else:
        p += 2

# 모든 과정을 거치고 남은 number 또한 소인수
factors.append(number)
print(factors)