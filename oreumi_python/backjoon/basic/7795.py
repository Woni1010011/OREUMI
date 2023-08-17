# https://www.acmicpc.net/problem/7795

import sys
input = sys.stdin.readline

def binary_search (l) :
    start = 0
    end = m - 1
    result = 0

    while start <= end :
        mid = (start + end) // 2 

        if right[mid] < l :
            start = mid+1
            reuslt = mid
        else :
            end = mid -1
    return reuslt + 1


t = int(input())

for _ in range(t) :
    n, m = map(int, input().split())
    left = sorted(list(map(int, input().split())))
    right = sorted(list(map(int, input().split())))
    count = 0

    for l in left :
        if l > right[0] :
            temp = binary_search(l)
            count += temp
       
    print(count)

