# https://www.acmicpc.net/problem/3085

# 1. n*n 만큼의 사탕을 받을 n을 입력값을 받는다.
# 2. 주어진 사탕을 2중 list로 저장
# 3. 각각의 사탕을 기준으로 x, y 의 값을 부여하여 탐색 후 횟수를 증가
# 4. result에 각 사탕마다 비교하여 최대값 저장

# 방문여부를 확인?

import sys
input = sys.stdin.readline

n = int(input())
candies = [list(input().rstrip('\n')) for _ in range(n)]
x = [0,0,1,-1]
y = [1,-1,0,0]

result = 0
temp = ''

for i in range(n) :
    for j in range(n) :
        for k in range(4) :
            nx = x[k] + j
            ny = y[k] + i
            if nx >= 0 and ny >= 0 and nx < n and ny < n :

                if candies[i][j] != candies[ny][nx] :
                    temp = candies[i][j]
                    candies[i][j] = candies[ny][ny]
                    candies[ny][nx] = temp
                
                row_cnt = 1
                col_cnt = 1

                for l in range(n-1) :
                    if candies[i][l] == candies[i][l+1] :
                        row_cnt += 1
                    else :
                        row_cnt = 1
                    if candies[l][j] == candies[l+1][j] :
                        col_cnt += 1
                    else :
                        col_cnt = 1
                    result = max(result, row_cnt, col_cnt)

                if candies[i][j] != candies[ny][nx] :
                    candies[ny][nx] = candies[i][j]
                    candies[i][j] = temp
print(result)