'''
키보드에서 입력받아
기존파일에 추가하기
'''
with open('files/text.txt' , 'a',encoding='UTF-8') as f: # 기존파일에 추가하겠다
    while True:
        keyIn = input('입력>')
        if keyIn == '-END':
            break
        
        f.write(keyIn + '\n')
   

print('파일 입력을 마칩니다')