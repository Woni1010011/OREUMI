string = input()

table = {}

for i in range(97, 123) :
    table[chr(i)] = -1

for i in string :
    if table[i] == -1 :
        index = string.index(i) + 1
        table[i] += index

print(*table.values())