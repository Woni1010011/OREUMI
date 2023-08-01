import sys
input = sys.stdin.readline

for _ in range(3) :
    li = map(int, input().split())
    li_sum = sum(li)
    if li_sum == 3 :
        print("A")
    elif li_sum == 2 :
        print("B")
    elif li_sum == 1 :
        print("C")
    elif li_sum == 4:
        print("E")
    else :
        print("D")