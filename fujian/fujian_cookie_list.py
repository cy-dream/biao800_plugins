import requests
from selenium import webdriver

def get_cookie():
  dir = 'D:\\LocoySpider_V9.6_Build20180409\\cookie.txt'
  browser = webdriver.PhantomJS()
  browser.set_window_size(1960,1080)
  url = 'https://www.fjggfw.gov.cn/Website/JYXXNew.aspx'
  browser.get(url)
  cookies = browser.get_cookies()
  cookie = ''
  for coo in cookies:
    cookie += coo['name']+'='+coo['value']+'; '
  with open(dir, 'w') as f:
    f.write(cookie)
    f.close()
  return cookie

def get_data(cookie):
  headers = {
    'Host':'www.fjggfw.gov.cn',
    'Connection':'keep-alive',
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer':'https://www.fjggfw.gov.cn/Website/JYXXNew.aspx',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'cookie':cookie
  }
  url = 'https://www.fjggfw.gov.cn/Website/AjaxHandler/BuilderHandler.ashx'
  args = [  
    'OPtype=GetListNew&pageNo=1&pageSize=10&proArea=-1&category=GCJS&announcementType=6&ProType=-1&xmlx=-1&projectName=&TopTime=2018-02-24+00%3A00%3A00&EndTime=2018-05-25+23%3A59%3A59&rrr=0.43111304156502284',
    'OPtype=GetListNew&pageNo=1&pageSize=10&proArea=-1&category=ZFCG&announcementType=1&ProType=-1&xmlx=-1&projectName=&TopTime=2018-02-24+00%3A00%3A00&EndTime=2018-05-25+23%3A59%3A59&rrr=0.06879845780359761',
    'OPtype=GetListNew&pageNo=1&pageSize=10&proArea=-1&category=ZFCG&announcementType=4&ProType=-1&xmlx=-1&projectName=&TopTime=2018-02-24+00%3A00%3A00&EndTime=2018-05-25+23%3A59%3A59&rrr=0.9955140983095208',
  ]
  for page in range(1, 11):
    args.append('OPtype=GetListNew&pageNo='+ str(page) +'&pageSize=10&proArea=-1&category=GCJS&announcementType=1&ProType=-1&xmlx=-1&projectName=&TopTime=2018-02-19+00%3A00%3A00&EndTime=2018-05-20+23%3A59%3A59&rrr=0.3859960628354766')
    args.append('OPtype=GetListNew&pageNo='+ str(page) +'&pageSize=10&proArea=-1&category=GCJS&announcementType=2%2C3%2C7&ProType=-1&xmlx=-1&projectName=&TopTime=2018-02-24+00%3A00%3A00&EndTime=2018-05-25+23%3A59%3A59&rrr=0.018610755892176645')
  
  response_html = ''
  for data in args:
    response = requests.post(url, data=data, headers=headers)
    response_html += response.text
  return response_html

if __name__ == '__main__':
  cookie = get_cookie()
  print(get_data(cookie))