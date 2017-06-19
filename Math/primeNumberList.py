primenumber=[]    # 소수들이 들어갈 빈 리스를 하나 만들고,
for i in range(2, 100):  # 2부터 99까지에서 소수들을 골라낼 거임
    if i==2:  #  만약 2라면 그냥 primenumber에 추가하고
        primenumber.append(i)
    else:
        for j in primenumber:
            if i%j==0:   # primenumber의 요소들로 i 가 나누어 떨어지는지 확인하여
                break   # 나누어 떨어지면 소수가 아니므로 그냥 루프를 빠져 나오고
        if j==primenumber[-1]:   # 끝까지  나누어 떨어지는 놈이 없었는지 확인
            primenumber.append(i)  # 그렇다면 primenumber에 i를 추가한다.
print(primenumber)
