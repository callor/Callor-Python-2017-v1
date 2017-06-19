import requests
r = requests.get("http://www.naver.com")

print(r.status_code)
print(r.headers)
print(r.content)