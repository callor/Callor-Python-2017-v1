#import urllib.request
from urllib.request import urlopen # urllib.request 모듈안에 urlopen 함수가 들어 있다. ^^
#from bs4 import BSoup # BeautifulSoup
import bs4
# import BeautifulSoup # module not found
url="http://movie.naver.com/movie/sdb/rank/rmovie.nhn"
# soup = BeautifulSoup( urllib.request.urlopen(url).read())
#soup = bs4.BeautifulSoup(urllib.request.urlopen(url).read())
soup = bs4.BeautifulSoup(urlopen(url).read())
pkg_list=soup.findAll('div', 'tit3')

count = 1
for i in pkg_list:
    title = i.findAll('a')
    print( count, '위: ', str(title)[str(title).find('title="')+7:str(title).find('">')])
    count=count+1



