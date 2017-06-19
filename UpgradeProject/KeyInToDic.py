'''
문자,숫자 형식으로 입력받아 딕셔너리에 저장
이미 입력된 문자(key)이면 안내 메시지 보이고 다시 입력
'''
grade = dict()
while True:
    keyin = input('입력>>')
    if keyin == '--END' :
        break
    
    alist = keyin.split(',')
    if grade.setdefault(alist[0],None) != None :
        print('이미 입력된 Key 입니다')
    else:
        grade[alist[0]] = alist[1] # 그대로 저장
        grade[alist[0]] = int(alist[1]) # 정수형으로 바꾸어서 저장
    
print(grade)
print('개수',len(grade))
print('합계',sum(grade.values()))
    