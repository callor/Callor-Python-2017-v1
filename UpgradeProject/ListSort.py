import random
def makeRandoms(size, limit):
    result = []
    for i in range(size):
            result.append(random.randrange(0,limit))
 
    return result
 
random.seed(1)
result = makeRandoms(20,100)
print(result)

result.sort()
print(result)

'''
역순정렬
'''
result.sort(reverse=True)
print(result)

'''
외부 함수인 sorted함수 사용하기
'''

other = sorted(result)
print(other)

'''
외부함수인 sorted함수를 사용하여 내림차순으로 정렬하기이다.
'''
other = sorted(result,reverse=True)
print(other)

'''
키를 만들어 사용하는 사용자 정의 정렬
    2자리 숫자를 가진 리스트에서 십의자리와는 무관하게 
    일의자리의 크기를 기준으로 정렬을 한다.
'''
def lastDigit(n):
    return n%10
 
other = sorted(result, reverse=True, key = lastDigit)
print(other)


'''
같은 방법을 이용하여 1의 자리와 10의자리의 합으로 정렬을 하였다.
'''
def digitSum(n):
    return n/10 + n %10
 
other = sorted(result,reverse=True,key=digitSum)
print(other)
