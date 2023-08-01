import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

m = int(input())
check = list(map(int, input().split()))

ans = {}

for i in check :
    ans[i] = 0

for i in li :
    if i in ans.keys() :
        ans[i] = 1

print(*ans.values())

# dict의 시간복잡도는 O(1)인데 dict를 셋팅하기 위해 for문이 돌아간다면 시간복잡도는 O(n)이 되는게 맞지 않나요?? O(n) 이 맞음