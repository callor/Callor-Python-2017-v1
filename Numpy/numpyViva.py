import numpy as np
a = [1, 2, 3]

# TypeError: 
# can only concatenate list (not "int") to list
# b = 2 * a + 1
# print b

c = np.array([1, 2, 3])
# 어메 Numpy 좋은 거 보소 1
# Numpy 배열 각 요소에 수학 연산을... 오~올
d = 2 * c + 1
print ("d: ", d)

# 어메 Numpy 좋은 거 보소 2
# Python 배열(리스트)를 Numpy 배열로...
e = np.array(a)
f = 2 * e + 1
print ("f: ", f) 



# 출처: http://expert0226.tistory.com/357 [여름나라겨울이야기]