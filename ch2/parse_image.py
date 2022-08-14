from urllib.request import urlopen
from html.parser import HTMLParser

class ImageParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'img':
            return
        if not hasattr(self, 'result'):
            self.result = []
        for name, value in attrs:
            if name == 'src':
                self.result.append(value)


def parse_image(data):
    parser = ImageParser()
    parser.feed(data)  # HTML 문장을 feed() 함수에 주면 파싱하여 parser.result 리스트에 추가해줌.
    data_set = set(x for x in parser.result)  # 파싱 결과를 중복 없이 받는다.
    return sorted(data_set)  # 책에서는 main에서 data_set을 sort해 주는데, 여기에서 해 주는 것도 괜찮을 거 같아서 바꿈.


def main():
    url = "http://www.google.co.kr"

    with urlopen(url) as f:
        # 사이트에서 가져오는 데이터는 인코딩된 상태이므로, 인코딩 방식을 알아내어 그 방식으로 인코딩해 줍니다.
        charset = f.info().get_param('charset')
        data = f.read().decode(charset)

    data_set = parse_image(data)
    print('\n>>>>>>> Fetch Images from', url)
    print('\n'.join(data_set))


if __name__ == '__main__':
    main()