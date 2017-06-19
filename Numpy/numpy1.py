import numpy as np

a = np.array([1, 2, 3])
b = np.array([3, 4, 5])

print ("a: ", a)
print ("b: ", b)

print ("1차원 합집합: ", np.union1d(a, b))
print ("1차원 교집합: ", np.intersect1d(a, b))
print ("1차원 차집합: ", np.setdiff1d(a, b))
print ("1차원 대칭차집합(합집합 - 교집합): ", np.setxor1d(a, b))

print ("난수 발생(1 개): ", np.random.random(1))
print ("난수 발생(3 개): ", np.random.random(3))

print ("평균: 0 / 표준편자: 1 / 갯수: 1")
print ("난수 발생(1 개): ", np.random.normal(0, 1, 1))

print ("평균: 1 / 표준편자: 1 / 갯수: 3")
print ("난수 발생(3 개): ", np.random.normal(1, 1, 3)) 



# 출처: http://expert0226.tistory.com/357 [여름나라겨울이야기]