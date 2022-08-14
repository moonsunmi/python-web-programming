import requests
from bs4 import BeautifulSoup


def parse_image(data):
    soup = BeautifulSoup(data, 'html.parser')
    img_tag_list = soup.find_all('img')
    data_set = set(x.attrs['src'] for x in img_tag_list)
    return sorted(data_set)


def main():
    url = 'http://www.google.co.kr'

    res = requests.get(url)
    charset = res.encoding
    data = res.content.decode(charset)

    data_set = parse_image(data)
    print('\n>>>>>>> Fetch Images from', url)
    print('\n'.join(data_set))


if __name__ == '__main__':
    main()


