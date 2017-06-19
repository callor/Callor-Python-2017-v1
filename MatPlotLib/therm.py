# %matplotlib inline
from matplotlib.pyplot import rc, plot, show, imshow, title, xlabel, ylabel, legend

# 이걸해야 그래프에 한글이 잘나온다.
rc('font',family='D2Coding')


# 책에는 뉴욕의 평균온도가 예제로 나온다. 나는 서울로 해보았다.
#
# 소스 : https://data.kma.go.kr/stcs/grnd/grndTaList.do?pgmNo=70
# 자료구분-일, 지점-서울, 기간은 적당히주고 CSV를 다운로드 했다.
#
# CSV에는 날짜,지점,평균기온(℃),최저기온(℃),최고기온(℃) 가 들어있다.
# 다음 명령으로 매년 7월1일의 최고 기온만 뽑았다.
#
# grep "20../07/01" ta_20160702203925.csv | awk -F','  '{print $5}'

temp = [31, 29.6, 27.9, 27.8, 26.7, 26.5, 24.7, 23.2, 29.3, 27.4, 30.7, 28.6, 25.4, 31.3, 31.2, 27.9, 26.6]
years = range(2000, 2017)
plot(years, temp)

# 이번에는 그래프여러개 + legend 표시

temp_top = [31, 29.6, 27.9, 27.8, 26.7, 26.5, 24.7, 23.2, 29.3, 27.4, 30.7, 28.6, 25.4, 31.3, 31.2, 27.9, 26.6]
temp_bot = [19.9, 21.4, 22.9, 20.2, 22, 21.6, 21.1, 19, 20.2, 20.7, 21.9, 22.2, 19.2, 23.9, 21.1, 21, 22]
temp_mean = [25.6, 25.1, 25, 23, 24, 23.8, 22.6, 19.8, 24.8, 23.5, 26.1, 25.1, 21.6, 27.1, 26, 23.7, 24]

years = range(2000, 2017)

plot(years, temp_top, years, temp_bot, years, temp_mean, marker='o')

title('서울의 기온 변화')
xlabel('연도')
ylabel('기온')
legend(['최고', '최저', '평균'])

show()