import re
import requests
from bs4 import BeautifulSoup
def get_html(link):
    headers = {
        'Host':'www.ahtba.org.cn',
        'Origin':'http://www.ahtba.org.cn',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Content-Type':'application/x-www-form-urlencoded'
    }
    url_data = link.split('?')
    url = url_data[0]
    data = url_data[1]
    response = requests.post(url, data=data, headers=headers)   
    html = re.search(r'^(.*<div class="zb_detail">)([\s\S]*)(<div class="zb01s fr">)', response.text, re.M|re.I)
    print(html)
    soup = BeautifulSoup(html.group(2), 'lxml')

    # delete script and style tags
    [script.extract() for script in soup.findAll('script')]
    [style.extract() for style in soup.findAll('style')]

    # replace all <table *> -> <table border='1' width='100%'>
    table_tags = [tag for tag in soup.findAll('table')]
    for table_tag in table_tags:
        del table_tag[True]
        table_tag['border'] = 1
        table_tag['width'] = '100%'

    # delete all class and style of tags
    tags = [tag for tag in soup.findAll(True)]
    for tag in tags:
        del tag['class']
        del tag['style']

    # delete span tags
    soup = re.sub(r'<span>', '', str(soup))
    content = re.sub(r'</span>', '', soup)

    # return [content, abstract]
    dr = re.compile(r'<[^>]+>',re.S)
    abstract = dr.sub('', content)
    abstract = re.sub(r'\s+','', abstract)[0:200]
    return [content, abstract]

if __name__ == '__main__':
    url = 'http://www.ahtba.org.cn/Notice/NoticeContent?id=665754'
    content, abstract = get_html(url)
    print(content)