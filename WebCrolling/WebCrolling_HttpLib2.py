import httplib2
h = httplib2.Http('.cache')                                                      #1
response, content = h.request('http://www.diveintopython3.net/examples/feed.xml')  #2
print(response.status)                                                           #3
print(content[:52])                                                              #4
print(len(content))
