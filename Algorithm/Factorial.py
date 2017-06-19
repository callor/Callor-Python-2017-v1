def factorial(x):              # x를 입력값으로 갖는 factorial 함수 생성
    if x >= 1:                 # x가 1이상일 경우에 명령을 실행 
        total = x              # 결과값 total에 초기값 x 할당
        y = x - 1              # 순차적으로 감소하는 값인 y에는 x-1 할당
        for i in range(x-1):   # 0부터 x-1의 횟수만큼 반복 
            total = total * y  # total값과 y를 곱하여 total에 할당
            y -= 1             # y의 값을 감소
        return total           # 연산이 끝난 결과값 total을 반납
    else:
        return x
 

"""
재귀 호출을 이용한 팩토리얼 계산
""" 
def factorialEach(x):
    if x <= 1:
        return 1
    return x*factorialEach(x-1)
    

x=input("Enter Number : ") # 인자 x의 값을 사용자로부터 입력
print(factorialEach(int(x)))        # factorial을 호출하고 결과값을 출력

