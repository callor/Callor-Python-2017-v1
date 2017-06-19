def multiple():
    
    mylist = list()
    for i in range(1000):
        if i % 3 == 0 or i % 7 == 0 :
            mylist.append(i)
    
    sum = 0 
    for s in mylist:
        sum += s
        
    print(mylist)
    print('합계=',sum)
    
def multipleUp():
    
    mylist = list()
    for i in range(1000):
        if i % 3 == 0 or i % 7 == 0 :
            mylist.append(i)
    
    mySum = sum(mylist,0) # 파이썬 합계구하기 함수 
         
    print(mylist)
    print('합계=',mySum)
multipleUp()