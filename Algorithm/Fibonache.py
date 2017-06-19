first = 1
second = 2

print(first, second)
for i in range(10):
    nextNum = first + second
    print(nextNum,'-')
    first = second
    second = nextNum
    
    
    
    