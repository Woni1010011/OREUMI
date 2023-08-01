import sys
input = sys.stdin.readline

li = list(map(lambda x : int(x)*2, input().split()))
print(li)


li1 = list(filter(lambda x : int(x)%2 == 0, input().split()))
print(li1)