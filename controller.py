from bs4 import BeautifulSoup
import urllib.request
import http
import os
from pathlib import Path
import time
import random

def stir(url):
    """
    # desktop
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'
    user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux armv7l; rv:17.0) Gecko/20100101 Firefox/17.0'
    user_agent = 'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13) AppleWebKit/603.1.13 (KHTML, like Gecko) Version/10.1 Safari/603.1.13'

    # mobile
    user_agent = 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7'
    """

    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13) AppleWebKit/603.1.13 (KHTML, like Gecko) Version/10.1 Safari/603.1.13'

    req = urllib.request.Request(url, data=None, headers={'User-Agent':user_agent})
    try:
        con = urllib.request.urlopen(req).read()
    except http.client.IncompleteRead as e:
        con = e.partial
    parser = 'html.parser'
    parser = 'html5lib'
    soup = BeautifulSoup(con, parser)
    return soup

def get_soup():
    url = 'http://tv.naver.com/'
    soup = stir(url)
    return soup

if __name__ == '__main__':
    while True:
        soup = get_soup()
        da_boxes = soup.find_all('div', class_='da_box')
        for box in da_boxes:
            try:
                img_url = box.find('img')['src']
                file_name = img_url.split('/')[-1]
                print(file_name)
                file_name = os.path.join('banners/naver_desktop', file_name)
                my_file = Path(file_name)
                if not my_file.is_file():
                    response = urllib.request.urlretrieve(img_url, file_name)
                    print(img_url)
                else:
                    print('File exists')
            except BaseException as e:
                print(e)
        rand_time = random.randint(3600, 10800)
        rand_mins = rand_time / 60
        print('Cool off: %dmin' % rand_mins)
        print('====================')
        time.sleep(rand_time)
