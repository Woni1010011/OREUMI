# https://www.acmicpc.net/problem/1264

import sys
input = sys.stdin.readline


while True :
    sentence = input().lower().rstrip()
    vowel = { 'a' : 0, 'e' : 0, 'i' : 0, 'o' : 0, 'u' : 0}


    if sentence == "#" :
        break
    for word in sentence :
        if word in vowel.keys() :
            vowel[word] += 1
    print(sum(vowel.values()))