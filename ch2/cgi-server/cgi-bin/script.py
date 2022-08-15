import cgi

form = cgi.FieldStorage()  # FieldStorage 클래스의 인스턴스를 생성해야 한다.
name = form.getvalue('name')  # 그리고 그 인스턴스의 getvalue() 메서드를 호출해야 한다.
email = form.getvalue('email')
url = form.getvalue('url')

print('Content-Type: text/plain')
print()

print('Welcome... CGI Scripts')
print('name is', name)
print('email is', email)
print('url is', url)