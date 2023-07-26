import sys
input = sys.stdin.readline

li = [int(input()) for x in range(9)]

print(max(li))
print(li.index(max(li))+1)