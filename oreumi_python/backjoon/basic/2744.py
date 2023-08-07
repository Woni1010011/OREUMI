# https://www.acmicpc.net/problem/2744

string = input()

for word in string :
    if word.isupper() :
        print(word.lower(), end='')
    else :
        print(word.upper(), end='')