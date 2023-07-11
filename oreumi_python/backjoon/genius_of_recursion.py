# --*--
# 작성자 : 박성원
# 작성일 2023-07-05

# 문제 : 25501 번 (재귀의 귀재)


import sys


n = int(input())
li = []

# 리스트에 입력값 추가
for i in range(n) :
    a = sys.stdin.readline().strip()
    li.append(a)


def recursion(s, l, r):
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l + 1, r - 1)

def isPalindrome(s):
    return recursion(s, 0, len(s) - 1)


# 재귀의 끝은 재귀의 횟수와 동일
def count(str, start, end) :
    
    if start >= end :
        return start + 1
    elif str[start] != str[end] :
        return start + 1
    else :
        return count(str, start+1, end-1)


# 입력받은 리스트를 프린트
for i in li :
    print(isPalindrome(i), count(i,0, len(i)-1))

### 위 방법으로 하게 되면 재귀함수가 하나 더 추가 되기 때문에 메모리를 많이 차지하는 문제점이 발생.
### recursion 에서 카운트까지 계산하면 더 효울적이라 생각
### 입력값을 리스트로 따로 관리하기보단, 출력과 동시에 하는 방법을 생각할 필요가 있음.