numlist = list()
with open('files/numlist.txt','r',encoding='UTF-8') as f :
    f.seek(0)
    while True:
        line = f.readline()
        if line:
            numlist.append(int(line))
        else:
            break
print(numlist)

sum = 0
mul = 1 
for i in numlist:
    sum += i
    mul *= i
    
print('합:',sum,'곱:',mul)