# # 문제 2445번 : 별찍기
# # 재귀함수로 풀어보기

# 출력

# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *


count = int(input())

def star(start, end) :
    # 상단기준
    if start < end :
        print('*'*start, ' '*(end*2-(2*start)), '*'*start, sep='')
        return star(start+1, end)
    # 중단기준
    elif start == end :
        print('*'*end*2)
        return star(start+1, end)
    # 하단기준
    elif start > end and start != end*2:
        print('*'*(2*end-start), ' '*((start-end)*2), '*'*(2*end-start), sep='')
        return star(start+1, end)

star(1, count)

# for문 2번 돌렸을때랑 비교해서 코드가 간결해졌고, 시간복잡도도 줄어들었다.