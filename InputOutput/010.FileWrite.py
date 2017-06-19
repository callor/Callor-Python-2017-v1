'''
파일을 쓰기용으로 열거나
새 파일을 만들어 내용을 써 넣는다
한글 인코딩 문제가 발생하므로 encoding='UTF-8'을 반드시 넣자
'''
with open("files/text.txt", 'w',encoding='UTF-8') as f:
    for i in range(1, 11):
        data = "%d번째 줄입니다.\n" % i
        f.write(data)

print('OK')