# coding=utf-8
from bs4 import BeautifulSoup
import requests
import datetime
import json
import time
import re

def select_post_data(url):
    datas = list()
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    today = '2018-07-11'
    if 'zhaobiao' in url:
        for i in range(1, 3):
            #data = '<batch><request type="json"><![CDATA[{"action":"load-data","dataProvider":"bidCallPublishCR#queryPublishInfo1","supportsEntity":true,"parameter":{"publishDateStart":"'+ today +'T00:00:36Z","publishDateEnd":"'+ today +'T23:20:39Z","$dataType":"v:qdp.view.bid.BidCallPublishFirst$Condition"},"resultDataType":"v:qdp.view.bid.BidCallPublishFirst$[v:qdp.view.bid.BidCallPublishFirst$PublishInfo]","pageSize":20,"pageNo":'+str(i)+',"context":{},"loadedDataTypes":["PublishInfoFile","PublishInfo","Condition"]}]]></request></batch>'
            data = '<batch><request type="json"><![CDATA[{"action":"load-data","dataProvider":"bidCallPublishCR#queryPublishInfo","supportsEntity":false,"parameter":{"classdName":"linshi09J","publishDateStart":"'+ today +'T00:00:36Z","publishDateEnd":"'+ today +'T23:20:39Z","$dataType":"v:qdp.view.bid.BidCallPublish$Condition"},"resultDataType":"v:qdp.view.bid.BidCallPublish$[v:qdp.view.bid.BidCallPublish$PublishInfo]","pageSize":20,"pageNo":'+str(i)+',"context":{}}]]></request></batch>'
            datas.append(data)
        return datas

def main(session):
    headers = {
        'Host':'cms.chinabidding.cn',
        'Connection':'keep-alive',
        'Content-Length':'298',
        'Origin':'https://cms.chinabidding.cn',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
        'content-type':'text/xml',
        'Referer':'https://cms.chinabidding.cn/cms/qdp.view.bid.BidCallPublishFirst.d'
    }
    url = 'https://cms.chinabidding.cn/cms/dorado/view-service'
    datas = select_post_data('zhaobiao')
    content = ''
    for data in datas:
        requests.packages.urllib3.disable_warnings();
        response = session.post(url,headers=headers, data=data, verify=False)
        text = response.text
        if 'exception' not in text:
            content += text
    return content  

def write_data(text):
    with open('text.txt', 'w') as f:
        f.write(text)
        f.close()

def get_session():
    headers = {
        'Host':'cms.chinabidding.cn',
        'Connection':'keep-alive',
        'Content-Length':'152',
        'Origin':'https://cms.chinabidding.cn',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
        'content-type':'text/javascript',
        'Accept':'*/*',
        'Referer':'https://cms.chinabidding.cn/cms/edf.view.index.Login.d',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
    }
    url = 'https://cms.chinabidding.cn/cms/dorado/view-service'
    requests.packages.urllib3.disable_warnings();
    session = requests.Session()
    data = '{"action":"remote-service","service":"loginControllerPR#login","parameter":{"username":"xxxxxxx","password":"xxxxxxx"},"context":{},"loadedDataTypes":[]}'
    r = session.post(url, headers=headers, data=data, verify=False)
    return session

if __name__ == '__main__':
    print(main(get_session()))