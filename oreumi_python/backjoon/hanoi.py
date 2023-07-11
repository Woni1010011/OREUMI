# 1914번 : 하노이탑
# index로 접근하기 보단, 로직에 집중
# 종료 지점과, 수행해야 할것과 어떤 요소를 넘기며 관리할지 집중

def hanoi(n, first, second, end) :
    if n == 1 :
        print(first, end)
        return
    else :
        hanoi(n-1,first, end, second)
        print(first, end)
        hanoi(n-1,second, first, end)
        

count = int(input())
print(2**count -1)

hanoi(count,1,2,3)