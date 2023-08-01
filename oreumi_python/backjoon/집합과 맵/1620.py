import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pokemon = {}

for i in range(1, n+1) :
    name = input().rstrip()
    pokemon[name] = i
    pokemon[i] = name

want = [input().rstrip() for _ in range(m)]

for i in want :
    if i.isdigit() : # isdigit() : 데이터타입이 int형인지 구분
        print(pokemon[int(i)])
    else :
        print(pokemon[i])
