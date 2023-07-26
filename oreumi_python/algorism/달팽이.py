import sys
input = sys.stdin.readline

n = int(input())
target = int(input())

board = [[0]*n for _ in range(n)]

x = (n-1)//2
y = (n-1)//2
board[x][y] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

i = 2
start = 3

while x != 0 or y != 0 :
    while i <= start * start :
        if x == y == (n-1) // 2 :
            up, down, left, right = start, start -1, start -1, start -2
            x += dx[0]
            y += dy[0]
            up -= 1

        elif right > 0 :
            x += dx[3]
            y += dy[3]
            right -= 1

        elif down > 0 :
            x += dx[1]
            y += dy[1]
            down -= 1

        elif left > 0 :
            x += dx[2]
            y += dy[2]
            left -= 1

        elif up > 0 :
            x += dx[0]
            y += dy[0]
            up -= 1

        board[x][y] = i
        i += 1
    n -= 2
    start += 2

for j in range(len(board)) :
    print(*board[j])
    if target in board[j] :
        mx = j + 1
        my = board[j].index(target) + 1
print(mx, my)
