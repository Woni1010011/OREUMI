

# <--- 백준 : 18258 번
# 큐2

# 큐 1과 다르게 deque(데크)를 사용해야한다.
# list의 경우 pop이 일어날때 앞으로 옮기는 과정에서 O(n)이라는 시간복잡도가 생겨
# 시간초과가 발생한다.
# deque는 시작접의 값을 넣고 빼거나, 끝 점의 값을 넣고 빼는데 최적화된 연산속도를 제공
# list보다 월등한 옵션


# import sys
# from collections import deque

# count = int(sys.stdin.readline())
# queue = deque([])

# for i in range(count) :
#     command = sys.stdin.readline().split()

#     if command[0] == 'push_back' :
#         queue.append(command[1])
#     elif command[0] == 'push_front' :
#         queue.appendleft(command[1])
#     elif command[0] == 'front' :
#         if len(queue) == 0 :
#             print(-1)
#         else :
#             print(queue[0])
#     elif command[0] == 'back' :
#         try :
#             print(queue[len(queue)-1])
#         except IndexError :
#             print(-1)
#     elif command[0] == 'size' :
#         print(len(queue))
#     elif command[0] == 'empty' :
#         if len(queue) == 0 :
#             print(1)
#         else :
#             print(0)
#     elif command[0] == 'pop_front' :
#         try :
#             print(queue.popleft())
#         except IndexError :
#             print(-1)
#     elif command[0] == 'pop_back' :
#         try :
#             print(queue.pop())
#         except IndexError :
#             print(-1)



# # for문 2번 돌렸을때랑 비교해서 코드가 간결해졌고, 시간복잡도도 줄어들었다.

# from functools import reduce
# li = [1,2,3,4,5,6,7,8]
# even = list(filter(lambda x : x % 2 == 0 , li))

# print(even)
