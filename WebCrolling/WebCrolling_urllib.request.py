import pickle
import urllib.request
temp = urllib.request.urlopen("http://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001").read()
print(temp)

"""
pickle을 사용해서 파일을 저장하려면 반드시 wb로 open 해야 한다
"""
f = open('news.txt', 'wb')
pickle.dump(temp,f)
f.close()

