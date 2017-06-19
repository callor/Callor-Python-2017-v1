'''
리스트의 요소가 모두 포함되어 있는가 검사
'''
import random


numList = list()
for i in range(100):
    numRnd = random.randint(1,10)
    numList.append(numRnd)
    

num1 = [1,2,3]

retVal = True
for i in num1:
    if i not in numList:
        retVal = False

if retVal :
    print('있음')
else:
    print('없음')
print(numList)