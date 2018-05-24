import requests
from selenium import webdriver
def test_selenium():
  browser = webdriver.PhantomJS()
  browser.set_window_size(1960,1080)
  url = 'https://www.fjggfw.gov.cn/Website/JYXXNew.aspx'
  browser.get(url)
  cookies = browser.get_cookies()
  cookie = ''
  for coo in cookies:
    cookie += coo['name']+'='+coo['value']+'; '

  print(cookie)


if __name__ == '__main__':
  test_selenium()