def g(max):
    count, a, b = 0, 0, 1
    while True:
        if count > max :
            break
        yield a 
        a, b = b, a + b
        count += 1
        
for i in g(100):
    print(i, end= ',')