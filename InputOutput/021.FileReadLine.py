'''
Text File을 라인단위(\n)로 읽어 오기
한글 인코딩 문제가 발생하므로 encoding='UTF-8'을 반드시 넣자
'''
with open('files/text.txt','r',encoding='UTF-8') as fileHandle :
    fileHandle.seek(0) # 읽기 point를 파일의 처음으로 설정
    while True:
        line = fileHandle.readline()
        if line : # 읽은 라인이 있으면  True, 없으면 false 
            print(line)
        else : # 더이상 읽을 라인이 없으면 끝
            break 
