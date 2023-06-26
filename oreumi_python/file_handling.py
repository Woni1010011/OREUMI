# --*--
# 문제 5
# 작성자 : 박성원
# 작성일 2023-06-26

# 문제
# 사용자로부터 파일 이름과 내용을 입력받아 텍스트파일(.txt)을 생성하고
# 입력한 내용을 파일에 저장하는 프로그램을 작성하세요. 
# 그리고, 입력한 파일 이름을 가지고 있는 동물이 파일을 열어 내용을 확인하는 장면을 가정하여 출력하는 프로그램을 작성해보세요.

# 예시 입출력:
# 파일 이름을 입력하세요: catFile.txt
# 파일 내용을 입력하세요: 파일내용입니다
# 파일 생성 및 내용 저장이 완료되었습니다.
# 파일을 열어 내용을 확인하는 동물이 있습니다...
# 고양이가 catFile.txt 파일을 열어 아래 내용을 확인합니다.
# 파일 내용: 파일내용입니다

# 코드요약 :
# 파일 이름과 파일 내용을 입력값으로 받아 text파일을 만듭니다.
# 파일이 생성 된 후 파일 이름과 내용을 출력합니다. 

text_name = input("파일 이름을 입력하세요 :")
text_content = input("파일 내용을 입력하세요 :")

# 파일 생성 및 추가 모드
file_path = f"{text_name}.txt"
with open(file_path, '+a', encoding='utf-8') as file:
    file.write(text_content)
print("파일 생성 및 내용 저장이 완료되었습니다.")
print("파일을 열어 내용을 확인하는동물이 있습니다.")
cat = "고양이"

# 파일 읽기 모드
# content에 file이 닫히더라도 내용을 저장
print(f"{cat}가 {text_name} 파일을 열어 아래내용을 확인합니다.")
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

print(f"파일 내용: {content}")