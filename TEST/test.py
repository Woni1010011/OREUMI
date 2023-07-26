# 끝말잇기

word = input("'마'로 시작하는 단어를 입력하세요 : ")
def start (word) :
    while True :
        temp = word
        if temp[len(temp)-1] == word[0] :
            word = input(f"'{temp[len(temp)-1]}'를 이을 단어를 입력하세요 : ")
        else :
            print('단어가 올바르지 않습니다.')
            break


start(word)


