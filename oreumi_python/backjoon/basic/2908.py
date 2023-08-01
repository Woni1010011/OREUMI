a,b = map(str, input().split())

rev_a = [i for i in reversed(a)]
rev_b = [i for i in reversed(b)]

temp = ""

for i in rev_a :
    temp += i
int_a = int(temp)
print(temp)
temp = ""
for i in rev_b :
    temp += i
int_b = int(temp)

result = int_a if int_a > int_b else int_b

print(result)