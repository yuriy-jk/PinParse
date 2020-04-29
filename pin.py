import os
from selenium import webdriver
import time
import re
import urllib.request

chromedriver = '/Users/yuriykhen/chromedriver'
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("--start-maximized")
options.add_argument('--window-size=7000,1080')
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)


def get_html(url):
    driver.get(url)
    #c = driver.get_window_size()
    #height = driver.execute_script("return document.body.scrollHeight")
    SCROLL_PAUSE_TIME = 2
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    #height1 = driver.execute_script("return document.body.scrollHeight")
    time.sleep(SCROLL_PAUSE_TIME)
    #scroll1 = driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    #height2 = driver.execute_script("return document.body.scrollHeight")
    #time.sleep(SCROLL_PAUSE_TIME)
    #scroll2 = driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    #height = driver.execute_script("return document.body.scrollHeight")
    #time.sleep(SCROLL_PAUSE_TIME)
    return driver.page_source



def parse(html):
    board = html
    print(type(board))
    #soup = BeautifulSoup(board, 'lxml')
    link = re.findall(r'https://i.pinimg.com/474x/.+?jpg', board)
    link1 = re.findall(r'https://i.pinimg.com/originals/.+?jpg', board)
    #link = soup.find_all(string=re.compile('https://i.pinimg.com/474x/.+?jpg'))
    link = set(link)
    link1 = set(link1)
    #print(len(link1))
    #print(len(link))
    return link


b = get_html('https://www.pinterest.ru/yuriyjk/1045/')
links = parse(b)
for i in links:
    destination = i.rsplit('/', 1)[1]
    destin = os.path.join('/Users/yuriykhen/Pinterest___Parse', destination)
    urllib.request.urlretrieve(i, destin)
