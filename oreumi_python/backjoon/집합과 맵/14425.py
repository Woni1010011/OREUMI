# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())

# s = {}
# for _ in range(n) :
#     s[input().rstrip()] = 0

# li = [input().rsplit()[0] for _ in range(m)]

# for i in li :
#     if i in s.keys() :
#         s[i] += 1

# print(sum(s.values()))


N, M = map(int,input().split())

N_list = []
for i in range(N):
    N_word = input().strip()
    N_list.append(N_word)

M_list = []
for j in range(M):
    M_word = input().strip()
    M_list.append(M_word)

count = 0
for word in M_list:
    if word in N_list:
        count += 1

print(count)