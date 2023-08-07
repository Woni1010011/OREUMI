# https://www.acmicpc.net/problem/1316

import sys
input = sys.stdin.readline

T = int(input())

li = [input().rstrip() for _ in range(T)]
count = T

for word in li :
    for i in range(len(word)-1) :
        if word[i] == word[i+1] :
            continue
        if word[i] in word[i+1:] :
            count -= 1
            break

print(count)

    
           