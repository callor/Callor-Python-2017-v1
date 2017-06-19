'''
텍스트 파일 복사
   text.txt 파일을 text2.txt 파일로 복사한다.
'''
with open('text2.txt','w',encoding='UTF-8') as target :
    with open('text.txt','r',encoding='UTF-8') as source:
        target.write(source.read())
        
    target.close()
    
print('파일 복사를 완료했습니다')
