'''
기존 파일에 추가하기
'''
with open('files/text.txt' , 'a',encoding='UTF-8') as f:# 기존파일에 추가하겠다
    for i in range(1, 11):
        data = "%d번째 줄입니다.\n" % i
        f.write(data)
    f.close()
print('파일 입력을 마칩니다')