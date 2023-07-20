# 10807번 : 개수 세기

n = int(input())
li = list(map(int, input().split()))
target = int(input())
count = 0

# for i in li :
#     if i == target :
#         count += 1

# print(count)


# count 함수 사용

print(li.count(target))

