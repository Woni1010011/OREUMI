# 피보나치 수열
# 원리 앞의 두 숫자의 합계를 사용하여 현재의 인덱스가 됨
# 예시
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....

# 원하는 자릿수 입력
n = int(input())

# 더해 나갈 첫번째와 두번째 요소 설정
fibonacci = [0, 1]

# list의 append를 이용하여 피보나치 수열 완성
for i in range(2,n) :
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

print(fibonacci)
