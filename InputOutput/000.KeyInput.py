count = 0
sum = 0
while True:
    count += 1      # count++ 처럼 사용할 수 없다.
    """
    input 함수를 만나면 프로그램은 broking 상태가 된다.
    """
    keyinput = input(str(count) + '번째 입력 > ') # 키보드로 부터 값을 입력받는 대기 상태


    if int(keyinput) == -1:
        break
    sum += int(keyinput)

print('결과',sum)
    
    
    