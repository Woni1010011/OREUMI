# https://www.acmicpc.net/problem/2577

multi = int(input()) * int(input()) *int(input())

numbers = {}

for i in range(10) :
    numbers[i] = 0

for number in str(multi) :
    if number in numbers.keys() :
        numbers[number] += 1

print(numbers.values())