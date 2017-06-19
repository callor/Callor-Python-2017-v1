"""
키보드로 입력받은 문자열에서 Consonant(자음)만 걸러내기
모음: Vowel
"""
def Consonant(text):           
    letters = list(text)        # 문자열 text를 list로 변환
    reversed_letters = ''       # 변환된 문자열을 저장할 reversed_letters(str 변수) 생성 및 초기화
    for x in range(len(text)):  # 문자열 text의 길이 만큼 for 반복문 실행
        if letters[x] not in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
            reversed_letters += letters[x] # 모음이 아닐 경우에 reversed_letters에 할당
 
    return reversed_letters     # 반복문 종료 후 reversed_letters를 반환
    
    
def ConsonantEach(text):
    letters = list(text)
    Consonant_letter = ''
    for x in letters:
        # print(x)
        if x not in list('aeiouAEIOU'):
            Consonant_letter += x
            
    return Consonant_letter

text=input("Enter text : ") # text의 값을 사용자로부터 입력
print('Result:' , ConsonantEach(text))          # anti_vowel을 호출하고 결과값을 출력
