"""
입력받은 숫자의 모든 자릿수를 덧셈
"""
def digit_sum(strNum):             # n을 입력으로 갖는 digit_sum 함수 생성
    if int(strNum) > 0:                  # n이 양의 수일 경우
        y = list(strNum)            # 텍스트형인 m을 리스트형으로 변환
        total = 0              # 합계를 구할 total을 0으로 초기화
        for x in y:            # 리스트 y의 처음부터 끝까지 반복
            total += int(x)    # 리스트 y의 각 단위값인 x를 total에 합산
        return total
    else:
        return False


"""
입력받은 숫자를 4개씩 끊어 덧셈 후 최대값 구하기
input : 9399394939439
sum1    9399
sum2     3993
sum3      9939
"""
def digit4_Sum_Max(strNum):
    if int(strNum) < 1 : return
    listNum = list(strNum)
    
    max = 0
    for i in range(len(strNum)):
        tmpSum = 0
        for x in listNum[i:i+4]:
            
            tmpSum += int(x)
            if tmpSum > max : max = tmpSum
        
        if len(listNum[i:i+4]) == 4 : 
            print(listNum[i:i+4],tmpSum)    
    return max
inputNum =input("Enter Number : ") # 인자 n의 값을 사용자로부터 입력

# print( digit_sum(inputNum))        # digit_sum을 호출하고 결과값을 출력
print( digit4_Sum_Max(inputNum))        # digit_sum을 호출하고 결과값을 출력