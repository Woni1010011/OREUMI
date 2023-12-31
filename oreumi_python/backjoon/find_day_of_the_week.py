# 백준 : 1924 - 2007년
# 문제 : 오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.
# 입력 : 첫째 줄에 빈 칸을 사이에 두고 x(1 ≤ x ≤ 12)와 y(1 ≤ y ≤ 31)이 주어진다. 
#       참고로 2007년에는 1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.
# 출력 : 첫째 줄에 x월 y일이 무슨 요일인지에 따라 SUN, MON, TUE, WED, THU, FRI, SAT중 하나를 출력한다.

# 접근방법
# 1. month 와 day 그리고 요일과의 상관관계에 집중
# 2. 주어진 (월 일) 의 총 합과 요일의 갯수 나머지 값의 연관성에 집중
# 3. 주어진 값을 총 일수로 만드는것에 집중

month, day = map(int, input().split())

# 각 월별 총 일수
MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAY = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

total_day = 0

# 입력된 월을 총 일수로 바꾸는 작업
for i in range(month-1):
    total_day += MONTH[i]

# 주어진 일수를 더해 총 일수를 완성
total_day += day

# 총 일수에 총 요일을 뺀 남은 수를 가지고 DAY의 인덱스 접근 후 출력
print(DAY[total_day % 7])