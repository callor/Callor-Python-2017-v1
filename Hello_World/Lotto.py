import random # 모듈을 연결, 추가 하는 키워드

# 함수 생성 키워드
def ran_set(num):
    count = 0
    print('=' * 50)
    print('로또번호 추출')
    print('=' * 50)
    for i in range(num): # 반복구문, 순환문
        
        result = set() # 비어있는 집합 자료형 생성, list 중의 하나

        while len(result) < 6 : # for( ;; )
            rnd = random.randrange(1,50) # 1부터 50까지 숫자를 랜덤으로 추출
            result.add(rnd)

        res = list(result) # 정렬이 가능한 list로 생성
        res.sort()
        count = count + 1 
        print(count,'번째:',res)
    print('-'*50)

ran_set(10) # ran_set을 호출하면서 10을 매개변수로 전달하는 것        