import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    string = input()
    print(string[0] + string[-1])