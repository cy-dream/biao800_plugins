import requests

def req_post(cookile):

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
    'cookile':cookile
    #'Cookie':'ASP.NET_SessionId=143nloujv5m0o2zuhuk0h1ec; Hm_lvt_63d8823bd78e78665043c516ae5b1514=1526823880; Hm_lpvt_63d8823bd78e78665043c516ae5b1514=1526823880; _qddagsx_02095bad0b=ce330e78eac4b50727985d1217430a5f09b97b898582837c99b20e5cbbbe195065a7c5e933ebcf42e21376237bffd64c2915928549066b0606353c624d0bcc0bd5b4be88a7de5fc776c6ea37fe81cfe8f5ce2bc432b4b423e30198b3952eb15b3cc3bfe9bb66aa156092199c66b61698af07f34568d5ed6f21a670841ebaed39; __root_domain_v=.fjggfw.gov.cn; _qddaz=QD.jntxri.9zv1cv.jhevim3q; _qdda=4-1.4euvh3; _qddab=4-muy3bq.jhevim7b; _qddamta_2852155767=4-0'
  }

  url = 'https://www.fjggfw.gov.cn/Website/AjaxHandler/BuilderHandler.ashx'
  data = 'OPtype=GetListNew&pageNo=1&pageSize=10&proArea=-1&category=GCJS&announcementType=1&ProType=-1&xmlx=-1&projectName=&TopTime=2018-02-19+00%3A00%3A00&EndTime=2018-05-20+23%3A59%3A59&rrr=0.3859960628354766'
  res = requests.post(url, data=data, headers=headers)
  print(res.text)

def req_cooklie():
  url = 'https://www.fjggfw.gov.cn/default.aspx'
  req = requests.get(url)
  return req.cookies

if __name__ == '__main__':
  cookile = req_cooklie()

