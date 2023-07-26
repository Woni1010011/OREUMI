import sys
input = sys.stdin.readline

li = [int(input()) for _ in range(10)]
ans = []

for i in li :
    ans.append(i%42)

result = set(ans)
print(len(result))