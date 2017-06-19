# with open('files/grade.txt','w',encoding='UTF-8') as f:
#     while True:
#         keyin = input('이름,점수1,점수2,점수3')
#         if keyin == '--END' :
#             break
#         
#         alist = keyin.split(',')
#         f.write(alist[0] + '~' + alist[1] + '~' + alist[2] + '~' + alist[3]  +'\n' )
#     
# print('완료!!')

with open('files/gradeTot.txt','w',encoding='UTF-8') as f1:
    with open('files/grade.txt','r',encoding='UTF-8') as f2:
        f2.seek(0)
        while True:
            readStr  = f2.readline()
            if readStr :
                alist = readStr.split('~')
                sum = int(alist[1])
                sum += int(alist[2])
                sum += int(alist[3])
                
                avg = int(sum / 3)
                wStr = readStr.replace('\n','')   \
                        +'~' + str(sum) + '~' + str(avg) + '\n'
                
                print(wStr)
                f1.write(wStr)
                
            else:
                break
    
print("계산완료")
    
    
gradeList = list()
with open('files/gradeTot.txt','r',encoding='UTF-8') as f:
    f.seek(0)
    while True:
        readStr = f.readline()
        if readStr :
            alist = readStr.replace('\n','').split('~')
            gradeList.append(alist)
        else:
            break
        
for i in range(len(gradeList)):
    for j in range(len(gradeList)):
        if int(gradeList[i][4]) > int(gradeList[j][4]) :
            gradeList[i], gradeList[j] = gradeList[j], gradeList[i]

for i in range(len(gradeList)):
    gradeList[i].append(i+1)
                
print(gradeList)

        
        
        
    
    
    