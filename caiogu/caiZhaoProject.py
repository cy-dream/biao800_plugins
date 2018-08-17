import requests
import datetime

def main(session):
    headers = {
        'Host':'cms.chinabidding.cn',
        'Connection':'keep-alive',
        'Content-Length':'393',
        'Origin':'https://cms.chinabidding.cn',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
        'content-type':'text/xml',
        'Referer':'https://cms.chinabidding.cn/cms/qdp.view.bid.BidCallPublishFirst.d',
    }
    url = 'https://cms.chinabidding.cn/cms/dorado/view-service'
    yesterday = (datetime.datetime.now()-datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    data = '<batch><request type="json"><![CDATA[{"action":"load-data","dataProvider":"projectInfoCR#queryProjectInfoMVP","supportsEntity":true,"parameter":{"publishDateStart":"'+ yesterday +'T06:00:53Z","publishDateEnd":"'+today+'","$dataType":"v:qdp.view.projectinfo.ProjectInfoMVP$Condition"},"resultDataType":"v:qdp.view.projectinfo.ProjectInfoMVP$[v:qdp.view.projectinfo.ProjectInfoMVP$PublishInfo]","pageSize":20,"pageNo":1,"context":{},"loadedDataTypes":["Dictionary","Condition","PublishInfoFile","ExportFiles","PublishInfo"]}]]></request></batch>'
    requests.packages.urllib3.disable_warnings();
    response = session.post(url,headers=headers, data=data, verify=False)
    content = response.text
    print(content)
    write_data(content)
    #return content

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

def write_data(content):
    with open('per_text', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    main(get_session())