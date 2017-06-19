import time
import pickle

# entry 데이터 생성
entry = {}          
entry['title'] = 'Dive into history, 2009 edition'
entry['article_link'] = 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition'
entry['comments_link'] = None
entry['internal_id'] = b'\xDE\xD5\xB4\xF8'
entry['tags'] = ('diveintopython', 'docbook', 'html')
entry['published'] = True

# 현재 시각 객체 생성
entry['published_date'] = time.strptime('Fri Mar 27 22:20:42 2009')    #3
print(entry['published_date'])

# 피클을 이용해서 데이터 저장
with open('entry.pickle', 'wb') as f:    #2
# ...
        pickle.dump(entry, f)            #3
