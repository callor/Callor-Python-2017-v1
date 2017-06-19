'''
readlines() 함수는 파일의 모든 라인을 읽어서 각각의 줄을 요소로 갖는 리스트로 리턴한다. 
따라서 예에서 
    lines는 ["1 번째 줄입니다.\n","2 번째 줄입니다.\n",..., "10 번째 줄입니다.\n"]라는 
    리스트가 된다. 
f.readlines()에서 f.readline()과는 달리 s가 하나 더 붙어 있음에 유의하자.
'''
with open('files/text.txt','r',encoding='UTF-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line)
