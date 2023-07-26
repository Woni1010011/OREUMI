# str = input().upper()

# comp_str = list(set(str))
# list_count = []
# # 많이 사용된 알파벳 확인
# count = 0

# # 여기서 사용된 문자에 대한 횟수 저장
# for i in comp_str :
#     list_count.append(str.count(i))

# max_number = max(list_count)
# index = list_count.index(max_number)

# # 많이 사용된 알파벳이 여러개인지 확인
# for i in list_count :
#     if i == max_number :
#         count+=1

# # pizza 입력해보셈

# if count != 1 :
#     print("?")
# else:
#     print(comp_str[index])

# dict로 풀기
# 무언가를 카운트를 할때 dict 생각해보기
word = input().upper()   # 대문자의 글자를 세야되기 때문에, 전부다 대문자로 변경

count = dict()

# 단어에서 등장한 글자를 순서대로 셉니다
for i in word:  
    if i in count.keys():  # 딕셔너리 글자가 존재한다면 개수+1
        count[i] += 1
    else:         # 글자의 카운팅을 1로 초기화
        count[i] = 1    # < --- 새로 추가

print(count)
# ("M", 1) 
sorted_count = sorted(count.items(), key=lambda x:x[1], reverse=True)

print(sorted_count)

max_value_2 = 0
for idx, (k, v) in enumerate(sorted_count):
    if idx == 0:
        max_value_1 = v           # 첫번째로 많이 등장한 글자 개수
        max_word = k              # 첫번째로 많은 글자 저장
    elif idx == 1:
        max_value_2 = v           # 두번째로 많이 등장한 글자 개수
    else:
        break

if max_value_1 == max_value_2:    # max값이 같은 글자가 존재한다면
    print("?")
else:
    print(max_word)
