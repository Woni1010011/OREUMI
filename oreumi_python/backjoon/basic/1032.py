# https://www.acmicpc.net/problem/1032

import sys
input = sys.stdin.readline

N = int(input())
string = list(input().rstrip())



for _ in range(N-1) :
    word = input().rstrip()
    for i in range(len(string)) :
        if string[i] != word[i] :
            string[i] = "?"

print(''.join(string))



