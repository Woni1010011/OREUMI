import sys

repeat = int(sys.stdin.readline())

for i in range(repeat) :
    a, b = map(str, sys.stdin.readline().split())
    for j in b :
        print(j*int(a), end='')
    if i != repeat-1 :
        print()