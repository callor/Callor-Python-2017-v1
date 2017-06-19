endDic ={'aa':1}
print(endDic)
print(endDic.keys())

a = { 'a': [1,2,3]}
print(a['a'][0]) # a key Value의 0번째 리스트

'''
키보드로 부터 영단어,의미 형식의 문자열을 입력받아
    딕셔너리에 저장 한 후
    --END 문자열을 만나면 입력을 종료한 후 파일에 저장
'''
engDic = dict()
while True:
    inkey = input('영단어,의미>>')
    if inkey == '--END' :
        break
    
    alist = inkey.split(',')
    engDic[alist[0]] = alist[1]
    
with open('files/dict.txt','w',encoding='UTF-8') as file:
    for d in engDic.keys():
        s = d+'~'+engDic[d]
        file.write(s + '\n')
        print(s)
    
# with open('files/dict.txt','w',encoding='UTF-8') as f :
    