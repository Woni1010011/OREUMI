dial = {}
timer = 3

for i in range(65, 80) :
    if (i - 64) % 3 != 0 :
        dial[chr(i)] = timer
    else:
        dial[chr(i)] = timer
        timer += 1

for i in range(80, 84) :
    dial[chr(i)] = timer
timer += 1
for i in range(84, 87) :
    dial[chr(i)] = timer
timer += 1
for i in range(87, 91) :
    dial[chr(i)] = timer

n = input()
result = 0

for i in n :
    result += dial[i]

print(result)