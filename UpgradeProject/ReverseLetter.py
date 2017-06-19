
"""
문자열 뒤집기 예제
"""   
alist = list('korea')
for i in range(len(alist)):
    print(alist[(-1)-i])   
    
    
"""
키보드로 입력받은 문자열 뒤집기
"""

def ReverseLetter(text): 
    letters = list(text)        # text를 리스트로 변환
    reversed_letters = ''       # 변환된 문자열을 저장할 reversed_letters 생성 및 초기화
    x = int(len(text)) - 1      # 변수 x에 text의 문자길이-1을 할당
    while x > -1:               # x가 -1보다 클때까지 반복
        reversed_letters += letters[x]  # reversed_letters에 마지막 문자부터 순서대로 추가
        x -= 1                          # x값을 -1씩 감소
    else:
        return reversed_letters         # 반복문 종료 후 reversed_letters 반환
 
def ReverseLetterEach(text): 
    letters = list(text)
    reversed_letters = ''
    letterLen = int(len(text))
    for i in range(letterLen):
        print(i)
        reversed_letters += letters[(i+1)*(-1)]
                                  
    else:
        pass
    return reversed_letters


def reversUp(inpStr):
    listStr = list(inpStr)
    
    reversStr = ''
    intLen = len(listStr) # list의 개수를 
    
    #for x in range(intLen):
    for x in listStr:
        # print(x)
        intLen -= 1
        reversStr += listStr[intLen]
    
        # reversStr += x
    return reversStr

def reversPy(inpStr):
    letter = list(inpStr)
    print(letter) ## debuf
    letter.reverse()

    reversStr = ''
    for s in letter:
         reversStr += s
    return letter, reversStr

text=input("Enter text : ") # text의 값을 사용자로부터 입력
          
print(reversPy(text))             # reverse를 호출하고 결과값을 출력