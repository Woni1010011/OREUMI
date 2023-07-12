# <--- 백준 : 18258 번
# 큐2

# 큐 1과 다르게 deque(데크)를 사용해야한다.
# list의 경우 pop이 일어날때 앞으로 옮기는 과정에서 O(n)이라는 시간복잡도가 생겨
# 시간초과가 발생한다.
# deque는 시작접의 값을 넣고 빼거나, 끝 점의 값을 넣고 빼는데 최적화된 연산속도를 제공
# list보다 월등한 옵션


import sys
from collections import deque

count = int(sys.stdin.readline())
li = deque([])

for i in range(count) :
    command = sys.stdin.readline().split()

    if command[0] == 'push' :
        li.append(command[1])
    elif command[0] == 'front' :
        if len(li) == 0 :
            print(-1)
        else :
            print(li[0])
    elif command[0] == 'back' :
        if len(li) == 0:
            print(-1)
        else :
            print(li[len(li)-1])
    elif command[0] == 'size' :
        print(len(li))
    elif command[0] == 'empty' :
        if len(li) == 0 :
            print(1)
        else :
            print(0)
    elif command[0] == 'pop' :
        if len(li) == 0 :
            print(-1)
        else :
            print(li.popleft())
    elif command[0] == 'push' :
        li.append(command[1])