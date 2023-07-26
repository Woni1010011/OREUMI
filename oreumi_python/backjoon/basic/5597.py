import sys

student_list = list(x for x in range(1, 31))

for _ in range(28) :
    a = int(sys.stdin.readline())
    student_list.remove(a)

student_list.sort()

for li in student_list :
    print(li)