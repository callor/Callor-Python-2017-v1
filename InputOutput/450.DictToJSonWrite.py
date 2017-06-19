import json

basic_entry = {}                                           #1
basic_entry['id'] = 256
basic_entry['title'] = 'Dive into history, 2009 edition'
basic_entry['tags'] = ('diveintopython', 'docbook', 'html')
basic_entry['published'] = True
basic_entry['comments_link'] = None

print(type(basic_entry))

"""
dict 구조의 데이터를 json으로 저장
"""
with open('basic.json', mode='w', encoding='utf-8') as f:  #2
    json.dump(basic_entry, f)     
    
with open('basic-pretty.json', mode='w', encoding='utf-8') as f:
    json.dump(basic_entry, f, indent=2)     