import sys
input = sys.stdin.readline

T = int(input())


for _ in range(T) :
    w, n = map(int, input().split())
    x = [0] * n
    w = [0] * n
    distance = 0
    w_load = w

    for i in range(n) :
        x[i], w[i] = map(int, input().split())

        i = 0

        while i < n :

            # 용량이 같을때
            if w_load == w[i]:
                distance += 2 * x[i]
                i += 1
                w_load = w
            #용량이 여유가 있을때
            elif w_load > w[i] :
                w_load -= w[i]
                i += 1

            # 용량이 넘칠때
            else :
                distance += 2 * x[i]
                w_load = w
        
        # 용량이 여유가 있는 상태로 맨 마지막 지점에 도착하게 된다면
        if w_load < w :
            distance += 2 * x[i]
        print(distance)


