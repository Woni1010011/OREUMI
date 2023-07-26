n = int(input())
li = list(map(int, input().split()))
m = max(li)

# new_li = [(lambda x : x/m*100) for _ in li]
new_li = [x / m * 100 for x in li]
sum_li = sum(new_li)

print(sum_li/len(new_li))

