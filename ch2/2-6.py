import urllib.request

url = 'http://www.example.com'
proxyServer = 'http://www.proxy.com:3128/'

# 프록시 서버를 통해 웹 서버로 요청을 보냄
proxy_handler = urllib.request.ProxyHandler({'http': proxyServer})

# 프록시 서버 설정을 무시하고 웹 서버로 요청을 보낸다.
proxy_handler = urllib.request.ProxyHandler({})

proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')

opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)

urllib.request.install_opener(opener)

f = urllib.request.urlopen(url)

print("geturl():", f.geturl())
print(f.read().decode('utf-8'))

