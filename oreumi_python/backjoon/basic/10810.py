M, N = map(int, input().split())
bucket = [0] * M
l = []

for i in range(N):
    l.append(input().split())

for i in l:
    for j in range(int(i[0])-1, int(i[1])):
        bucket[j] = i[2]

print(*bucket)