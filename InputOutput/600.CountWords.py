'''
파일을 읽어 단어로 구분하여 출력
'''
with open('files/dict.txt','r', encoding = 'UTF-8') as fh:
    readVal = fh.read()
    words = readVal.split()
    print(words)
    print('단어개수', len(words))
    
    
'''
리스트에 담긴 단어중 가장 긴 단어를 찾아 출력
'''
maxlen = 0 
maxword = ''
for w in words:
    if len(w) > maxlen:
        maxlen = len(w)
        maxword = w
        
print('가장 긴 단어:',maxword,'알파벳수:',maxlen)
wordList = list(maxword)
print(wordList)
wordList.sort(key=None, reverse=True)
print(wordList)