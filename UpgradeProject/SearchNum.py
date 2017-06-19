'''
랜덤으로 생성된 100개의 숫자중
키 입력한 값과 일치한 숫자 찾기
'''
import random

alist = list()

for i in range(100):
    rnd = random.randint(1,100)
    alist.append(rnd)
    
print(alist)

search = 0
inkey = input('100미만 숫자>>')

for i in alist:
    if i == int(inkey):
        #print(i,'번째에서 찾았습니다')
        break
    
    search += 1
    
if search < 100 :
    print(search,'번째에서 찾음')
else:
    print('찾을 수 없습니다')


    
count = 0
for i in alist:
    if i == int(inkey):
        count += 1
    
if count > 0 :
    print(count,'번 있음')
else:
    print('찾을 수 없습니다')

