from bs4 import BeautifulSoup
import requests
import re
# 内容页
# 福建省公共资源交易公共服务平台有限公司 plugin
def strip_css(html):
	soup = BeautifulSoup(html, 'lxml')
	table_tags = [tag for tag in soup.findAll('table')]
	for table_tag in table_tags:
		del table_tag[True]
		table_tag['border'] = 1
		table_tag['width'] = '100%'
	for tag in soup.findAll(True):
		del tag['class']
		del tag['style']
	soup = re.sub(r'<span>', '', str(soup))
	soup = re.sub(r'</span>', '', soup)
	return soup

def read_cookie():
	with open('D:\\LocoySpider_V9.6_Build20180409\\cookie.txt', 'r') as f:
		return f.read()
		f.close()
def get_html(url):
	cookie = read_cookie()
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
	response = requests.get(url, headers=headers)
	content = re.search(r'(\"data\":\[\")([\s\S]*)(\"\],\"node\")', str(response.text), re.M|re.I)
	content = content.group(2).replace('\\n', '').replace('\\', '')
	content = strip_css(content)
	con = content.split('","')
	if len(con) != 1:
		return con[1]
	else:
		return content

if __name__ == '__main__':
	url = 'https://www.fjggfw.gov.cn/Website/AjaxHandler/BuilderHandler.ashx?OPtype=GetGGInfoPC&ID=77346&GGTYPE=1&url=AjaxHandler%2FBuilderHandler.ashx'
	with open('aa.html', 'w', encoding='utf-8') as f:
		f.write(get_html(url))
