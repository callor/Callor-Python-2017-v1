'''
임의의 숫자를 생성하여 Dictionary에 저장
'''
import random

numDic= dict()

for i in range(100):
    numRnd = random.randint(1,100)
    numDic[numRnd] = numRnd
        
print(numDic)


'''
임의의 숫자를 생성하여 Dictionary에 저장
중복된 Key가 있으면 합산하여 저장
'''
import random

numDic= dict()

for i in range(100):
    numRnd = random.randint(1,100)
    if numDic.setdefault(numRnd,None) == None :
        numDic[numRnd] = numRnd
    else:
        numDic[numRnd] += numRnd
        
print(numDic)