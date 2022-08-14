import os.path
from http.client import HTTPConnection
from urllib.parse import urljoin, urlunparse
from urllib.request import urlretrieve
from html.parser import HTMLParser


class ImageParser(HTMLParser):
    """img 태그를 파서하는 듯?"""
    def handle_starttag(self, tag: str, attrs):
        if tag != 'img':
            return
        if not hasattr(self, 'result'):
            self.result = []
        for name, value in attrs:
            if name == 'src':
                self.result.append(value)


def download_image(url, data):
    """HTML 문장이 주어지면 ImageParser 클래스를 이용해서 이미지를 찾고, 그 이미지들을 DOWNLOAD 디렉토리에 다운로드한다."""

    if not os.path.exists('DOWNLOAD'):
        os.makedirs('DOWNLOAD')

    parser = ImageParser()
    parser.feed(data)  #parser.result에 결과 넣어줌
    dataSet = set(x for x in parser.result)

    for x in sorted(dataSet):
        imageUrl = urljoin(url, x)  # url과 타깃 파일명 지정함.
        basename = os.path.basename(imageUrl)
        targetFile = os.path.join('DOWNLOAD', basename)

        print('Downloading...', imageUrl)
        urlretrieve(imageUrl, targetFile)  # image 다운로드 함수.


def main():
    host = 'www.google.co.kr'

    conn = HTTPConnection(host)
    conn.request('GET', '')
    resp = conn.getresponse()

    charset = resp.msg.get_param('charset')
    data = resp.read().decode(charset)
    conn.close()

    print("\n>>>>> Download Images from", host)
    url = urlunparse(('http', host, '', '', '', ''))
    download_image(url, data)


if __name__ == '__main__':
    main()

