# https://www.acmicpc.net/problem/1064

ax, ay, bx, by, cx, cy = map(int, input().split())

# 기울기가 같다면
if ((ay-by)*(ax-cx) == (ay-cy)*(ax-bx)):
    print(-1.0)

# 기울기가 다르다면, 평행사변형의 제일 큰 둘레와 제일 작은 둘레의 차이 구하기
else:
    ab_length = ((ax-bx)**2 + (ay-by)**2)**0.5
    ac_length = ((ax-cx)**2 + (ay-cy)**2)**0.5
    bc_length = ((bx-cx)**2 + (by-cy)**2)**0.5

    length = [ab_length, ac_length, bc_length]
    result = max(length) - min(length)
    print(2*result)