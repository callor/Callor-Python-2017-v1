def is_prime(x):             # x를 입력값으로 갖는 is_prime 함수 생성
    if x < 2:                # x가 2보다 작은 경우 False를 반환
        return False         
#     elif x == 2:             # x가 2인 경우에는 True를 반환
    if x == 2:             # x가 2인 경우에는 True를 반환
        return True          
    else:                   
        for i in range(2,x): # 2부터 x까지 범위를 반복 연산
            if x % i == 0:   # x를 i로 나누어 나머지가 0이되는 경우 소수가 아님
                return False # False를 반환

    return True

def is_primeEach(x):
    ret_result = True
    if x < 2 : 
        ret_result = False

    # x가 이일때는 포함이 안되므로 x가 2일때는 통과^^
    for i in range(2,x):        # 2부터 x까지 범위를 반복 연산
        if x % i == 0:          # x를 i로 나누어 나머지가 0이되는 경우 소수가 아님
            ret_result = False  #break # return False # False를 반환
            break

    return ret_result

for i in range(1000):    
    # x=input("Enter Number : ") # 인자 x의 값을 사용자로부터 입력
            
    # print(str(is_prime(int(x))))    # is_prime을 호출하고 결과값을 출력
    print(i,is_primeEach(int(i)))    # is_prime을 호출하고 결과값을 출력
    