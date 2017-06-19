primenumber=[2]
for i in range(3, 100000):
    j=0
    index=i
    while primenumber[j]<=index:
        if i%primenumber[j]==0:
            break
        else:
            index=int(i/primenumber[j])+1
        if primenumber[j]>=index or primenumber[j+1]>index:
            primenumber.append(i)
            break
        else:
            j+=1
 
print(primenumber)


