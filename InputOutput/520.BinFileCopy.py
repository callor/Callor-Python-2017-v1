'''
바이너리 파일을 열때는 옵션에 반드시 b를 포함해야 한다
   2 진 파일 예제
   2017.jpg 파일을 201701.jpg 파일로 복사한다.
'''
with open('201701.jpg','wb') as target :
    with open('2017.jpg','rb') as source:
        target.write(source.read())
        
    target.close()
    
print('파일 복사를 완료했습니다')
