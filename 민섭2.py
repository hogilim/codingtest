word = input("단어를 입력하세요 : ")
print(word[0: word.index("o")])

word = input("단어를 입력하세요 : ")
for i in word:
    if i == "o":
        break
    print(i, end="")  # 문자 출력후 끝에 자동삽입되는 엔터 삭제

word = input("단어를 입력하세요 : ")
for i in range(len(word)):
    if word[i] == "o":
        print(word[0:i])