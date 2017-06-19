from pandas import Series

#Series는 일련의 객체를 담을 수 있는 1차원 배열과 같은 자료구조로 색인을 갖는다.
obj = Series([3, 7, -5, 4]) 
print(obj)

print()
obj2 = Series([3, 7, -5, 4], index=['a', 'b', 'c', 'd'])  #색인을 지정
print(obj2)

print("\n배열 값 얻기")
print(obj2.values) 
print("\n배열 인덱스 얻기")
print(obj2.index)  

print()
#파이썬 dict type의 자료로 Series 객체를 생성
names = {'mouse':12000, 'keyboard':25000, 'mornitor':'450000'} 
print(names)

obj3 = Series(names)
print(obj3)

print()
obj3.index = ['키보드', '모니터', '마우스']   #Series의 색인은 대입을 통해 변경이 가능
print(obj3)


# 출처: http://bisn.tistory.com/12 [Bisn]