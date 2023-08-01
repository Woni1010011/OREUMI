a, b, v = map(int, input().split())

day = (v-b) / (a-b)

result = int(day) if int(day) == day else int(day) + 1

print(result)