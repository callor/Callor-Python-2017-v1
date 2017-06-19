'''
키보드에서 입력받아 파일에 저장하기

'''
with open('files/text.txt','w',encoding='UTF-8') as f:# 쓰기용
    while True :
        keyin = input('입력> ')
        if keyin == '-END':
            break 
         
        f.write(keyin + '\n')
     
    # break 후에 실행될 위치 
print('파일 입력을 마칩니다')



