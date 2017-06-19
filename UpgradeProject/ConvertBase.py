"""
진법변환
BaseConvert(정수, 진법수)
  단, 16진수 A-F 까지는 10진수로 표현하고 있음
"""
def baseCon(num):
    
    base = list()
    while True:
        if num < 2:
            base.append(num)
            break
        base.append(num%2)
        num = int(num / 2)

    j = 0
    retStr = ''
    for i in base:
        j -= 1
        # print(base[j],end=',')
        retStr += str(base[j])
        
    retStr = ''
    for i in range(len(base)):
        # print(base[(-1)-i],end='')
        retStr += str(base[(-1)-i])
        
    return retStr
    

num = input('숫자입력')
print(baseCon(int(num)))
    

def BaseConvert(dec,base):
    
    baseCon = list()
    while True :
        baseCon.append(dec % base)
        dec = int(dec / base)
        if dec < base :
            baseCon.append(dec)
            break
    
    baseResult = list()
    baseLen = len(baseCon)
    for i in range(baseLen) :    
        # baseCon.reverse()  
        print((-1)-i)   
        baseResult.append(baseCon[(-1) - i])
        
    return  baseResult 

def BaseConvertUp(dec,base):
    
    baseCon = list()
    while True :
        baseCon.append(dec % base)
        dec = int(dec / base)
        if dec < base :
            baseCon.append(dec)
            break
       
    baseCon.reverse()     
        
    return  baseCon 


def BaseConvert2Up(dec,base):
    
    baseCon = list()
    while True :
        baseCon.append(dec % base)
        dec = dec // base
        if dec < base :
            baseCon.append(dec)
            break
       
    baseCon.reverse()     
        
    return  baseCon 



def BaseConvertPy(num):
    
    num = 12345
    # 10진수 -> 2진수 변환 : 0b11000000111001
    print(bin(num))
 
    # 10진수 -> 8진수 변환 : 030071
    print(oct(num))

    # 10진수 -> 16진수 변환 : 0x3039 
    print(hex(num))

    # 2진수 -> 10진수 변환 : 12345
    print(int(bin(num),2))
    
    # 16진수 -> 10진수 변환 : 12345    
    print(int(hex(num),16))
    

    
print(BaseConvert(255,2))
BaseConvertUp(255,2)
        