# n = int(input())
# line = n * 2 -1
# star = 1
# for i in range(line) :
#     if i < n:
#         for j in range(n-i-1):
#             print(" ", end='')
#         for j in range(star):
#             print("*", end='')
#         star += 2
#     if i == n:
#         star -= 2
#     if i >= n:
#         star -= 2
#         for j in range(i-n+1):
#             print(" ", end='')
#         for j in range(star):
#             print("*", end='')
#     if i <= line:
#         print()


n = int(input())

def star(start, n) :
    if start < n :
        pass
    elif start == n :
        pass
    elif start == n * 2:
        pass
