import sys
input = sys.stdin.readline

ans = {}
n = int(input())
for _ in range(n) :
    name, work = map(str, input().split())
    ans[name] = work
rev_ans = sorted(ans.items(), reverse=True)

for i in rev_ans :
    if i[1] == 'enter' :
        print(i[0])