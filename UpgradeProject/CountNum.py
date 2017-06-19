import random

alist = list()
clist = list()
for i in range(100):
    alist.append(random.randint(1,10))
    
print(alist)


'''
 10개의 리스트를 만들고 0으로 초기화
'''
clist = [0]*11

'''
alist 요소값을 index로 하여 count 계산
'''
for i in alist:
    #print(i)
    clist[i] += 1
    
index = 0
for item in clist:
    print(index,'>>',item)
    index += 1

for i in range(len(clist)):
    print(i,'**',clist[i])
   
for index,value in enumerate(clist):
    print(index,'=', value)
    
print(' '.join(clist))   
print(clist)