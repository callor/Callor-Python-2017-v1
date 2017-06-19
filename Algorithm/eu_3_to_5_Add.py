"""
1000 이하의 값중에서 3의 배수 또는, 5의 배수
"""
sum = 0 # 전체 합이 담길 변수

for i in range(1000):
    if ( i % 3 == 0) or ( i % 5 == 0):
        sum += i # sum = sum + i
        
print('합계:', sum)

