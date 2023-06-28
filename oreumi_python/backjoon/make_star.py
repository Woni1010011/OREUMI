# 백준 2446번 : 별 찍기 - 9

# 예제 입력 : 5

# 예상 출력
# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********

# 조건 : 이중 for문을 사용 할 것

# 접근방법
# 1. 예상 출력의 총 길이와 입력값의 연관성에 집중
# 2. line의 증가와 blank의 연관성에 집중
# 3. 5번째 줄 기준으로 조건식으로 별의 갯수 증감 조절


# 예제입력
n = int(input()) 

# 첫 줄의 별의 갯수 설정
stars = n*2 -1

# 첫 for문은 line 에 집중
for line in range(n*2-1):

    # 상단 별의 갯수가 줄어드는 조건
    if line < n:

        # 라인이 증가 할수록 공백도 늘어남
        for blank in range(line):
            print(" ", end='')
        for star in range(stars):
            print("*", end='')
        stars -= 2
    
    # 5번째 줄 이후에 맞게 별의 갯수 설정
    if line == n :
        stars += 4
    
    # 하단 별의 갯수가 증가하는 조건
    if line >= n:

        # 라인이 증가 할 수록 공백은 줄어듦
        for blank in range(n*2 - line-2):
            print(" ", end='')
        for star in range(stars):
            print("*", end='')
        stars += 2

    print("")