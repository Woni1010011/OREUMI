# https://www.acmicpc.net/problem/2002

# 1. 차량 대수의 입력값을 받는다.
# 2. 입력받은 수 만큼 차량을 순서대로 dict로 만든다.
# 3. 나가는 차량을 리스트로 만든다.
# 4. 나가는 차량의 순서가 들어온 차량의 순서보다 클 경우 추월.
# 5. 추월 횟수를 증가 시킨 후 다음차량 추월 비교



import sys
input = sys.stdin.readline

n = int(input())
cars = {}
out = []
count = 0

for i in range(n) :
    cars[input().rstrip()] = i

for _ in range(n) :
    out.append(input().rstrip())

for j in range(n-1) :

    for k in range(j+1, n) :
        if cars[out[j]] > cars[out[k]] :
            count += 1
            break


print(count)