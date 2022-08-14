from urllib.request import Request, HTTPCookieProcessor, build_opener

# 쿠키를 담기 위한 준비를 하고, 서버로 요청을 보낸다.
url = 'http://127.0.0.1:8000/cookie/'

cookie_handler = HTTPCookieProcessor()
opener = build_opener(cookie_handler)

req = Request(url)
res = opener.open(req)

print(res.info())
print(res.read().decode('utf-8'))

print("--------")

# 첫 번째 응답에서 받은 쿠키를 헤더에 담아서 요청을 보낸다.
data = "language=python&framework=django"
encData = bytes(data, encoding='utf-8')

req = Request(url, encData)
res = opener.open(req)

print(res.info())
print(res.read().decode('utf-8'))
