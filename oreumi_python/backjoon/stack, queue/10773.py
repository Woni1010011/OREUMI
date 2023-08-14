# https://www.acmicpc.net/problem/10773

import sys
input = sys.stdin.readline

k = int(input()) 
stack = []

for _ in range(k) :
    number = int(input())
    if number != 0 :
        stack.append(number)
    else :
        stack.pop()

print(sum(stack))
