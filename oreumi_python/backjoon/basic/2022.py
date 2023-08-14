# https://www.acmicpc.net/problem/2002
# bfs? 브루트포스? 

# 1. 차량대수를 입력값을 받는다
# 2. 차량대수만큼 터널에 들어간 차량을 순서대로 담는다
# 3. 터널에 나온 차량을 순서대로 list or dict로 담는다
# 4. 추월한 차량의 대수를 출력한다.

import sys
input = sys.stdin.readline

n = int(input())
cars = {}

for i in range(n) :
    cars[input().rstrip()] = i

print(cars)