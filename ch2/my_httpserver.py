from http.server import HTTPServer, BaseHTTPRequestHandler


class MyHandler(BaseHTTPRequestHandler):
    """웹 클라이언트로부터 요청을 받고 'Hello World'라는 문장을 되돌려 주는 웹 서버"""
    def do_GET(self):
        self.send_response_only(200, 'OK')
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hello World')


if __name__ == '__main__':
    server = HTTPServer(('', 8888), MyHandler)  # HTTPServer 객체 생성(인자: 서버의 IP, PORT, 핸들러 클래스)
    print('Started WebServer on port 8888...')
    print('Press ^C to quit WebServer.')
    server.serve_forever()


