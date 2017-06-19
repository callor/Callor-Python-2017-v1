'''
f.read()는 파일의 내용 전체를 문자열로 리턴한다. 
따라서 코드의 data는 파일의 전체 내용이다.
한글 인코딩 문제가 발생하므로 encoding='UTF-8'을 반드시 넣자
'''
with open("files/text.txt", 'r',encoding='UTF-8') as f:
    data = f.read()
    print(data)