"""
with를 사용하면 순환문(loop)가 끝난 후 
    파일 핸들(fh)를 반납하므로
자동으로 파일을 닫는 것과 같다.

"""
with open('files/text.txt','w') as f: # fh = open('text01.txt')
    keyIn = input('입력>')
    if keyIn == '-END':
        break
    
    f.write(keyIn + '\n')
    
