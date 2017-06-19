'''
파일을 읽어서 빈도수를 구하시오
'''
numList = list()
numDic = {}
with open('files/numlist.txt','r',encoding='UTF-8') as file:
    file.seek(0)
    line = True
    while line :
        line = file.readline()
        if line:
            # print(line)
            numList.append(int(line))
#             print(numDic[int(line)])
            if int(line) in numDic:
                numDic[int(line)] += 1 # numDic[int(line)]
            else:
                numDic[int(line)] = 1
        else:
            break 
sorted_x = sorted(numDic.items(), key=operator.itemgetter(0))
print(sorted_x)