import random

#stlist =['대한민국','Korea',"English"]
#print(stlist.index('대한민국'))

alist =list()
for i in range(100):
    rnd = random.randint(1,100)
    alist.append(rnd)
    
print(alist)
    
inInt = input('100이하 숫자입력>>')
index = 0
for val in alist:
    if  int(inInt) == int(val):
        print(index,'위치에서 발견됨')
        break
    
    index += 1
if index >= 100:
    print('찾을 수 없습니다')
    
