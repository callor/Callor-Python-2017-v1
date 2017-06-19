import random
import operator

with open('files/numlist.txt','w',encoding='UTF-8') as file :
    for i in range(100):
        num = random.randint(1,10)
        file.write(str(num) + '\n')
    
print('File Write OK!!')

