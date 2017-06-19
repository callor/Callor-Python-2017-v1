listA = [1,2,3,3,4,5,6,7]
listB = [1,9]

'''
listB의 요소가 listA에 모두 포함되어 있는가?
'''
def inAllList(listA,listB):
    retVal = True
    for i in listB:
        if i not in listA :
            retVal = False
    return retVal

'''
listB의 요소가 listA에 한개이상 포함되어 있는가?
'''
def inFirstList(listA,listB):
    retVal = True
    for i in listB:
        if i not in listA :
            retVal = False
    return retVal

print('모두포함?',inAllList(listA, listB))
print('한개이상 포함?',inFirstList(listA, listB))


print('한개이상포함 any?',any(x for x in listB if x in listA))
print('한개이상포함 any?',any(x in listA for x in listB))

print('모두 포함 all?',all(x in listA for x in listB))

print('모두포함 all-결과 오류',all(x for x in listB if x in listA))

print([x for x in listB if x in listA])



# print(all([x for x in lista2 if x in lista1]))
# print(x for x in lista1)
# print(all([x for x in lista1 if type(x) == str]))
# print([x for x in lista2 if x in lista1])
# print([type(x) is str for x in lista2])

# print(all(x in lista1 for x in lista2))