def pytha():
    for a in range(2,1000):
        for b in range(2,1000):
            for c in range(2,1000):
                
                if a+b+c == 1000:
                    print(a,b,c)
                    if  a*a + b*b == c*c :
                        return a*b*c
                    
print(pytha())    