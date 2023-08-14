# https://www.acmicpc.net/problem/2566

import sys
input = sys.stdin.readline

borad = [list(map(int, input().split())) for _ in range(9)]

max_number = 0
for row in range(9) :
    for col in range(9) :
        max_number = max(borad[row][col], max_number)
print(max_number)

for row in range(9) :
    for col in range(9) :
        if borad[row][col] == max_number :
            print(row+1, col+1)
            break