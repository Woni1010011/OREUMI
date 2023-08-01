import sys
input = sys.stdin.readline

T = int(input())


for _ in range(T) :
    w, n = map(int, input().split())
    b = [[0,0]]
    count = 1
    for _ in range(n) :
        x, y = map(int, input().split())
        b.append([x, y])
    
    i = 0
    capacity = 0

    while i < n:
        capacity += b[i][1]
        # 쓰레기가 채워지지 않은 경우
        if capacity < w :
            count += 1
            i+=1
            capacity += b[i][1]
        elif capacity == w :
            pass

        # 쓰레기가 다 채워진 경우
        # 쓰레기가 초과되서 채워지려는 경우
        
    print(count)



