'''
파이썬 별그리기
'''
def printStar(number):
    for y in range(1,number+1):
        printStr = ''
        for x in range(y):
            printStr += '* '
            #print("*", end=" ")
        print(y, printStr)


def printRevesStar(number):
    for y in range(number, 1, -1):
        for star in range(1, y):
            print("*", end=" ")
        print("")

def printStarList(num):
#     num = 5
    listStar = []
    for y in range(1,num+1):
        pStar = []
        for x in range(1,y+1):
            pStar.append('*')
            
        listStar.append(pStar)
    
    for y in range(len(listStar)):
        for x in range(len(listStar[y])) :
            
            print(listStar[y][x], end=' ')
        
        print('')

def printSpaceStar(number):
    
    for y in range(number):
        print('  ' * y,'* ' * (number-y))


# printRevesStar(10)
# printSpaceStar(10)

printStar(5)

'''
A 문자열을 10개 출력
결과 : AAAAAAAAAA
'''
print( 'A' * 10 ) # A 문자열을 10개 출력

