# https://www.acmicpc.net/problem/20310

# from collections import deque

# s = list(input())

# zero = s.count('0') // 2
# one = s.count('1') // 2

# for _ in range(zero) :
#     s.pop(-s[::-1].index('0')-1)
# for _ in range(one) :
#     s.pop(s.index('1'))

# print(''.join(s))

s = input()
cnt_0 = s.count('0')
cnt_1 = len(s) - cnt_0
cnt_0 //= 2
cnt_1 //= 2

s_arr = [char for char in s]
idx = 0
for i in range(len(s_arr)-1, -1, -1):
    if s_arr[i] == '0':
        idx += 1
        s_arr[i] = 'x'
    if idx == cnt_0:
        break

idx = 0
for i in range(len(s_arr)):
    if s_arr[i] == '1':
        idx += 1
        s_arr[i] = 'x'
    if idx == cnt_1:
        break
    
for i in s_arr:
    if i != 'x':
        print(i, end='')